"""Renders the README demo animations and the social preview.

Usage: python3 make_assets.py <output-dir>
Fonts: Bitstream Charter and DejaVu Sans Mono. Adjust the paths below to your system.
"""
import sys
from PIL import Image, ImageDraw, ImageFont

OUT = sys.argv[1]
SERIF = "/usr/share/fonts/X11/Type1/c0648bt_.pfb"
SERIF_BOLD = "/usr/share/fonts/X11/Type1/c0632bt_.pfb"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

BG = (245, 241, 234)
INK = (34, 32, 28)
MUTED = (110, 104, 95)
ACCENT = (180, 68, 30)
TINT = (243, 215, 200)
RULE = (221, 213, 201)

W, H = 1200, 630
PAD = 72
S = 2  # supersampling


def font(path, size):
    return ImageFont.truetype(path, size * S)


EN = {
    "before_label": "Before", "after_label": "After",
    "count": "markers: {n}", "final": "{n} markers → 0",
    "kept": "Every idea kept. Form rewritten.",
    "flag": "Flagged for the author: “measurable growth” comes with no figure.",
    "segments": [
        ("In today's fast-paced digital landscape,", 1, "generic opener, banned word"),
        ("building a website is", None, None),
        ("no longer just about code", 2, "“it's not X, it's Y”"),
        ("—", 3, "em dash"),
        ("it's about", 2, None),
        ("crafting", None, None),
        ("seamless", 4, "banned word"),
        ("experiences that", None, None),
        ("truly", 5, "empty intensifier"),
        ("resonate", 6, "banned word"),
        ("with your audience.", None, None),
        ("Whether you're a startup or an enterprise,", 7, "stock opener"),
        ("our", None, None),
        ("cutting-edge", 8, "banned word"),
        ("platform", None, None),
        ("empowers", 9, "banned word"),
        ("you to", None, None),
        ("unlock your full potential.", 10, "banned phrase"),
        ("The result?", 11, "question answered right away"),
        ("Faster launches, happier customers, and measurable growth.", 12, "reflex group of three"),
        ("It's not just a tool. It's a", 13, "“it's not X, it's Y” again"),
        ("game-changer.", 14, "banned word"),
    ],
    "after": "Building a website takes more than code: people have to enjoy using it. "
             "Our platform helps startups and large companies launch sooner. "
             "Customers stay happier, and the growth shows up in your numbers.",
}

FR = {
    "before_label": "Avant", "after_label": "Après",
    "count": "marqueurs : {n}", "final": "{n} marqueurs → 0",
    "kept": "Toutes les idées gardées. La forme réécrite.",
    "flag": None,
    "segments": [
        ("Dans un monde en constante évolution,", 1, "généralité passe-partout"),
        ("créer un site web", None, None),
        ("ne se résume plus au code", 2, "« ce n'est pas X, c'est Y »"),
        ("—", 3, "tiret cadratin"),
        ("c'est avant tout", 2, None),
        ("une expérience.", None, None),
        ("Que vous soyez freelance ou grande entreprise,", 4, "ouverture toute faite"),
        ("notre solution", None, None),
        ("innovante", 5, "mot banni"),
        ("vous permet de", None, None),
        ("booster", 6, "mot banni"),
        ("votre visibilité.", None, None),
        ("Le résultat ?", 7, "question suivie de sa réponse"),
        ("Plus de clients, plus de temps, plus de sérénité.", 8, "groupe de trois réflexe"),
        ("Ce n'est pas un outil. C'est un", 9, "« ce n'est pas X, c'est Y », encore"),
        ("véritable", 10, "intensif creux"),
        ("levier", 11, "mot banni"),
        ("de croissance.", None, None),
    ],
    "after": "Un site web doit aussi être agréable à utiliser. "
             "Notre solution aide les freelances comme les grandes entreprises à se faire connaître. "
             "Vous gagnez des clients et du temps. Votre activité grandit, et vous travaillez plus sereinement.",
}

F_TEXT = font(SERIF, 31)
F_MONO = font(MONO, 19)
F_MONO_BIG = font(MONO, 24)
F_CMD = font(MONO, 22)
LINE = int(31 * 1.5) * S
MAXW = (W - 2 * PAD) * S
TOP = 150 * S


def tokens(segments):
    out = []
    for text, mid, _ in segments:
        for w in text.split(" "):
            out.append((w, mid))
    return out


def layout(toks):
    lines, cur, x = [], [], 0
    space = F_TEXT.getlength(" ")
    for w, mid in toks:
        wl = F_TEXT.getlength(w.replace(" ", " "))
        if cur and x + wl > MAXW:
            lines.append(cur)
            cur, x = [], 0
        cur.append((w, mid, x, wl))
        x += wl + space
    if cur:
        lines.append(cur)
    return lines


def base(lang, label, right_text, caption):
    img = Image.new("RGB", (W * S, H * S), BG)
    d = ImageDraw.Draw(img)
    d.text((PAD * S, 56 * S), "/deslop", font=F_CMD, fill=ACCENT)
    cmd_w = F_CMD.getlength("/deslop ")
    d.text((PAD * S + cmd_w, 58 * S), label, font=F_MONO, fill=MUTED)
    d.line([(PAD * S, 104 * S), ((W - PAD) * S, 104 * S)], fill=RULE, width=S)
    d.line([(PAD * S, (H - 92) * S), ((W - PAD) * S, (H - 92) * S)], fill=RULE, width=S)
    if caption:
        d.text((PAD * S, (H - 66) * S), caption, font=F_MONO, fill=MUTED)
    if right_text:
        rw = F_MONO_BIG.getlength(right_text)
        d.text(((W - PAD) * S - rw, (H - 70) * S), right_text, font=F_MONO_BIG, fill=ACCENT)
    return img, d


def before_frame(lang, revealed, current):
    labels = {m: c for _, m, c in lang["segments"] if m and c}
    caption = labels.get(current, "") if current else ""
    n = len(revealed)
    img, d = base(lang, lang["before_label"], lang["count"].format(n=n), caption)
    lines = layout(tokens(lang["segments"]))
    space = F_TEXT.getlength(" ")
    for i, line in enumerate(lines):
        y = TOP + i * LINE
        for j, (w, mid, x, wl) in enumerate(line):
            if mid in revealed:
                ext = space if j + 1 < len(line) and line[j + 1][1] == mid else 0
                color = TINT
                d.rounded_rectangle([PAD * S + x - 3 * S, y - 2 * S, PAD * S + x + wl + ext + 3 * S, y + 40 * S],
                                    radius=4 * S, fill=color)
                if mid == current:
                    d.line([(PAD * S + x - 3 * S, y + 40 * S), (PAD * S + x + wl + ext + 3 * S, y + 40 * S)],
                           fill=ACCENT, width=2 * S)
        for w, mid, x, wl in line:
            d.text((PAD * S + x, y), w.replace(" ", " "), font=F_TEXT, fill=INK)
    return img


def after_frame(lang, total):
    img, d = base(lang, lang["after_label"], lang["final"].format(n=total), lang["kept"])
    toks = [(w, None) for w in lang["after"].split(" ")]
    lines = layout(toks)
    for i, line in enumerate(lines):
        y = TOP + i * LINE
        for w, mid, x, wl in line:
            d.text((PAD * S + x, y), w.replace(" ", " "), font=F_TEXT, fill=INK)
    if lang["flag"]:
        y = TOP + (len(lines) + 1) * LINE
        d.text((PAD * S, y), lang["flag"], font=F_MONO, fill=MUTED)
    return img


def shrink(img):
    return img.resize((W, H), Image.LANCZOS)


def gif(lang, path):
    order = []
    for _, m, _ in lang["segments"]:
        if m and m not in order:
            order.append(m)
    frames, durations = [], []
    frames.append(before_frame(lang, set(), None)); durations.append(2200)
    revealed = set()
    for m in order:
        revealed.add(m)
        frames.append(before_frame(lang, set(revealed), m)); durations.append(650)
    frames.append(before_frame(lang, set(revealed), None)); durations.append(1600)
    frames.append(after_frame(lang, len(order))); durations.append(4500)
    small = [shrink(f).convert("P", palette=Image.ADAPTIVE, colors=128) for f in frames]
    small[0].save(path, save_all=True, append_images=small[1:], duration=durations, loop=0, optimize=True)


def social(path):
    w, h = 1280, 640
    img = Image.new("RGB", (w * S, h * S), BG)
    d = ImageDraw.Draw(img)
    d.text((80 * S, 150 * S), "No Slop Kit", font=font(SERIF_BOLD, 84), fill=INK)
    d.text((80 * S, 268 * S), "Global rules and five skills for Claude Code.", font=font(SERIF, 36), fill=INK)
    d.text((80 * S, 320 * S), "Less code, nothing invented, fewer tokens, no AI slop.", font=font(SERIF, 36), fill=MUTED)
    ex = "It's not just a tool. It's a game-changer."
    f = font(SERIF, 32)
    x0, y0 = 80 * S, 430 * S
    tw = f.getlength(ex)
    d.rounded_rectangle([x0 - 4 * S, y0 - 4 * S, x0 + tw + 4 * S, y0 + 42 * S], radius=4 * S, fill=TINT)
    d.text((x0, y0), ex, font=f, fill=INK)
    d.line([(x0, y0 + 18 * S), (x0 + tw, y0 + 18 * S)], fill=ACCENT, width=3 * S)
    d.text((80 * S, 540 * S), "/deslop  /ui-design  /security  /reliability  /project-setup", font=font(MONO, 22), fill=ACCENT)
    gh = "github.com/withmre/no-slop-kit"
    gf = font(MONO, 22)
    d.text(((w - 80) * S - gf.getlength(gh), 70 * S), gh, font=gf, fill=MUTED)
    img.resize((w, h), Image.LANCZOS).save(path, optimize=True)


gif(EN, OUT + "/deslop-demo.gif")
gif(FR, OUT + "/deslop-demo-fr.gif")
social(OUT + "/social-preview.png")
