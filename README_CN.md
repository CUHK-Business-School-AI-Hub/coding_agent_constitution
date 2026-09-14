<div align="center">

# Coding Agent Constitution

**先把软件想法说清楚、写下来，再让 AI 一步步做出来。**

[English](README.md) · [繁體中文（香港）](README_HK.md)

[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-SKILL.md-111827)](#)
[![Codex](https://img.shields.io/badge/Codex-compatible-10a37f)](#)
[![Cursor](https://img.shields.io/badge/Cursor-compatible-5b5bf7)](#)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-d97706)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

</div>

---

## 最近更新 - 2026-09-14

- 更准确地判断何时需要这个技能：已经说清楚的小修改，不必先走一遍规划流程。
- 少问重复问题：已有决定直接沿用，有实际取舍时才比较方案。
- 更清楚地判断何时完成：只要规划就不写代码；已同意实施的任务，会做到约定的检查完成。与当前任务无关的旧问题单独说明。

## 最近更新 - 2026-09-12

- 检查更可靠：修复了“任务漏写重要段落，也可能显示通过”的问题，并加入自动测试。
- 使用更顺畅：已经确认过的任务，不再为同一个决定反复询问；实现和检查可以交给你常用的 AI 工具。
- 安装说明已更新：通用规则尽量只写一份，需要时才增加工具专用文件。
- 文档更好读：减少术语，补充普通人能直接复制使用的提示词。

## 最近更新 - 2026-06-30

- 做重要技术选择时，会写清楚有哪些方案、推荐哪个，以及以后是否容易调整。
- 生成文件后，会检查有没有说不清楚、互相矛盾或遗漏的地方。
- 每个任务会写明：要做什么、哪些地方可以改，以及怎样检查是否完成。

## 这是什么？

这是一个给 **Codex、Cursor、Claude Code** 使用的免费开源技能（Agent Skill）。你可以把它理解成一份给 AI 用的工作指南。

比如你说：

> 我想做一个工具，帮小团队收集客户意见，但不知道从哪里开始。

它会先帮你理清三个问题：**给谁用、先做什么、做到怎样算完成**，再把答案保存在项目文件夹里。以后换一个聊天、换一个 AI，或者交给工程师，都能接着做。

通常会得到这些文件，你不需要先学会它们的名字：

| 文件 | 用人话说 |
| --- | --- |
| `SPEC.md` | 要做什么，暂时不做什么 |
| `ARCH.md` | 各部分怎么配合，为什么这样选技术 |
| `RULES.md` | 开发时要遵守的规则 |
| `CONTRACTS/` | 不同部分交换数据时，约定好格式和行为 |
| `TASKS/` | 下一步要完成的小任务，以及检查方法 |
| `AGENTS.md` | 给 AI 的项目说明 |

文件数量会按项目情况调整，小型个人项目可以只保留两份主要文件。需要时，还会为你使用的工具生成读取说明。

想了解这些概念，可以看[第一次做软件产品的入门说明](constitution-skill/references/rookie-onboarding_CN.md)，也可以直接看下面的快速开始。

## 为什么需要它？

直接请 AI 写代码，有时会遇到这些问题：

- 需求还没想清楚，就已经做了很多功能。
- 换一个聊天或工具，又要从头解释。
- 不知道 AI 按什么要求做，也不知道怎样检查结果。

这个技能先把需求和重要决定写下来，再拆成小任务。每做完一步，检查结果，有用的新发现也写回项目文件。

## 适合谁？

适合已经有一个软件想法，想请 AI 帮忙实现、又希望事情保持清楚的人，例如：

- 准备启动新项目的产品经理。
- 做个人项目、以后可能找人合作的你。
- 想把工作经验做成工具的设计师、分析师或运营人员。
- 不会写代码，但希望能看懂计划、提出修改意见的创业者。
- 想让 AI 按明确要求工作的工程师。

你负责说明需求、检查结果，并决定重要取舍；AI 帮你整理文件和拆分任务。

## 它适合什么时候用？

适合在想法还不清楚、不知道先做哪一步，或者准备把项目交给别人接手时使用。

如果只是改错别字、修一个已经明确的小问题，直接让 AI 修改就好，不需要每次重新整理整个项目。重要的产品选择仍由你决定。

## 什么时候应该停止使用它？

当项目已有清楚的计划、工程师或团队能接着维护时，就不必每次都调用这个技能。已经整理好的文件可以继续使用。

以后遇到新的模糊需求，再请它帮忙整理即可。

## 三大智能体兼容方式

**选你已经在用的工具就好，不需要同时安装三个。** 三者都可以实现任务或检查改动。

| 工具 | 怎样读取项目说明 |
| --- | --- |
| Codex | 读取 `AGENTS.md` |
| Cursor | 当前版本可直接读取 `AGENTS.md`；有特别需要时再加专用规则 |
| Claude Code | 通过 `CLAUDE.md` 读取共享说明 |

通用规则尽量只保留一份，避免改了一处、忘了另一处。已有项目的专用规则会保留。[详细兼容说明](constitution-skill/references/cross-agent-compatibility.md)供需要配置工具的读者参考。

## 快速开始（推荐）

先打开你的项目文件夹，再把这段话发给 AI：

```text
请安装这个仓库里的 constitution-skill 技能：
https://github.com/CUHK-Business-School-AI-Hub/coding_agent_constitution
请按我正在使用的工具选择安装位置，并检查能否找到这个技能。
```

安装后新开一个会话，试着发送下面“最简单的使用方式”里的提示词。如果找不到技能，请让 AI 检查安装位置。

## 可选联动 Skill：`waymark`

如果你想先通过一问一答把想法讲清楚，可以使用我们团队开发的 [Waymark](https://github.com/CUHK-Business-School-AI-Hub/waymark)。它是 `grill-me` 的变种，对非技术人士更友好：你用日常语言描述工作，它会逐个提问，帮你理清谁来做、怎么做、遇到例外怎么办，再整理成可以照着执行的说明。

如果接下来想把这套流程做成软件，再交给 `constitution-skill` 整理项目计划和开发任务。Waymark 是可选辅助，不是必需安装的依赖。

组合使用时可以说：

```text
先用 waymark 帮我把实际工作流程和需求问清楚，用简单的话解释需要我决定的地方。
如果确定要做成软件，再用 constitution-skill 把确认的内容写成项目计划和第一个小任务。
```

## 如果你想自己动手安装...

以下命令假设你已下载本仓库，并在仓库根目录打开终端，适用于首次安装。如果已经安装过，请让 AI 先比较版本，避免覆盖自己的修改。

### Codex

安装到你的个人技能目录：

```bash
mkdir -p ~/.agents/skills
cp -R constitution-skill ~/.agents/skills/constitution-skill
```

如果只想在一个项目里使用，把技能复制到目标项目的 `.agents/skills/constitution-skill/` 即可。

### Cursor

把 `constitution-skill/` 复制到目标项目的 `.agents/skills/` 文件夹。这里已有 Codex 的项目副本时，当前 Cursor 版本可以共用；也仍可使用 `.cursor/skills/`。

### Claude Code

把 `constitution-skill/` 复制到目标项目的 `.claude/skills/` 文件夹。共享项目说明时，`CLAUDE.md` 可以用这一行读取：

```markdown
@AGENTS.md
```

安装后新开一个会话，检查技能是否可用。已有安装能正常使用时，先核实工具支持的位置，再决定是否迁移，不必重复复制。

## 最简单的使用方式

把下面的例子换成你的想法即可：

```text
我想做一个给小团队用的客户意见收集工具，能整理大家最常提的需求。
我不会设计技术方案。
请用 constitution-skill 先帮我说清楚第一版做什么、不做什么，
把计划保存在项目里，再列出第一个小任务和检查方法。
需要我决定的地方，请用简单的话解释；先不要写应用代码。
```

你会得到一份能查看和修改的项目计划，以及下一步任务。普通项目的文件通常放在 `docs/` 下；小型个人项目可能只需要 `AGENTS.md` 和 `docs/PLAN.md`。

先看看它有没有理解你的意思，尤其是“暂时不做什么”和“怎样算完成”。不对的地方，直接让 AI 改。

## 文档生成以后，怎么真正开始实现？

确认计划后，先做第一个小任务。可以直接对 AI 说：

```text
请找到计划里的第一个任务，向我说明它要实现什么。
按照我们已经确认的范围完成它，运行相应检查。
如果需要新增重要决定或超出范围，先告诉我原因。
做完后，请用简单的话说明做了什么、检查结果，以及我该怎样试用。
```

每完成一个任务，看三件事：

1. 结果是不是你想要的，有没有顺手加了不需要的功能？
2. AI 实际做了哪些检查，还有什么没检查？
3. 新做出的重要决定，是否已经写回项目文件？

可以请另一个 AI 或工程师检查改动，再继续下一项。写代码的许可不自动等于上线或删除正式数据的许可，这些操作按你们约定的权限处理。

## 按产品形态组合默认方案

你不需要挑选内部模板。告诉 AI 你要做的是客户记录、审批流程、聊天助手，还是只在自己电脑上运行的小工具，它会选取相关说明。

项目已有技术方案时，优先沿用。新项目才会参考内置建议：例如网站可考虑 TypeScript/PostgreSQL，本地个人工具可考虑 Python/SQLite。它会解释为什么适合你，并记录需要调整的地方。

这些是起点，具体选择仍取决于你的需求。

## 核心原则

你决定要解决什么问题；AI 按确认的范围做事；每一步都要检查。以后还会用到的重要说明，保存在项目里。

## 仓库结构

<details>
<summary>展开文件目录和开发者参考资料</summary>

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
   │  ├─ rookie-onboarding.md          # 给第一次做软件产品的人的概念入门
   │  ├─ bootstrap-question-bank.md    # 该问什么问题
   │  ├─ cross-agent-compatibility.md  # Codex / Cursor / Claude Code 适配映射
   │  ├─ governance-asset-guide.md     # 长期 vs 一次性资产、提升规则
   │  ├─ anti-patterns.md              # 常见的治理反模式
   │  ├─ task-sizing.md                # 量化的 bounded task 限制
   │  ├─ retrofit-mode.md              # 把治理引入 legacy 仓库
   │  ├─ governance-evolution.md       # 版本演进、ADR、归档
   │  ├─ minimal-mode.md               # 单人 / 极简项目的轻量模式
   │  ├─ wiki-record-crud-apps.md      # 记录型应用工程 wiki
   │  ├─ wiki-linear-workflows.md      # 线性 / 持久化流程工程 wiki
   │  ├─ wiki-conversational-assistants.md # 对话助手工程 wiki
   │  ├─ product-pattern-routing.md    # profile/module/recipe 选择
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
   │  ├─ module-overlays/               # 可组合的治理与 contract 片段
   │  ├─ templates/                     # 被提及时静默取用的 MVP 表面模板
   │  ├─ contracts-examples/           # 填好的 OpenAPI / JSON Schema / event / SQL / CLI / 文件格式范例
   │  └─ examples/
   │     └─ feedback-inbox/            # 完整填好的样例项目
   └─ scripts/
      ├─ check-governance.sh           # 检查项目说明是否有漏项
      └─ test_check_governance.py       # 检查脚本的自动测试
```

</details>

## 关于那条校验警告（WARN）

技能带有一个检查脚本，帮助找出项目说明中的漏项：

- `ERROR`：有需要修正的问题，例如任务没有写检查方法。
- `WARN`：需要留意的提醒，由你或 AI 判断怎样处理。
- `OK`：本次文档结构检查未发现错误。

**通过这项检查，不代表软件已经测试通过或可以上线。** 它不会替你运行任务中的命令，也不检查轻量模式的 `docs/PLAN.md`；这些需要另外核实。没有找到文件时，它会明确提醒。

样例中的“规则重复”警告，意思是有些说明在多个工具文件里各写了一遍。旧项目可以保留确有用途的副本，但修改时要保持一致；新项目优先共用 `AGENTS.md`。

如果你不熟悉命令，让 AI 运行并解释结果即可。维护本技能的开发者可以运行：

```bash
bash constitution-skill/scripts/check-governance.sh constitution-skill/assets/examples/feedback-inbox
python3 constitution-skill/scripts/test_check_governance.py
```

## 许可证

MIT License。随便用、fork、改造，让你的编码智能体少一点混乱，多一点秩序。
