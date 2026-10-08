<div align="center">

# Coding Agent Constitution

**讓 AI 先聽明白你要甚麼才動手，做完也查得清楚。**

[English](README.md) · [简体中文](README_CN.md)

[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-SKILL.md-111827)](#)
[![Codex](https://img.shields.io/badge/Codex-compatible-10a37f)](#)
[![Cursor](https://img.shields.io/badge/Cursor-compatible-5b5bf7)](#)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-d97706)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

</div>

> 最近更新（2026-10-08）：新增輕量的 Flash 模式，重寫了新手入門說明，並新增一份新手詞典。較早的變更見[更新紀錄](#更新紀錄)。

## 這是甚麼？

Coding Agent Constitution 是一個免費開源的技能（skill），供三款 AI 編程工具使用：Codex（OpenAI 出品）、Cursor（內置 AI 的程式碼編輯器）和 Claude Code（Anthropic 出品）。這幾款工具可以打開你電腦上某個資料夾裏的檔案，幫你修改、執行命令、寫程式。技能就是一套寫給 AI 看的說明，工具遇到相關要求時會去讀它。你可以把它想像成新同事上班第一天，你交給他的那本「我們團隊是這樣做事的」。

裝好這個技能之後，AI 寫程式之前會先做些準備：問清楚你想達到甚麼目的，把你的回答寫進項目資料夾，再把工作拆成一個個小步驟，每一步都附帶檢查方法。下星期你回來繼續、開一個新對話，或者換另一個 AI 工具，都可以從這些紀錄接上，不用全靠你自己記住。

你不需要懂得寫程式。你要做的，是講清楚想要甚麼，讀一讀 AI 寫回來的內容，在重要的地方拍板。

## 它可以幫你解決甚麼問題？

如果你試過直接叫 AI「幫我做出來」，以下情況你可能不會陌生：

- 想法還未想清楚，它已經做了一大堆，還順手加了你沒有要求的功能。
- 每開一個新對話都由零開始，背景又要從頭講一次。
- 它說「做好了」，你卻不知道它究竟檢查過甚麼。
- 過了幾個星期，沒有人記得某樣東西當初為甚麼這樣做，包括你自己。

這個技能把計劃和重要決定寫成普通的文字檔案，放在你的項目裏。你自己、一個新對話、另一個 AI 工具，或者日後加入的工程師，打開這些檔案就知道事情做到哪一步。

## 按需要選擇工作方式

這個技能有兩種工作方式，也知道甚麼時候不應插手。

| 你的需要 | 會發生甚麼 | 例子 |
| --- | --- | --- |
| 一個已經講清楚的小改動 | AI 直接修改，做相應檢查，不走規劃流程 | 「把註冊頁面上的錯字改好。」 |
| Flash：日常工作，需要先理順 | AI 先寫一份簡短的任務約定，只補充這個任務用得着的結構 | 「幫我們團隊比較三種收集客戶意見的方法。」 |
| Standard：一個正式的軟件項目 | AI 先把想法問清楚，寫出整套項目文件，再規劃一個個小任務 | 「我想做一個幫小團隊收集客戶意見的工具，但不知道從哪裏開始。」 |

這些名稱不用記。講清楚你要甚麼、希望 AI 幫到甚麼程度，它會自己選一種方式，並用一兩句話告訴你原因。如果你手上已經有一套程式碼，但沒有這些文件，還有一個 Retrofit（補建）模式：由你快要修改的那部分程式碼開始，逐步把文件補上。

### Flash 怎樣運作

Flash 適合日常工作、資料搜集、寫文件、做小型軟件，也適合做可以重複使用的能力，例如技能。它由一份簡短的任務約定開始（文件裏叫 task contract），寫清楚以下幾件事：

- 目標是甚麼，結果給誰用
- 背景情況，要用到哪些資料
- 哪些在範圍之內，哪些不做
- 限制條件，例如截止日期、格式、預算
- 做到甚麼程度才算完成，怎樣檢查
- 未想清楚的問題，以及暫時的假設

約定定下的是「怎樣才算成功」。至於怎樣做到，可以邊做邊調整，但不可以悄悄降低標準，也不可以為了遷就做法而把目標換掉。

視乎任務需要，AI 可能再補充以下一種或幾種細節：

- 行為：用在會重複運行的東西上，例如腳本、軟件功能或技能。輸入甚麼、輸出甚麼、舉幾個例子、遇到錯誤輸入時怎樣處理。
- 證據與判斷：用在資料搜集和提出建議上。要回答哪些問題、用哪些來源、按甚麼標準比較、結論有多大把握。
- 內容與結構：用在文件、投影片和訊息上。寫給誰看、最想表達甚麼、大綱和格式。
- 行動：用在真正要改動某樣東西的時候，例如更改會議時間、更新一條紀錄、發出一份報告。具體改甚麼、事前要符合甚麼條件、按甚麼次序做、怎樣確認真的改好了。

一個任務可以同時用上幾種，而且每一種都不要求另建檔案。很多時候，在對話裏講清楚已經足夠。如果是持續進行的項目，一般由一個 `AGENTS.md` 檔案加一份簡短的任務說明開始，任務說明通常放在 `docs/PLAN.md`。

想了解更多，可以看 [Flash 指南](constitution-skill/references/flash-mode.md)、[組件說明](constitution-skill/references/flash-components.md)和[場景例子](constitution-skill/references/flash-scenarios.md)（這三份是英文）。可選用的起步模板有 [AGENTS.md](constitution-skill/assets/flash-templates/AGENTS.md) 和 [PLAN.md](constitution-skill/assets/flash-templates/PLAN.md)。

### Standard 怎樣運作

Standard 是做軟件項目的完整流程。AI 會先問你要解決甚麼問題、給誰用、第一版必須做到甚麼，然後把以下這類檔案寫進你的項目，一般放在 `docs/` 資料夾。這些檔案名稱不用預先記住。

| 檔案 | 裏面寫甚麼 |
| --- | --- |
| `SPEC.md` | 要做甚麼、給誰用、這一版暫時不做甚麼 |
| `ARCH.md` | 各部分怎樣配合，為甚麼選用這些技術 |
| `RULES.md` | 每次改動都要遵守的規則，包括測試和安全方面 |
| `CONTRACTS/` | 各部分之間傳遞資料的精確約定，例如 API 和數據庫的格式 |
| `DECISIONS/` | 很難反悔的重大決定，以及當時比較過哪些方案 |
| `TASKS/` | 接下來的一個個小任務，每個都附帶檢查方法 |
| `AGENTS.md` | 寫給所有 AI 工具的項目說明 |

實際有哪些檔案，視乎項目情況。想看看寫好之後的樣子，可以打開 [Feedback Inbox](constitution-skill/assets/examples/feedback-inbox/)，這是一個所有檔案都已填好的樣例項目。

## 快速開始

先在你的 AI 編程工具裏打開項目資料夾。項目資料夾就是你電腦上一個普通的資料夾，用來存放這個項目的所有檔案。如果是由零開始，開一個空資料夾就可以。

然後把以下這段話發給 AI：

```text
請安裝這個倉庫裏的 constitution-skill 技能：
https://github.com/CUHK-Business-School-AI-Hub/coding_agent_constitution
請按我正在使用的工具選擇安裝位置，並檢查能否找到這個技能。
```

裝好之後，開一個新對話，讓工具載入這個技能，再試試下一節的提示詞。如果 AI 說找不到技能，請它查一查裝到了哪裏。

## 第一句話可以這樣說

如果要做一個正式的軟件項目（Standard），把以下例子換成你自己的想法：

```text
我想做一個給小團隊用的客戶意見收集工具，能整理大家最常提的需求。
我不懂設計技術方案。
請用 constitution-skill 的 Standard 模式，先幫我說清楚第一版做甚麼、不做甚麼，
把計劃儲存在項目裏，再列出第一個小任務和檢查方法。
需要我決定的地方，請用淺白文字解釋；先不要寫應用程式碼。
```

AI 會問你一些問題。答「我不知道」完全沒問題，它應該提出一個穩妥的預設選擇，並把它記為「假設」。最後你會得到一份看得懂、可以修改的計劃，以及第一個任務。

繼續之前，先把計劃讀一遍。最值得留意的是兩處：第一版「暫時不做甚麼」，以及「怎樣才算完成」。哪裏不對，用你自己的說法告訴 AI，請它修改檔案。

如果是較輕的任務（Flash），可以改用這段：

```text
請用 constitution-skill 的 Flash 模式，幫我比較三種收集客戶意見的方法。
結果是給我們的小型產品團隊看的。請用我提供的筆記，並指出還欠缺哪些重要證據。
先講清楚比較的範圍，以及一份有用的比較需要說明甚麼，再按這個任務的需要選擇組件。
把「要達到的結果」和「可以邊做邊調整的步驟」分開寫。
先在這個對話或現有的任務說明裏整理；如果建立項目檔案方便日後重用，才建立。
```

## 計劃寫好之後，怎樣真正做出來？

對計劃滿意之後，就一個任務接一個任務地做。可以這樣對 AI 說：

```text
請找到計劃裏的第一個任務，向我說明它要實現甚麼。
按照我們已經確認的範圍完成它，執行相應檢查。
如果需要新增重要決定或超出範圍，先告訴我原因。
完成後，請用淺白文字說明做了甚麼、檢查結果，以及我該怎樣試用。
```

AI 匯報之後，看三件事：

1. 這是你想要的嗎？有沒有加入了你沒有要求的東西？
2. 它實際檢查了甚麼，還有甚麼未檢查？
3. 如果它作出了新的重要決定，有沒有寫回項目檔案？

開始下一個任務之前，可以請另一個 AI 工具或者工程師檢查一次改動。你同意它做某個任務，不等於同意它把東西上線，也不等於同意它刪除真實資料。這些操作要按你們事先約定的權限處理。

## 你和 AI 怎樣分工

你決定要解決甚麼問題，那些改起來代價很大的決定也由你拍板。AI 負責發問、寫計劃、一小步一小步地做，並告訴你它檢查了甚麼。項目檔案記下所有決定，重要的東西不會只留在某個聊天視窗裏。

## 看不明白那些詞？

有兩份文件是專門寫給沒有技術背景的人：

- [新手入門說明](constitution-skill/references/rookie-onboarding_HK.md)：一個項目大致怎樣進行，每個檔案有甚麼用，每一步可以對 AI 說甚麼。
- [新手詞典](constitution-skill/references/rookie-wiki_HK.md)：用幾句淺白的話解釋做應用程式時常見的詞，由 API、數據庫，到部署和 Git。

遇到看不明白的詞，也可以直接問 AI：「假設我從來沒寫過程式，用一個日常生活的例子解釋給我聽。」

## 常見產品的預設方案

你不用自己挑選模板，也不用自己選技術。告訴 AI 你要做的是甚麼，例如客戶名單、審批流程、聊天機械人，或者只在自己電腦上用的小工具，技能會自動找來相應的說明。

如果你的項目已經用了某些技術，AI 會優先沿用。新項目則有幾個經過檢查的起點，例如網站可以用 TypeScript 加 PostgreSQL，只在自己電腦上運行的小工具可以用 Python 加 SQLite。它會解釋為甚麼適合你，並把調整記錄下來。這些只是起點，最後仍然取決於你的需要。

## 可選拍檔：Waymark

如果你想在規劃軟件之前，先把想法理清楚，可以試試我們團隊開發的 [Waymark](https://github.com/CUHK-Business-School-AI-Hub/waymark)。它是 `grill-me` 的變種，對非技術背景的人更友善。你用日常的說法描述自己的工作，它每次只問一個問題：誰負責、實際怎樣做、出了問題怎麼辦。最後，它會整理出一份大家跟着就能執行的說明。

如果之後決定把這套流程做成軟件，就交給 `constitution-skill` 寫項目計劃和開發任務。Waymark 是可選的，不裝它也能用這個技能。兩個一起用時，可以這樣說：

```text
先用 waymark 幫我把實際工作流程和需求問清楚，用淺白文字解釋需要我決定的地方。
如果確定要做成軟件，再用 constitution-skill 把確認的內容寫成項目計劃和第一個小任務。
```

## 應該用哪個 AI 工具？

用你手上已有的那個就可以，不需要三個都裝。任何一個都可以做任務，也可以檢查改動。

| 工具 | 怎樣找到項目說明 |
| --- | --- |
| Codex | 讀取 `AGENTS.md` |
| Cursor | 目前版本會讀取 `AGENTS.md`；確實有需要時，才加 Cursor 專用規則 |
| Claude Code | 目前版本可以自己找到 `AGENTS.md`；加入兼容入口之前，先看看已有的 Claude 專用檔案 |

通用規則只寫在一份 `AGENTS.md` 裏，這樣修改一條規則時，不會在別處留下過時的副本。新項目預設使用這個共用檔案。已有項目裏的專用規則會保留，仍然有用的 Claude 專用說明也一樣。具體怎樣設定，見[兼容說明](constitution-skill/references/cross-agent-compatibility.md)（英文）。

## 自己動手安裝

上面「快速開始」那段話是最方便的方法。如果你想自己安裝，先下載這個倉庫，在倉庫最外層的資料夾打開終端機（就是輸入命令的那個視窗）。以下步驟適用於首次安裝。如果你之前裝過，請先讓 AI 比較兩個版本，以免覆蓋你自己改過的內容。

### Codex

安裝到你的個人帳戶：

```bash
mkdir -p ~/.agents/skills
cp -R constitution-skill ~/.agents/skills/constitution-skill
```

如果只想在某一個項目裏使用，就把技能複製到那個項目的 `.agents/skills/constitution-skill/` 資料夾。

### Cursor

把 `constitution-skill/` 複製到目標項目的 `.agents/skills/` 資料夾。如果這裏已有給 Codex 用的項目副本，目前版本的 Cursor 可以直接共用。放在 `.cursor/skills/` 也可以。

### Claude Code

把 `constitution-skill/` 複製到目標項目的 `.claude/skills/` 資料夾，共用的項目說明仍然放在 `AGENTS.md`。目前版本的 Claude Code 可以自己找到 `AGENTS.md`，但如果項目或者上層資料夾已經有 Claude 的入口檔案，這項功能可能會被停用。所以先看看你安裝的版本在這個項目裏實際讀取了甚麼，詳見[兼容說明](constitution-skill/references/cross-agent-compatibility.md)和 [Claude Code 官方文件](https://code.claude.com/docs/en/memory#agentsmd)。

只有項目確實需要兼容入口時，才加一個簡短的 `CLAUDE.md` 來匯入共用檔案，並保留已有的 Claude 專用規則：

```markdown
@AGENTS.md
```

裝好之後，開一個新對話，確認技能可以使用。如果原有的安裝已經運作正常，先查清楚工具支援哪些位置，再決定要不要搬，不必多複製幾份。

## 甚麼時候可以不用它？

當項目已經有清楚的計劃，也有工程師或團隊能夠接手維護，就不必每次改動都使用這個技能。它寫下的檔案會繼續為項目服務。日後遇到新的、未想清楚的需求，再請它出來幫忙整理。

## 關於檢查腳本（ERROR、WARN、OK）

技能附有一個檢查腳本，用來找出 Standard 項目文件裏遺漏的東西，例如某個任務沒有寫檢查方法。它會給出三種結果：

- `ERROR`：有地方需要修正。
- `WARN`：有地方值得留意，由你或 AI 決定怎樣處理。
- `OK`：這次文件結構檢查沒有發現問題。

通過這項檢查，不代表軟件能用、測試已經通過，或者可以上線。腳本不會執行任務裏寫的命令，也無法判斷 Flash 的任務約定或計劃寫得好不好。在 Flash 模式下（`--mode flash`），它會檢查共用的說明檔案和引用，並且總會多給一條 WARN，提醒你另外檢查任務本身。如果一個項目檔案都找不到，它也會直接講明。

如果已有的工具專用檔案重複了共用規則，或者 Claude 專用的入口檔案令 Claude Code 找不到 `AGENTS.md`，腳本也可能發出警告。看看這些檔案還需不需要：有用的專用規則保留，確實需要兼容入口時，用簡短的匯入就可以。倉庫裏的樣例只用了一份共用的 `AGENTS.md`。

不熟悉命令也沒關係，讓 AI 幫你執行，再請它解釋結果就可以。維護這個技能的開發者可以執行：

```bash
bash constitution-skill/scripts/check-governance.sh constitution-skill/assets/examples/feedback-inbox
python3 constitution-skill/scripts/test_check_governance.py
```

## 更新紀錄

### 2026-10-08

- 新增 Flash，作為日常工作、資料搜集、文件、軟件和可重用能力的統一輕量入口；Standard 保留完整的軟件項目流程。
- 為沒有技術背景的讀者重寫了這份 README 和新手入門說明，並新增三種語言的新手詞典。
- 更新 Claude Code 兼容說明：優先共用 `AGENTS.md`，先確認工具實際讀取了甚麼，再按需要加入簡短的兼容入口。
- 檔案數和程式碼行數改為提醒檢查難度的訊號，不再強制拆分任務；放在一起檢查更穩妥的相關改動，可以保持完整。
- 保留原有的工作方式：沿用已確認的決定，自己選擇誰負責實現、誰負責檢查，驗證要求和安全界線照樣寫清楚。

### 2026-09-14

- 已經講清楚的小修改，不必先走一遍規劃流程。
- 少問重複的問題：已有的決定直接沿用，確實有取捨時才比較方案。
- 何時停下來更清楚：只要規劃就不寫程式；已經同意實行的任務，會做到約定的檢查完成為止。與目前任務無關的舊問題分開說明。

### 2026-09-12

- 檢查更可靠：修正了「任務漏寫重要段落，也可能顯示通過」的問題，並加入自動測試。
- 交接更順暢：已經確認的任務，不再為同一個決定反覆詢問；實現和檢查可以交給你常用的 AI 工具。
- 安裝說明更新：通用規則盡量只寫一份，有需要才增加工具專用檔案。
- 文件更易讀：術語少了，多了沒有技術背景也能直接複製使用的提示詞。

### 2026-06-30

- 作出重要技術選擇時，會寫清楚有哪些方案、推薦哪一個，以及日後修改難不難。
- 產生檔案之後，會檢查有沒有講不清楚、互相矛盾或者遺漏的地方。
- 每個任務都會寫明：要做甚麼、哪些地方可以改，以及怎樣檢查是否完成。

## 倉庫結構

<details>
<summary>展開檔案目錄和開發者參考資料</summary>

```text
.
├─ README.md                          # 英文說明
├─ README_CN.md                       # 簡體中文
├─ README_HK.md                       # 本頁
├─ LICENSE
├─ constitution.md                    # 早期設計筆記
├─ TODO_CASE_DERIVED_EVOLUTION.md     # 有待真實項目驗證的改進構思
└─ constitution-skill/
   ├─ SKILL.md                        # 技能的主要說明
   ├─ agents/
   │  └─ openai.yaml
   ├─ references/
   │  ├─ rookie-onboarding.md          # 新手入門說明
   │  ├─ rookie-onboarding_CN.md
   │  ├─ rookie-onboarding_HK.md
   │  ├─ rookie-wiki.md                # 新手詞典
   │  ├─ rookie-wiki_CN.md
   │  ├─ rookie-wiki_HK.md
   │  ├─ flash-mode.md                 # 跨任務類型的輕量入口
   │  ├─ flash-components.md           # 可選、可組合的任務組件
   │  ├─ flash-scenarios.md            # 組件選擇的場景例子
   │  ├─ bootstrap-question-bank.md    # 應該問哪些問題
   │  ├─ cross-agent-compatibility.md  # Codex / Cursor / Claude Code 設定
   │  ├─ frontier-model-guidance.md    # portable Astra / Opus authoring guidance
   │  ├─ governance-asset-guide.md     # 長期檔案與一次性檔案、提升規則
   │  ├─ governance-review-rubrics.md  # 生成文件的就緒檢查
   │  ├─ governance-evolution.md       # 版本演進、決策紀錄、歸檔
   │  ├─ anti-patterns.md              # 常見的錯誤做法
   │  ├─ task-sizing.md                # 範圍完整、可檢查任務的提醒訊號
   │  ├─ task-review-contract.md       # 怎樣檢查一個完成了的任務
   │  ├─ retrofit-mode.md              # 為已有程式碼補建文件
   │  ├─ product-pattern-routing.md    # profile / module / recipe 選擇
   │  ├─ profile-transactional-record-system.md
   │  ├─ module-identity-access.md
   │  ├─ module-llm-boundary.md
   │  ├─ module-deterministic-workflow.md
   │  ├─ recipe-typescript-web-postgres.md
   │  ├─ recipe-local-python-sqlite.md
   │  ├─ wiki-record-crud-apps.md      # 紀錄型應用的工程筆記
   │  ├─ wiki-linear-workflows.md      # 分步驟流程的工程筆記
   │  └─ wiki-conversational-assistants.md # 對話助手的工程筆記
   ├─ assets/
   │  ├─ flash-templates/              # 可選的 AGENTS.md 和 PLAN.md 起點
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
   │  ├─ module-overlays/              # 針對特定能力的補充片段
   │  ├─ templates/                    # 常見產品類型的隱藏起點
   │  ├─ contracts-examples/           # 填好的 OpenAPI / JSON Schema / event / SQL / CLI / 檔案格式範例
   │  └─ examples/
   │     └─ feedback-inbox/            # 完整填好的樣例項目
   └─ scripts/
      ├─ check-governance.sh           # 檢查項目文件有沒有遺漏
      └─ test_check_governance.py      # 檢查腳本的自動測試
```

</details>

## 授權

MIT License。放心使用、fork、改造，令你的編碼智能體少一點混亂，多一點秩序。
