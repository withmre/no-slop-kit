# Components

Rules for the pieces that come back in every project. Restyle any library component to the project's tokens.

## Forms

- Visible label above each field. A placeholder never replaces a label: it disappears when typing.
- Mark the optional fields or the required ones, whichever is fewer, and say which convention you use.
- Validate on blur or on submit, never on every keystroke. Show the error next to the field, keep what the user typed, and move focus to the first error on submit.
- Right `type`, `inputmode` and `autocomplete` on every input (`email`, `tel`, `postal-code`, `current-password`, `new-password`, `one-time-code`).
- One column. Fields that belong together (postal code and city) may share a line.
- Fewer fields: every field must earn its place. No « Comment nous avez-vous connus ? » by reflex.
- Password fields have a show button. No confirmation field when a show button exists.
- Radio buttons for under five options, a select beyond. A checkbox for a single yes or no.
- Submit button labeled with the action, disabled and showing progress while sending.

## Buttons and links

- Three styles at most: primary, secondary, destructive. One primary per screen.
- A link goes somewhere, a button does something. Never a `div` with a click handler.
- Same height for buttons and inputs on the same line.
- External links don't open a new tab by default, unless leaving would lose work.

## Navigation, header, footer

- Five main navigation items at most. Labels are the plain page names.
- Current page visible in the navigation.
- Mobile menu: opens, closes with a button and with `Escape`, closes after a click, locks the page scroll while open.
- Sticky header only if it's slim, and never more than about 15 % of a mobile screen.
- Logo links to the home page.
- Footer: legal links (mentions légales, confidentialité, CGV or CGU, cookie settings), contact, and only links to pages that exist.

## Modals, drawers, toasts

- A modal only for a decision that blocks the task. Never for content that could live on the page.
- Built on `<dialog>` or an accessible library: focus trapped inside, `Escape` closes, focus returns to the trigger, background scroll locked.
- Destructive confirmations name the object and the consequence.
- Toasts only for non-critical feedback (« Enregistré »). Errors that need action stay on the page. Toasts stay long enough to read and can be dismissed.

## Tables and data

- Numbers right-aligned with tabular figures, text left-aligned, units in the header.
- Sticky header on long tables. Sorting and filtering when there are more than a screenful of rows.
- On mobile, a table becomes a list of rows, or scrolls inside its own container with the first column fixed. Never the whole page.
- Empty table: say why it's empty and what to do.
- Charts: label the lines or bars directly instead of a legend when possible. For a handful of numbers, a table beats a chart.

## App screens and dashboards

- Density over air: smaller type scale, tighter spacing, more on screen than a marketing page.
- Consistency over personality: the same action looks and sits the same way on every screen.
- First run: an empty state that teaches the first action. Skip the ten-step tour.
- Destructive actions are reversible when possible (undo), confirmed otherwise.
- Keyboard: forms submit with `Enter`, dialogs close with `Escape`, the main lists are navigable.
- Settings save explicitly or auto-save with visible feedback, never silently.

## Cookie banner

- Two buttons of equal weight: « Tout accepter » and « Tout refuser », plus « Personnaliser ».
- Doesn't cover the main content on mobile, doesn't block reading.
- The choice is remembered, and a footer link reopens it.
