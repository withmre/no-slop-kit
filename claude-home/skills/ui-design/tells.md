# Tells

Read before building, and again at the self-check or during an audit. Part 1 is never acceptable. Part 2 is acceptable only when the brief says why.

Severity for audits: part 1 is **critical**, except quick fixes (copyright year, favicon, leftover title) and the craft faults, which are **major**. Part 2 is **major** when it dominates a screen, **minor** otherwise.

## Part 1. Trust killers: never ship these

Fix them or flag them as `[À FOURNIR : ...]`.

Fakes

- Fake testimonials: glowing reviews signed with invented first names and generated portraits.
- Fake visitor counter (« 47 personnes consultent cette page », a number drifting in the same range).
- Fake customer counter (« Rejoignez 10 000 utilisateurs » on launch day).
- Invented figures: satisfaction, growth or speed claims nothing measures (« 10x faster », « +47 % conversion »). Use the real number, a visible placeholder, or another structure without a proof slot.
- Fake scarcity or urgency: invented stock levels, countdown timers that reset on reload.
- Visibly AI-generated photos: over-smooth faces, odd hands, garbled text inside the image.
- A generic stock photo as hero: handshake, smiling team around a laptop, abstract city at night.

Dark patterns (also a legal risk in the EU)

- Pre-checked boxes for newsletters, options or consent.
- Confirmshaming: « Non merci, je préfère payer plus cher ».
- Cancel or unsubscribe harder to find than sign up.
- Items or options added to the cart without asking. Costs revealed only at the last step.
- A cookie banner where refusing takes more clicks than accepting.

Broken or unfinished

- Buttons and links that do nothing: `href="#"`, dead links, buttons without a handler.
- Empty or boilerplate privacy policy, CGU, CGV or mentions légales.
- Framework leftovers: default page title (« Vite + React », « Create Next App », « Untitled »), default favicon, default meta description, starter content.
- Placeholder content: lorem ipsum, « Votre titre ici », `John Doe`, `Jane Smith`, `example.com`. `[À FOURNIR]` markers are fine while drafting and block the launch.
- A copyright year that isn't current.
- No favicon.
- Horizontal scroll on mobile, or a button label wrapping onto two lines.
- Errors in the browser console.
- The generator's badge left in the footer.
- Deployment subdomain as the public address (`*.vercel.app`, `*.netlify.app`, `*.pages.dev`).

Craft faults

- A card inside a card.
- `transition: all`, and bouncy, overshooting easings on buttons, menus and dialogs.
- Hover effects on elements that aren't clickable.
- Focus rings that fade in instead of appearing at once.

Signature of a generated site

- Emoji as icons: a rocket, a light bulb, a lightning bolt.
- A headline that says nothing (« Libérez tout votre potentiel »).
- Em dashes in site copy.
- A logo that is just the name typed in the default font. Ask for the real logo, or build a deliberate wordmark and flag it as temporary.
- A decorative handwritten or cursive font on a professional site.
- Gradient text in headings, animated or not.
- One italic word inside an upright headline (« Built to *think* »), or italic display type on every heading.
- Re-drawn chrome: a fake browser bar with three dots, a fake phone frame, a fake code or terminal window, a fake IDE. Use a real screenshot in a `<figure>` with at most a hairline border, or no frame.
- No real demonstration of the product: only illustrations and promises. Use a real screenshot, a short video or a live demo. None available: `[À FOURNIR]`.
- Startup-cliché names in demo content: Acme, Nexus, Pulse, Apex, Quantum.

## Part 2. Default reflexes: only when chosen

Ask of each: did I choose it, or was it there by default?

Page structure

- The template rhythm: centered hero, three features, call to action, footer.
- A hero that fills the whole screen with everything centered on one axis and one short sentence. Let the hero be as tall as its content, and break the axis.
- Two pages of the same project sharing the same structure, with only the copy changed.
- Every section padded the same, separated only by equal whitespace.
- Every section ending with the same call-to-action block.
- Everything piled on a single page when the content needs several.

Navigation and footer

- The default nav: wordmark left, a row of links in the middle, a button right, full width, sticky, white, hairline border. It looks the same on a bakery and a SaaS. Shape the nav after the site: two links for a small site, a masthead for an editorial site, a command bar for a developer tool.
- The default footer: four columns (Product, Company, Resources, Legal), a row of social icons, a tiny copyright line. A footer closes the page: legal links, contact, and only what exists.

Color and background

- Saturated colors clashing in a gradient, purple to blue above all. Purple and black.
- Neon on dark backgrounds, or a colored glow around cards on dark. Basic washed-out pastels.
- A different hue per section, rainbow style, with no decided palette.
- Pure `#FFFFFF` or pure `#000` as the base.
- A colored accent band crossing the page for no reason.
- Blurry glowing orbs, aurora backgrounds, dot grids, grid lines, grain on everything.

Surfaces

- A drop shadow on every element.
- The same soft radius on every corner, with no hierarchy.
- Liquid glass blur applied everywhere.
- Everything boxed in cards.
- A thick colored stripe on one side of a card.
- Gradient or animated borders on cards and buttons.

Section patterns

- Three feature cards side by side, always with an icon in a tinted rounded square on top.
- Bento grid as the reflex for any presentation section.
- Three pricing tiers with the middle one highlighted, even with a single offer.
- A green checkmark before every benefit.
- Pill badge above the hero title (« Nouveau », « Propulsé par l'IA »).
- Hero with a solid button plus a ghost button.
- A small uppercase label above every section title. Labels are off by default: use them only when sections are numbered steps or chapters, one or two per page, stacked directly above their heading. Never a label in a left column with the heading on the right.
- Big stat row (« 10x », « 99,9 % ») unless the numbers are real and sourced. A number is never the whole headline.
- Logo wall or infinite logo marquee without real logos used with permission.
- FAQ accordion filled with invented questions.

Component-gallery effects

- Shimmer text, typewriter text, words that swap in a loop.
- Spotlight glow following the cursor, 3D tilt cards.
- Border beams, meteors, sparkles, particles, animated beams between logos.
- Numbers counting up from zero.
- Floating pill-shaped navigation bar.

Decoration

- Decoration with no anchor in the content: a floating ornament, a random number in a corner, a cursor beside a headline, a badge or sticker that means nothing. Decoration has to name something (an edition, a year, a step) or respond to the user.
- The sparkle icon meaning « IA » on every button.
- Bouncing arrows inviting the visitor to scroll.
- Stock 3D illustrations, abstract generated images, SVG blobs.
- A Lottie animation where CSS or a small SVG would do. A rotating 3D object nobody can interact with.

Motion and behavior

- Every block fading in on scroll. One entrance on first load is enough.
- A hover animation on every clickable element, or several hover effects at once on one element.
- Parallax, scroll hijacking, custom cursor or cursor-follower dot.
- A splash screen or preloader on a site that loads fast anyway.
- Autoplay video with sound. Carousels, above all auto-rotating ones without pause.
- Newsletter popup on arrival or on exit. Chat bubble added by default.
- A celebratory toast for an action whose result is already visible.

Typography and framework defaults

- Inter, Geist, Space Grotesk: excellent, and instantly recognizable as generator defaults. Also overused: Poppins, Montserrat, Roboto, Open Sans, DM Sans, Plus Jakarta Sans, Manrope, Outfit, Playfair Display, Instrument Serif.
- Tailwind or shadcn left untouched: slate or zinc greys, `rounded-lg` everywhere, `indigo-500` or `blue-600` accent, `shadow-md` on every block, `hover:scale-105` on every card.
