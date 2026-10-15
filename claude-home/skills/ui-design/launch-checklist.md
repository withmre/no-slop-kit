# Launch checklist

The site can look finished and still miss what makes it work, get found on Google and share properly. Go through every item.

Report in three lists: done, missing, needs information from me. Never invent content, legal text or figures to tick a box.

## Domain and identity

- Custom domain, no deployment subdomain. HTTPS enforced, one canonical version (www or apex) with the other redirected.
- Real logo, or the temporary wordmark flagged.
- Full favicon set: `favicon.ico`, an SVG icon, `apple-touch-icon` 180×180, and 192 and 512 px PNGs declared in a web manifest for the home screen.
- No generator badge or "Made with" mention.
- Transactional emails sent from the site's domain, with SPF, DKIM and DMARC set.
- Real contact address. Mandatory in most countries, reassuring everywhere. An address on the site's domain looks more serious than a webmail one.

## Content and search

- The main call to action fits in the first screen without scrolling, on mobile and desktop.
- A unique `<title>` per page: it's what Google shows and what the tab displays.
- A unique meta description per page: the text under the link in search results.
- Canonical URL on every page.
- Share image: `og:image` at 1200×630, with `og:title`, `og:description`, `og:url` and `twitter:card` set to `summary_large_image`. Without it, a shared link shows a grey rectangle. Test with a share preview tool.
- `robots.txt` present, and no `noindex` or `Disallow: /` left over from staging.
- `sitemap.xml` listing every page, referenced in `robots.txt`, submitted to Google Search Console.
- Alt text on every image, for accessibility and search.
- `lang` on `<html>`, one `h1` per page.
- Structured data (schema.org `Organization` or `LocalBusiness`) when relevant. `hreflang` if the site has several languages.
- No lorem ipsum, placeholder image, `[À FOURNIR]` marker or framework leftover (default title, favicon or description).
- Copyright year current or generated.

## Pages and links

- Custom 404 page with a link back home and to the main pages, instead of the raw server error. A 500 page if the stack allows.
- Every link and button works. No `href="#"`. Run a link checker.
- Browser console clean on every page: no errors, no failed requests.
- A real demonstration of the product: screenshot, video or live demo.

## Mobile and interaction

- Real mobile breakpoints, tested at 320, 375, 414 and 768 px and on a wide screen. No horizontal scroll, no button label on two lines. Checked on a real iPhone with Safari, where layouts break most.
- Touch targets at least 44 px.
- Inputs with the right `type` and `autocomplete`. Mobile menu works.
- Hover and focus states on everything clickable, none on the rest.
- On long mobile pages, the main action stays reachable (slim sticky button, or the action repeated).
- Loading states and skeletons. Buttons disabled while submitting.
- Empty states.

## Forms

- Error messages that say which field is wrong and why, next to the field, without erasing what was typed.
- Server-side validation (see the `security` skill).
- Anti-spam: honeypot or a privacy-friendly captcha.
- A confirmation page with its own URL after sending. Without it, nobody knows if it worked, and it's also what you measure conversions with.

## Performance

- Images compressed as WebP or AVIF, sized for their display size, `width` and `height` set, lazy-loaded below the fold. The main above-the-fold image is not lazy-loaded.
- Fonts self-hosted, limited to the weights used, `font-display: swap`, main font preloaded.
- Total page weight checked. A page of several megabytes loses visitors before it even renders.
- PageSpeed Insights or Lighthouse run on mobile, performance and accessibility reviewed. No visible layout shift.
- Static assets cached long-term, HTML not over-cached.

## Legal (France and EU)

- Real mentions légales: publisher identity, SIRET or RCS number, address, publication director, host name and address.
- A real privacy policy, filled in and matching what the site actually collects (forms, analytics, cookies): purposes, retention, rights, contact.
- Real CGV if the site sells, CGU if there are user accounts. Not a template.
- Cookie banner with « Refuser » as easy as « Accepter », no tracker set before consent, and a footer link to change the choice later.
- Users with accounts can delete their account and get their data (RGPD), from the interface or by a documented request.
- If the site sells to consumers, check whether the European Accessibility Act applies (in force since June 2025, micro-enterprises exempt).

## Analytics

- Audience measurement installed and receiving data, checked in its dashboard. Without it, you never learn what works or where people leave.
- Configured for the CNIL consent exemption, or loaded only after consent.
- Conversions tracked through the confirmation page.

## Reliability and security

- `reliability` skill items checked: rate limits, API caps, timeouts, error and empty states, error tracking, uptime monitoring, backup restore tested.
- `security` skill audit (`audit.md`) run.

## Trust

- No fake testimonial, counter or invented figure. Every number on the site has a source.
- Real photos or none.
- Tells audit from the skill done (`tells.md`), with every remaining part 2 pattern justified in `DESIGN.md`.
