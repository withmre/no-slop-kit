# [Project name]

[One sentence: what the project does and for whom.]

Global rules in ~/.claude/CLAUDE.md apply. This file only holds what is specific to this project.

## Stack

- Framework: [e.g. Next.js 15, App Router]
- Database and auth: [e.g. Supabase]
- Hosting: [e.g. Vercel]
- Package manager: [e.g. pnpm]. Don't use any other.

## Commands

Short-output version of each command, to save context.

- Dev: `[pnpm dev]`
- Single test: `[pnpm vitest run path/to/file --reporter=dot]`
- All tests: `[pnpm test --silent]`
- Typecheck: `[pnpm tsc --noEmit]`
- Lint: `[pnpm lint --quiet]`
- Build: `[pnpm build]`
- New migration: `[supabase migration new name]`

## Where things live

- `[src/server/]`: server-only code, the only place that reads secrets
- `[src/lib/validation/]`: validation schemas
- `[src/components/ui/]`: components to reuse before creating new ones

## Design

- Design decisions live in `DESIGN.md` (written by the `ui-design` skill once the brief is approved). Read it before any UI work.

## Operations

- Error tracking: [tool, or À FOURNIR]
- Uptime monitoring: [tool, or À FOURNIR]
- Backups: [where, how often]. Restore procedure: [command]. Last restore test: [date].

## Conventions

- Code and identifiers: [English]. Comments: [French]. Commits: [e.g. Conventional Commits, in French].
- [Any convention that can't be guessed by reading the code]

## Known pitfalls

- [Add a line each time you correct the same Claude mistake twice.]

## Never modify

- [Generated files, e.g. `src/types/database.ts`]
- [Already-applied migrations]
