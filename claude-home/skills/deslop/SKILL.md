---
name: deslop
description: Rewrite a text (French or English) to remove what sounds AI-generated, keeping the author's ideas and examples and changing only the form, then show what was removed and why. Use when I ask to proofread, reread, humanize or « désloper » a text, when writing any copy meant for publication (site copy, article, LinkedIn post, newsletter, email, README, product description), and before delivering interface text.
---

# Deslop

## 1. Contract

- Keep every idea, example, figure, name and the author's stance. Change the form only.
- Add nothing: no new idea, no new example, no new argument, no conclusion. The result is usually shorter, never longer.
- Keep the register (tu or vous, familiar or formal), the person (je, nous, on) and the author's deliberate quirks: a recurring expression, a joke, a regional word, a chosen anglicism.
- If a fix would change the meaning, leave the sentence and flag it.
- Don't silently correct facts. Flag anything that looks wrong, and any claim with no source (« les études montrent », « de nombreux experts »).

## 2. Load the catalogue

Detect the text's language and read the matching file in this skill's folder: `fr.md` for French, `en.md` for English. Mixed text: read both.

## 3. Two kinds of rules

Absolute. Remove every instance, no exception:

- Em dash and en dash used as punctuation.
- « Ce n'est pas X, c'est Y » and all its variants (« It's not X, it's Y » in English).
- Emoji, unless I asked for them.
- The banned words of the catalogue.
- Leftovers from a generator (« Voici une version révisée », « Bien sûr ! », `[Insérer]`, Markdown symbols in a plain-text channel).

Frequency. Remove the reflex, not every occurrence. A human text has a list now and then, a bold word, a group of three, a colon. What signs a machine is repetition: every paragraph built the same way, every list in threes, every line with a colon. Fix until the pattern disappears, and keep the occurrences that carry meaning.

## 4. Don't swap one tic for another

The classic failures of a rewrite:

- Every em dash turned into a colon. Vary: comma, period, parentheses, or rebuild the sentence.
- Every triplet cut to a pair. Now everything comes in twos.
- Every long sentence chopped into fragments. Staccato is a tic too.
- Every hedge replaced by a confident punchline.
- Synonyms swapped word for word while the structure stays robotic. Change the structure.

## 5. Procedure

1. Read the whole text once. Identify its channel (site, email, LinkedIn, article, README, UI) and the author's voice before changing anything.
2. List the patterns present and their frequency.
3. Rewrite, structure first, then sentences, then words.
4. Read the result as if aloud. Any sentence you can't say in one breath gets cut.
5. Compare with the original: every idea, example and figure is still there.
6. Check: no em dash, no en dash, no banned word, no new tic from section 4.

If my request includes instructions (a light pass only, a target channel, a length), follow them over the defaults.

## 6. Output

1. The rewritten text, complete, ready to paste.
2. « Ce que j'ai retiré »: a table with columns Avant, Après, Pourquoi. One row per kind of fix, grouping repeats (« 6 tirets cadratins remplacés par des virgules, des points ou des parenthèses »). Quote short excerpts only.
3. « Laissé tel quel », only if needed: sentences kept because a fix would change the meaning, doubtful facts, unsourced claims.
4. One line: « Marqueurs : N avant, N après. »

Nothing else: no introduction, no comment on the quality of the text.
