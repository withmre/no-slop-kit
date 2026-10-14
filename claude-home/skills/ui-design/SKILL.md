---
name: ui-design
description: Design rules against generic AI-looking interfaces (trust killers, dark patterns, default reflexes, component-gallery effects, boxed layouts, default fonts and colors), plus hierarchy, typography, color, tokens, imagery, states, mobile, accessibility, components and a launch checklist. Use whenever a task creates or changes UI: a marketing site, landing page, app screen, dashboard, component, layout, colors, fonts or interface copy, and before saying a site is done.
---

# UI design

A visitor never reads the code. In a few seconds they spot a handful of details, often without being able to name them, and decide how serious the site is. The goal is an interface that could only belong to this project.

The rule behind everything below: every visible element is a choice. Most patterns listed here are fine when someone decided them for a reason. Stacked by default, they sign a site nobody designed.

Files in this skill's folder:

- `components.md`: read it when building forms, buttons, navigation, header and footer, modals, toasts, tables, dashboards or app screens.
- `launch-checklist.md`: read it before saying a site is done.

## 1. Direction first, code second

Decide which kind of interface this is:

- Marketing site: persuade and get one action. Personality, rhythm and real proof matter.
- Application or dashboard: let people work. Density, consistency and predictability matter. No hero, no decoration, no marketing copy inside the product.

For a new site, a new app or a redesign, write a short brief and show it to me before building:

- Who it's for, and the one action the page must get them to take.
- Tone, in a few words.
- One real-world reference that fits: a print magazine, a signage system, an art movement, a period, a site I like. Ask me if I have one.
- Palette (hex values) and fonts, each with one sentence tying the choice to the project.
- Layout principle: editorial single column, dense data grid, asymmetric split, etc.
- Site structure: which pages, and why.
- Any pattern from section 3 you intend to use on purpose, with the reason.

When nothing is set, propose two clearly different directions and let me pick. If the project has a brand or a design system, follow it strictly and skip the brief.

Once approved, write the design tokens before any component (section 7), and record the choices in the project's CLAUDE.md under "Design" so every later page stays consistent.

Your first instinct for a font or a color is probably your usual default. If you'd make the same choice for any project, drop it and pick again.

## 2. Trust killers: never ship these

These are faults, whatever the taste. Fix them or flag them as `[À FOURNIR : ...]`.

Fakes

- Fake testimonials: glowing reviews signed with invented first names and generated portraits.
- Fake visitor counter (« 47 personnes consultent cette page », a number drifting in the same range).
- Fake customer counter (« Rejoignez 10 000 utilisateurs » on launch day).
- Invented figures: satisfaction or growth percentages nothing measures.
- Fake scarcity or urgency: invented stock levels, countdown timers that reset on reload.
- Visibly AI-generated photos: over-smooth faces, odd hands, garbled text inside the image.
- A generic stock photo as hero: handshake, smiling team around a laptop, abstract city at night.

Dark patterns (also a legal risk in the EU)

- Pre-checked boxes for newsletters, options or consent.
- Confirmshaming: « Non merci, je préfère payer plus cher ».
- Cancel or unsubscribe harder to find than sign up.
- Items or options added to the cart without asking. Costs revealed only at the last step.
- A cookie banner where refusing takes more clicks than accepting.

Broken or unfinished

- Buttons and links that do nothing: `href="#"`, dead links, buttons without a handler. Every interactive element works, or it goes.
- Empty or boilerplate privacy policy, CGU, CGV or mentions légales.
- Framework leftovers: default page title (« Vite + React », « Create Next App », « Untitled »), default favicon, default meta description, starter content.
- Placeholder text: lorem ipsum, « Votre titre ici », `John Doe`, `example.com`, `[À FOURNIR]` markers.
- A copyright year that isn't current. Generate it, or drop the year.
- No favicon: the empty icon in the tab.
- Horizontal scroll on mobile.
- Errors in the browser console.
- The generator's badge left in the footer.
- Deployment subdomain as the public address (`*.vercel.app`, `*.netlify.app`, `*.pages.dev`).

Signature of a generated site

- Emoji as icons: a rocket, a light bulb, a lightning bolt.
- A headline that says nothing (« Libérez tout votre potentiel »).
- Em dashes in site copy.
- A logo that is just the name typed in the default font. Ask for the real logo. Without one, build a deliberate wordmark (chosen typeface, weight, spacing) and flag it as temporary.
- A decorative handwritten or cursive font on a professional site.
- A headline whose gradient color cycles in a loop.
- No real demonstration of the product: only illustrations and promises. This one costs the most. Use a real screenshot, a short video or a live demo. None available: `[À FOURNIR]`.
- Everything piled on a single page with no structure. One page suits a single offer. Beyond that, real pages, and only pages that have real content.

## 3. Default reflexes: only when chosen

None of these is a mistake on its own. A bento grid can be the right layout, Inter is an excellent typeface, well-used liquid glass works. Ask of each element: did I choose it, or was it there by default? Use one only if the brief says why.

Color and background

- Saturated colors clashing in a gradient, purple to blue above all. Purple and black.
- Neon on dark backgrounds. Basic washed-out pastels, the exact opposite and just as automatic.
- A different hue per section, rainbow style, with no decided palette.
- Pure `#FFFFFF` background, never broken. Same for pure `#000`.
- A colored accent band crossing the page for no reason.
- Blurry glowing orbs, aurora backgrounds, dot grids, grid lines, grain or noise overlay on everything.

Surfaces

- A drop shadow on every element.
- The same soft radius on every corner, with no hierarchy.
- Liquid glass blur applied everywhere.
- Everything boxed in cards (section 4).
- Gradient or animated borders on cards and buttons.

Section patterns

- Three feature cards side by side, always with an icon on top.
- Bento grid as the reflex for any presentation section.
- Three pricing tiers with the middle one highlighted, even with a single offer. Show the offers that actually exist.
- A green checkmark before every benefit.
- Pill badge above the hero title (« Nouveau », « Propulsé par l'IA »).
- Hero with a solid button plus a ghost button.
- Small uppercase, wide-tracked label above every section title.
- An icon in a tinted rounded square above every card title.
- Big stat row (« 10x », « 99,9 % »), unless the numbers are real and sourced.
- Logo wall « Ils nous font confiance », or an infinite logo marquee, without real logos used with permission.
- FAQ accordion filled with invented questions.
- Four-column footer linking to pages that don't exist.
- Every section ending with the same call-to-action block.

Component-gallery effects (Aceternity, Magic UI and similar)

- Shimmer text, typewriter text, words that swap in a loop.
- Spotlight glow following the cursor on cards. 3D tilt cards.
- Border beams, meteors, sparkles, particles, animated beams between logos.
- Numbers counting up from zero.
- Floating pill-shaped navigation bar.

Icons and decoration

- Decorative pictograms floating in the margins.
- The sparkle icon meaning « IA » on every button.
- Bouncing arrows inviting the visitor to scroll.
- A fake terminal or code window, even for a product with no code.
- Stock 3D illustrations, abstract generated images, SVG blobs.

Motion and behavior

- Every block fading in on scroll.
- A hover animation on everything, including what isn't clickable.
- Parallax, scroll hijacking, custom cursor.
- A splash screen or preloader on a site that loads fast anyway.
- Autoplay video with sound. Carousels.
- Newsletter popup on arrival or on exit. Chat bubble added by default. « Back to top » button on a short page.

Typography and framework defaults

- Inter, Geist, Space Grotesk: excellent, and instantly recognizable as generator defaults. Also overused: Poppins, Montserrat, Roboto, Open Sans, DM Sans, Plus Jakarta Sans, Manrope, Outfit, Playfair Display, Instrument Serif.
- Tailwind or shadcn left untouched: slate or zinc greys, `rounded-lg` everywhere, `indigo-500` or `blue-600` accent, `shadow-md` on every block.

## 4. Layout and hierarchy

- Not everything goes in a card. Group with spacing, alignment, type size and the occasional thin rule. A card is for a repeated, self-contained item the user clicks or compares.
- Never a card inside a card. One level of container at most.
- One separator per boundary: a border, a background or a shadow. Never all three.
- One primary action per screen. Other actions are visibly secondary.
- Squint test: blur your eyes. The most important element should still stand out, and the reading order should be obvious.
- A grid: a max content width, consistent columns, everything aligned to shared edges. Nothing floating at an arbitrary offset.
- Don't build every section the same way. Alternate a text-led section, a split layout, a full-width image, a plain list, a table.
- Left-align text by default. Center only short hero lines.
- Spacing with rhythm: tight inside a group, generous between sections. Every margin, padding and gap comes from the spacing scale. No arbitrary values like `mt-[37px]`.
- Body text: 60 to 75 characters per line.
- French text runs 20 to 30 % longer than English. Design with the real French copy. Short placeholder words hide overflow problems.
- Stress-test with extreme content: a very long name, a title on three lines, a missing image, zero items, one item, a thousand items.

## 5. Color

- Derive the palette from the project: logo, subject, audience, the reference from the brief. Never from habit.
- Structure: one neutral scale with a faint tint (warm or cool), one accent, semantic colors for success, warning and error. Nothing more without a reason.
- The accent is rare: call to action, links, active state. About a tenth of the surface at most.
- Background: an off-white or an off-black chosen with the palette.
- Color never carries meaning alone: errors also get an icon or text, links in body text are underlined.
- Dark mode only if both themes are designed. A dark theme is its own palette, with lower-contrast surfaces and a desaturated accent. Inverting the light theme looks broken.
- Set `::selection`, focus ring color and the `theme-color` meta from the palette.
- Check AA contrast for every text and background pair actually used, including text on images.

## 6. Typography

- Choose fonts for the project's character and justify in one sentence.
- Look beyond Google Fonts: Fontshare, Velvetyne, independent foundries. Check the license allows web use. Self-host the files.
- For an app or a dashboard, the system font stack is a legitimate lazy choice: nothing to load, native feel. Say so when you pick it.
- One family is often enough, two at most. A second only for real contrast: a serif with a sans, or a monospace for data. Three families means nobody chose.
- Strong scale with few sizes: headings clearly larger than body. Fluid sizes with `clamp()` for large headings.
- Body text at least 16 px. Inputs at least 16 px too, or iOS Safari zooms on focus.
- Body line-height around 1.5, large headings tighter (1.1 to 1.2) with slightly tighter letter-spacing. No wide tracking on lowercase text. No justified text.
- `text-wrap: balance` on headings, `text-wrap: pretty` on paragraphs where supported, to avoid lone words on the last line.
- French typography: `lang="fr"`, « guillemets » with non-breaking spaces, non-breaking space before `:` `;` `!` `?`, accented capitals (À, É), `hyphens: auto` on narrow columns.
- `font-variant-numeric: tabular-nums` for tables and figures.

## 7. Tokens and surfaces

Define tokens in one place before building components: colors, type scale, spacing scale, radii, shadows, border colors, motion durations and easings. Components only use tokens.

- Radii: two or three values with a role (small for inputs and tags, larger for panels). Nested elements follow `inner radius = outer radius - padding`, or the corners look off.
- Shadows: two or three elevation levels at most, one consistent light source. Many interfaces need none.
- Borders: 1 px, one or two border colors from the neutral scale.
- Icons: one library, one stroke width, one size per context, aligned with the text next to them.

## 8. Imagery

- One art direction for all images: same treatment, same light, same crop logic, fixed aspect ratios with `aspect-ratio`.
- Real photos of the product, the team, the place or the work. No stock that could illustrate anything.
- No text baked into images: it doesn't translate, scale or read on mobile.
- Screenshots of the product kept current, at a readable size, cropped on what matters.

## 9. States, interaction and mobile

- Every interactive element has hover, focus, active and disabled states, and `cursor: pointer` when clickable. Non-interactive elements have no hover effect.
- Data states (loading, empty, error, partial) and failure handling: follow the `reliability` skill. Loading uses a skeleton shaped like the content.
- Submit buttons show progress and are disabled while sending.
- After a submission, a confirmation page with its own URL.
- On mobile, when the page is long, keep the main action reachable (sticky button) without covering content, and respect `env(safe-area-inset-bottom)`.
- Full-height sections use `100dvh`, not `100vh`, so mobile browser bars don't cut them.
- No layout shift: images and embeds have dimensions, fonts use `font-display: swap`, late content gets reserved space.
- Motion: one purposeful transition (state change, panel opening) beats ten decorative ones. 150 to 250 ms, ease-out for entering, animate only `transform` and `opacity`. Respect `prefers-reduced-motion`.

## 10. Interface copy

- Apply the `deslop` rules to every piece of copy.
- The main headline says what the product does and for whom.
- Buttons name the action (« Créer mon devis »). Avoid « Commencer », « Découvrir », « En savoir plus ».
- Destructive actions name what gets destroyed (« Supprimer le projet »), next to a plain « Annuler ».
- Error messages say what happened and what to do, without blaming the user and without technical codes.
- No filler adjectives: puissant, intuitif, fluide, simple, innovant.
- Dates, numbers and prices formatted for the locale (`Intl`, « 1 234,50 € » in French).
- Missing copy, figures, names or legal text: `[À FOURNIR : ...]`, listed in your reply.

## 11. Lazy version

- HTML and CSS first. JavaScript only when native isn't enough: `<details>`, `<dialog>`, native form validation, CSS `:has()` and scroll snap before a library.
- Reuse the project's components or the installed UI library before creating new ones. Restyle a library to the tokens rather than shipping its defaults.
- No animation library for a fade.
- Before adding a section, say what it gives the visitor. No answer, no section.

## 12. Accessibility

- AA contrast minimum, full keyboard navigation in a logical order, visible focus.
- A label for every field. Descriptive `alt` on informative images, `alt=""` on decorative ones. `aria-label` on icon-only buttons.
- `lang` on `<html>`, a coherent heading hierarchy, one `h1` per page, landmarks (`header`, `nav`, `main`, `footer`).
- Touch targets at least 44 px.
- Usable at 200 % zoom without horizontal scroll.

## 13. Self-check before showing me

- Logo test: hide the logo. If the page could be anyone's, rework what makes it generic.
- Reflex audit: list every item from sections 2 and 3 present on the page. For each, write "chosen: reason from the brief" or "default: removed". Section 2 items are never "chosen".
- Count the boxes. If most content sits in cards, remove cards.
- Count fonts, sizes, colors, radii and shadows. Cut what isn't used on purpose.
- Squint test on each screen.
- Stress test with extreme content (section 4).
- Click every link and button. Tab through the page with the keyboard only.
- Open the browser console: zero errors.
- Search the code for leftovers: `lorem`, `TODO`, `John Doe`, `example.com`, `Vite + React`, `Create Next App`, hard-coded hex values and arbitrary spacing outside the tokens.
- If you can render the page (Playwright, a browser tool), look at screenshots at 375 px and on a wide screen. Mention that Safari on iOS still needs a real-device check.
