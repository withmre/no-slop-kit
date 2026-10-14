# No Slop Kit for Claude Code

Global rules and five skills for Claude Code. With them, Claude writes less code, invents nothing, spends fewer tokens, and stops producing the text and design that make people think "an AI made this".

![License: MIT](https://img.shields.io/badge/license-MIT-blue) ![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen) ![Claude Code](https://img.shields.io/badge/for-Claude%20Code-d97757) ![GitHub stars](https://img.shields.io/github/stars/withmre/no-slop-kit?style=social)

[Version française](README.fr.md)

![Animation: /deslop highlights 14 AI writing markers in a paragraph one by one, then shows the rewritten version with every idea kept](assets/deslop-demo.gif)

## Why I made this

I build websites with AI every day. It saves me hours. It also kept handing me the same things: em dashes everywhere, "it's not X, it's Y", purple gradients, three feature cards with an icon on top, fake testimonials, a package that doesn't exist, a 400-line rewrite for a one-line fix.

I'm against slop for one reason. AI should give us time back to spend on ideas and creative work. Slop does the opposite: it lets us stop thinking, and every site and every paragraph starts to look like the next one.

So I wrote down every rule I kept repeating to Claude and turned them into a kit anyone can install in a few minutes. It's free and open. I'll take any suggestion: open an issue, or send a pull request directly.

## See it work

Here is what `/deslop` does to a typical AI-written paragraph. The animation at the top replays this example from the skill's report.

**Before**

> In today's fast-paced digital landscape, building a website is no longer just about code — it's about crafting seamless experiences that truly resonate with your audience. Whether you're a startup or an enterprise, our cutting-edge platform empowers you to unlock your full potential. The result? Faster launches, happier customers, and measurable growth. It's not just a tool. It's a game-changer.

**After**

> Building a website takes more than code: people have to enjoy using it. Our platform helps startups and large companies launch sooner. Customers stay happier, and the growth shows up in your numbers.

**What the skill reported**

| Before | After | Why |
|---|---|---|
| "In today's fast-paced digital landscape" | cut | Generic opener that fits any text, and "landscape" is banned |
| "—" | ":" | Em dash, always removed |
| "no longer just about code, it's about" | "takes more than code" | "It's not X, it's Y" construction |
| "seamless", "truly", "resonate", "cutting-edge", "empowers", "unlock your full potential", "game-changer" | removed | Banned vocabulary and empty intensifiers |
| "Whether you're a startup or an enterprise" | "startups and large companies" | Stock opener |
| "The result? Faster launches, happier customers, and measurable growth." | two plain sentences | Question answered right away, and a reflex group of three |
| "It's not just a tool. It's a game-changer." | cut | Same construction again, and it adds no idea |

Flagged and left for the author: "measurable growth" comes with no figure. Add a real one or drop the claim.

Markers: 14 before, 0 after.

Every idea of the original survived. The skill changes the form, keeps the author's examples, and flags claims it can't check. It never invents a number to make a sentence stronger.

This README went through the same skill before publication.

## What's inside

| File | What it does | When it loads |
|---|---|---|
| `CLAUDE.md` | Global rules: never invent, lazy development, token economy, security baseline, writing style | Every session |
| `settings.json` | Blocks reading `.env` files, lockfiles and build folders, and a few destructive commands | Every session |
| `skills/deslop` | Rewrites a text to remove AI tells, with French and English catalogues, and shows what it removed and why | On text meant for publication, or `/deslop` |
| `skills/ui-design` | Trust killers, dark patterns, default design reflexes, typography, color, tokens, components, launch checklist | On any UI work, or `/ui-design` |
| `skills/security` | 19 sections from secrets to webhooks and payments, plus a pre-release audit with concrete commands | On auth, data, API or payment work, or `/security` |
| `skills/reliability` | Rate limits, API cost caps, timeouts, empty and error states, indexes, caching, monitoring, backups that restore | On data, API and deployment work |
| `skills/project-setup` | Writes a project's `CLAUDE.md` from the files in the repository, with nothing invented | Only with `/project-setup` |

## What changes in practice

### Code

Claude checks the installed version of a library before using its API, and checks that a package exists before installing it, since a hallucinated package name can belong to a malicious package. It cites `file:line` when it talks about your code. Before writing anything it walks down a ladder: delete, reuse, native platform feature, standard library, installed dependency. New code comes last. The diff stays as small as possible, with no bonus refactor, and Claude never claims it tested something it didn't run.

"Lazy" in this kit means lazy about code: the less Claude writes, the less you have to review. It never means lazy about thinking.

### Tokens

Claude searches before reading, skips lockfiles and build output, runs one test file while iterating and the full suite once, and ends a task in three lines. The main `CLAUDE.md` stays under the 200 lines Anthropic recommends. Each skill costs only its description until a task needs it.

### Design

Before any code, Claude writes a short brief with a real-world reference and proposes two directions. It drops its own first instinct for fonts and colors, because that instinct is the same on every project. Before showing a page, it audits every default pattern it used and marks each one "chosen, because..." or removes it.

### Text

No em dashes, no "it's not X, it's Y", no "delve", no rhetorical question answered in the next sentence. The full list lives in the deslop catalogues.

### Security and reliability

Server-side checks on every route, row-level security on every table, prices computed on the server, orders fulfilled on a verified webhook, timeouts on every outbound call, and backups someone has restored at least once.

## Install

### Let Claude Code do it

```bash
git clone https://github.com/withmre/no-slop-kit.git
cd no-slop-kit
claude
```

Then type:

```
Read INSTALL.md and install this kit.
```

Claude backs up your current configuration, asks before replacing anything, merges your `settings.json` instead of overwriting it, and checks the result.

### By hand (macOS, Linux, WSL)

```bash
mkdir -p ~/.claude/skills
cp -r claude-home/skills/* ~/.claude/skills/
cp -n claude-home/CLAUDE.md ~/.claude/CLAUDE.md
cp -n claude-home/settings.json ~/.claude/settings.json
```

`cp -n` leaves your existing `CLAUDE.md` and `settings.json` alone: merge them by hand if you already have some. The skills copy overwrites skills with the same names.

Open a new session, type `/` to see the skills, and run `/context` to check the rules are loaded.

## Use it

Most of the time you do nothing. Claude loads each skill when the task calls for it. You can also call them directly:

- `/deslop` followed by your text, or a path to a file.
- `/ui-design` before starting a page or a redesign.
- `/security` for an audit before a release.
- `/project-setup` once in each new repository.

## Make it yours

Claude replies in French by default. To change that, edit the line "Always reply in French" in `CLAUDE.md`. Section 8 of the same file holds the French writing rules, and the deslop skill already ships an English catalogue.

Banned words live in `skills/deslop/fr.md` and `skills/deslop/en.md`. Add yours.

Every line of `CLAUDE.md` costs tokens in every session, so remove what you don't use.

## Habits that save the most tokens

- `/clear` between unrelated tasks.
- `/compact` with an instruction when a session grows: `/compact keep the decisions about the schema`.
- Plan mode (`Shift+Tab`) for a big task, and `Esc` as soon as Claude heads the wrong way.
- `/mcp` to turn off servers you don't use.
- Precise requests that name the file.

## Contributing

I accept every proposal worth discussing, and pull requests are welcome without asking first. The goal is to help as many people as possible use AI well.

What would help most:

- A deslop catalogue for your language: Spanish, German, Portuguese, Italian.
- AI tells you keep seeing that the catalogues miss.
- Design reflexes from the latest component galleries.
- Security or reliability checks for a stack the skills don't cover yet.
- False positives: a rule that made Claude worse. These matter as much as new rules.

Details in [CONTRIBUTING.md](CONTRIBUTING.md).

If the kit saved you a rewrite, a star helps other people find it.

## Star history

[![Star history chart](https://api.star-history.com/svg?repos=withmre/no-slop-kit&type=Date)](https://star-history.com/#withmre/no-slop-kit&Date)

## License

[MIT](LICENSE). Use it, fork it, change it.
