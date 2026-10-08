# Rookie onboarding

[简体中文](rookie-onboarding_CN.md) · [繁體中文（香港）](rookie-onboarding_HK.md)

This guide is for people building software with AI for the first time: a product manager starting a project, a founder who doesn't code, a designer or analyst turning their know-how into a tool, or anyone who's curious. You don't need to write code to use the constitution skill. You will see some engineering words in the files it writes, though, and you'll be asked to make a few decisions. This page explains how the work goes, what the files are for, and what to say to the AI along the way.

Read it once from top to bottom, which takes about half an hour, then come back to a section when you need it. For single words, the [beginner glossary](rookie-wiki.md) has short, plain explanations of common terms.

If you remember only one thing, make it this: you decide what to build and why, the AI proposes how and does the work, and the project files remember what was decided.

## Before you start

You need three things:

- An AI coding tool: Codex, Cursor or Claude Code. Any one of them is enough.
- The skill installed in that tool. The [Quick start in the README](../../README.md#quick-start) installs it with one message.
- A project folder, meaning an ordinary folder on your computer for this project. An empty one is fine.

You don't need to know a programming language, memorize the file names in this guide, or pick templates. The AI handles those parts and tells you what it chose.

## Part 1: How a project goes

### A typical first week with Standard

Here's roughly what happens when you bring a new idea to Standard. Say you want a tool that collects customer feedback for your small team.

1. You describe the idea in everyday words, including the parts you haven't figured out.
2. The AI asks a handful of questions that would change the plan: who uses it, what the first version must do, what can wait, what must never go wrong. It skips anything you've already answered.
3. You answer what you can. For the rest, the AI proposes a safe default and writes it down as an assumption you can revisit.
4. The AI writes the plan into files in your project.
5. You read the plan and correct whatever is off. This step saves the most rework later.
6. The AI proposes the first small task, with a clear result and a way to check it.
7. You say go. The AI builds it, runs the checks, and tells you in plain words what changed and how to try it.
8. If you like, a second AI tool or an engineer reviews the change.
9. Any new decision gets written back into the files, and you move on to the next task.

You never have to read code in this loop. You read plans, results and short reports.

### Who does what

There are usually four roles, and one person or tool can hold more than one.

You are the owner. You decide the goal, the priorities and anything that's expensive to undo, you approve risky changes, and you decide what gets accepted.

The implementer is an AI tool that edits files and runs checks inside an agreed task.

The reviewer is another AI tool or an engineer who checks the change against the task and the project's rules.

The project files hold the shared memory, so the next chat, tool or person doesn't depend on what someone said in an old conversation.

Codex, Cursor and Claude Code can each play implementer or reviewer. Choose based on the tools you have and the work at hand; there's no fixed assignment. One habit helps: keep one main editor per change, so two tools aren't rewriting the same part at the same time.

### Why write things down

An AI's memory of a chat is short, and it doesn't carry over to a new chat. A file in your project stays put. When the plan lives in files, you can start a fresh chat, switch tools, take a week off or hand the project to someone else, and the work continues from what's written down instead of from what anyone remembers.

## Part 2: How much structure does your task need?

The skill has a few ways of working. You don't have to choose one by name; describe the task and the AI picks. Still, it helps to know what each looks like.

### Just do it: small, clear tasks

If a task is small and already clear, the AI should simply do it and run the relevant checks. No interview, no new files.

Examples: fix a typo, change a button's label, answer a specific question about your code, shorten a memo you've pasted in.

### Flash: lightweight, for many kinds of work

Flash is for tasks that need a little clarity or structure, but not a whole project setup. It covers everyday work, research, documents, software, and reusable capabilities such as skills.

Examples: compare three tools for collecting feedback and recommend one; create a skill that turns meeting notes into an action list colleagues can reuse; build a small script that reads a usage export and reports the remaining quota; prepare a short decision deck for a purchasing team; move a team meeting and notify the people invited.

### Standard: full software projects

Standard is for real software that will grow, have real users, or involve several people or AI tools. It produces the full set of project documents and then works through small, checked tasks.

Examples: a feedback inbox for small teams, an internal approval system, an appointment service, an AI support assistant.

### Retrofit: existing code with no documents

If you already have a codebase that nobody documented, Retrofit adds documents one part at a time, starting with the part you're about to change. It doesn't try to document everything up front: nobody remembers the original intent, so a big document written from scratch would mostly be guesswork.

### Not sure which?

Ask yourself a few questions:

- Is it already clear what to do and how to check it? Then just ask for it.
- Is it one piece of work, like a comparison, a document, a script, a skill or an action, that needs its goal and finish line pinned down? That's Flash.
- Is it a product you'll keep building, with users, data and several moving parts? That's Standard.
- Is there already a lot of code? That's Retrofit.

When you can't tell, say so: "I'm not sure how much planning this needs. Suggest a mode and tell me why in a sentence or two." Starting light is fine. Flash work can grow into a bigger setup later, once things get hard to keep track of, several parts or people depend on stable agreements, or handoffs need their own records.

## Part 3: Flash, step by step

### The task agreement

Flash starts by pinning down a short agreement about the task. The docs call it a task contract. It covers seven things, shown here with a running example: comparing three ways to collect customer feedback for a product team.

1. Goal: the result you want, and why. "Pick a feedback method we can start using next month."
2. User or audience: who will use or judge the result. "Our product team, none of whom are engineers."
3. Context: the background and material to work from. "My notes from last quarter, and the two tools we already tried."
4. Scope: what's included, and what's deliberately left out. "Compare three options. Don't sign up for anything or contact vendors."
5. Constraints: limits that shape the result. "It has to fit our current budget and work with the chat tool we already use."
6. Observable completion: what will be true when it's done, and how you'll check. "A one-page comparison with a recommendation, where every important claim points to a source."
7. Unknowns: open questions and assumptions. "We don't know one vendor's current price. Flag it instead of guessing."

A small task might cover all seven in two or three sentences of chat. Work that runs over several days, or gets handed to someone else, needs them written down.

### The outcome stays put, the plan can move

The agreement says what counts as success. The plan says how the AI will try to get there: the approach, the steps and where things stand. When an approach fails or better information turns up, the plan should change. The outcome should not quietly change along with it. The AI shouldn't lower the bar, switch the audience or inflate the deliverable to match what it managed to do. If the outcome really does need to change, that's a conversation with you, and the change gets written down.

Related to this: a first draft, a progress update or a job that has started is not the same as finished. If something is still running or blocked, the AI should say so plainly.

### Four kinds of extra detail

On top of the agreement, the AI adds only the detail a task needs. There are four kinds. A task can use several of them, or none.

Behavior applies when you're building something that runs more than once: a script, a feature, a skill, an agent. The useful details are what goes in and how it starts, what comes out, what it keeps between runs, a few examples (including awkward ones), and what happens when input is missing or wrong. For a quota-report script, that means asking what happens if the export file is empty, or if the quota figure is missing.

Evidence and judgment applies to research, comparisons, diagnoses and recommendations. The useful details are the questions that must be answered, where the evidence comes from (with dates, because facts go stale), the criteria for comparing options, and how sure the conclusion is. Good research keeps what was observed apart from what was inferred.

Content and structure applies to documents, slides, messages and anything else people read. The useful details are who reads it, the main message, the outline, and the presentation: format, tone and length. For anything with a layout, like slides, checking means looking at the rendered result, not only the text.

Action applies when something real changes: organizing files, rescheduling a meeting, updating a record, sending a report. The useful details are exactly which thing changes, what it looks like now and afterwards, what must be true first, the order of steps, and how to confirm the result. Starting an action doesn't prove it worked. The AI should look at the actual result, such as the meeting's new time on the calendar.

You don't pick these yourself. They aren't separate modes, and none of them needs its own file. A market comparison that turns into a slide deck uses evidence and content together; a weekly report agent might use all four.

### Where Flash keeps things

For a one-off task, the chat is usually enough. For work that continues, a light setup helps:

- `AGENTS.md` holds stable project context: what the project is, where the important files are, recurring conventions, and how to check work.
- `docs/PLAN.md`, or an existing brief, holds the task agreement, any extra detail, the current plan, and the evidence of what's been checked.

That's a starting point, not a required set of files. If a skill already describes its behavior in its own `SKILL.md`, or the project already has a task record or a data schema, the AI should link to those instead of copying them. Optional starters exist for [AGENTS.md](../assets/flash-templates/AGENTS.md) and [PLAN.md](../assets/flash-templates/PLAN.md).

### Checking a Flash result

Each kind of result gets checked in its own way:

- Something that runs: try it on representative examples and look at the output. Results from fake data or a dry run should be labeled as such.
- Research: check the important claims against their sources and dates, and make sure gaps and conflicts are visible.
- A document or slides: read the finished thing, and look at the rendered version when layout matters.
- An action: look at the actual state afterwards, or at the receipt or status the system sent back.

One question works at the end of any Flash task: "Which parts of our agreement are done, how do you know, and what's still open?"

### A Flash prompt to copy

Replace the parts in angle brackets:

```text
Use constitution-skill in Flash mode for this task: <describe it>.
It's for <who>. Here's the background: <notes or files>.
First write a short task agreement: goal, audience, scope and non-goals,
constraints, how we'll know it's done, and open questions.
Add only the extra detail this task needs, and keep the plan separate from the outcome.
Keep it in this chat unless a project file would help us reuse it.
```

For more, read the [Flash guide](flash-mode.md), the [component guide](flash-components.md) and the [worked scenarios](flash-scenarios.md).

## Part 4: Standard, step by step

### The planning conversation

Standard starts with questions. Expect them to cover your users, the problem, what the first version must do, what can wait, what must never go wrong, and constraints such as budget, deadline, privacy or an existing system you have to work with. There's no minimum number of questions. The AI should ask only what would change the plan, and reuse anything you've already said.

Some tips:

- "I don't know" is a good answer. The AI should offer a reasonable default, explain it in plain words and mark it as an assumption.
- Describe the problem in your own terms. "Our team loses feedback in a shared spreadsheet" tells the AI far more than "I want a React app."
- Mention what you're replacing (a spreadsheet, a form, a manual routine) and what you'd hate to lose.
- If a question contains a word you don't know, ask about the word before answering. A useful follow-up is "What would change depending on my answer?"

### The files you'll get

Standard writes a small set of documents, usually in a `docs/` folder, plus `AGENTS.md` at the top of the project. Each one answers a different question.

`SPEC.md` answers "what does the product do for its users?" It covers the goals, the users, the main workflows, what's deliberately left out (non-goals), constraints, and acceptance criteria, which are checkable statements of what "done" looks like. There's no code in it.

`ARCH.md` answers "what parts are inside, and how do they fit together?" It covers the modules and their boundaries, where data lives, technology choices with their reasons, and how the product will run. It also records the product shape: which common product type, add-on capabilities and default technology the project uses.

`RULES.md` answers "what must every change respect?" It holds the coding conventions that matter for this project, testing expectations and safety rules. Generic programming advice doesn't belong there.

`CONTRACTS/` answers "what exactly have the parts agreed on?" It holds API shapes, database table layouts, event messages and file formats, written precisely, often in standard formats, with examples.

`DECISIONS/` holds records of decisions that are expensive to reverse, such as which database to use. Each record notes the context, the choice, its costs and the alternatives that were turned down. Engineers call these ADRs, short for architecture decision records.

`TASKS/` holds the small next steps. Each task has one goal, what it may and may not touch, acceptance criteria, and the exact commands that check it. Tasks are disposable: once one is done and its lessons are recorded, it can be cleared away.

`AGENTS.md` is the instruction sheet for AI tools: where to look first, which commands to run, what's sensitive, what needs your approval and how to report back.

If a picture helps: the spec is the brochure, the architecture is the floor plan, the rules are the building code, and the contracts are the door frames that everything passing through has to fit. Decisions are the signed change orders, and tasks are today's work tickets.

Everything except the tasks is long-lived, so keep it up to date as the project changes. Tasks, scratch notes and one-off plans can be thrown away.

### A look at the worked example

The skill comes with a filled-in example called [Feedback Inbox](../assets/examples/feedback-inbox/). It's a tool for small product teams of 3 to 15 people: it collects feedback from a public form, groups it into themes and turns the strongest items into development tasks. Skim it to see what good documents look like. You don't need to follow every line.

A few things worth noticing:

- The spec lists non-goals, such as not replacing the team's issue tracker and not letting AI agents reply to customers directly. Writing down what you won't build keeps the AI from wandering off.
- The acceptance criteria are things anyone can check, like "a customer can submit feedback via the public form and see a confirmation page."
- The first decision record explains why outgoing events are stored in the main database instead of in a separate messaging service: one less service to run, at the cost of a little delay and a limit on how much traffic it can handle. The rejected options are listed with reasons.
- The [first task](../assets/examples/feedback-inbox/docs/TASKS/001-bootstrap-feedback-inbox.md) names the files it may touch, the files it must not touch, and the commands that prove it works.

### Reading your plan: a checklist

You don't have to judge the technology. You do need to check that the plan matches what you meant. Go through these questions:

- Does the spec describe the users and the problem the way you would?
- Are the non-goals right? Is something missing that you'd never want in version one, or is something listed there that you actually need?
- Could you check each acceptance criterion yourself, or watch someone check it?
- Are you comfortable with the assumptions?
- Are the open questions really open, and does anything depend on them?
- Does the first task deliver something you could see or try?
- For the big, hard-to-undo choices, did the AI ask for your approval and explain the options in words you understood?

If any answer is "no" or "not sure", say so. Fixing the plan costs far less than fixing the software.

## Part 5: Ideas you'll meet in the files

These ten ideas come up again and again. Each section says what the idea is, why it matters to you, and what you can do about it.

### 1. Assumptions and open questions

An assumption is a guess written down so that everyone knows it's a guess: "We assume one team per installation in the first version." An open question is something nobody has decided yet: "Should anonymous feedback come with a reply link?"

Both are healthy. The skill puts them in clearly labeled sections instead of burying them in the text. Read them, confirm or correct the assumptions, and notice when a task depends on an open question. A task that depends on an unresolved question isn't ready to build.

### 2. Schema and migrations

A schema is the shape of the data your product stores. A `feedback` table with the columns `id`, `source`, `message` and `created_at` is a schema. It's a lot like the column headers of a spreadsheet, except that the database enforces them.

A migration is a script that changes the schema in a recorded, repeatable way, for example "add a `tags` column to the `feedback` table".

Two things are worth knowing. Once real users exist, every schema change touches their data: adding a column is usually safe, while renaming a column, removing one or changing what it means is often risky. And most teams treat migrations as forward-only. If one turns out wrong, they write a new migration to fix it instead of editing the old one.

That's why new or changed schema decisions need your explicit approval. If an approved task already spells out the change, the AI can implement it without asking again. Running a migration on the live product needs a separate permission. You'll never have to write a migration, but notice when one is happening and ask: "Can this be undone? What happens to the existing data?"

### 3. APIs and contracts

An API (application programming interface) is the way one piece of software talks to another. The most common kind is a web API: one program sends a request to a web address, and another program sends back a response, often in a text format called JSON. A restaurant menu is a fair picture. It lists what you can order and what you'll get, and the kitchen can change how it cooks as long as the menu stays true.

A contract describes an API precisely enough that two people or teams can each build their side separately and still fit together. It usually says where requests go, which fields a request contains and which are required, what a successful response looks like, and what an error looks like.

Once anything relies on your API, whether it's your own mobile app, an integration like Zapier or a partner's system, changing the API costs real effort. So the contract file is treated as the source of truth, and the contract gets updated before the code does. When the AI proposes changing a public contract, ask who relies on it and how they'll be affected.

### 4. Authentication and authorization

These two sound alike and often get mixed up.

- Authentication answers "who are you?" It covers logging in, sessions and password resets. Engineers shorten it to authn.
- Authorization answers "what are you allowed to do?" Think "only the team owner can delete a workspace" or "free users can see ten feedback items a month". It's shortened to authz.

An office building is a good picture. The front desk checking your ID is authentication. Your key card opening some floors and not others is authorization.

Both are easy to get subtly wrong, and the usual failures are serious: one user seeing another user's data, or someone getting more access than intended. So new or changed login and permission decisions need your explicit approval, even when they look small. An approved task covers what it says; if the scope or the risk changes, the AI should ask again. When permissions come up, describe them as plain sentences about who can do what to which data, and ask how they'll be tested.

### 5. Bounded tasks and vertical slices

A bounded task has one clear outcome, an agreed scope, and checks that show whether it worked. Someone else, a person or another AI, should be able to review it as one sensible change.

The skill uses some numbers as review signals. A task touching more than about five files or 300 changed lines, for instance, deserves a closer look from the reviewer. These aren't hard limits. A task gets split when splitting lowers the risk or makes it easier to check, and related changes stay together when splitting would leave things half-working. Every necessary check still runs, even if that takes more than three commands.

A vertical slice is a thin piece of the product that works from top to bottom: a small change on screen, plus the server change behind it, plus the database change behind that, delivered together and working end to end. Picture cutting one thin slice through every layer of a cake.

Prefer first tasks that give you something you can see or try. Be wary of tasks named after a whole feature ("build authentication") or a vague goal ("improve the code").

### 6. Development, staging and production

Software usually runs in three places:

- Development is your own computer, or the AI's workspace. Things can break freely, and there are no real users.
- Staging is a copy that runs on a server and looks like the real product, but holds test data. It's the dress rehearsal.
- Production is the real product, with real users, real data and real consequences.

Some small projects skip staging, but the idea stays the same: try things where mistakes are cheap before they reach real people. Deploying to production needs explicit permission, because a mistake there affects everyone. Permission to build or test a change doesn't cover deploying it. You'll see these names in `ARCH.md` and in deployment files.

### 7. Reversible and irreversible decisions

Some decisions are cheap to undo. Others are expensive.

- Cheap to undo: a font, a button label, how code is arranged inside a function.
- Expensive to undo: the shape of the database, the web address of a public API, how login works, the payment provider, what happens when a user deletes their account, how long data is kept.

The skill keeps an approval list for decisions that are risky or hard to reverse, and the AI must not make new decisions in those areas on its own. Once you've approved a decision and the work that goes with it, the AI shouldn't ask you about the same thing again. Changed scope, changed risk, and separate permissions such as deploying still get attention.

A habit worth building: when the AI is about to make a choice, ask yourself, "If this turns out to be wrong, how painful is it to change later?" If the answer is "easy", let it carry on. If it's "painful" or "we'd have to move users' data", stop and talk it through.

### 8. Tests and verification

A test is a small program that checks whether another piece of code behaves as expected. For example: "If I submit feedback with no message, the system rejects it with a clear error." Tests run automatically, so they keep checking after every change.

Tests do two jobs. They catch regressions, meaning things that used to work and then quietly broke. And they give an honest answer to "is this task done?"

In Standard, every task file has a verification section listing the exact commands to run and what each should show. You don't need to write tests, but don't accept "done" without evidence. Ask which commands ran and what they showed. If something wasn't checked, the report should say so.

### 9. Review

A review means a second person or AI reads a change before it's accepted into the project. The reviewer asks:

- Does the change do what the task said?
- Does it break anything that used to work?
- Does it cross a boundary set in `ARCH.md` or `RULES.md`?
- Did it touch anything on the approval list without approval?

The skill asks reviewers to judge two things separately: did the change do what was requested, and is it well built? Passing tests can hide a change that solves the wrong problem, and a change that solves the right problem can still be fragile. Review finds problems and checks the evidence. You still make the important calls and decide what's accepted.

### 10. The promotion habit

This is the most useful habit the skill teaches, and it has nothing to do with technology. When you catch yourself explaining the same thing a second time, write it into one of the long-lived files.

- Said it twice in reviews: put it in `RULES.md`.
- Said it twice about how parts exchange data: put it in `docs/CONTRACTS/`.
- Said it twice about how the product should behave: put it in `docs/SPEC.md`.
- Said it twice to an AI: put it in `AGENTS.md`.

Anything you have to repeat is something the next person, the next AI, or you three months from now won't know unless it's written down. You can simply say: "We've discussed this twice. Please add it to the right project file."

## Part 6: Your working loop, with prompts

Copy these and replace the parts in angle brackets.

Starting a project with Standard:

```text
I want to build <your idea>. It's for <who>, and the main problem is <problem>.
Use constitution-skill in Standard mode. Ask me only the questions that change the plan,
explain any decision I need to make in plain language, and suggest defaults when I'm unsure.
Save the plan in the project and propose the first small task. Don't write application code yet.
```

Understanding the plan:

```text
Walk me through the plan as if I'm new to software. What will the first version do,
what does it leave out, and what are you assuming? Which decisions are hard to undo?
```

Building the next task:

```text
Take the next task in docs/TASKS/. Tell me what it will deliver, then build it within its scope
and run its verification. If you need a new important decision or a bigger scope, ask first.
When done, tell me what changed, what you checked and the results, and how I can try it.
```

Getting a review from a second tool:

```text
Review the latest change against its task file and the project documents.
Judge separately whether it does what the task asked and whether it's well built.
List problems by severity, check the verification evidence, and don't rewrite code unless I ask.
```

Saving a decision:

```text
We just decided <decision>. Record it in the right project file. If it's hard to reverse,
add a decision record with the options we considered and why we chose this one.
```

Picking up in a new chat:

```text
Read AGENTS.md and the current plan or task, then tell me in a few sentences
where the project stands, what's next, and anything that's waiting on me.
```

## Part 7: What needs your approval

The AI should get your explicit approval before it makes new or changed decisions about:

- the public shape of an API that other software relies on
- the database structure, or migrations that change it
- login and permissions
- payments, billing, legal, privacy or compliance behavior
- deleting data, or any other operation that can't be undone
- how and where the live product is deployed

Three things to know about approval:

- Approving a task covers what that task states. The AI shouldn't ask you again for the same decision.
- Approval to build is not approval to deploy, and it's not approval to delete real data. Those follow their own permissions.
- If the AI says a rule is stopping it, it should name the file, quote the rule and explain which decision is missing. If it can't point to one, it may be treating its own preference as a rule, and you can ask it to carry on.

## Part 8: Warning signs, and what to say

| What happens | What you can say |
| --- | --- |
| The AI says "done" but not what it checked | "Which commands did you run, and what did they show? What wasn't checked?" |
| It added things you didn't ask for | "Please remove <thing>. It's outside this task's scope." |
| It wants to change the database, login or payments | "Explain the options, your recommendation, and how hard each would be to change later. Then wait for my decision." |
| It asks about something you already decided | "We decided this in <file>. Please reuse that decision." |
| It wants to deploy or delete real data | "Not yet. Approval to build doesn't cover that." |
| An error message you can't follow | "Explain this error in plain words: what broke, why, and what you'll do next." |
| The plan uses words you don't know | "Explain <word> with an everyday example." You can also look it up in the [glossary](rookie-wiki.md). |
| A task keeps growing | "Can we split off a smaller first step that still works end to end?" |
| You're starting a new chat | "Read AGENTS.md first and tell me where we are." |
| The check script shows a WARN | "Explain each warning and whether it affects this task." |

## Part 9: The check script, in plain words

The skill includes a script that checks whether project documents are missing required parts. It reports `ERROR` when something needs fixing, `WARN` when something is worth a look (you or the AI decide what to do), and `OK` when it finds no structural problems. You can ask the AI to run it and explain the result.

Passing the check doesn't prove the software works, because the script doesn't run your tasks' commands. In Flash mode it also can't judge whether a task agreement is any good, so it always adds a reminder to review the task itself. Real checks of the result, like tests, sources and the actual state of things, still matter.

## Where to go next

- The [beginner glossary](rookie-wiki.md), for any word you haven't met yet.
- The [Flash guide](flash-mode.md), [components](flash-components.md) and [scenarios](flash-scenarios.md), for more on lightweight work.
- The [worked example](../assets/examples/feedback-inbox/), to see a complete Standard project. Its [first task](../assets/examples/feedback-inbox/docs/TASKS/001-bootstrap-feedback-inbox.md) shows what a good task file looks like.
- The [asset guide](governance-asset-guide.md), for a longer explanation of which file holds what.

The skill will keep using these ideas. Come back here whenever a term feels foreign. After a few projects, you probably won't need this page at all.
