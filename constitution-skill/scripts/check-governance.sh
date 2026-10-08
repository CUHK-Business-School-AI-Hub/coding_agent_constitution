#!/usr/bin/env bash
# check-governance.sh
# Detect common governance-asset problems in a project that uses the constitution skill.
#
# Checks performed:
#   1. Canonical AGENTS.md presence and common local Claude entry shadowing.
#   2. Required sections present in each TASKS/*.md file.
#   3. Required sections present in SPEC.md, ARCH.md, RULES.md.
#   4. Contract files referenced by ARCH.md/RULES.md actually exist.
#   5. Significant duplication between AGENTS.md, CLAUDE.md, .cursor/rules/*, .claude/rules/*.
#   6. TASKS that lack execution-contract sections such as Interfaces,
#      Verification, or Governance Drift Check.
#   7. Placeholder and vague wording in governance assets.
#   8. Product-profile/module declarations and their expected contract files.
#   9. Files marked `Status: Active` whose `Last Reviewed` is older than 180 days.
#
# Exit code: 0 for no errors (warnings allowed), 1 for errors, 2 for invalid input.
# This is a structural lint, not proof of completeness or successful execution.
#
# Usage:
#   scripts/check-governance.sh              # run in current repo root
#   scripts/check-governance.sh path/to/repo

set -u

ROOT="${1:-.}"
if [ ! -d "$ROOT" ]; then
    printf "error: '%s' is not a directory\n" "$ROOT" >&2
    exit 2
fi

cd "$ROOT" || exit 2

ISSUES=0
WARNINGS=0

c_red=$(printf '\033[31m')
c_yel=$(printf '\033[33m')
c_grn=$(printf '\033[32m')
c_rst=$(printf '\033[0m')

report_error() {
    printf "%sERROR%s  %s\n" "$c_red" "$c_rst" "$1"
    ISSUES=$((ISSUES + 1))
}

report_warn() {
    printf "%sWARN%s   %s\n" "$c_yel" "$c_rst" "$1"
    WARNINGS=$((WARNINGS + 1))
}

report_ok() {
    printf "%sOK%s     %s\n" "$c_grn" "$c_rst" "$1"
}

# 1. Adapter orphans -----------------------------------------------------------

has_agents=0
[ -f "AGENTS.md" ] && has_agents=1

has_claude=0
for f in CLAUDE.md .claude/CLAUDE.md CLAUDE.local.md; do
    [ -f "$f" ] && has_claude=1
done

has_cursor_rules=0
if [ -d ".cursor/rules" ] && ls .cursor/rules/*.mdc >/dev/null 2>&1; then
    has_cursor_rules=1
fi

has_claude_rules=0
if [ -d ".claude/rules" ] && ls .claude/rules/*.md >/dev/null 2>&1; then
    has_claude_rules=1
fi

if [ "$has_agents" -eq 0 ] && { [ "$has_claude" -eq 1 ] || [ "$has_cursor_rules" -eq 1 ] || [ "$has_claude_rules" -eq 1 ]; }; then
    report_error "Tool adapter files exist (CLAUDE.md / .cursor/rules / .claude/rules) but AGENTS.md is missing. Add a canonical AGENTS.md."
fi

# Read Markdown outside fenced examples. Normalize CRLF and trailing whitespace.
markdown_text() {
    awk -v keep_code="${2:-0}" '
        { sub(/\r$/, ""); sub(/[ \t]+$/, "") }
        {
            line = $0
            sub(/^ ? ? ?/, "", line)
            if (match(line, /^```+|^~~~+/)) {
                mark = substr(line, 1, 1)
                size = RLENGTH
                if (!fence) { fence = mark; width = size; next }
                if (mark == fence && size >= width && substr(line, size + 1) ~ /^[ \t]*$/) {
                    fence = ""
                    next
                }
            }
            if (!fence) print
            else if (keep_code) print "| " $0
        }
    ' "$1"
}

section_text() {
    markdown_text "$1" | awk -v heading="## $2" '
        /^##? / { active = ($0 == heading); next }
        active { print }
    '
}

check_required_sections() {
    local file="$1" sec missing=""
    shift
    [ -f "$file" ] || return 0
    for sec in "$@"; do
        if ! markdown_text "$file" | grep -Fx "## $sec" >/dev/null; then
            missing="$missing '$sec'"
        fi
    done
    if [ -n "$missing" ]; then
        report_error "$file missing sections:$missing"
    fi
}

# Default native Claude AGENTS discovery is suppressed by a project Claude entry.
# Recognize the common explicit root imports; do not claim to resolve every import
# graph, ancestor setting, plugin configuration, or live-client loading state.
if [ "$has_agents" -eq 1 ] && [ "$has_claude" -eq 1 ]; then
    imports_agents=0
    for f in CLAUDE.md CLAUDE.local.md; do
        [ -f "$f" ] || continue
        if markdown_text "$f" | grep -E '^[[:space:]]*@([.]/)?AGENTS[.]md[[:space:]]*$' >/dev/null; then
            imports_agents=1
        fi
    done
    if [ -f .claude/CLAUDE.md ] && markdown_text .claude/CLAUDE.md | grep -E '^[[:space:]]*@[.][.]/AGENTS[.]md[[:space:]]*$' >/dev/null; then
        imports_agents=1
    fi
    if [ "$imports_agents" -eq 0 ]; then
        report_warn "Claude project entry files can suppress native AGENTS.md discovery, and no direct canonical import was recognized. Verify loading or use a thin @AGENTS.md adapter (relative to its location); indirect imports/custom plugin settings need manual review."
    fi
fi

# 2. TASKS sections ------------------------------------------------------------

TASK_DIRS="docs/TASKS TASKS"
TASK_REQUIRED=("Goal" "Source Context" "Scope" "Interfaces" "Acceptance Criteria" "Verification" "Governance Drift Check")

for dir in $TASK_DIRS; do
    if [ -d "$dir" ]; then
        for f in "$dir"/*.md; do
            [ -f "$f" ] || continue
            check_required_sections "$f" "${TASK_REQUIRED[@]}"
        done
    fi
done

# 3. Required sections in SPEC/ARCH/RULES --------------------------------------

for spec_path in docs/SPEC.md SPEC.md; do
    [ -f "$spec_path" ] || continue
    check_required_sections "$spec_path" \
        "Product Intent" "Users" "Goals" "Non-Goals" "Acceptance Criteria"
done

for arch_path in docs/ARCH.md ARCH.md; do
    [ -f "$arch_path" ] || continue
    check_required_sections "$arch_path" \
        "Architecture Summary" "Module Boundaries" "Dependency Rules"
    if ! grep -Eq '^## Considered Approaches$' "$arch_path"; then
        report_warn "$arch_path has no Considered Approaches section. Record the rationale and any useful alternatives for non-obvious choices, or state why it is not needed."
    fi
done

for rules_path in docs/RULES.md RULES.md; do
    [ -f "$rules_path" ] || continue
    check_required_sections "$rules_path" \
        "Coding Rules" "Testing Rules" "Security And Safety Rules"
done

# 4. Contract files referenced from ARCH.md / RULES.md must exist --------------

for ref_file in docs/ARCH.md docs/RULES.md ARCH.md RULES.md; do
    [ -f "$ref_file" ] || continue
    # Match links like `docs/CONTRACTS/whatever.yaml` or `CONTRACTS/whatever.md`
    refs=$(grep -Eo '(docs/)?CONTRACTS/[A-Za-z0-9._/-]+' "$ref_file" | sort -u)
    for r in $refs; do
        if [ ! -e "$r" ]; then
            report_warn "$ref_file references missing contract: $r"
        fi
    done
done

# 5. Duplication between AGENTS.md, CLAUDE.md, .cursor/rules/, .claude/rules/ ---

# Strategy: extract distinctive non-trivial lines (>= 40 chars, alphabetic) from
# each file, sort+unique, then look for cross-file overlap above a threshold.

dup_inputs=""
for f in AGENTS.md CLAUDE.md .claude/CLAUDE.md CLAUDE.local.md; do
    [ -f "$f" ] && dup_inputs="$dup_inputs $f"
done
if [ "$has_cursor_rules" -eq 1 ]; then
    for f in .cursor/rules/*.mdc; do
        [ -e "$f" ] && dup_inputs="$dup_inputs $f"
    done
fi
if [ "$has_claude_rules" -eq 1 ]; then
    for f in .claude/rules/*.md; do
        [ -e "$f" ] && dup_inputs="$dup_inputs $f"
    done
fi

if [ -n "$dup_inputs" ]; then
    tmp_all=$(mktemp)
    trap 'rm -f "$tmp_all"' EXIT
    for f in $dup_inputs; do
        awk -v path="$f" 'NF >= 1 {
            line = $0
            gsub(/^[ \t]+|[ \t]+$/, "", line)
            if (length(line) >= 40 && line !~ /^#/ && line !~ /^---/ && line !~ /^@/) {
                print path "\t" line
            }
        }' "$f"
    done > "$tmp_all"

    # Find lines appearing in 2+ files
    dup_lines=$(awk -F'\t' '{ count[$2]++; files[$2] = files[$2] " " $1 }
        END {
            for (l in count) {
                if (count[l] >= 2) {
                    n = split(files[l], parts, " ")
                    delete seen
                    distinct = 0
                    for (i = 1; i <= n; i++) {
                        if (parts[i] != "" && !(parts[i] in seen)) {
                            seen[parts[i]] = 1
                            distinct++
                        }
                    }
                    if (distinct >= 2) {
                        printf "%d\t%s\n", distinct, l
                    }
                }
            }
        }' "$tmp_all" | sort -nr | head -n 5)

    if [ -n "$dup_lines" ]; then
        report_warn "Repeated lines across adapter files (top 5). Consider keeping AGENTS.md canonical:"
        printf "%s\n" "$dup_lines" | while IFS=$(printf '\t') read -r n line; do
            printf "         in %s files: %s\n" "$n" "$line"
        done
    fi
fi

# 6. Task execution-contract content -----------------------------------------

for dir in $TASK_DIRS; do
    if [ -d "$dir" ]; then
        for f in "$dir"/*.md; do
            [ -e "$f" ] || continue
            verification=$(section_text "$f" "Verification")
            if ! printf '%s\n' "$verification" | grep -Eq '^- Command:[[:space:]]+[^[:space:]`]|^- Command:[[:space:]]+`[^`[:space:]][^`]*`|^- `[^`[:space:]][^`]*`'; then
                report_error "$f Verification should include exact non-empty command(s) in that section."
            fi
            if ! printf '%s\n' "$verification" | grep -Eq '^[[:space:]]*- Expected evidence:[[:space:]]+[^[:space:]]'; then
                report_error "$f Verification should include non-empty Expected evidence in that section."
            fi
            interfaces=$(section_text "$f" "Interfaces")
            for field in "Consumes" "Produces" "Public contracts touched" "Downstream tasks relying on this"; do
                if ! printf '%s\n' "$interfaces" | grep -Eq "^- $field:[[:space:]]+[^[:space:]]"; then
                    report_error "$f Interfaces should include $field with a value or None in that section."
                fi
            done
        done
    fi
done

# 7. Placeholder and vague wording -------------------------------------------

scan_governance_text() {
    for f in "$@"; do
        [ -f "$f" ] || continue
        # Open Questions may hold unresolved decisions; other sections may not.
        # Keep code blocks in this scan so unfinished contract examples are caught.
        if { case "$f" in
            *.md) markdown_text "$f" 1 | awk '
                /^##? / { questions = ($0 ~ /^## Open Questions[[:space:]]*$/) }
                !questions { print }
            ' ;;
            *) cat "$f" ;;
        esac; } | grep -Ei '(TBD|TODO|as discussed|implement later|add proper error handling|write tests|make sure it works)' >/dev/null; then
            report_error "$f contains placeholder or vague wording. Move real uncertainty to Open Questions or replace it with concrete requirements."
        fi
    done
}

scan_governance_text \
    AGENTS.md CLAUDE.md .claude/CLAUDE.md CLAUDE.local.md \
    docs/SPEC.md docs/ARCH.md docs/RULES.md \
    SPEC.md ARCH.md RULES.md

for dir in docs/TASKS TASKS docs/DECISIONS DECISIONS docs/CONTRACTS CONTRACTS; do
    if [ -d "$dir" ]; then
        for f in "$dir"/*; do
            case "$f" in
                *.md|*.yaml|*.yml|*.json|*.sql) scan_governance_text "$f" ;;
            esac
        done
    fi
done

# 8. Product pattern declarations ---------------------------------------------

check_product_shape() {
    file="$1"

    if ! grep -Eq '^## Product Shape$' "$file"; then
        report_warn "$file has no Product Shape section. Record the selected profile, modules, recipe, and deviations."
        return
    fi

    base=$(grep -E '^- Base profile:' "$file" | head -n 1 | sed -E 's/^- Base profile:[[:space:]]*//; s/`//g')
    modules=$(grep -E '^- Capability modules:' "$file" | head -n 1 | sed -E 's/^- Capability modules:[[:space:]]*//; s/`//g')
    recipe=$(grep -E '^- Technology recipe:' "$file" | head -n 1 | sed -E 's/^- Technology recipe:[[:space:]]*//; s/`//g')

    if [ -z "$base" ] || [ -z "$modules" ] || [ -z "$recipe" ]; then
        report_warn "$file Product Shape should declare Base profile, Capability modules, and Technology recipe."
    fi

    case "$base" in
        transactional-record-system|custom|none|"") ;;
        *) report_warn "$file declares an unknown base profile: $base" ;;
    esac

    case "$recipe" in
        typescript-web-postgres|local-python-sqlite|existing-stack|none|"") ;;
        *) report_warn "$file declares an unknown technology recipe: $recipe" ;;
    esac

    normalized_modules=$(printf '%s' "$modules" | tr ',' ' ')
    for module in $normalized_modules; do
        case "$module" in
            identity-access)
                [ -f "docs/CONTRACTS/identity-access.md" ] || [ -f "CONTRACTS/identity-access.md" ] || \
                    report_warn "$file selects identity-access but its contract file is missing."
                ;;
            llm-boundary)
                [ -f "docs/CONTRACTS/llm-boundary.md" ] || [ -f "CONTRACTS/llm-boundary.md" ] || \
                    report_warn "$file selects llm-boundary but its contract file is missing."
                ;;
            deterministic-workflow)
                [ -f "docs/CONTRACTS/workflow.md" ] || [ -f "CONTRACTS/workflow.md" ] || \
                    report_warn "$file selects deterministic-workflow but its contract file is missing."
                ;;
            none|"") ;;
            *) report_warn "$file declares an unknown capability module: $module" ;;
        esac
    done
}

for arch_path in docs/ARCH.md ARCH.md; do
    [ -f "$arch_path" ] || continue
    check_product_shape "$arch_path"
done

# 9. Last-reviewed staleness ---------------------------------------------------

now_epoch=$(date +%s)
stale_threshold=$((180 * 24 * 60 * 60))

scan_for_stale() {
    for f in "$@"; do
        [ -f "$f" ] || continue
        last=$(grep -E '^Last Reviewed:' "$f" | head -n 1 | sed -E 's/^Last Reviewed:[[:space:]]*//')
        status=$(grep -E '^Status:' "$f" | head -n 1 | sed -E 's/^Status:[[:space:]]*//')
        [ -z "$last" ] && continue
        case "$status" in
            Active|active|"") ;;
            *) continue ;;
        esac
        # Try GNU date first, fall back to BSD date
        if last_epoch=$(date -d "$last" +%s 2>/dev/null); then
            :
        elif last_epoch=$(date -j -f "%Y-%m-%d" "$last" +%s 2>/dev/null); then
            :
        else
            continue
        fi
        age=$((now_epoch - last_epoch))
        if [ "$age" -gt "$stale_threshold" ]; then
            days=$((age / 86400))
            report_warn "$f Last Reviewed is $days days old (>180); consider re-reviewing."
        fi
    done
}

scan_for_stale \
    AGENTS.md CLAUDE.md .claude/CLAUDE.md CLAUDE.local.md \
    docs/SPEC.md docs/ARCH.md docs/RULES.md \
    SPEC.md ARCH.md RULES.md
if [ -d "docs/DECISIONS" ]; then
    # shellcheck disable=SC2046
    scan_for_stale $(ls docs/DECISIONS/*.md 2>/dev/null)
fi
if [ -d "docs/CONTRACTS" ]; then
    # shellcheck disable=SC2046
    scan_for_stale $(ls docs/CONTRACTS/*.md 2>/dev/null)
fi

# Do not present an empty scan or an unchecked Minimal plan as full validation.
found_governance=0
for f in AGENTS.md CLAUDE.md .claude/CLAUDE.md CLAUDE.local.md docs/SPEC.md SPEC.md docs/ARCH.md ARCH.md docs/RULES.md RULES.md \
    docs/TASKS/*.md TASKS/*.md docs/CONTRACTS/* CONTRACTS/* .cursor/rules/*.mdc .claude/rules/*.md; do
    [ -f "$f" ] && found_governance=1
done
if [ -f docs/PLAN.md ]; then
    report_warn "Minimal docs/PLAN.md is not structurally checked by this lint; review its scope, acceptance criteria, and verification separately."
elif [ "$found_governance" -eq 0 ]; then
    report_warn "No governance files found. No project readiness check was performed."
fi

# Summary ----------------------------------------------------------------------

printf "\n"
if [ "$ISSUES" -eq 0 ] && [ "$WARNINGS" -eq 0 ]; then
    report_ok "Governance structural checks passed. Execution and project readiness still require review."
    exit 0
fi

printf "Issues: %d  Warnings: %d\n" "$ISSUES" "$WARNINGS"
if [ "$ISSUES" -gt 0 ]; then
    exit 1
fi
exit 0
