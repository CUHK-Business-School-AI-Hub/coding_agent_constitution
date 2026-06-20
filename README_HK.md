<div align="center">

# Coding Agent Constitution

**將模糊的軟件想法，先變成可重用的項目前置治理資產，再交給智能體寫程式碼。**

[English](README.md) · [簡體中文](README_CN.md)

[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-SKILL.md-111827)](#)
[![Codex](https://img.shields.io/badge/Codex-compatible-10a37f)](#)
[![Cursor](https://img.shields.io/badge/Cursor-compatible-5b5bf7)](#)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-d97706)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

</div>

---

## 這是甚麼？

這是一個給 **Codex、Cursor、Claude Code** 使用的開源 Agent Skill。

它不會一開始就急着寫程式碼。它會先幫你把一句很模糊的說法：

> 我想做一個工具，幫我把這個項目做起來。

整理成真正可以重用的倉庫檔案：

```text
docs/SPEC.md                  產品目標、功能邊界、非目標
docs/ARCH.md                  架構、模組邊界、技術選擇
docs/RULES.md                 編碼規則、測試規則、安全邊界
docs/CONTRACTS/README.md      API、資料結構、事件、介面約束
docs/TASKS/001-*.md           可執行的小任務
AGENTS.md                     Codex / 多智能體共享規則
CLAUDE.md                     Claude Code 入口
.cursor/rules/*.mdc           Cursor Project Rules
.claude/rules/*.md            Claude Code 模組化規則
```

一句話：

> 它把「聊天入面的想法」變成「倉庫入面的資產」。

如果上面這些檔名你大部分都未熟，沒問題。先讀 [`constitution-skill/references/rookie-onboarding.md`](constitution-skill/references/rookie-onboarding.md)，這份是給「第一次做軟件產品的人」準備的簡短入門，讀完再回來這裡。

## 為甚麼需要它？

直接叫智能體寫程式碼，常見問題是：

- 需求還未清楚，程式碼已經開始長出來
- 架構判斷藏在聊天記錄入面，下一輪就不見了
- API、資料模型、測試標準沒有人寫低
- Cursor、Codex、Claude Code 各自讀不同上下文
- 人類審查時不知道智能體到底跟了甚麼規則

這個 skill 的思路是：

```text
模糊意圖
-> 前置治理檔案
-> 有邊界的小任務
-> 智能體實現
-> Cursor / Claude / 人類審查
-> 決策再沉澱回檔案
```

## 適合邊個用？

這是一個**階段性工具**：用在「我有一個軟件產品的想法」同「我已經有一位工程師完全接手項目」之間嘅一段時間。它的設計係鋒利、專注，唔會試圖乜都做。

如果你係以下其中一種，這個 skill 可能適合你：

- 一位準備啟動新項目的產品經理，希望文檔比 kickoff 聊天活得更耐
- 喺做副業項目、之後會搵協作者入嚟的人
- 領域專家（設計師、分析員、營運）第一次做軟件產品
- 願意學少少工程的非技術 founder，令成品可以順利移交
- 想喺 agent 開始改程式碼之前先建立好基線的工程師

如果你對生成出嚟的檔案中的工程術語仲好陌生，請先讀 [`constitution-skill/references/rookie-onboarding.md`](constitution-skill/references/rookie-onboarding.md)。呢份係給「第一次做軟件產品的人」準備的簡短概念入門，唔要求你識寫程式碼。

## 甚麼時候適合用？

適合：

- 你只有一個產品想法，但未知道技術棧
- 你不知道應該先做哪個功能
- 你想讓 Codex / Cursor / Claude Code 協同工作
- 你想建立 `SPEC.md`、`ARCH.md`、`RULES.md`
- 你想把聊天入面的規則沉澱到倉庫入面
- 你要把一個大需求拆成多個安全的小任務

不適合：

- 已經很清楚的小 bug
- 只改一個函數
- 純粹格式化程式碼
- 取代人類做產品或架構最終決策
- 想完全唔接觸任何工程概念（這是學習腳手架，唔係 no-code 平台）

## 幾時應該停止用？

這個 skill 的設計是：當項目穩定之後，它會主動退出日常流程。合理的「畢業」信號包括：

- 已經有一位全職工程師在維護 `docs/SPEC.md`、`docs/ARCH.md`、`docs/RULES.md`
- 每個改動都會經人手 code review
- 團隊已經有自己的 onboarding 文檔，可以取代 rookie primer

到這一步之後，那啲長期檔案仲會繼續用，但 skill 本身已經唔再係你日常入口。

## 三大智能體兼容方式

| 智能體 | 建議入口 | 用途 |
| --- | --- | --- |
| Codex | `AGENTS.md` + `constitution-skill/SKILL.md` | 實現 bounded tasks、執行檢查、產出 reviewable changes |
| Cursor | `.cursor/rules/*.mdc` + optional `.cursor/skills/` | 做 IDE review、架構邊界檢查、局部修正 |
| Claude Code | `CLAUDE.md` + `.claude/rules/*.md` + optional `.claude/skills/` | 實現或 review bounded tasks，讀取 Claude 項目記憶 |

注意：

Cursor 雖然建基於 VS Code，但 agent 規則不應該主要放在 `.vscode/`。Cursor 的規則入口是 `.cursor/rules/`，skill 入口是 `.cursor/skills/`。

## 快速開始（推薦）

將下面這段提示詞發給你的編碼智能體（Codex / Claude Code / Cursor）即可：

```
Install the skill in this repo: https://github.com/UbicusMyron/coding_agent_constitution. Make sure you always call it when I mention `constitution-skill`.
```
然後你可以去沖杯咖啡，等智能體把一切都搞定。

## 如果你想自己動手安裝...

### Codex

將 skill 目錄放到你的 Codex skills 目錄：

```bash
mkdir -p ~/.codex/skills
cp -R constitution-skill ~/.codex/skills/constitution-skill
```

然後對 Codex 說：

```text
Use constitution-skill to turn this software idea into governance docs before coding.
```

### Cursor

項目級安裝：

```bash
mkdir -p .cursor/skills
cp -R constitution-skill .cursor/skills/constitution-skill
```

Cursor 項目規則建議使用生成出來的：

```text
.cursor/rules/project-governance.mdc
```

### Claude Code

項目級安裝：

```bash
mkdir -p .claude/skills
cp -R constitution-skill .claude/skills/constitution-skill
```

Claude Code 的項目入口建議使用：

```text
CLAUDE.md
```

其中 `CLAUDE.md` 可以直接導入共享規則：

```markdown
@AGENTS.md

## Claude Code

- Read the governance docs before implementation.
- Ask before changing risky surfaces.
```

## 最簡單的使用方式

直接把你的想法告訴 agent：

```text
我想做一個 SaaS 工具，幫小團隊追蹤客戶反饋、自動總結需求、生成開發任務。
我還不知道技術棧、資料庫、API 應該怎樣設計。
請先用 constitution-skill 做前置治理，不要急着寫程式碼。
```

理想輸出不是一堆程式碼，而是：

```text
docs/SPEC.md
docs/ARCH.md
docs/RULES.md
docs/CONTRACTS/README.md
docs/TASKS/001-bootstrap-feedback-inbox.md
AGENTS.md
CLAUDE.md
.cursor/rules/project-governance.mdc
.claude/rules/project-governance.md
```

## 文件生成之後，怎樣真正開始實現？

當前置治理檔案已經生成，不要直接對智能體說「把整個 app 做出來」。這樣項目很容易再次失控。正確做法是：把第一個任務檔案當成由規劃進入實現的橋。

1. 打開第一個任務。

   通常由類似這個檔案開始：

   ```text
   docs/TASKS/001-bootstrap-feedback-inbox.md
   ```

   這個檔案應該只描述一個細小、清楚、方便 review 的實現切片。

2. 讓一個編碼智能體只實現這個任務。

   可以這樣說：

   ```text
   Read AGENTS.md, docs/SPEC.md, docs/ARCH.md, docs/RULES.md,
   and docs/TASKS/001-bootstrap-feedback-inbox.md.

   Implement only this task.
   Do not change public APIs, database schemas, auth, billing,
   or destructive behavior unless the task explicitly says so.

   Run the listed verification checks.
   Then summarize files changed, checks run, risks, and what needs review.
   ```

3. 做完之後先 review，再做下一個任務。

   你可以用 Cursor、Claude Code、Codex review mode，或者自己人工檢查：

   - diff 是否符合任務？
   - 智能體有沒有改到範圍外的檔案？
   - 有沒有測試或驗證步驟？
   - 有沒有改變架構、契約、產品決策？

4. 把長期有用的新發現寫回檔案。

   如果實現過程中發現了之後還會用到的規則、介面、架構選擇或產品澄清，就更新：

   ```text
   docs/SPEC.md
   docs/ARCH.md
   docs/RULES.md
   docs/CONTRACTS/
   AGENTS.md
   CLAUDE.md
   .cursor/rules/
   .claude/rules/
   ```

5. 再進入下一個小任務。

   循環很簡單：

   ```text
   選擇一個任務
   -> 實現它
   -> 執行檢查
   -> review diff
   -> 必要時更新長期文件
   -> 選擇下一個任務
   ```

對新手來說，最安全的規則是：

> 一次只做一個任務，一次只讓一個智能體主實現，一次 review 之後再繼續。

## 按產品形態組合預設方案

skill 唔再要所有產品只套同一份空白模板，而係組合治理內容：

```text
項目模式
+ 基礎 profile（例如記錄型事務系統）
+ 能力模組（身份權限、LLM 邊界、持久化工作流）
+ 可選嘅已覆核技術 recipe
-> 項目自己嘅 SPEC / ARCH / RULES / CONTRACTS / TASKS
```

當項目冇既有技術限制時，內置 recipe 會為部署型 Web 產品推薦
TypeScript/PostgreSQL，為單機本地工具推薦 Python/SQLite。佢哋係可以
覆核嘅預設方案，唔係永久規則；生成嘅 `ARCH.md` 會記錄所用 recipe 同
所有偏離項。SQLite 預設先用關係查詢同 FTS5，向量檢索只係按需要升級。

## 核心原則

```text
Human owns intent.
Agents implement bounded work.
Review layers inspect diffs.
Durable knowledge belongs in files.
Disposable plans can be replaced.
```

中文解釋：

```text
人類定義意圖。
智能體只做有邊界的改動。
review 工具檢查 diff。
長期知識寫進檔案。
一次性執行計劃可以丟掉。
```

## 倉庫結構

```text
.
├─ README.md
├─ README_CN.md
├─ README_HK.md
├─ LICENSE
├─ constitution.md
└─ constitution-skill/
   ├─ SKILL.md
   ├─ agents/
   │  └─ openai.yaml
   ├─ references/
   │  ├─ rookie-onboarding.md          # 給第一次做軟件產品的人的概念入門
   │  ├─ bootstrap-question-bank.md    # 應該問甚麼問題
   │  ├─ cross-agent-compatibility.md  # Codex / Cursor / Claude Code 適配映射
   │  ├─ governance-asset-guide.md     # 長期 vs 一次性資產、提升規則
   │  ├─ anti-patterns.md              # 常見的治理反模式
   │  ├─ task-sizing.md                # 量化的 bounded task 限制
   │  ├─ retrofit-mode.md              # 把治理引入 legacy 倉庫
   │  ├─ governance-evolution.md       # 版本演進、ADR、歸檔
   │  ├─ minimal-mode.md               # 單人 / 極簡項目的輕量模式
   │  ├─ product-pattern-routing.md    # profile/module/recipe 選擇
   │  ├─ profile-transactional-record-system.md
   │  ├─ module-identity-access.md
   │  ├─ module-llm-boundary.md
   │  ├─ module-deterministic-workflow.md
   │  ├─ recipe-typescript-web-postgres.md
   │  └─ recipe-local-python-sqlite.md
   ├─ assets/
   │  ├─ governance-templates/
   │  │  ├─ AGENTS.md
   │  │  ├─ CLAUDE.md
   │  │  ├─ SPEC.md
   │  │  ├─ ARCH.md
   │  │  ├─ RULES.md
   │  │  ├─ TASK.md
   │  │  ├─ DECISION.md
   │  │  ├─ CONTRACTS_README.md
   │  │  ├─ cursor-project-governance.mdc
   │  │  └─ claude-project-governance.md
   │  ├─ module-overlays/               # 可組合嘅治理同 contract 片段
   │  ├─ contracts-examples/           # 填好的 OpenAPI / JSON Schema / event / SQL / CLI / 檔案格式範例
   │  └─ examples/
   │     └─ feedback-inbox/            # 完整填好的樣例項目
   └─ scripts/
      └─ check-governance.sh           # 漂移與缺失段落檢測腳本
```

## 關於那條校驗警告（WARN）

skill 自帶一個細小的校驗腳本 `constitution-skill/scripts/check-governance.sh`，用嚟掃描項目入面嘅治理檔案有冇常見問題。它會輸出三種結果：

- `ERROR` —— 真係有問題（例如某個任務檔案漏咗 `## Verification` 段落），呢樣會阻斷「完成」。
- `WARN` —— 善意提醒，值得睇一眼，但唔會阻斷。
- `OK` —— 通過。

當你攞佢去跑自帶樣例（或者你自己嘅項目）時，多數會見到一條咁嘅 `WARN`：

```text
WARN   Repeated lines across adapter files (top 5). Consider keeping AGENTS.md canonical:
```

**呢個係預期之內，而且我哋係故意保留嘅。** 通俗啲解釋：

Cursor 同 Claude Code 各自讀自己嘅規則檔案——Cursor 讀 `.cursor/rules/*.mdc`，Claude Code 讀 `.claude/rules/*.md`。呢個係兩個工具嘅兩個唔同檔案，所以有幾條重要嘅安全規則（例如「唔好將原始 email 地址寫入 log」或者「改資料庫結構、認證、計費之前要先問人類」）會喺兩個檔案各寫一份。腳本見到呢啲重複行，就提你一提。

我哋**故意唔刪**呢啲重複，原因係：

- 將安全規則直接寫喺每個工具自己嘅檔案入面，可以保證：無論你用邊個智能體，呢條規則都實實在在擺喺佢面前。
- 如果為咗「去重」，淨係叫每個工具寫一句「見 AGENTS.md」，咁呢條規則就要靠工具去載入 `AGENTS.md` 先睇到。但唔係每個工具、每個版本都會自動載入 `AGENTS.md`，萬一冇載入，關鍵安全規則就會靜雞雞咁消失——呢樣比多寫幾行重複更差。

所以呢條 `WARN` 請當佢係「設計上已經接受」。唯一要記住嘅係：如果你改咗某條重複規則嘅其中一處，記得連另一處都一齊改，唔好等佢哋慢慢變到唔一致。

> 一句話原則：`ERROR` 一定要先修好先算任務完成；`WARN` 係建議——睇一睇，再自己判斷。而呢條「重複」 `WARN`，係我哋已經決定接受嗰一類。

## 授權

MIT License。放心使用、fork、改造，令你的編碼智能體少一點混亂，多一點秩序。
