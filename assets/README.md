# assets

## manga_shop_scene

A single-scene manga-style illustration of a small Japanese clothing shop in
trouble: everything measurable is bright and rising, everything human is dimmed,
disconnected or removed. Hand-inked look, screentone shading, warm off-white
paper, one wide scene with no panel borders and no text anywhere.

| file | what it is |
| --- | --- |
| `manga_shop_scene.svg` | the artwork, vector, 1800x1050 |
| `manga_shop_scene.png` | raster, 1800x1050 |
| `manga_shop_scene@2x.png` | raster, 3600x2100 |
| `make_manga_shop_scene.py` | generator that produces the SVG |

Regenerate the vector:

```sh
python3 assets/make_manga_shop_scene.py assets/manga_shop_scene.svg
```

The PNGs were rasterised from the SVG with headless Chromium (the SVG uses
`feTurbulence` for the paper grain and the hand-drawn line wobble, so a
renderer without filter support will not reproduce them).
