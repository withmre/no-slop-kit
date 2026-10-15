"""Renders assets/web-before-after.gif from the six pages in assets/src/pages.

Usage: python3 make_web_demo.py <output-dir>

For each example: the "without" page appears and its tells are listed one by one, a wipe reveals the
"with" page, its own animation plays, then the page scrolls to the bottom.

Needs Playwright with Chromium, Pillow and ffmpeg. The "with" pages self-host their fonts (pages/fonts,
SIL Open Font License). The "without" pages expect Inter, Poppins and TeX Gyre Chorus installed locally.
The labels use Bitstream Charter and DejaVu Sans Mono; adjust LABEL_SERIF and LABEL_MONO for your system.
The "without" pages reproduce the default patterns the ui-design skill targets. Brands, people and prices
are fictional.
"""
import os, shutil, subprocess, sys, tempfile
from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1]
LABEL_SERIF = "/usr/share/fonts/X11/Type1/c0648bt_.pfb"
LABEL_MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
BG, INK, MUTED, RULE = (242, 241, 237), (30, 30, 28), (107, 106, 102), (216, 214, 208)
FPS = 10
VW, VH = 1280, 800            # browser viewport
W, PH = 920, 575             # page area in the GIF
TOP, BOT = 46, 42

EXAMPLES = [
    ("1/3  Landing page for an invoicing app",
     ["purple gradient", "pill badge", "gradient word", "centered hero", "fake 10,000+", "emoji icons", "three cards"],
     "carbon-copy booklet, product first, Schibsted Grotesk + Plex Mono, red only for 'paid'"),
    ("2/3  Website for a neighborhood bakery",
     ["script font", "full-screen centered hero", "pastel gradient", "invented rating", "emoji", "empty promises"],
     "Lyon shopfront and awning, oven times first, Gloock + Newsreader, green as the only accent"),
    ("3/3  Portfolio of a product designer",
     ["pure black", "neon glow", "dot grid", "italic word in headline", "typed cursor", "invented stats"],
     "letter structure, annotated paper form, Young Serif + Hanken Grotesk, non-photo blue"),
]

ser = ImageFont.truetype(LABEL_SERIF, 21)
mono = ImageFont.truetype(LABEL_MONO, 14)
mono_s = ImageFont.truetype(LABEL_MONO, 12)
mono_l = ImageFont.truetype(LABEL_MONO, 16)


def chrome(page_img, title, label, caption):
    img = Image.new("RGB", (W, TOP + PH + BOT), BG)
    d = ImageDraw.Draw(img)
    d.text((20, 13), title, font=ser, fill=INK)
    d.text((W - 20 - mono_l.getlength(label), 15), label, font=mono_l, fill=INK if label.startswith("with ") else MUTED)
    img.paste(page_img, (0, TOP))
    d.line([(0, TOP - 1), (W, TOP - 1)], fill=RULE)
    d.line([(0, TOP + PH), (W, TOP + PH)], fill=RULE)
    f = mono
    if f.getlength(caption) > W - 40:
        f = mono_s
    d.text((20, TOP + PH + 13), caption, font=f, fill=INK)
    return img


def shrink(path):
    return Image.open(path).convert("RGB").resize((W, PH), Image.LANCZOS)


def ease(t):
    return t * t * (3 - 2 * t)


def capture(tmp):
    shots = {}
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": VW, "height": VH})
        for i in (1, 2, 3):
            pg.goto("file://" + os.path.join(HERE, "pages", f"{i}-without.html"))
            pg.wait_for_timeout(400)
            f = os.path.join(tmp, f"{i}-without.png"); pg.screenshot(path=f)
            shots[(i, "without")] = [f]

            pg.goto("file://" + os.path.join(HERE, "pages", f"{i}-with.html"))
            pg.evaluate("document.fonts.ready")
            pg.evaluate("document.getAnimations().forEach(a => { a.pause(); a.currentTime = 0; })")
            anim = []
            for k in range(int(2.6 * FPS)):
                ms = k * 1000 / FPS
                pg.evaluate(f"document.getAnimations().forEach(a => a.currentTime = {ms})")
                f = os.path.join(tmp, f"{i}-anim-{k:03d}.png"); pg.screenshot(path=f); anim.append(f)
            shots[(i, "anim")] = anim
            pg.evaluate("document.getAnimations().forEach(a => a.finish())")
            height = pg.evaluate("document.documentElement.scrollHeight")
            scroll = []
            n = int(2.8 * FPS)
            for k in range(n + 1):
                y = int(ease(k / n) * max(0, height - VH))
                pg.evaluate(f"window.scrollTo(0, {y})")
                f = os.path.join(tmp, f"{i}-scroll-{k:03d}.png"); pg.screenshot(path=f); scroll.append(f)
            shots[(i, "scroll")] = scroll
        b.close()
    return shots


def build(shots, frames_dir):
    n = 0
    def emit(img, count=1):
        nonlocal n
        for _ in range(count):
            img.save(os.path.join(frames_dir, f"f{n:05d}.png")); n += 1
    for i, (title, tells, choices) in enumerate(EXAMPLES, 1):
        without = shrink(shots[(i, "without")][0])
        first_with = shrink(shots[(i, "anim")][0])
        emit(chrome(without, title, "without the kit", "Tells:"), int(1.0 * FPS))
        for k in range(1, len(tells) + 1):
            emit(chrome(without, title, "without the kit", "Tells: " + ", ".join(tells[:k])), int(0.45 * FPS))
        emit(chrome(without, title, "without the kit", "Tells: " + ", ".join(tells)), int(1.2 * FPS))
        steps = int(1.0 * FPS)
        for k in range(1, steps + 1):
            x = int(ease(k / steps) * W)
            mix = without.copy(); mix.paste(first_with.crop((0, 0, x, PH)), (0, 0))
            ImageDraw.Draw(mix).line([(x, 0), (x, PH)], fill=INK, width=3)
            label = "with the kit" if k > steps / 2 else "without the kit"
            emit(chrome(mix, title, label, "Choices: " + choices if k > steps / 2 else "Tells: " + ", ".join(tells)))
        for f in shots[(i, "anim")]:
            emit(chrome(shrink(f), title, "with the kit", "Choices: " + choices))
        for f in shots[(i, "scroll")]:
            emit(chrome(shrink(f), title, "with the kit", "Choices: " + choices))
        emit(chrome(shrink(shots[(i, "scroll")][-1]), title, "with the kit", "Choices: " + choices), int(1.0 * FPS))
    return n


def main():
    tmp = tempfile.mkdtemp()
    frames = os.path.join(tmp, "frames"); os.makedirs(frames)
    shots = capture(tmp)
    build(shots, frames)
    pal = os.path.join(tmp, "palette.png")
    src = os.path.join(frames, "f%05d.png")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-framerate", str(FPS), "-i", src,
                    "-vf", "palettegen=max_colors=200:stats_mode=diff", pal], check=True)
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-framerate", str(FPS), "-i", src, "-i", pal,
                    "-lavfi", "paletteuse=dither=bayer:bayer_scale=5:diff_mode=rectangle",
                    "-loop", "0", os.path.join(OUT, "web-before-after.gif")], check=True)
    shutil.rmtree(tmp)


main()
