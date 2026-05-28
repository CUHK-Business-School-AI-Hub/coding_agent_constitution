# Rookie Onboarding

[English](rookie-onboarding.md) · [简体中文](rookie-onboarding_CN.md)

一份給「第一次做軟件產品的人」的簡短概念入門。如果你是準備啟動新項目的產品經理、在做副業項目的人、想跨行做軟件的領域專家，或者只是剛接觸軟件產品的各種組成部分，這份文檔對你都有幫助。

你不需要識寫程式碼也可以用 constitution skill。但你會在它生成的檔案入面遇到下面這些概念。這頁的目的，是用 15 到 20 分鐘讓你對每個概念都有一個基本印象，使 skill 後面的內容讀起來像工具，而唔係一堵術語牆。

它唔係一本把術語藏起來的字典，而係一份令術語變得平易近人的短讀物。

## 閱讀順序

整頁快速瀏覽一遍。當你在生成的治理檔案入面見到某個詞時，再回來精讀對應小節。

## 1. Spec, Architecture, Rules, Contracts

這是 skill 幫你產出的四類長期文檔，分別回答四個唔同的問題。

- **Spec** 回答的是：*這個產品給用戶做了甚麼？*
  目標、用戶、非目標、acceptance criteria。這裡不寫程式碼。
- **Architecture** 回答的是：*產品內部有邊啲組成部分？它們點樣拼起來？*
  模組、資料流、技術選擇、部署形態。是決策，唔係意見。
- **Rules** 回答的是：*在這個程式碼庫裡，每個改動都要遵守邊啲嘢？*
  對這個倉庫有意義的編碼風格、testing 要求、安全邊界。
- **Contracts** 回答的是：*產品內部唔同部分之間，或產品與外部之間，有邊啲穩定的介面？*
  API 形狀、database 表結構、event payload、檔案格式。

一個有用的畫面：Spec 是產品手冊，Architecture 是樓宇平面圖，Rules 是屋宇規範（電線、水管），Contracts 是門框——所有想穿過去的東西必須符合尺寸。

## 2. Schema 同 Migration

**Schema** 是你的產品儲存的資料的「形狀」。例如一張 `feedback` 表，包含 `id`、`source`、`message`、`created_at` 這幾欄，就是一個 schema。Schema 通常住在 database 裡。

**Migration** 是用來改 schema 的一段腳本。例如「給 `feedback` 表加一欄 `tags`」。

兩件需要知道的事：

- 一旦產品上了線、有了真實用戶，每次 schema 改動都會動到他們的資料。加一欄通常是安全的；改變某欄的含義、刪除某欄、為某欄改名，往往是有風險的。
- 大多數團隊的 migration 只能往前。錯咗就寫下一個 migration 去修，不會回頭改過去的腳本。

這就是為甚麼 skill 把任何 schema 改動都列為 "Approval Required"。你不需要識寫 migration，但需要能睇得出別人正在做這件事。

## 3. APIs 同 Contracts

**API**（Application Programming Interface）是一段程式與另一段程式溝通的方式。最常見的形態是 web API：一段程式發出一個 HTTP request，另一段程式回一個 JSON response。

**Contract** 是對 API 形狀的精確描述，細到兩個團隊可以各自開工仲對得上。Contract 通常會講明：

- URL（向邊度發 request）。
- request 的形狀（有邊啲欄位、類型是甚麼、邊啲是必填）。
- response 的形狀（成功係點、失敗係點）。
- error envelope（錯誤長甚麼樣）。

為甚麼這在做產品時重要：一旦任何外部系統（你自己的 mobile app、Zapier 整合、合作方）開始依賴你的 API，改 API 就是要付代價的。把 contract 檔案當成真相源——先改 contract，再改程式碼。

## 4. Authentication 同 Authorization

兩件經常被混在一起、但完全唔同的事。

- **Authentication（authn）** 回答的是：「你是誰？」
  登入流程、session、token、密碼重置。
- **Authorization（authz）** 回答的是：「你被允許做甚麼？」
  「只有 team owner 可以刪除 workspace。」「免費用戶每月最多睇 10 條 feedback。」

兩者都好微妙，都容易做錯。最常見的失敗方式是：用戶之間資料洩露，或者意外地放開了過多權限。這就是為甚麼 skill 把任何 authn / authz 改動都列為 "Approval Required"。即使睇起來是小改動，在這兩塊也要放慢。

## 5. Bounded Task 同 Vertical Slice

**Bounded task** 是指一項小到一個人（或一個 AI agent）在一次工作中能做完、別人能 review 的工作。Skill 設了硬限制：大致 5 個檔案、300 行程式碼改動、3 條 verification 命令以內。

**Vertical slice** 是一段貫穿整個技術棧的產品工作：一小段 UI 改動 + 對應的 API 改動 + 對應的 database 改動，作為一個整體交付，端到端跑得通。

兩個想法都是在對抗「一口氣把整個 feature 做完」這種直覺。它們是團隊能持續交付又唔會把產品搞壞的方法。當 skill 叫你寫一個 task 檔案時，你就在練這個習慣。

## 6. 環境：Production、Staging、Development

一個現代軟件產品通常會在三個地方運行。

- **Development** 在你的電腦上。東西可以隨便壞。沒有真實用戶。
- **Staging** 是 production 的一份副本，跑在雲上，長得像 production，但裡面是測試資料。用來在面對真實用戶之前先驗證。
- **Production** 是真正運行的產品。真實用戶。真實資料。真實後果。

Skill 把任何 production 部署變更都列為 "Approval Required"，因為出問題的影響面太大。絕大多數粗心錯誤會被 staging 攔住；穿到 production 的，才是真正重要的那批。

你會在 `ARCH.md` 同部署檔案裡見到這三個名。它們分開的原因，純粹是為了安全。

## 7. Reversible vs Irreversible 決策

有些決策撤銷幾乎無成本。有些撤銷代價非常大。

- Reversible：換字體、為按鈕起名、函數內部用邊種 loop。
- Irreversible（或撤銷好貴）：database 結構、public API 的 URL、authentication 模型、支付供應商整合、用戶刪除如何處理、資料保留策略。

Skill 的 "Approval Required" 清單，正好就是這類 irreversible 的事。當你在讀那個清單時，你其實是在讀「AI agent 唔可以自己單獨決定的事」。

一個好習慣：每當 agent 準備做一個選擇，問一句：「如果這選錯了，以後改返去有幾痛？」——答案是「好簡單」就放手；答案是「好痛」或「要做用戶資料遷移」就暫停。

## 8. Tests 同 Verification

**Test** 是一段小程式，用來證明另一段程式碼的行為符合預期。例如：「如果我提交一條沒有 message 的 feedback，API 應該回 400 錯誤。」每次程式碼改動之後，tests 會被自動跑一次。

Tests 做兩件事：

- 抓 regression：原本能跑、後來跑唔通的程式碼。
- 給「這個 task 算唔算做完？」一個誠實的答案。

在 skill 裡，每個 task 檔案都有 `## Verification` 段落，寫住具體要跑的命令。這些命令通常包含 tests。你不需要自己寫 tests，但應該堅持：verification 沒跑過，task 唔算完。

## 9. Review

**Review** 是另一個人（或另一個 agent）在改動被合併進程式碼庫之前先讀它。Reviewer 會問四個問題：

- 這個改動是否做了 task 講的事？
- 它有沒有破壞原本能跑的東西？
- 它有沒有越過 `ARCH.md` 同 `RULES.md` 裡列的邊界？
- 它有沒有在沒批准的情況下，碰了 "Approval Required" 列表裡的東西？

當 skill 提到 Cursor review diff、或者人類 reviewer 批准合併，講的就是這件事。Review 唔係把門，係發現問題成本最低的位置。

## 10. The Promotion Habit

這是 skill 想你養成的最重要的一個習慣——而且它唔係技術習慣。

任何時候，當你發現自己向 AI agent、向隊友、甚至向「過幾日的自己」，**重複解釋同一件事**——把它寫進一份長期檔案裡。一般規則：

- 在 code review 裡講過兩次的事 -> 寫進 `RULES.md`。
- 關於介面講過兩次的事 -> 寫進 `docs/CONTRACTS/`。
- 關於產品該如何行為講過兩次的事 -> 寫進 `docs/SPEC.md`。
- 向 agent 講過兩次的事 -> 寫進 `AGENTS.md`。

重點唔係官僚，重點是：**任何你需要重複解釋的東西，下一個人（或下一個 agent，或未來的你）在沒人話佢知的情況下是唔會知道的。**

## 接下來

讀完這一遍之後：

- 打開 `references/governance-asset-guide.md`，那裡有對檔案家族更長的描述。
- 打開 `assets/examples/feedback-inbox/` 這個完整樣例，把每個檔案都翻一遍。不要試圖全懂，先感受每份檔案的形狀。
- 當 skill 叫你寫 task 檔案時，去睇 `assets/examples/feedback-inbox/docs/TASKS/001-bootstrap-feedback-inbox.md`——那就是「好」嘅樣。

Skill 後面會不斷引用這些概念。哪個詞陌生了，再回來這裡。做過幾個項目之後，你就不需要這份檔案了。
