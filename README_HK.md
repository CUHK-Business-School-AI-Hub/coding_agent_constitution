<div align="center">

# Coding Agent Constitution

**先把軟件想法說清楚、寫下來，再讓 AI 一步步做出來。**

[English](README.md) · [簡體中文](README_CN.md)

[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-SKILL.md-111827)](#)
[![Codex](https://img.shields.io/badge/Codex-compatible-10a37f)](#)
[![Cursor](https://img.shields.io/badge/Cursor-compatible-5b5bf7)](#)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-d97706)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

</div>

---

## 最近更新 - 2026-09-12

- 檢查更可靠：修復了「任務漏寫重要段落，也可能顯示通過」的問題，並加入自動測試。
- 使用更順暢：已經確認的任務，不再為同一個決定反覆詢問；實作和檢查可以交給你常用的 AI 工具。
- 安裝說明已更新：通用規則盡量只寫一份，有需要才增加工具專用檔案。
- 文檔更易讀：減少術語，補充可以直接複製使用的提示詞。

## 最近更新 - 2026-06-30

- 做重要技術選擇時，會寫清楚有哪些方案、推薦哪個，以及日後是否容易調整。
- 產生檔案後，會檢查有沒有說不清楚、互相矛盾或遺漏的地方。
- 每個任務會寫明：要做甚麼、哪些地方可以改，以及怎樣檢查是否完成。

## 這是甚麼？

這是一個給 **Codex、Cursor、Claude Code** 使用的免費開源技能（Agent Skill）。你可以把它理解成一份給 AI 用的工作指南。

例如你說：

> 我想做一個工具，幫小團隊收集客戶意見，但不知道從哪裏開始。

它會先幫你理清三個問題：**給誰用、先做甚麼、做到怎樣算完成**，再把答案儲存在項目資料夾。日後換一個對話、換一個 AI，或者交給工程師，都能接着做。

通常會得到這些檔案，你不需要先學會它們的名稱：

| 檔案 | 簡單解釋 |
| --- | --- |
| `SPEC.md` | 要做甚麼，暫時不做甚麼 |
| `ARCH.md` | 各部分怎樣配合，為甚麼這樣選技術 |
| `RULES.md` | 開發時要遵守的規則 |
| `CONTRACTS/` | 不同部分交換資料時，約定好格式和行為 |
| `TASKS/` | 下一步要完成的小任務，以及檢查方法 |
| `AGENTS.md` | 給 AI 的項目說明 |

檔案數量會按項目情況調整，小型個人項目可以只保留兩份主要檔案。有需要時，還會為你使用的工具產生讀取說明。

想了解這些概念，可以看[第一次做軟件產品的入門說明](constitution-skill/references/rookie-onboarding_HK.md)，也可以直接看下面的快速開始。

## 為甚麼需要它？

直接請 AI 寫程式，有時會遇到這些問題：

- 需求還未想清楚，就已經做了很多功能。
- 換一個對話或工具，又要從頭解釋。
- 不知道 AI 按甚麼要求做，也不知道怎樣檢查結果。

這個技能先把需求和重要決定寫下來，再拆成小任務。每做完一步，檢查結果，有用的新發現也寫回項目檔案。

## 適合邊個用？

適合已經有一個軟件想法，想請 AI 幫忙實現、又希望事情保持清楚的人，例如：

- 準備啟動新項目的產品經理。
- 做個人項目、日後可能找人合作的你。
- 想把工作經驗做成工具的設計師、分析師或營運人員。
- 不會寫程式，但希望能看懂計劃、提出修改意見的創業者。
- 想讓 AI 按明確要求工作的工程師。

你負責說明需求、檢查結果，並決定重要取捨；AI 幫你整理檔案和拆分任務。

## 甚麼時候適合用？

適合在想法還不清楚、不知道先做哪一步，或者準備把項目交給別人接手時使用。

如果只是改錯字、修一個已經明確的小問題，直接讓 AI 修改就可以，不需要每次重新整理整個項目。重要的產品選擇仍由你決定。

## 幾時應該停止用？

當項目已有清楚的計劃、工程師或團隊能接着維護時，就不必每次都使用這個技能。已經整理好的檔案可以繼續使用。

日後遇到新的模糊需求，再請它幫忙整理即可。

## 三大智能體兼容方式

**選你已經在用的工具就可以，不需要同時安裝三個。** 三者都可以實作任務或檢查改動。

| 工具 | 怎樣讀取項目說明 |
| --- | --- |
| Codex | 讀取 `AGENTS.md` |
| Cursor | 目前版本可直接讀取 `AGENTS.md`；有特別需要才加專用規則 |
| Claude Code | 透過 `CLAUDE.md` 讀取共享說明 |

通用規則盡量只保留一份，避免改了一處、忘了另一處。已有項目的專用規則會保留。[詳細兼容說明](constitution-skill/references/cross-agent-compatibility.md)供需要設定工具的讀者參考。

## 快速開始（推薦）

先打開你的項目資料夾，再把這段話發給 AI：

```text
請安裝這個倉庫裏的 constitution-skill 技能：
https://github.com/CUHK-Business-School-AI-Hub/coding_agent_constitution
請按我正在使用的工具選擇安裝位置，並檢查能否找到這個技能。
```

安裝後開一個新對話，試着發送下面「最簡單的使用方式」裏的提示詞。如果找不到技能，請讓 AI 檢查安裝位置。

## 可選聯動 Skill：`waymark`

如果你想先透過一問一答把想法講清楚，可以使用我們團隊開發的 [Waymark](https://github.com/CUHK-Business-School-AI-Hub/waymark)。它是 `grill-me` 的變種，對非技術人士更友善：你用日常語言描述工作，它會逐個提問，幫你理清誰來做、怎樣做、遇到例外怎樣處理，再整理成可以跟着執行的說明。

如果接下來想把這套流程做成軟件，再交給 `constitution-skill` 整理項目計劃和開發任務。Waymark 是可選輔助，不是必須安裝的依賴。

配合使用時可以說：

```text
先用 waymark 幫我把實際工作流程和需求問清楚，用淺白文字解釋需要我決定的地方。
如果確定要做成軟件，再用 constitution-skill 把確認的內容寫成項目計劃和第一個小任務。
```

## 如果你想自己動手安裝...

以下命令假設你已下載本倉庫，並在倉庫根目錄打開終端，適用於首次安裝。如果已經安裝過，請讓 AI 先比較版本，避免覆蓋自己的修改。

### Codex

安裝到你的個人技能目錄：

```bash
mkdir -p ~/.agents/skills
cp -R constitution-skill ~/.agents/skills/constitution-skill
```

如果只想在一個項目裏使用，把技能複製到目標項目的 `.agents/skills/constitution-skill/` 即可。

### Cursor

把 `constitution-skill/` 複製到目標項目的 `.agents/skills/` 資料夾。這裏已有 Codex 的項目副本時，目前 Cursor 版本可以共用；也仍可使用 `.cursor/skills/`。

### Claude Code

把 `constitution-skill/` 複製到目標項目的 `.claude/skills/` 資料夾。共享項目說明時，`CLAUDE.md` 可以用這一行讀取：

```markdown
@AGENTS.md
```

安裝後開一個新對話，檢查技能是否可用。已有安裝能正常使用時，先核實工具支援的位置，再決定是否遷移，不必重複複製。

## 最簡單的使用方式

把下面的例子換成你的想法即可：

```text
我想做一個給小團隊用的客戶意見收集工具，能整理大家最常提的需求。
我不懂設計技術方案。
請用 constitution-skill 先幫我說清楚第一版做甚麼、不做甚麼，
把計劃儲存在項目裏，再列出第一個小任務和檢查方法。
需要我決定的地方，請用淺白文字解釋；先不要寫應用程式碼。
```

你會得到一份能查看和修改的項目計劃，以及下一步任務。一般項目的檔案通常放在 `docs/` 下；小型個人項目可能只需要 `AGENTS.md` 和 `docs/PLAN.md`。

先看看它有沒有理解你的意思，尤其是「暫時不做甚麼」和「怎樣算完成」。不對的地方，直接讓 AI 改。

## 文件生成之後，怎樣真正開始實現？

確認計劃後，先做第一個小任務。可以直接對 AI 說：

```text
請找到計劃裏的第一個任務，向我說明它要實現甚麼。
按照我們已經確認的範圍完成它，執行相應檢查。
如果需要新增重要決定或超出範圍，先告訴我原因。
完成後，請用淺白文字說明做了甚麼、檢查結果，以及我該怎樣試用。
```

每完成一個任務，看三件事：

1. 結果是不是你想要的，有沒有順手加了不需要的功能？
2. AI 實際做了哪些檢查，還有甚麼未檢查？
3. 新做出的重要決定，是否已經寫回項目檔案？

可以請另一個 AI 或工程師檢查改動，再繼續下一項。寫程式的許可不自動等於上線或刪除正式資料的許可，這些操作按你們約定的權限處理。

## 按產品形態組合預設方案

你不需要挑選內部模板。告訴 AI 你要做的是客戶記錄、審批流程、聊天助手，還是只在自己電腦上執行的小工具，它會選取相關說明。

項目已有技術方案時，優先沿用。新項目才會參考內置建議：例如網站可考慮 TypeScript/PostgreSQL，本地個人工具可考慮 Python/SQLite。它會解釋為甚麼適合你，並記錄需要調整的地方。

這些是起點，具體選擇仍取決於你的需求。

## 核心原則

你決定要解決甚麼問題；AI 按確認的範圍做事；每一步都要檢查。日後還會用到的重要說明，儲存在項目裏。

## 倉庫結構

<details>
<summary>展開檔案目錄和開發者參考資料</summary>

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
   │  ├─ wiki-record-crud-apps.md      # 記錄型應用工程 wiki
   │  ├─ wiki-linear-workflows.md      # 線性 / 持久化流程工程 wiki
   │  ├─ wiki-conversational-assistants.md # 對話助手工程 wiki
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
   │  ├─ templates/                     # 被提到時靜默取用嘅 MVP 表面模板
   │  ├─ contracts-examples/           # 填好的 OpenAPI / JSON Schema / event / SQL / CLI / 檔案格式範例
   │  └─ examples/
   │     └─ feedback-inbox/            # 完整填好的樣例項目
   └─ scripts/
      ├─ check-governance.sh           # 檢查項目說明是否有遺漏
      └─ test_check_governance.py       # 檢查腳本的自動測試
```

</details>

## 關於那條校驗警告（WARN）

技能附有一個檢查腳本，幫助找出項目說明中的遺漏：

- `ERROR`：有需要修正的問題，例如任務沒有寫檢查方法。
- `WARN`：需要留意的提醒，由你或 AI 判斷怎樣處理。
- `OK`：本次文檔結構檢查未發現錯誤。

**通過這項檢查，不代表軟件已經測試通過或可以上線。** 它不會替你執行任務中的命令，也不檢查輕量模式的 `docs/PLAN.md`；這些需要另外核實。沒有找到檔案時，它會明確提醒。

樣例中的「規則重複」警告，意思是有些說明在多個工具檔案裏各寫了一遍。舊項目可以保留確有用途的副本，但修改時要保持一致；新項目優先共用 `AGENTS.md`。

如果你不熟悉命令，讓 AI 執行並解釋結果即可。維護本技能的開發者可以執行：

```bash
bash constitution-skill/scripts/check-governance.sh constitution-skill/assets/examples/feedback-inbox
python3 constitution-skill/scripts/test_check_governance.py
```

## 授權

MIT License。放心使用、fork、改造，令你的編碼智能體少一點混亂，多一點秩序。
