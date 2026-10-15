# Contributing

Every proposal is welcome. You don't need to open an issue before a pull request. Contributions in French are welcome too.

## What helps most

- A deslop catalogue for a new language: add `claude-home/skills/deslop/<code>.md` (for example `es.md`), following the structure of `en.md`, and reference it in `deslop/SKILL.md` (section 3 and the `description` line, which names the supported languages).
- An AI tell, design reflex, security, reliability or container check that's missing.
- A false positive: a rule that made Claude worse. Removing a bad rule is as useful as adding a good one.
- Support for a stack the skills don't mention yet.

## A good pull request

- One change, or one coherent group of changes.
- An example of what it catches: the sloppy sentence, the generic layout, the vulnerable code. A before and after is ideal.
- Short. Every line of `CLAUDE.md` costs tokens in every session, and skills cost tokens each time they load. Prefer adding to a skill over adding to `CLAUDE.md`.
- Follows the kit's own rules: no em dashes, no "it's not X, it's Y", no invented figures.
- Instructions in English, examples in their own language.

## Testing a change

Install your version locally (see the README), open a new session, and run the skill on a real case: `/deslop` on a text that has the tell, `/ui-design` on a page that has the reflex. Describe the result in the pull request.

## Issues

Use issues for bugs in the install, rules that conflict with each other, or ideas you'd like to discuss first. A screenshot or a copied sentence helps more than a description.

## Demo animations

The deslop GIFs and `assets/social-preview.png` are rendered from the README examples by `assets/src/make_assets.py`. If you change an example, update the script and run `python3 assets/src/make_assets.py assets`.

The with and without comparison (`assets/web-before-after.gif`) comes from the six pages in `assets/src/pages`, rendered by `python3 assets/src/make_web_demo.py assets`. It needs Playwright with Chromium, Pillow and ffmpeg; the docstring lists the fonts.
