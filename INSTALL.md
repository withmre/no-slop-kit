# Install instructions for Claude Code

You are installing a personal configuration kit into the user's global Claude Code folder. Reply in the user's language, briefly.

Source: the `claude-home/` folder next to this file. It mirrors the target layout.
Target: the user's global Claude folder, `~/.claude/` (on Windows `%USERPROFILE%\.claude\`). Create it if missing.

Do not modify any project repository. Only the global folder.

## Steps

1. Detect the OS and resolve the target path. List what already exists in it: `CLAUDE.md`, `settings.json`, `skills/`.
2. Back up every file or folder you are about to replace or merge into `~/.claude/backup-kit-YYYYMMDD-HHMM/`, keeping the same relative paths. Skip if nothing exists yet.
3. `CLAUDE.md`
   - None exists: copy `claude-home/CLAUDE.md`.
   - One exists: summarize in a few lines what it contains that the kit doesn't, then ask the user: replace, merge (kit as the base, their extra lines added in the matching section), or skip. If merged, keep the result under 200 lines.
4. Skills: copy each folder of `claude-home/skills/` into `~/.claude/skills/`, with all its files (some skills have more than one). If a skill folder with the same name exists, ask before replacing it.
5. `settings.json`
   - None exists: copy `claude-home/settings.json`.
   - One exists: never overwrite it. Add only the entries of `permissions.deny` and `permissions.ask` that are missing. If `permissions.deny` contains an entry that the kit lists under `permissions.ask` (older versions of this kit denied `rm -rf` and forced pushes), move it to `ask`. Keep everything else untouched, and check the result is valid JSON.
6. Verify:
   - List every installed file with its path.
   - Check that `settings.json` parses as JSON.
   - Check that each `SKILL.md` starts with a frontmatter block containing `name` and `description`.
7. Tell the user, in their language and in a few lines: what was installed, where the backup is, and to open a new session and type `/` to see `security`, `reliability`, `ui-design`, `deslop` and `project-setup` listed, then run `/context` to check the global CLAUDE.md is loaded.

The kit folder (cloned or unzipped) can be deleted afterwards. Say so, but don't delete it yourself.
