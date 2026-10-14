# Pre-release security audit

Run before a release or when I ask for a security audit. Report in three lists: OK, problem (with `file:line` or URL), not checked (and why). Don't install a tool without asking. Prefer what's already available.

## In the repository

1. Secrets in the code: search for `sk_live_`, `sk_test_`, `service_role`, `-----BEGIN`, `PRIVATE_KEY`, `SECRET`, `PASSWORD=`, `apiKey`, connection strings (`postgres://`, `mongodb+srv://`, `mysql://`). If `gitleaks` or `trufflehog` is installed, run it on the full git history.
2. `.gitignore` covers `.env*` except `.env.example`. `git ls-files | grep -i env` shows no real env file.
3. Public env prefixes: list every variable with a public prefix and confirm none is a secret.
4. Every route, server action and API handler: auth check present, permission or ownership check present. List any handler without one.
5. Every place the request body reaches the ORM: field allowlist present (mass assignment).
6. Raw SQL and Mongo queries: parameterized, no operator injection.
7. `dangerouslySetInnerHTML`, `v-html`, `{@html}`, `innerHTML`, `|safe`, `eval`, `new Function`, `exec`, `child_process`: each use justified and safe.
8. Supabase: every table has RLS enabled and policies. Firebase: rules contain no `if true`.
9. Payment flow: amount computed server-side, fulfillment on verified webhook only.
10. Webhook handlers: signature check present.
11. Upload handlers: size limit, content type check, private storage.
12. Debug flags, test routes, seed scripts: off or absent in production config.
13. Source maps disabled in the production build config, or uploaded privately.
14. Dependency audit.

## In the production build

1. Search the built client bundle (`dist/`, `.next/static/`, `build/`, `.output/public/`) for the patterns of step 1 above. Any JWT found (`eyJ...`): decode the payload and confirm it's a public key (for Supabase, `"role":"anon"`).
2. No `.map` file in the deployed output, unless intended.

## On the deployed site (read-only GET requests)

1. `curl -s -o /dev/null -w "%{http_code}" <url>/.env` returns 404. Same for `/.git/config`, `/.env.local`, `/config.json`, and the main bundle path with `.map` appended.
2. `curl -sI <url>` shows HSTS, Content-Security-Policy, X-Content-Type-Options, Referrer-Policy, frame protection, and no `X-Powered-By`.
3. An unknown route returns the custom 404, without a stack trace.
4. `http://` redirects to `https://`.
5. Admin paths and tool UIs (`/admin`, `/graphql`, `/api/docs`, `/swagger`, `/phpmyadmin`) require auth or return 404.
6. CORS: a request with `Origin: https://evil.example` does not get it echoed back in `Access-Control-Allow-Origin`.

Never run write requests, brute force or load tests against production without my explicit go.
