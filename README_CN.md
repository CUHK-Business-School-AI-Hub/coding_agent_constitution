<div align="center">

# Coding Agent Constitution

**让 AI 先听懂你要什么再动手，做完了也查得清楚。**

[English](README.md) · [繁體中文（香港）](README_HK.md)

[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-SKILL.md-111827)](#)
[![Codex](https://img.shields.io/badge/Codex-compatible-10a37f)](#)
[![Cursor](https://img.shields.io/badge/Cursor-compatible-5b5bf7)](#)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-d97706)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

</div>

> 最近更新（2026-10-08）：新增轻量的 Flash 模式，重写了新手入门说明，还新增了一份新手词典。更早的变化见[更新记录](#更新记录)。

## 这是什么？

Coding Agent Constitution 是一个免费开源的技能（skill），给三款 AI 编程工具用：Codex（OpenAI 出品）、Cursor（内置 AI 的代码编辑器）和 Claude Code（Anthropic 出品）。这几款工具可以打开你电脑上某个文件夹里的文件，帮你修改、运行命令、写代码。技能就是一包写给 AI 看的说明，工具遇到相关的请求时会去读它。你可以把它想成新同事入职第一天，你递过去的那本“我们团队是这样干活的”。

装上这个技能以后，AI 在写代码之前会先做些准备：问清楚你想达到什么目的，把你的回答写进项目文件夹，再把工作拆成一个个小步骤，每一步都带着检查办法。下周你回来接着做、开一个新对话，或者换一个 AI 工具，都可以从这些记录接上，不用全靠你自己记着。

你不需要会写代码。你要做的，是说清楚想要什么，读一读 AI 写回来的东西，在重要的地方拍板。

## 它能帮你解决什么问题？

如果你试过直接让 AI “帮我做出来”，下面这些情况你可能不陌生：

- 想法还没想清楚，它已经做了一大堆，还顺手加了你没要的功能。
- 每开一个新对话都从零开始，背景又得从头讲一遍。
- 它说“做好了”，你却不知道它到底检查过什么。
- 过了几个星期，没人记得某个东西当初为什么这么做，包括你自己。

这个技能把计划和重要决定写成普通的文本文件，放在你的项目里。你自己、一个新对话、另一个 AI 工具，或者以后加入的工程师，打开这些文件就能知道事情做到了哪一步。

## 按需要选择工作方式

这个技能有两种工作方式，也知道什么时候不该插手。

| 你的需求 | 会发生什么 | 例子 |
| --- | --- | --- |
| 一个已经说清楚的小改动 | AI 直接改，做相应的检查，不走规划流程 | “把注册页上的错别字改掉。” |
| Flash：日常工作，需要先理一理 | AI 先写一份简短的任务约定，只补充这个任务用得上的结构 | “帮我们团队比较三种收集客户意见的方法。” |
| Standard：一个正式的软件项目 | AI 先把想法问清楚，写出整套项目文档，再规划一个个小任务 | “我想做一个帮小团队收集客户意见的工具，但不知道从哪儿开始。” |

这些名字不用记。说清楚你要什么、希望 AI 帮到什么程度，它会自己选一种方式，并用一两句话告诉你为什么。如果你手上已经有一套代码，但没有这些文档，还有一个 Retrofit（补建）模式：从你马上要改的那部分代码开始，一点点把文档补上。

### Flash 是怎样工作的

Flash 适合日常工作、调研、写文档、做小软件，也适合做可以反复使用的能力，比如技能。它从一份简短的任务约定开始（文档里叫 task contract），写清楚这几件事：

- 目标是什么，结果给谁用
- 背景情况，要用到哪些材料
- 哪些在范围内，哪些不做
- 限制条件，比如截止时间、格式、预算
- 做到什么程度算完成，怎么检查
- 还没想清楚的问题，以及暂时的假设

约定定下来的是“怎样才算成功”。至于怎么做到，可以边做边调整，但不能悄悄降低标准，也不能为了迁就做法把目标换掉。

根据任务的需要，AI 可能再补充下面一种或几种细节：

- 行为：用在会反复运行的东西上，比如脚本、软件功能或技能。输入什么、输出什么、举几个例子、遇到错误的输入怎么办。
- 证据与判断：用在调研和给建议上。要回答哪些问题、用哪些来源、按什么标准比较、结论有几成把握。
- 内容与结构：用在文档、幻灯片和消息上。写给谁看、最想说的是什么、提纲和格式。
- 行动：用在真正要改动某样东西的时候，比如改会议时间、更新一条记录、发出一份报告。具体改什么、事先要满足什么条件、按什么顺序做、怎么确认真的改好了。

一个任务可以同时用到好几种，而且哪一种都不要求单独建文件。很多时候，在对话里说清楚就够了。如果是持续进行的项目，通常从一个 `AGENTS.md` 文件加一份简短的任务简报开始，简报常放在 `docs/PLAN.md`。

想了解更多，可以看 [Flash 指南](constitution-skill/references/flash-mode.md)、[组件说明](constitution-skill/references/flash-components.md)和[场景示例](constitution-skill/references/flash-scenarios.md)（这三份是英文）。可选的起步模板有 [AGENTS.md](constitution-skill/assets/flash-templates/AGENTS.md) 和 [PLAN.md](constitution-skill/assets/flash-templates/PLAN.md)。

### Standard 是怎样工作的

Standard 是做软件项目的完整流程。AI 会先问你要解决什么问题、给谁用、第一版必须做到什么，然后把下面这类文件写进你的项目，一般放在 `docs/` 文件夹里。这些文件名不用提前背。

| 文件 | 里面写什么 |
| --- | --- |
| `SPEC.md` | 要做什么、给谁用、这一版先不做什么 |
| `ARCH.md` | 各个部分怎么配合，为什么选这些技术 |
| `RULES.md` | 每次改动都要遵守的规则，包括测试和安全方面的 |
| `CONTRACTS/` | 各部分之间传递数据的精确约定，比如接口和数据库的格式 |
| `DECISIONS/` | 很难反悔的大决定，以及当时比较过哪些方案 |
| `TASKS/` | 接下来的一个个小任务，每个都带着检查办法 |
| `AGENTS.md` | 写给所有 AI 工具的项目说明 |

具体有哪些文件，看项目情况而定。想看看写好之后是什么样子，可以打开 [Feedback Inbox](constitution-skill/assets/examples/feedback-inbox/)，这是一个所有文件都已填好的样例项目。

## 快速开始

先在你的 AI 编程工具里打开项目文件夹。项目文件夹就是你电脑上的一个普通文件夹，用来放这个项目的所有文件。如果是从零开始，新建一个空文件夹就行。

然后把下面这段话发给 AI：

```text
请安装这个仓库里的 constitution-skill 技能：
https://github.com/CUHK-Business-School-AI-Hub/coding_agent_constitution
请按我正在使用的工具选择安装位置，并检查能否找到这个技能。
```

装好以后，新开一个对话，让工具加载这个技能，再试试下一节的提示词。如果 AI 说找不到技能，请它查一下装到了哪里。

## 第一句话可以这样说

如果要做一个正式的软件项目（Standard），把下面的例子换成你自己的想法：

```text
我想做一个给小团队用的客户意见收集工具，能整理大家最常提的需求。
我不会设计技术方案。
请用 constitution-skill 的 Standard 模式，先帮我说清楚第一版做什么、不做什么，
把计划保存在项目里，再列出第一个小任务和检查方法。
需要我决定的地方，请用简单的话解释；先不要写应用代码。
```

AI 会问你一些问题。回答“我不知道”完全没问题，它应该给出一个稳妥的默认选择，并把它记成“假设”。最后你会拿到一份能看懂、能修改的计划，以及第一个任务。

继续之前，先把计划读一遍。最值得看的是两处：第一版“暂时不做什么”，以及“怎样算完成”。哪里不对，用你自己的话告诉 AI，让它改文件。

如果是轻一点的任务（Flash），可以改用这段：

```text
请用 constitution-skill 的 Flash 模式，帮我比较三种收集客户意见的方法。
结果是给我们的小产品团队看的。请用我提供的笔记，并指出还缺哪些重要证据。
先说清楚比较的范围，以及一份有用的比较需要讲明白什么，再按这个任务的需要选择组件。
把“要达到的结果”和“可以边做边调整的步骤”分开写。
先在这个对话或已有的简报里整理；如果建一个项目文件能方便以后复用，再建。
```

## 计划写好以后，怎么真正做出来？

对计划满意以后，就一个任务一个任务地做。可以这样对 AI 说：

```text
请找到计划里的第一个任务，向我说明它要实现什么。
按照我们已经确认的范围完成它，运行相应检查。
如果需要新增重要决定或超出范围，先告诉我原因。
做完后，请用简单的话说明做了什么、检查结果，以及我该怎样试用。
```

AI 汇报回来以后，看三件事：

1. 这是你想要的吗？有没有加了你没要的东西？
2. 它实际检查了什么，还有什么没检查？
3. 如果它做了新的重要决定，有没有写回项目文件？

进入下一个任务之前，可以请另一个 AI 工具或者工程师帮忙检查一遍改动。你同意它做某个任务，不等于同意它把东西上线，也不等于同意它删除真实数据。这些操作要按你们事先约定的权限来。

## 你和 AI 怎么分工

你决定要解决什么问题，那些改起来代价很大的决定也由你来拍板。AI 负责提问、写计划、一小步一小步地做，并告诉你它检查了什么。项目文件记下所有决定，重要的东西不会只留在某个聊天窗口里。

## 看不懂那些词？

有两份文档是专门写给没有技术背景的人的：

- [新手入门说明](constitution-skill/references/rookie-onboarding_CN.md)：一个项目大概怎么走，每个文件是干什么的，每一步可以对 AI 说什么。
- [新手词典](constitution-skill/references/rookie-wiki_CN.md)：用几句大白话解释做应用时常见的词，从 API、数据库，到部署和 Git。

遇到看不懂的词，也可以直接问 AI：“假设我从来没写过代码，用一个生活里的例子给我解释一下。”

## 常见产品的默认方案

你不用自己挑模板，也不用自己选技术。告诉 AI 你要做的是什么，比如客户名单、审批流程、聊天助手，或者只在自己电脑上用的小工具，技能会自动找来对应的说明。

如果你的项目已经用了某些技术，AI 会优先沿用。新项目则有几个经过检查的起点，比如网站可以用 TypeScript 加 PostgreSQL，只在自己电脑上跑的小工具可以用 Python 加 SQLite。它会解释为什么适合你，并把调整记下来。这些只是起点，最后还是看你的需求。

## 可选搭档：Waymark

如果你想在规划软件之前，先把想法聊清楚，可以试试我们团队开发的 [Waymark](https://github.com/CUHK-Business-School-AI-Hub/waymark)。它是 `grill-me` 的一个变种，对非技术背景的人更友好。你用日常的话描述自己的工作，它一次只问一个问题：谁来做、实际怎么做、出了岔子怎么办。最后，它会整理出一份大家照着就能执行的说明。

如果接下来决定把这套流程做成软件，就交给 `constitution-skill` 写项目计划和开发任务。Waymark 是可选的，不装它也能用这个技能。两个一起用时，可以这样说：

```text
先用 waymark 帮我把实际工作流程和需求问清楚，用简单的话解释需要我决定的地方。
如果确定要做成软件，再用 constitution-skill 把确认的内容写成项目计划和第一个小任务。
```

## 用哪个 AI 工具？

用你手上已经有的那个就行，不需要三个都装。哪一个都可以做任务，也可以检查改动。

| 工具 | 怎样找到项目说明 |
| --- | --- |
| Codex | 读取 `AGENTS.md` |
| Cursor | 当前版本会读取 `AGENTS.md`；确实需要时，再加 Cursor 专用规则 |
| Claude Code | 当前版本可以自己找到 `AGENTS.md`；加兼容入口之前，先看看已有的 Claude 专用文件 |

通用规则只写在一份 `AGENTS.md` 里，这样改一条规则时，不会在别处留下过时的副本。新项目默认用这个共享文件。已有项目里的专用规则会保留，仍然有用的 Claude 专用说明也一样。具体怎么配置，见[兼容说明](constitution-skill/references/cross-agent-compatibility.md)（英文）。

## 自己动手安装

上面“快速开始”里的那段话是最省事的办法。如果你想自己装，先下载这个仓库，在仓库最外层的文件夹里打开终端（就是那个输入命令的窗口）。下面的步骤适用于第一次安装。如果你之前装过，请先让 AI 比较一下两个版本，免得覆盖你自己改过的内容。

### Codex

装到你的个人账户下：

```bash
mkdir -p ~/.agents/skills
cp -R constitution-skill ~/.agents/skills/constitution-skill
```

如果只想在某一个项目里用，就把技能复制到那个项目的 `.agents/skills/constitution-skill/` 文件夹。

### Cursor

把 `constitution-skill/` 复制到目标项目的 `.agents/skills/` 文件夹。如果这里已经有给 Codex 用的项目副本，当前版本的 Cursor 可以直接共用。放在 `.cursor/skills/` 也可以。

### Claude Code

把 `constitution-skill/` 复制到目标项目的 `.claude/skills/` 文件夹，共享的项目说明仍然放在 `AGENTS.md`。当前版本的 Claude Code 可以自己找到 `AGENTS.md`，但如果项目或者上级文件夹里已经有 Claude 的入口文件，这个功能可能会被关掉。所以先看看你装的版本在这个项目里实际读取了什么，详见[兼容说明](constitution-skill/references/cross-agent-compatibility.md)和 [Claude Code 官方文档](https://code.claude.com/docs/en/memory#agentsmd)。

只有项目确实需要兼容入口时，才加一个简短的 `CLAUDE.md` 来导入共享文件，已有的 Claude 专用规则要保留：

```markdown
@AGENTS.md
```

装好以后，新开一个对话，确认技能可以用。如果原来的安装已经能正常工作，先查清楚工具支持哪些位置，再决定要不要挪，没必要多复制几份。

## 什么时候可以不用它了？

当项目已经有清楚的计划，也有工程师或团队能接手维护，就不必每次改动都调用这个技能了。它写下的那些文件会继续为项目服务。以后遇到新的、还没想清楚的需求，再请它出来帮忙整理。

## 关于检查脚本（ERROR、WARN、OK）

技能里带着一个检查脚本，用来找出 Standard 项目文档里漏掉的东西，比如某个任务没写检查办法。它会给出三种结果：

- `ERROR`：有地方需要改。
- `WARN`：有地方值得看一眼，由你或 AI 决定怎么处理。
- `OK`：这次文档结构检查没有发现问题。

通过这项检查，不代表软件能用、测试通过了，或者可以上线了。脚本不会去运行任务里写的命令，也判断不了 Flash 的任务约定或计划写得好不好。在 Flash 模式下（`--mode flash`），它会检查共享的说明文件和引用，并且总会多给一条 WARN，提醒你另外检查任务本身。如果一个项目文件都没找到，它也会直说。

如果已有的工具专用文件重复了共享规则，或者 Claude 专用的入口文件让 Claude Code 找不到 `AGENTS.md`，脚本也可能发出警告。看看这些文件还需不需要：有用的专用规则留着，确实需要兼容入口时，用简短的导入就好。仓库里的样例只用了一份共享的 `AGENTS.md`。

不熟悉命令也没关系，让 AI 帮你运行，再请它解释结果就行。维护这个技能的开发者可以运行：

```bash
bash constitution-skill/scripts/check-governance.sh constitution-skill/assets/examples/feedback-inbox
python3 constitution-skill/scripts/test_check_governance.py
```

## 更新记录

### 2026-10-08

- 新增 Flash，作为日常工作、调研、文档、软件和可复用能力的统一轻量入口；Standard 保留完整的软件项目流程。
- 为没有技术背景的读者重写了这份 README 和新手入门说明，并新增三种语言的新手词典。
- 更新 Claude Code 兼容说明：优先共用 `AGENTS.md`，先确认工具实际读取了什么，再按需要加简短的兼容入口。
- 文件数和代码行数改为提醒检查难度的信号，不再强制拆分任务；放在一起检查更稳妥的相关改动，可以保持完整。
- 保留原有的工作方式：沿用已确认的决定，自己选择谁来实现、谁来检查，验证要求和安全边界照样写清楚。

### 2026-09-14

- 已经说清楚的小修改，不必先走一遍规划流程。
- 少问重复的问题：已有的决定直接沿用，确实有取舍时才比较方案。
- 什么时候停更清楚：只要规划就不写代码；已经同意实施的任务，会做到约定的检查完成为止。和当前任务无关的旧问题单独说明。

### 2026-09-12

- 检查更可靠：修复了“任务漏写重要段落，也可能显示通过”的问题，并加入自动测试。
- 交接更顺：已经确认过的任务，不再为同一个决定反复询问；实现和检查可以交给你常用的 AI 工具。
- 安装说明更新：通用规则尽量只写一份，需要时才增加工具专用文件。
- 文档更好读：少了术语，多了没有技术背景也能直接复制使用的提示词。

### 2026-06-30

- 做重要技术选择时，会写清楚有哪些方案、推荐哪个，以及以后改起来难不难。
- 生成文件之后，会检查有没有说不清楚、互相矛盾或者遗漏的地方。
- 每个任务都会写明：要做什么、哪些地方可以改，以及怎样检查是否完成。

## 仓库结构

<details>
<summary>展开文件目录和开发者参考资料</summary>

```text
.
├─ README.md                          # 英文说明
├─ README_CN.md                       # 本页
├─ README_HK.md                       # 繁体中文（香港）
├─ LICENSE
├─ constitution.md                    # 早期设计笔记
├─ TODO_CASE_DERIVED_EVOLUTION.md     # 等待真实项目验证的改进想法
└─ constitution-skill/
   ├─ SKILL.md                        # 技能的主说明
   ├─ agents/
   │  └─ openai.yaml
   ├─ references/
   │  ├─ rookie-onboarding.md          # 新手入门说明
   │  ├─ rookie-onboarding_CN.md
   │  ├─ rookie-onboarding_HK.md
   │  ├─ rookie-wiki.md                # 新手词典
   │  ├─ rookie-wiki_CN.md
   │  ├─ rookie-wiki_HK.md
   │  ├─ flash-mode.md                 # 跨任务类型的轻量入口
   │  ├─ flash-components.md           # 可选、可组合的任务组件
   │  ├─ flash-scenarios.md            # 组件选择的场景示例
   │  ├─ bootstrap-question-bank.md    # 该问哪些问题
   │  ├─ cross-agent-compatibility.md  # Codex / Cursor / Claude Code 配置
   │  ├─ frontier-model-guidance.md    # portable Astra / Opus authoring guidance
   │  ├─ governance-asset-guide.md     # 长期文件和一次性文件、提升规则
   │  ├─ governance-review-rubrics.md  # 生成文档的就绪检查
   │  ├─ governance-evolution.md       # 版本演进、决策记录、归档
   │  ├─ anti-patterns.md              # 常见的错误做法
   │  ├─ task-sizing.md                # 范围完整、可检查的任务的提醒信号
   │  ├─ task-review-contract.md       # 怎样检查一个做完的任务
   │  ├─ retrofit-mode.md              # 给已有代码补建文档
   │  ├─ product-pattern-routing.md    # profile / module / recipe 选择
   │  ├─ profile-transactional-record-system.md
   │  ├─ module-identity-access.md
   │  ├─ module-llm-boundary.md
   │  ├─ module-deterministic-workflow.md
   │  ├─ recipe-typescript-web-postgres.md
   │  ├─ recipe-local-python-sqlite.md
   │  ├─ wiki-record-crud-apps.md      # 记录型应用的工程笔记
   │  ├─ wiki-linear-workflows.md      # 分步骤流程的工程笔记
   │  └─ wiki-conversational-assistants.md # 对话助手的工程笔记
   ├─ assets/
   │  ├─ flash-templates/              # 可选的 AGENTS.md 和 PLAN.md 起点
   │  ├─ governance-templates/         # Standard 空白模板
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
   │  ├─ module-overlays/              # 针对特定能力的补充片段
   │  ├─ templates/                    # 常见产品类型的隐藏起点
   │  ├─ contracts-examples/           # 填好的 OpenAPI / JSON Schema / event / SQL / CLI / 文件格式范例
   │  └─ examples/
   │     └─ feedback-inbox/            # 完整填好的样例项目
   └─ scripts/
      ├─ check-governance.sh           # 检查项目文档有没有漏项
      └─ test_check_governance.py      # 检查脚本的自动测试
```

</details>

## 许可证

MIT License。随便用、fork、改造，让你的编码智能体少一点混乱，多一点秩序。
