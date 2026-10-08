# Rookie Onboarding

[English](rookie-onboarding.md) · [繁體中文（香港）](rookie-onboarding_HK.md)

先简要介绍 Flash，再为“第一次做软件产品的人”介绍 Standard 的概念。如果你是产品经理在启动新项目、做副业项目的人、想跨行做软件的领域专家，或者只是刚开始接触软件产品的种种组成部分，这份文档对你都有帮助。

你不需要会写代码也可以使用 constitution skill。但你会在它生成的文件里遇到下面这些概念。这页的目的，是让你用 15 到 20 分钟把每个概念都建立一个工作印象，让 skill 后面的内容读起来像工具，而不是一堵术语墙。

它不是把术语藏起来的字典，而是一份让术语变得平易近人的短读物。

## 先选合适的工作结构

**已经明确的小任务**可以直接执行和检查，不必先做启动问答。**Standard** 保留下面第 1–10 节介绍的完整软件项目流程。**Flash** 是日常工作、研究、文档、软件和技能等可复用能力的统一轻量入口。

Flash 先整理简短的任务约定：目标、使用者或读者、背景、范围、约束、可观察的完成标准，以及重要未知项。预期结果说明要达到什么，实施计划说明怎样做；计划可以随新发现调整。

AI 按需选择可选组件：**行为**（输入、输出、示例）、**证据与判断**（来源、标准、不确定性）、**内容与结构**（读者、组织方式、格式）和**行动**（步骤、依赖、结果检查）。同一任务可以组合多个组件；它们不是互斥模式，也不是必须各建一份文件。

持续维护的项目默认使用 `AGENTS.md` 加一份 `PLAN.md` 或简报，常见位置是 `docs/PLAN.md`。聊天、现有任务、`SKILL.md` 或 schema 引用已经提供所需背景时，可以直接沿用。检查实际结果是否符合任务约定，不能只看计划里的步骤是否都尝试过。

详见 [Flash 指南](flash-mode.md)、[组件说明](flash-components.md)和[场景示例](flash-scenarios.md)。文件有帮助时，可以选用 [AGENTS.md](../assets/flash-templates/AGENTS.md) 和 [PLAN.md](../assets/flash-templates/PLAN.md) 模板。

## Standard 阅读顺序

整页快速浏览一遍。当你在生成的治理文件里遇到某个词时，再回到这里精读对应小节。

## 1. Spec, Architecture, Rules, Contracts

这是 Standard 帮你产出的四类长期文档，分别回答四个不同的问题。

- **Spec** 回答的是：*这个产品给用户做了什么？*
  目标、用户、非目标、acceptance criteria。这里不写代码。
- **Architecture** 回答的是：*产品内部有哪些组成部分？它们怎么拼起来？*
  模块、数据流、技术选择、部署形态。是决策，不是观点。
- **Rules** 回答的是：*在这个代码库里，每个改动都需要遵守哪些东西？*
  对这个仓库有意义的编码风格、testing 期望、安全边界。
- **Contracts** 回答的是：*产品内部不同部分之间、或产品与外部之间，有哪些稳定的接口？*
  API 形状、数据库表结构、event payload、文件格式。

一个有用的画面：Spec 是产品手册，Architecture 是户型图，Rules 是房屋规范（电路、水管），Contracts 是门框——所有要穿过去的东西必须符合尺寸。

## 2. Schema 和 Migration

**Schema** 是你的产品存储的数据的"形状"。比如一张 `feedback` 表，含有 `id`、`source`、`message`、`created_at` 这几列，就是一个 schema。Schema 通常住在 database 里。

**Migration** 是用来改 schema 的一段脚本。比如"给 `feedback` 表加一列 `tags`"。

两件需要知道的事：

- 一旦产品上了线、有了真实用户，每一次 schema 改动都会动到他们的数据。加一列通常是安全的；改变某列的含义、删除某列、给某列改名，往往是有风险的。
- 大多数团队的 migration 是只能往前的。错了就写下一个 migration 去修，不会回头改过去的脚本。

因此，新增或改变 schema 的决定需要明确批准。如果已批准的任务已经写清楚这项改动，agent 可以按范围实现，不必为同一决定再次询问。把 migration 应用到正式环境，仍须按独立的操作权限处理。你不需要会写 migration，但需要能看出别人正在做这件事。

## 3. APIs 和 Contracts

**API**（Application Programming Interface）是一段程序与另一段程序交流的方式。最常见的形态是 web API：一段程序发出一个 HTTP request，另一段程序返回一个 JSON response。

**Contract** 是对 API 形状的精确描述，细到两个团队可以各自开工还对得上。Contract 通常说明：

- URL（向哪里发 request）。
- request 的形状（有哪些字段、类型是什么、哪些是必填）。
- response 的形状（成功是什么样、失败是什么样）。
- error envelope（错误长什么样）。

为什么这在做产品时重要：一旦任何外部系统（你自己的 mobile app、Zapier 集成、合作方）开始依赖你的 API，改 API 就是要付代价的。把 contract 文件当成真相源，先改 contract，再改代码。

## 4. Authentication 和 Authorization

两件经常被混在一起、但完全不同的事。

- **Authentication（authn）** 回答的是："你是谁？"
  登录流程、session、token、密码重置。
- **Authorization（authz）** 回答的是："你被允许做什么？"
  "只有 team owner 可以删除 workspace"。"免费用户每月最多看 10 条 feedback"。

两者都很微妙，都容易做错。最常见的失败方式是：用户之间数据泄露，或者意外地放开了过多权限。因此，新增或改变 authn / authz 的决定需要明确批准，哪怕看起来只是小改动。已批准的任务覆盖其写明的实现范围；范围或风险改变时才需要再次确认，相关安全检查仍要完成。

## 5. Bounded Task 和 Vertical Slice

**Bounded task** 是一项有明确结果、约定范围和检查方法的工作，别人能把它作为一个完整改动来 review。5 个文件或约 300 行代码改动这样的数量，只用于提醒检查难度，不是硬限制，也不是自动停工的理由。拆分能降低风险或更容易验证时再拆；如果拆开会让结果前后不一致，就把相关改动放在一起。所有必要检查都要运行，即使超过 3 条命令。

**Vertical slice** 是一段贯穿整个技术栈的产品工作：一小段 UI 改动 + 对应的 API 改动 + 对应的 database 改动，作为一个整体交付，端到端能跑通。

这两个概念都帮助你定义一个可检查、可 review 的结果，避免混入无关工作。完整的 vertical slice 可以跨多个文件或技术层，仍然是一个合理的任务。当 skill 让你写一个 task 文件时，你就在练这个习惯。

## 6. 环境：Production、Staging、Development

一个现代软件产品通常会在三个地方运行。

- **Development** 在你的电脑上。东西可以随便坏。没有真实用户。
- **Staging** 是 production 的一份副本，跑在云上，长得像 production，但里面是测试数据。用来在面对真实用户之前先验证。
- **Production** 是真正运行的产品。真实用户。真实数据。真实后果。

Production 部署需要明确授权，因为出问题的影响面太大。获准实现或测试某项改动，不等于获准上线。绝大多数粗心错误会被 staging 拦住；穿到 production 的，才是真正重要的那批。

你会在 `ARCH.md` 和部署文件里看到这三个名字。它们之所以分开，纯粹是为了安全。

## 7. Reversible vs Irreversible 决策

有些决策撤销几乎没成本。有些撤销代价非常大。

- Reversible：换字体、给按钮起名、函数内部用哪种循环。
- Irreversible（或撤销很贵）：database 结构、public API 的 URL、authentication 模型、支付供应商集成、用户删除如何处理、数据保留策略。

Skill 的 "Approval Required" 清单标出了风险高或难以撤销的决定。Agent 不能在这些领域独自做出新决定。你已批准某个决定及其实现范围后，不必为同一决定反复确认；范围变化、风险变化和独立的操作权限仍要留意。

一个好习惯：每当 agent 准备做一个选择，问一句"如果这选错了，以后改回去有多痛？"——答案是"很简单"，就放手让 agent 跑；答案是"很痛"或"我们要给用户做迁移"，就暂停。

## 8. Tests 和 Verification

**Test** 是一段小程序，用来证明另一段代码的行为符合预期。比如："如果我提交一条没有 message 的 feedback，API 应该返回 400 错误。" 每次代码改动后，tests 会被自动跑一次。

Tests 做两件事：

- 抓 regression：原本能跑、后来跑不通的代码。
- 给"这个 task 算不算做完了？"一个诚实的答案。

在 Standard 里，每个 task 文件都有 `## Verification` 段落，写着具体的执行命令。这些命令通常包含 tests。你不需要自己写 tests，但应该坚持：verification 没跑过，task 不算完。

## 9. Review

**Review** 是另一个人（或另一个 agent）在改动被合并进代码库之前先读它。Reviewer 会问四个问题：

- 这个改动是否做了 task 说要做的事？
- 它有没有破坏原本能跑的东西？
- 它有没有越过 `ARCH.md` 和 `RULES.md` 里列的边界？
- 它有没有在没批准的情况下碰了 "Approval Required" 列表里的东西？

Codex、Cursor 或 Claude Code 都可以实现任务或检查改动。按现有工具和实际工作选择角色，不固定分配给某个工具。Review 应该查看证据、发现问题；重要决定和合并仍须遵守项目的人类审批规则。

## 10. The Promotion Habit

这是 skill 想让你养成的最重要的一个习惯——而且它不是技术习惯。

任何时候，当你发现自己在向 AI agent、向队友、甚至向"过几天的自己"，**重复解释同一件事**——把它写进一份长期文件里。一般规则：

- 在 code review 里说过两次的事 -> 写进 `RULES.md`。
- 关于接口说过两次的事 -> 写进 `docs/CONTRACTS/`。
- 关于产品该怎么行为说过两次的事 -> 写进 `docs/SPEC.md`。
- 向 agent 说过两次的事 -> 写进 `AGENTS.md`。

重点不是繁文缛节，重点是：**任何你需要重复解释的东西，下一个人（或下一个 agent，或未来的你）在没人告诉他的时候是不会知道的。**

## Standard 接下来怎么做

读完这一遍之后：

- 打开 `references/governance-asset-guide.md`，那里对文件家族有更长的描述。
- 打开 `assets/examples/feedback-inbox/` 这个完整样例，把每个文件翻一遍。不要试图全懂，先感受每份文件的形状。
- 当 skill 让你写 task 文件时，去看 `assets/examples/feedback-inbox/docs/TASKS/001-bootstrap-feedback-inbox.md`——那是"好"的样子。

Skill 后面会不断引用这些概念。哪个词陌生了，再回到这里。做过几个项目之后，你就不需要这份文档了。
