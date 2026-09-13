#!/usr/bin/env python3
"""
Generate a single-scene manga-style illustration of a small Japanese clothing
shop in trouble, as a self-contained SVG (hand-inked look, screentone shading,
warm off-white paper). No text, no lettering, no speech bubbles anywhere.

Usage:  python3 assets/make_manga_shop_scene.py [out.svg]
"""
import math
import random
import sys

W, H = 1800, 1050
INK = "#15130f"
PAPER = "#f7f2e6"
GHOST = "#15130f"

rnd = random.Random(20260913)
P = []


def add(s):
    P.append(s)


# --------------------------------------------------------------------------
# drawing helpers
# --------------------------------------------------------------------------
def path(d, fill="none", stroke=INK, w=3.0, op=1.0, extra=""):
    return (f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{w}" '
            f'stroke-linecap="round" stroke-linejoin="round" opacity="{op}" {extra}/>')


def line(x1, y1, x2, y2, w=3.0, stroke=INK, op=1.0, extra=""):
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{stroke}" stroke-width="{w}" stroke-linecap="round" '
            f'opacity="{op}" {extra}/>')


def circle(cx, cy, r, fill="none", stroke=INK, w=3.0, op=1.0):
    return (f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{w}" opacity="{op}"/>')


def tube(d, w, fill=PAPER, ink=3.2):
    """A limb: paper-filled stroke with an ink outline."""
    return (path(d, stroke=INK, w=w + ink * 2) +
            path(d, stroke=fill, w=w))


def taper_ray(cx, cy, ang, r0, r1, half, op=1.0, fill=INK):
    """Tapered speed/focus line: wide at r0, pointed at r1."""
    nx, ny = -math.sin(ang), math.cos(ang)
    ax, ay = cx + r0 * math.cos(ang), cy + r0 * math.sin(ang)
    bx, by = cx + r1 * math.cos(ang), cy + r1 * math.sin(ang)
    pts = (f"{ax + nx * half:.1f},{ay + ny * half:.1f} "
           f"{bx:.1f},{by:.1f} "
           f"{ax - nx * half:.1f},{ay - ny * half:.1f}")
    return f'<polygon points="{pts}" fill="{fill}" opacity="{op}"/>'


def gloom(x0, x1, ytop, hmin, hmax, n, op=0.62, seed_shift=0.0):
    """Vertical 'gloom' lines that fall over a character."""
    out = []
    for i in range(n):
        t = i / max(1, n - 1)
        x = x0 + (x1 - x0) * t + rnd.uniform(-2.5, 2.5)
        h = hmin + (hmax - hmin) * abs(math.sin(t * 5.1 + seed_shift)) + rnd.uniform(-8, 10)
        wtop = rnd.uniform(2.4, 4.2)
        pts = (f"{x - wtop / 2:.1f},{ytop:.1f} {x + wtop / 2:.1f},{ytop:.1f} "
               f"{x + 0.35:.1f},{ytop + h:.1f} {x - 0.35:.1f},{ytop + h:.1f}")
        out.append(f'<polygon points="{pts}" fill="{INK}" opacity="{op:.2f}"/>')
    return "".join(out)


def zigzag(x, y0, y1, amp, step):
    pts = []
    y = y0
    k = 0
    while y < y1:
        pts.append((x + (amp if k % 2 == 0 else -amp), y))
        y += step
        k += 1
    d = "M " + " L ".join(f"{px:.1f} {py:.1f}" for px, py in pts)
    return d


def light_arrow(x, y, size=1.0, op=0.95, rot=0.0):
    """A small rising arrow of light (white body, ink outline)."""
    s = size
    d = (f"M {x:.1f} {y:.1f} l {-9*s:.1f} {16*s:.1f} l {4.5*s:.1f} 0 "
         f"l 0 {16*s:.1f} l {9*s:.1f} 0 l 0 {-16*s:.1f} l {4.5*s:.1f} 0 z")
    g = f'<g transform="rotate({rot} {x} {y})" opacity="{op}">'
    g += path(d, fill="#ffffff", stroke=INK, w=2.4)
    g += "</g>"
    return g


# --------------------------------------------------------------------------
# defs: screentone patterns, paper texture, hand-drawn ink wobble
# --------------------------------------------------------------------------
DEFS = f'''
<defs>
  <pattern id="tone" width="9" height="9" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
    <circle cx="2.6" cy="2.6" r="1.7" fill="{INK}" opacity="0.42"/>
  </pattern>
  <pattern id="toneFine" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
    <circle cx="2" cy="2" r="1.1" fill="{INK}" opacity="0.34"/>
  </pattern>
  <pattern id="toneDark" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
    <circle cx="2.4" cy="2.4" r="2.5" fill="{INK}" opacity="0.55"/>
  </pattern>
  <pattern id="hatch" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(30)">
    <line x1="0" y1="0" x2="0" y2="10" stroke="{INK}" stroke-width="1.5" opacity="0.35"/>
  </pattern>
  <radialGradient id="screenGlow" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#ffffff" stop-opacity="1"/>
    <stop offset="62%" stop-color="#ffffff" stop-opacity="0.75"/>
    <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="doorLight" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#ffffff" stop-opacity="0.95"/>
    <stop offset="100%" stop-color="#ffffff" stop-opacity="0.55"/>
  </linearGradient>
  <radialGradient id="vignette" cx="58%" cy="34%" r="78%">
    <stop offset="55%" stop-color="#15130f" stop-opacity="0"/>
    <stop offset="100%" stop-color="#15130f" stop-opacity="0.16"/>
  </radialGradient>
  <filter id="paperTex" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.75" numOctaves="4" seed="11" result="n"/>
    <feColorMatrix in="n" type="saturate" values="0"/>
  </filter>
  <filter id="inkWobble" filterUnits="userSpaceOnUse" x="-20" y="-20" width="1840" height="1090">
    <feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="2" seed="5" result="t"/>
    <feDisplacementMap in="SourceGraphic" in2="t" scale="2.6" xChannelSelector="R" yChannelSelector="G"/>
  </filter>
</defs>
'''


def contour(d, fill=PAPER, w=4.6):
    """Filled shape with a heavy outer ink contour (manga silhouette weight)."""
    return path(d, fill=fill, stroke=INK, w=w)


def hand(cx, cy, r=15, fill=PAPER, ang=0.0):
    """A small closed hand: palm mass, knuckle creases, thumb."""
    g = [f'<g transform="rotate({ang} {cx} {cy})">']
    g.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{r*0.86:.1f}" ry="{r:.1f}" '
             f'fill="{fill}" stroke="{INK}" stroke-width="3.2"/>')
    for i in range(3):
        fx = cx - r * 0.42 + i * r * 0.42
        g.append(path(f"M {fx:.1f} {cy+r*0.18:.1f} q {r*0.18:.1f} {r*0.42:.1f} "
                      f"{-r*0.04:.1f} {r*0.62:.1f}", w=2.0, op=0.55))
    g.append(path(f"M {cx-r*0.8:.1f} {cy-r*0.1:.1f} q {-r*0.5:.1f} {r*0.35:.1f} "
                  f"{-r*0.05:.1f} {r*0.72:.1f}", fill=fill, w=2.8))
    g.append('</g>')
    return "".join(g)


# --------------------------------------------------------------------------
# background: paper, wall, floor
# --------------------------------------------------------------------------
add(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
add(f'<rect width="{W}" height="{H}" filter="url(#paperTex)" opacity="0.10"/>')

add('<g id="artwork" filter="url(#inkWobble)">')

add(line(0, 848, W, 848, w=3.6, op=0.9))
add(line(0, 855, 1040, 855, w=1.6, op=0.4))
for fx in (300, 700, 1120):
    add(line(900, 848, fx, 1050, w=1.3, op=0.13))
add(f'<rect x="0" y="848" width="{W}" height="{H-848}" fill="url(#toneFine)" opacity="0.28"/>')

# --------------------------------------------------------------------------
# the shop itself: a rail of hanging clothes along the back wall
# --------------------------------------------------------------------------
add('<g id="clothes-rail" opacity="0.92">')
add(line(270, 846, 270, 478, w=5.0))
add(line(214, 846, 326, 846, w=5.0))
add(line(270, 820, 222, 846, w=3.0))
add(line(270, 820, 318, 846, w=3.0))
add(line(158, 474, 382, 474, w=5.4))
for i, hx in enumerate((186, 226, 268, 310, 352)):
    add(path(f"M {hx} 474 q 6 -12 -4 -14", w=2.4))
    add(line(hx - 14, 496, hx + 14, 496, w=2.4))
    add(line(hx, 478, hx, 494, w=2.2))
    if i == 2:
        body = (f"M {hx-30} 512 L {hx-16} 496 L {hx} 503 L {hx+16} 496 L {hx+30} 512 "
                f"L {hx+21} 527 L {hx+24} 664 L {hx-24} 664 L {hx-21} 527 Z")
    else:
        body = (f"M {hx-28} 510 L {hx-15} 496 L {hx} 502 L {hx+15} 496 L {hx+28} 510 "
                f"L {hx+20} 524 L {hx+22} 612 L {hx-22} 612 L {hx-20} 524 Z")
    add(contour(body, w=3.2))
    add(f'<path d="{body}" fill="url(#toneFine)" opacity="0.34"/>')
    add(path(f"M {hx-9} 502 q 9 8 18 -1", w=2.2, op=0.6))
add('</g>')

# --------------------------------------------------------------------------
# TOP LEFT: ghost of the deceased previous owner, an older woman in kimono
# --------------------------------------------------------------------------
GD = 'stroke-dasharray="11 9"'
add('<g id="ghost-owner" opacity="0.40">')
add(path("M 126 132 C 122 96 140 78 164 80 C 190 82 204 102 200 136 "
         "C 198 158 188 176 172 182 C 162 186 152 185 144 179 C 132 170 127 152 126 132 Z",
         fill="#ffffff", w=2.6, extra=GD))
add(path("M 122 122 C 118 80 142 62 166 64 C 192 66 208 88 202 126 "
         "C 196 104 186 92 164 90 C 142 88 130 100 122 122 Z", w=2.4, extra=GD))
add(path("M 178 74 c 20 -10 36 4 28 18 c -5 9 -20 10 -30 3", w=2.4, extra=GD))
add(path("M 140 132 q 9 8 18 0", w=2.2, extra=GD))
add(path("M 170 130 q 9 8 17 -1", w=2.2, extra=GD))
add(path("M 156 162 q 9 4 17 -1", w=2.0, extra=GD))
add(path("M 164 186 L 130 202 L 102 228 L 90 304 L 116 310 L 126 254 L 118 336 "
         "L 216 338 L 208 252 L 216 310 L 242 304 L 228 226 L 198 200 Z",
         fill="#ffffff", w=2.6, extra=GD))
add(path("M 164 190 L 150 240 L 180 240 L 164 190", w=2.0, extra=GD))
add(line(124, 260, 212, 258, w=2.6, extra=GD))
add(line(124, 278, 212, 276, w=2.0, extra=GD))
add('</g>')

# --------------------------------------------------------------------------
# LEFT-CENTER: young man, proud, pointing right at the monitor
# --------------------------------------------------------------------------
add('<g id="speed-lines">')
for i in range(50):
    a = rnd.uniform(0, 2 * math.pi)
    ca, sa = math.cos(a), math.sin(a)
    if ca > 0.45 and -0.75 < sa < 0.25:
        continue                       # keep the pointing direction clear
    r0 = rnd.uniform(128, 182)
    r1 = r0 + rnd.uniform(46, 120)
    if ca < -0.4 and sa < -0.3:
        r1 = r0 + rnd.uniform(30, 62)  # stay clear of the ghost, top left
    add(taper_ray(446, 486, a, r0, r1, rnd.uniform(2.2, 5.0), op=rnd.uniform(0.4, 0.85)))
add('</g>')

add('<g id="young-man">')
# legs
add(tube("M 418 636 L 410 756 L 416 862", 31))
add(tube("M 480 636 L 490 758 L 480 862", 31))
add(path("M 396 862 q 22 -10 42 0 q 4 16 -10 19 q -26 2 -34 -5 z", fill=INK, w=2.8))
add(path("M 456 862 q 22 -10 42 0 q 4 16 -10 19 q -26 2 -34 -5 z", fill=INK, w=2.8))
# torso: casual shirt
add(contour("M 372 462 C 356 490 352 552 358 596 L 366 662 L 528 662 L 534 596 "
            "C 540 552 536 490 520 462 C 490 440 402 440 372 462 Z"))
add(path("M 422 444 L 448 500 L 476 442", w=3.4))
add(path("M 448 500 L 446 662", w=2.2, op=0.5))
add(circle(452, 542, 4, fill=INK, w=0, op=0.6))
add(circle(450, 592, 4, fill=INK, w=0, op=0.6))
add(path("M 372 520 q 28 14 20 44", w=2.2, op=0.42))
add(path("M 524 520 q -26 16 -18 44", w=2.2, op=0.42))
add(path("M 366 662 q 82 16 162 0", w=3.0))
add(f'<path d="M 372 462 C 356 490 352 552 358 596 L 366 662 L 420 662 L 412 560 '
    f'C 408 508 412 478 424 452 C 404 448 384 452 372 462 Z" fill="url(#toneFine)" opacity="0.34"/>')
# arms (drawn over the torso so the joints read)
add(tube("M 374 480 L 352 578 L 376 640", 22))          # relaxed arm
add(tube("M 520 478 L 580 396 L 624 304", 23))          # raised, pointing arm
add(path("M 380 500 q 22 10 30 -2", w=2.6, op=0.6))     # short sleeve edges
add(path("M 516 506 q 26 -10 34 -26", w=2.6, op=0.6))
add(hand(378, 646, r=15, ang=8))
# pointing hand: fist with the index finger extended toward the monitor
add(tube("M 634 294 L 686 278", 13))
add(path("M 620 284 c -16 3 -23 19 -14 31 c 9 12 29 14 41 4 c 10 -8 9 -26 -2 -33 "
         "c -7 -4 -17 -4 -25 -2 z", fill=PAPER, w=3.4))
add(path("M 624 292 q 12 7 9 21", w=2.2, op=0.6))
add(path("M 638 290 q 12 7 9 21", w=2.2, op=0.6))
add(line(690, 270, 714, 264, w=3.0, op=0.55))           # a flick of motion off the fingertip
add(line(690, 286, 712, 286, w=3.0, op=0.4))
# neck + head
add(tube("M 444 402 L 444 452", 17))
add(contour("M 404 352 C 402 312 420 294 445 294 C 472 294 488 314 487 354 "
            "C 486 384 474 410 455 418 C 445 422 436 422 428 415 C 412 402 405 378 404 352 Z"))
add(path("M 404 362 c -10 -3 -16 7 -10 16 c 5 8 12 9 16 6", w=3.0))
# spiky black hair
add(path("M 396 354 C 386 300 412 272 445 272 C 480 272 500 302 490 356 "
         "L 481 326 L 471 348 L 461 318 L 450 342 L 440 312 L 429 338 L 419 314 "
         "L 409 340 L 401 320 Z", fill=INK, w=2.8))
add(path("M 428 278 l 12 -26 l 10 24", fill=INK, w=2.6))
add(path("M 458 282 l 18 -22 l 4 24", fill=INK, w=2.6))
add(path("M 400 300 l -16 -16 l 18 2", fill=INK, w=2.6))
# face: grinning eyes, raised brows, wide open grin
add(path("M 417 352 q 11 -14 21 -1", w=4.0))
add(path("M 452 350 q 11 -14 21 -1", w=4.0))
add(path("M 415 328 q 11 -8 22 -3", w=3.0))
add(path("M 451 325 q 11 -4 20 4", w=3.0))
add(path("M 445 364 q 6 9 -3 12", w=2.4, op=0.7))
add(path("M 421 382 q 22 8 40 -7 q -1 28 -19 29 q -19 1 -21 -22 z", fill=INK, w=2.8))
add(path("M 424 386 q 19 6 34 -6", stroke="#ffffff", w=3.4))
add(line(474, 370, 486, 366, w=2.4, op=0.7))
add(line(473, 379, 485, 376, w=2.4, op=0.7))
add(line(472, 388, 482, 386, w=2.4, op=0.55))
add('</g>')

# --------------------------------------------------------------------------
# BETWEEN THEM: jagged vertical tension line
# --------------------------------------------------------------------------
add('<g id="tension">')
add(path(zigzag(600, 430, 806, 18, 34), w=5.2, op=0.95))
add(path(zigzag(600, 444, 798, 9, 34), w=1.6, op=0.38))
add('</g>')

# --------------------------------------------------------------------------
# BESIDE HIM: the older woman, shop apron, looking away toward the entrance
# --------------------------------------------------------------------------
add('<g id="shopkeeper" transform="translate(40,0)">')
# skirt + shoes
add(contour("M 690 646 L 660 862 L 806 862 L 782 646 Z"))
add(path("M 714 664 L 700 858", w=1.9, op=0.38))
add(path("M 752 664 L 762 858", w=1.9, op=0.38))
add(path("M 664 862 q 24 -8 44 0 q 2 16 -12 18 q -28 2 -34 -6 z", fill=INK, w=2.8))
add(path("M 756 862 q 24 -8 44 0 q 2 16 -12 18 q -28 2 -34 -6 z", fill=INK, w=2.8))
add(f'<path d="M 690 646 L 660 862 L 726 862 L 730 646 Z" fill="url(#toneFine)" opacity="0.38"/>')
# torso / blouse
add(contour("M 688 492 C 674 518 672 566 676 606 L 682 668 L 812 668 L 816 606 "
            "C 820 566 816 518 802 492 C 774 474 714 474 688 492 Z"))
# apron over it
add(contour("M 720 500 L 714 530 L 692 574 L 688 676 L 806 676 L 802 574 L 780 530 L 774 500 "
            "C 758 510 736 510 720 500 Z", w=3.4))
add(path("M 722 500 L 732 470", w=2.8))
add(path("M 774 500 L 764 470", w=2.8))
add(line(688, 642, 806, 642, w=2.8))
add(path("M 688 642 q -24 8 -32 26", w=2.6))
add(path("M 806 642 q 24 8 32 26", w=2.6))
add(path("M 718 574 L 718 640", w=1.9, op=0.38))
add(path("M 776 574 L 776 640", w=1.9, op=0.38))
add(f'<path d="M 720 500 L 714 530 L 692 574 L 688 676 L 806 676 L 802 574 L 780 530 L 774 500 '
    f'C 758 510 736 510 720 500 Z" fill="url(#toneFine)" opacity="0.5"/>')
# arms: one half-raised as if about to speak, then stopped
add(tube("M 694 516 L 660 578 L 704 552", 20))
add(tube("M 806 514 L 824 604 L 806 668", 20))
add(hand(712, 542, r=16, ang=-20))
add(hand(808, 676, r=15, ang=6))
add(path("M 694 540 q 22 8 28 -4", w=2.4, op=0.5))
# neck + head, tilted down toward the entrance in the lower right
add(tube("M 744 440 L 748 484", 15))
add(contour("M 710 388 C 708 350 726 330 748 330 C 772 330 786 352 784 390 "
            "C 782 420 770 442 753 448 C 744 451 735 450 728 444 C 715 432 711 410 710 388 Z"))
add(path("M 710 394 c -10 -2 -15 8 -9 16 c 5 7 11 8 15 5", w=3.0))
# hair: pulled back, low bun
add(path("M 704 394 C 698 346 722 320 748 320 C 776 320 794 346 790 394 "
         "C 782 366 770 352 748 350 C 724 348 712 368 704 394 Z", fill=INK, w=2.8))
add(path("M 706 380 C 692 402 688 428 698 444 C 708 460 724 452 724 436", fill=INK, w=2.8))
add(circle(694, 438, 21, fill=INK, w=3.0))
add(path("M 680 430 q 15 -11 30 -2", stroke=PAPER, w=2.2, op=0.5))
add(path("M 786 382 q 8 20 0 38", fill=INK, w=2.8))
# downcast eyes turned toward the lower right, tired mouth
add(path("M 722 386 q 11 10 22 1", w=3.4))
add(path("M 754 384 q 11 9 21 -1", w=3.4))
add(line(731, 393, 738, 397, w=2.6, op=0.85))
add(line(763, 391, 770, 395, w=2.6, op=0.85))
add(path("M 720 370 q 12 -6 22 -1", w=2.6, op=0.85))
add(path("M 753 367 q 11 -3 20 4", w=2.6, op=0.85))
add(path("M 748 400 q 6 9 -3 12", w=2.2, op=0.7))
add(path("M 734 424 q 16 -5 27 1", w=3.0))
add(line(717, 400, 723, 407, w=1.7, op=0.5))
add(line(775, 398, 781, 405, w=1.7, op=0.5))
add(path("M 730 412 q 5 9 2 14", w=1.7, op=0.45))
add(path("M 766 410 q -4 9 -1 14", w=1.7, op=0.45))
# a single sweat drop at her temple
add(path("M 794 358 c 9 12 11 21 4 27 c -8 6 -17 -1 -15 -10 c 1 -7 6 -11 11 -17 z",
         fill="#ffffff", w=2.8))
add(path("M 790 376 q 3 -5 5 -10", stroke="#ffffff", w=2.2))
# vertical gloom lines falling over her head
add(f'<g>{gloom(708, 792, 292, 78, 172, 17, op=0.34)}</g>')
add(f'<ellipse cx="748" cy="366" rx="50" ry="40" fill="url(#tone)" opacity="0.38"/>')
add('</g>')

# --------------------------------------------------------------------------
# a counter beside her, with a teacup on it
# --------------------------------------------------------------------------
add('<g id="counter" transform="translate(44,0)">')
add(contour("M 868 656 L 1030 644 L 1044 670 L 882 684 Z"))
add(contour("M 882 684 L 886 850 L 1036 842 L 1044 670 Z"))
add(line(886, 716, 1042, 706, w=2.2, op=0.45))
add(f'<path d="M 882 684 L 886 850 L 1036 842 L 1044 670 Z" fill="url(#toneFine)" opacity="0.45"/>')
add(path("M 906 650 q 28 10 54 -2", w=2.6))
add(path("M 912 618 L 916 644 q 15 8 30 -1 L 950 616 Z", fill=PAPER, w=3.0))
add(path("M 912 618 q 19 8 38 -2", w=2.6))
add(path("M 950 622 c 13 -2 15 13 2 16", w=2.6))
add(contour("M 986 646 L 1044 640 L 1044 620 L 986 626 Z", w=3.0))
add(contour("M 990 624 L 1046 618 L 1046 600 L 990 606 Z", w=3.0))
add(line(992, 616, 1042, 611, w=1.8, op=0.45))
add(f'<path d="M 986 646 L 1044 640 L 1044 620 L 986 626 Z" fill="url(#toneFine)" opacity="0.4"/>')
add('</g>')

# --------------------------------------------------------------------------
# RIGHT: the glowing wall monitor, rising line graph, sharp focus lines
# --------------------------------------------------------------------------
MX1, MY1, MX2, MY2 = 1080, 92, 1540, 420
MCX, MCY = (MX1 + MX2) / 2, (MY1 + MY2) / 2

add('<g id="monitor-focus">')
ha, hb = (MX2 - MX1) / 2 + 18, (MY2 - MY1) / 2 + 18
for i in range(88):
    a = (i / 88) * 2 * math.pi + rnd.uniform(-0.014, 0.014)
    ca, sa = math.cos(a), math.sin(a)
    r0 = min(ha / max(abs(ca), 1e-6), hb / max(abs(sa), 1e-6)) + rnd.uniform(4, 12)
    ln = rnd.uniform(48, 150)
    if ca < -0.5:
        ln *= 0.42
    add(taper_ray(MCX, MCY, a, r0, r0 + ln, rnd.uniform(2.2, 5.0), op=rnd.uniform(0.45, 0.95)))
add('</g>')

add('<g id="monitor">')
add(f'<ellipse cx="{MCX}" cy="{MCY}" rx="330" ry="250" fill="url(#screenGlow)" opacity="0.9"/>')
add(f'<rect x="{MX1}" y="{MY1}" width="{MX2-MX1}" height="{MY2-MY1}" rx="12" '
    f'fill="{PAPER}" stroke="{INK}" stroke-width="7"/>')
add(f'<rect x="{MX1+16}" y="{MY1+16}" width="{MX2-MX1-32}" height="{MY2-MY1-32}" rx="5" '
    f'fill="#ffffff" stroke="{INK}" stroke-width="3.4"/>')
add(path(f"M {MCX-28:.0f} {MY2} l 9 36 l 38 0 l 9 -36", w=3.4, fill=PAPER))
add(line(MCX - 58, MY2 + 36, MCX + 58, MY2 + 36, w=4.6))
for gy in range(MY1 + 56, MY2 - 24, 52):
    add(line(MX1 + 34, gy, MX2 - 34, gy, w=1.4, op=0.2))
add(line(MX1 + 46, MY1 + 44, MX1 + 46, MY2 - 44, w=3.2))
add(line(MX1 + 46, MY2 - 44, MX2 - 40, MY2 - 44, w=3.2))
pts = [(1136, 350), (1186, 332), (1236, 340), (1286, 296), (1336, 306),
       (1386, 250), (1436, 260), (1478, 176), (1500, 146)]
for x, y in pts[:-1]:
    add(f'<rect x="{x-11}" y="{y}" width="22" height="{376-y}" fill="url(#toneFine)" opacity="0.4"/>')
add(path("M " + " L ".join(f"{x} {y}" for x, y in pts), w=6.2))
add(path("M 1500 146 l -28 7 l 7 -27 z", fill=INK, w=2.6))
for x, y in pts[:-1]:
    add(circle(x, y, 4.6, fill=INK, w=0))
add('</g>')

# --------------------------------------------------------------------------
# the measured devices, stacked in a column below the monitor
# --------------------------------------------------------------------------
add('<g id="devices">')
# 1. self-checkout kiosk
add(contour("M 1214 664 L 1372 664 L 1356 604 L 1230 604 Z", w=3.6))
add(contour("M 1256 604 L 1330 604 L 1330 540 L 1256 540 Z", w=3.6))
add(contour("M 1240 540 L 1348 540 L 1360 476 L 1250 476 Z", w=3.8))
add(path("M 1252 532 L 1342 532 L 1352 486 L 1258 486 Z", fill="#ffffff", w=2.8))
add(line(1268, 500, 1332, 498, w=2.4, op=0.45))
add(line(1268, 513, 1314, 512, w=2.4, op=0.45))
add(circle(1345, 566, 10, fill="#ffffff", w=3.0))
add(circle(1345, 566, 4, fill=INK, w=0))
add(path("M 1240 630 L 1278 630 L 1278 650 L 1240 650 Z", fill=PAPER, w=2.6))
add(f'<path d="M 1214 664 L 1372 664 L 1356 604 L 1230 604 Z" fill="url(#toneFine)" opacity="0.45"/>')
# 2. fitting-room recording tablet on a stand
add(f'<rect x="1240" y="692" width="104" height="98" rx="8" fill="{PAPER}" stroke="{INK}" stroke-width="3.8"/>')
add(f'<rect x="1250" y="704" width="84" height="76" fill="#ffffff" stroke="{INK}" stroke-width="2.6"/>')
add(circle(1292, 700, 13, fill="none", w=2.2, op=0.55))
add(circle(1292, 700, 6, fill=INK, w=0))
add(path("M 1262 722 q 30 -10 58 2", w=2.2, op=0.4))
add(path("M 1264 748 q 28 8 54 -4", w=2.2, op=0.4))
add(line(1292, 790, 1292, 842, w=5.2))
add(line(1292, 842, 1248, 864, w=4.6))
add(line(1292, 842, 1336, 864, w=4.6))
add(line(1292, 842, 1292, 868, w=4.6))
add(f'<rect x="1240" y="692" width="104" height="98" rx="8" fill="url(#toneFine)" opacity="0.34"/>')
# 3. shelf sensor
add(line(1200, 920, 1388, 920, w=5.4))
add(path("M 1210 920 L 1218 948", w=3.2))
add(path("M 1378 920 L 1370 948", w=3.2))
add(contour("M 1236 920 L 1236 884 L 1272 884 L 1272 920 Z", w=3.0))
add(contour("M 1282 920 L 1282 892 L 1312 892 L 1312 920 Z", w=3.0))
add(contour("M 1326 920 L 1326 878 L 1374 878 L 1374 920 Z", w=3.4))
add(circle(1350, 896, 7, fill=INK, w=0))
for k, r in enumerate((17, 27, 37)):
    add(path(f"M {1350-r} {896-int(r*0.6)} q {int(r*0.5)} {-int(r*0.6)} {r} 0", w=2.5, op=0.75 - k * 0.17))
add('</g>')

# small arrows of light rising from each device into the monitor
add('<g id="light-arrows">')
for (ax, ay, sz, rot) in ((1160, 624, 1.0, -12), (1160, 558, 0.85, -12), (1160, 494, 0.72, -12),
                          (1428, 640, 1.0, 12), (1428, 574, 0.85, 12), (1428, 510, 0.72, 12),
                          (1176, 766, 0.92, -10), (1412, 752, 0.92, 10),
                          (1186, 886, 0.85, -8), (1404, 880, 0.85, 8),
                          (1224, 448, 0.8, -6), (1360, 448, 0.8, 6)):
    add(light_arrow(ax, ay, sz, op=0.95, rot=rot))
add('</g>')

# --------------------------------------------------------------------------
# LOWER RIGHT: the doorway, a young woman walking out, defeated
# --------------------------------------------------------------------------
add('<g id="doorway">')
add(f'<rect x="1556" y="404" width="228" height="606" fill="url(#doorLight)" '
    f'stroke="{INK}" stroke-width="7"/>')
add(f'<rect x="1576" y="424" width="188" height="566" fill="none" stroke="{INK}" stroke-width="3"/>')
add(line(1556, 404, 1784, 404, w=8))
add(line(1560, 988, 1782, 988, w=4.2))
add(line(1550, 1012, 1792, 1012, w=5.2))
add('</g>')

add('<g id="leaving-customer">')
# legs, mid-step
add(tube("M 1636 812 L 1626 900 L 1632 958", 20))
add(tube("M 1682 812 L 1696 896 L 1684 956", 20))
add(path("M 1610 958 q 22 -8 40 0 q 2 14 -12 16 q -26 2 -30 -5 z", fill=INK, w=2.8))
add(path("M 1662 956 q 22 -8 40 0 q 2 14 -12 16 q -26 2 -30 -5 z", fill=INK, w=2.8))
# coat / dress, shoulders pulled in
add(contour("M 1610 660 C 1596 690 1592 740 1598 782 L 1606 834 L 1712 834 L 1720 782 "
            "C 1726 740 1722 690 1708 660 C 1682 642 1636 642 1610 660 Z"))
add(f'<path d="M 1610 660 C 1596 690 1592 740 1598 782 L 1606 834 L 1712 834 L 1720 782 '
    f'C 1726 740 1722 690 1708 660 C 1682 642 1636 642 1610 660 Z" fill="url(#tone)" opacity="0.4"/>')
add(path("M 1606 668 q 24 -30 53 -30 q 29 0 53 30", w=3.2, op=0.75))
add(path("M 1659 690 L 1659 830", w=2.0, op=0.4))
# arms over the coat
add(tube("M 1612 674 L 1598 756 L 1612 806", 17))
add(tube("M 1706 674 L 1722 756 L 1712 802", 17))
add(hand(1610, 812, r=13, ang=-6))
add(hand(1714, 806, r=13, ang=6))
# shopping bag, hanging
add(path("M 1714 812 L 1714 828", w=2.6))
add(path("M 1696 828 L 1752 828 L 1746 908 L 1704 908 Z", fill=PAPER, w=3.6))
add(path("M 1710 828 q 14 -24 28 0", w=2.8))
add(f'<path d="M 1696 828 L 1752 828 L 1746 908 L 1704 908 Z" fill="url(#toneFine)" opacity="0.5"/>')
# head, bowed; long hair hides the eyes
add(tube("M 1658 626 L 1658 656", 15))
add(contour("M 1622 594 C 1620 560 1637 540 1659 540 C 1683 540 1698 562 1696 596 "
            "C 1694 624 1682 644 1666 650 C 1657 653 1649 652 1642 646 C 1628 634 1623 614 1622 594 Z"))
add(path("M 1614 604 C 1606 550 1630 522 1659 522 C 1690 522 1708 550 1702 606 "
         "C 1698 574 1690 554 1659 552 C 1628 550 1618 574 1614 604 Z", fill=INK, w=2.8))
add(path("M 1616 578 C 1596 614 1594 684 1602 728 L 1630 722 C 1620 674 1620 618 1630 590 Z",
         fill=INK, w=2.8))
add(path("M 1700 578 C 1720 614 1722 684 1714 728 L 1686 722 C 1696 674 1696 618 1686 590 Z",
         fill=INK, w=2.8))
add(path("M 1620 592 q 40 20 78 0 q -5 26 -39 26 q -34 0 -39 -26 z", fill=INK, w=2.4))
add(path("M 1648 632 q 14 -5 25 1", w=2.8))
add(path("M 1659 612 q 5 8 -3 10", w=2.2, op=0.6))
add(f'<g>{gloom(1614, 1706, 492, 66, 172, 15, op=0.34, seed_shift=1.4)}</g>')
add('</g>')

# --------------------------------------------------------------------------
# LOWER LEFT CORNER: an elderly man reading, saying nothing
# --------------------------------------------------------------------------
add('<g id="elder-reader">')
add(tube("M 112 876 L 104 928 L 112 962", 21))
add(tube("M 172 876 L 182 928 L 172 962", 21))
add(path("M 88 962 q 20 -8 38 0 q 2 14 -10 16 q -24 2 -30 -5 z", fill=INK, w=2.8))
add(path("M 150 962 q 20 -8 38 0 q 2 14 -10 16 q -24 2 -30 -5 z", fill=INK, w=2.8))
add(contour("M 84 800 C 72 828 68 872 74 898 L 80 896 L 202 896 L 208 898 "
            "C 214 872 210 828 198 800 C 172 782 110 782 84 800 Z"))
add(tube("M 86 816 L 62 868 L 92 892", 17))
add(tube("M 196 816 L 220 868 L 190 892", 17))
# open book
add(contour("M 54 838 L 140 826 L 140 884 L 54 898 Z", w=3.4))
add(contour("M 226 838 L 140 826 L 140 884 L 226 898 Z", w=3.4))
add(line(140, 826, 140, 884, w=2.8))
add(hand(64, 872, r=12, ang=-16))
add(hand(216, 872, r=12, ang=16))
for oy in (846, 858, 870):
    add(line(70, oy + 4, 128, oy - 4, w=1.7, op=0.38))
    add(line(152, oy - 4, 210, oy + 4, w=1.7, op=0.38))
# head: round glasses, small mustache, eyes closed
add(tube("M 140 754 L 140 800", 15))
add(contour("M 104 700 C 102 664 118 646 141 646 C 166 646 180 666 178 704 "
            "C 176 732 164 752 148 758 C 139 761 131 760 124 754 C 110 742 105 722 104 700 Z"))
add(path("M 104 684 C 100 652 118 634 141 634 C 166 634 182 654 179 688 "
         "C 169 672 158 664 141 664 C 122 664 111 672 104 684 Z", fill=INK, w=2.6, op=0.8))
add(path("M 103 700 c -10 -2 -15 7 -9 15 c 4 6 11 7 15 5", w=2.8))
add(circle(122, 706, 16, fill="none", w=3.2))
add(circle(160, 704, 16, fill="none", w=3.2))
add(line(138, 705, 144, 704, w=2.8))
add(line(106, 702, 98, 699, w=2.6))
add(line(176, 701, 184, 698, w=2.6))
add(path("M 114 707 q 8 5 16 0", w=2.8))
add(path("M 152 705 q 8 5 16 0", w=2.8))
add(path("M 130 730 q 12 -9 24 -1 q -12 7 -24 1 z", fill=INK, w=2.2))
add(path("M 132 746 q 10 4 20 -1", w=2.6))
add(f'<ellipse cx="140" cy="820" rx="140" ry="240" fill="url(#toneFine)" opacity="0.30"/>')
add('</g>')

# --------------------------------------------------------------------------
# the chair that is no longer there, drawn as a ghost outline
# --------------------------------------------------------------------------
add('<g id="ghost-chair" opacity="0.36">')
add(path("M 258 878 L 352 864 L 392 888 L 298 904 Z", fill="none", w=2.8, extra=GD))
add(path("M 352 864 L 338 772", fill="none", w=2.8, extra=GD))
add(path("M 392 888 L 378 796", fill="none", w=2.8, extra=GD))
add(line(338, 776, 380, 800, w=2.6, extra=GD))
add(line(342, 812, 384, 836, w=2.6, extra=GD))
add(line(258, 878, 262, 936, w=2.8, extra=GD))
add(line(298, 904, 302, 964, w=2.8, extra=GD))
add(line(392, 890, 396, 948, w=2.8, extra=GD))
add(line(352, 866, 356, 890, w=2.2, extra=GD))
add('</g>')

# a broken, snapped line running from the ghost chair toward a customer entering
add('<g id="snapped-line">')
add(path("M 400 900 L 432 910 L 462 920 l 11 12 l -6 -14 l 13 5", w=4.8, op=0.88))
add(path("M 560 954 l -13 -4 l 7 14 l -10 -12 L 518 938", w=4.8, op=0.88))
add(line(492, 930, 504, 918, w=2.8, op=0.7))
add(line(500, 942, 514, 938, w=2.8, op=0.7))
add(line(486, 944, 494, 954, w=2.4, op=0.55))
add('</g>')

# a faint silhouette of a customer coming in through the entrance
add('<g id="entering-customer">')
add(f'<g opacity="0.13" fill="{INK}">')
add('<ellipse cx="622" cy="892" rx="50" ry="58"/>')
add(path("M 622 948 C 540 962 494 1000 482 1050 L 762 1050 C 750 1000 704 962 622 948 Z",
         fill=INK, w=0))
add('</g>')
add('<g opacity="0.26">')
add(path("M 572 892 a 50 58 0 1 1 100 0 a 50 58 0 1 1 -100 0", fill="none", w=2.8, extra=GD))
add(path("M 622 948 C 540 962 494 1000 482 1050", fill="none", w=2.8, extra=GD))
add(path("M 622 948 C 704 962 750 1000 762 1050", fill="none", w=2.8, extra=GD))
add(path("M 600 946 q 22 14 44 0", fill="none", w=2.4, extra=GD))
add('</g>')
add('</g>')

# --------------------------------------------------------------------------
# contact shadows
for scx, srx in ((448, 84), (784, 92), (140, 70), (1662, 82), (1292, 96), (964, 92)):
    add(f'<ellipse cx="{scx}" cy="{884 if scx not in (1292,) else 946}" rx="{srx}" ry="14" '
        f'fill="url(#toneFine)" opacity="0.55"/>')

# final mood pass: the human side dimmed, the measured side left bright
# --------------------------------------------------------------------------
add(f'<ellipse cx="748" cy="640" rx="160" ry="340" fill="url(#toneFine)" opacity="0.14"/>')
add(f'<ellipse cx="1660" cy="770" rx="150" ry="300" fill="url(#toneFine)" opacity="0.16"/>')
add(f'<rect width="{W}" height="{H}" fill="url(#vignette)"/>')
add('</g>')  # /artwork

svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
       f'viewBox="0 0 {W} {H}">' + DEFS + "".join(P) + "</svg>")

out = sys.argv[1] if len(sys.argv) > 1 else "assets/manga_shop_scene.svg"
with open(out, "w", encoding="utf-8") as f:
    f.write(svg)
print(f"wrote {out} ({len(svg)} bytes)")
