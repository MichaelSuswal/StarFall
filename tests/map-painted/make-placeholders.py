#!/usr/bin/env python3
"""Synthesize placeholder paintings for the painted-map test: tests/map-painted/map/{surface,under-1,clouds}.png.
Stands in for the image model until the real dry-run paintings arrive. Run from anywhere."""
import os
import random

from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "map")
SIZE = (1024, 1024)


def noise(size, sigma, blur):
    n = Image.effect_noise(size, sigma).filter(ImageFilter.GaussianBlur(blur))
    return n


def clouds():
    """Soft grey-white cloud: three octaves of blurred noise, mixed."""
    a = noise(SIZE, 64, 40)
    b = noise(SIZE, 64, 14)
    c = noise(SIZE, 64, 4)
    m = Image.blend(Image.blend(a, b, 0.35), c, 0.12)
    m = m.point(lambda v: max(0, min(255, int((v - 128) * 1.6 + 128))))
    light = Image.new("RGB", SIZE, (246, 244, 238))
    dark = Image.new("RGB", SIZE, (176, 178, 184))
    return Image.composite(light, dark, m)


def surface():
    """A few terrain blobs on a parchment-green ground, blurred into paint."""
    im = Image.new("RGB", SIZE, (176, 182, 128))  # plain
    d = ImageDraw.Draw(im)
    # the Grey Sea, left
    d.polygon([(0, 0), (190, 0), (230, 180), (200, 420), (250, 640), (200, 900), (170, 1024), (0, 1024)], fill=(118, 134, 142))
    # the Sea Marsh, lower left
    d.polygon([(200, 420), (250, 640), (200, 900), (170, 1024), (470, 1024), (440, 760), (380, 560)], fill=(132, 144, 104))
    # the Ald Valley, center
    d.polygon([(230, 180), (200, 420), (380, 560), (440, 760), (470, 1024), (700, 1024), (660, 700), (620, 460), (560, 260)], fill=(150, 176, 104))
    # the Drover's Hills, east
    d.polygon([(620, 460), (660, 700), (700, 1024), (1024, 1024), (1024, 520), (860, 420)], fill=(190, 168, 112))
    # the North Wood, top
    d.polygon([(190, 0), (230, 180), (560, 260), (620, 460), (860, 420), (760, 220), (700, 0)], fill=(76, 104, 62))
    # the Greywall, upper right
    d.polygon([(700, 0), (760, 220), (860, 420), (1024, 520), (1024, 0)], fill=(134, 126, 118))
    # the River Ald, a pale thread from the hills to the sea marsh
    river = [(760, 300), (690, 380), (600, 480), (520, 560), (470, 640), (420, 720), (360, 800), (300, 860), (240, 900)]
    d.line(river, fill=(110, 132, 150), width=10, joint="curve")
    # Black Mere
    d.ellipse([560, 300, 640, 360], fill=(96, 112, 126))
    im = im.filter(ImageFilter.GaussianBlur(6))
    grain = noise(SIZE, 18, 1.5).convert("RGB")
    im = Image.blend(im, grain, 0.08)
    # snow on the range
    d = ImageDraw.Draw(im)
    rng = random.Random(7)
    for _ in range(140):
        x, y = rng.randint(760, 1020), rng.randint(10, 360)
        if (x - 700) * 1.6 > (y - 0) * 0.3 + 60:
            d.polygon([(x, y), (x - 9, y + 16), (x + 9, y + 16)], fill=(230, 230, 226))
    return im.filter(ImageFilter.GaussianBlur(1.2))


def under():
    """Dark rock with a pale gallery."""
    im = Image.new("RGB", SIZE, (54, 46, 40))
    rock = noise(SIZE, 40, 6).convert("RGB")
    im = Image.blend(im, rock, 0.25)
    d = ImageDraw.Draw(im)
    d.line([(300, 860), (420, 760), (520, 660), (640, 560)], fill=(150, 140, 120), width=14, joint="curve")
    return im.filter(ImageFilter.GaussianBlur(2))


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    surface().save(os.path.join(OUT, "surface.png"))
    under().save(os.path.join(OUT, "under-1.png"))
    clouds().save(os.path.join(OUT, "clouds.png"))
    print("wrote", OUT)
