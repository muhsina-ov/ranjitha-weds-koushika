import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
images_dir = os.path.join(base_dir, "public", "images")
fonts_dir = os.path.join(base_dir, "scripts", "fonts")

output_path_png = os.path.join(images_dir, "og-image.png")
output_path_jpg = os.path.join(images_dir, "og-image.jpg")
public_jpg = os.path.join(base_dir, "public", "og-image.jpg")

W, H = 1200, 630

# -----------------------------------------------------------------------------
# 1. Base Canvas & Luxurious Deep Emerald Gradient
# -----------------------------------------------------------------------------
canvas = Image.new("RGBA", (W, H), (4, 25, 19, 255))
draw = ImageDraw.Draw(canvas)

for y in range(H):
    ratio = y / H
    # Subtle royal gradient from deep emerald jade to darker midnight pine
    r = int(7 * (1 - ratio) + 3 * ratio)
    g = int(38 * (1 - ratio) + 18 * ratio)
    b = int(29 * (1 - ratio) + 14 * ratio)
    draw.line([(0, y), (W, y)], fill=(r, g, b, 255))

# Ambient warm radial glows
glow_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
g_draw = ImageDraw.Draw(glow_layer)

# Halo glow behind couple's arch (centered around x=280, y=340)
for r in range(360, 0, -6):
    alpha = int(40 * (1 - r / 360) ** 1.5)
    g_draw.ellipse([280 - r, 340 - r, 280 + r, 340 + r], fill=(238, 202, 115, alpha))

# Warm gold ambient glow behind typography (x=840, y=310)
for r in range(420, 0, -6):
    alpha = int(26 * (1 - r / 420) ** 1.4)
    g_draw.ellipse([840 - r, 310 - r, 840 + r, 310 + r], fill=(245, 218, 130, alpha))

canvas = Image.alpha_composite(canvas, glow_layer)

# -----------------------------------------------------------------------------
# 2. Sacred Mandala Background Textures
# -----------------------------------------------------------------------------
mandala_path = os.path.join(images_dir, "mandala-texture.jpg")
if os.path.exists(mandala_path):
    mandala = Image.open(mandala_path).convert("RGBA")
    mw, mh = 700, 700
    mandala_resized = mandala.resize((mw, mh), Image.Resampling.LANCZOS)

    # Left background mandala behind arch
    m_left = mandala_resized.copy()
    m_alpha = m_left.split()[3].point(lambda p: int(p * 0.12))
    m_left.putalpha(m_alpha)
    canvas.paste(m_left, (-150, -50), m_left)

    # Right bottom background mandala
    m_right = mandala_resized.copy()
    m_alpha_r = m_right.split()[3].point(lambda p: int(p * 0.09))
    m_right.putalpha(m_alpha_r)
    canvas.paste(m_right, (W - 400, H - 400), m_right)

# -----------------------------------------------------------------------------
# 3. Double Gold Outer Border Frame
# -----------------------------------------------------------------------------
border_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
b_draw = ImageDraw.Draw(border_layer)
# Outer solid gold line
b_draw.rectangle([18, 18, W - 18, H - 18], outline=(226, 183, 85, 175), width=2)
# Inner delicate line
b_draw.rectangle([25, 25, W - 25, H - 25], outline=(226, 183, 85, 90), width=1)
canvas = Image.alpha_composite(canvas, border_layer)

# -----------------------------------------------------------------------------
# 4. Corner Floral Lotus Ornaments
# -----------------------------------------------------------------------------
corner_path = os.path.join(images_dir, "floral-corner.png")
if os.path.exists(corner_path):
    corner = Image.open(corner_path).convert("RGBA")
    cw, ch = 124, 124
    corner = corner.resize((cw, ch), Image.Resampling.LANCZOS)
    r, g, b, a = corner.split()
    a = a.point(lambda p: int(p * 0.70))
    corner.putalpha(a)

    canvas.paste(corner, (26, 26), corner)
    tr = corner.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    canvas.paste(tr, (W - 26 - cw, 26), tr)
    bl = corner.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    canvas.paste(bl, (26, H - 26 - ch), bl)
    br = corner.transpose(Image.Transpose.ROTATE_180)
    canvas.paste(br, (W - 26 - cw, H - 26 - ch), br)

# -----------------------------------------------------------------------------
# 5. Left Side: Royal Jharokha Arch Frame for the Couple
# -----------------------------------------------------------------------------
arch_x, arch_y = 65, 58
arch_w, arch_h = 420, 524

arch_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
a_draw = ImageDraw.Draw(arch_layer)

# Architectural arch mask (rounded dome top, straight sides, rounded base)
arch_mask = Image.new("L", (W, H), 0)
m_draw = ImageDraw.Draw(arch_mask)
# Top dome ellipse
m_draw.ellipse([arch_x, arch_y, arch_x + arch_w, arch_y + arch_w], fill=255)
# Bottom body
m_draw.rounded_rectangle(
    [arch_x, arch_y + arch_w // 2, arch_x + arch_w, arch_y + arch_h],
    radius=18,
    fill=255,
)

# Fill arch background with rich dark velvet emerald
arch_bg = Image.new("RGBA", (W, H), (5, 30, 23, 240))
canvas.paste(arch_bg, (0, 0), arch_mask)

# Arch borders: outer gold
a_draw.arc(
    [arch_x, arch_y, arch_x + arch_w, arch_y + arch_w],
    start=180,
    end=0,
    fill=(226, 183, 85, 200),
    width=2,
)
a_draw.line(
    [(arch_x, arch_y + arch_w // 2), (arch_x, arch_y + arch_h - 18)],
    fill=(226, 183, 85, 200),
    width=2,
)
a_draw.line(
    [(arch_x + arch_w, arch_y + arch_w // 2), (arch_x + arch_w, arch_y + arch_h - 18)],
    fill=(226, 183, 85, 200),
    width=2,
)
a_draw.arc(
    [arch_x, arch_y + arch_h - 36, arch_x + 36, arch_y + arch_h],
    start=90,
    end=180,
    fill=(226, 183, 85, 200),
    width=2,
)
a_draw.arc(
    [arch_x + arch_w - 36, arch_y + arch_h - 36, arch_x + arch_w, arch_y + arch_h],
    start=0,
    end=90,
    fill=(226, 183, 85, 200),
    width=2,
)
a_draw.line(
    [(arch_x + 18, arch_y + arch_h), (arch_x + arch_w - 18, arch_y + arch_h)],
    fill=(226, 183, 85, 200),
    width=2,
)

# Inner delicate arch outline (inset 7px)
ix, iy, iw, ih = arch_x + 7, arch_y + 7, arch_w - 14, arch_h - 14
a_draw.arc([ix, iy, ix + iw, iy + iw], start=180, end=0, fill=(226, 183, 85, 90), width=1)
a_draw.line([(ix, iy + iw // 2), (ix, iy + ih - 14)], fill=(226, 183, 85, 90), width=1)
a_draw.line([(ix + iw, iy + iw // 2), (ix + iw, iy + ih - 14)], fill=(226, 183, 85, 90), width=1)
a_draw.arc(
    [ix, iy + ih - 28, ix + 28, iy + ih],
    start=90,
    end=180,
    fill=(226, 183, 85, 90),
    width=1,
)
a_draw.arc(
    [ix + iw - 28, iy + ih - 28, ix + iw, iy + ih],
    start=0,
    end=90,
    fill=(226, 183, 85, 90),
    width=1,
)
a_draw.line([(ix + 14, iy + ih), (ix + iw - 14, iy + ih)], fill=(226, 183, 85, 90), width=1)

canvas = Image.alpha_composite(canvas, arch_layer)

# Garland across top of the arch
garland_path = os.path.join(images_dir, "garland.png")
if os.path.exists(garland_path):
    garland = Image.open(garland_path).convert("RGBA")
    gw = 620
    gh = int(garland.height * (gw / garland.width))
    garland = garland.resize((gw, gh), Image.Resampling.LANCZOS)
    canvas.paste(garland, (65, -36), garland)

# Couple Image inside Arch
couple_path = os.path.join(images_dir, "couple-hero.png")
if os.path.exists(couple_path):
    couple = Image.open(couple_path).convert("RGBA")

    target_h = 515
    target_w = int(couple.width * (target_h / couple.height))
    couple_resized = couple.resize((target_w, target_h), Image.Resampling.LANCZOS)

    # Soft feather fade at bottom 45px
    fade_mask = Image.new("L", (target_w, target_h), 255)
    f_draw = ImageDraw.Draw(fade_mask)
    for y in range(target_h - 45, target_h):
        val = int(255 * (1 - (y - (target_h - 45)) / 45))
        f_draw.line([(0, y), (target_w, y)], fill=val)

    orig_a = couple_resized.split()[3]
    final_a = Image.composite(orig_a, Image.new("L", (target_w, target_h), 0), fade_mask)
    couple_resized.putalpha(final_a)

    c_x = arch_x + (arch_w - target_w) // 2
    c_y = arch_y + arch_h - target_h + 10

    canvas.paste(couple_resized, (c_x, c_y), couple_resized)

# -----------------------------------------------------------------------------
# 6. Typography on Right Side (Center at x = 860)
# -----------------------------------------------------------------------------
f_garamond_bold = os.path.join(fonts_dir, "CormorantGaramond-Bold.ttf")
f_garamond_med = os.path.join(fonts_dir, "CormorantGaramond-Medium.ttf")
f_greatvibes = os.path.join(fonts_dir, "GreatVibes-Regular.ttf")
f_jost_med = os.path.join(fonts_dir, "Jost-Medium.ttf")
f_jost_semi = os.path.join(fonts_dir, "Jost-SemiBold.ttf")

font_pre = ImageFont.truetype(f_jost_med, 14)
font_names = ImageFont.truetype(f_garamond_bold, 68)
font_and = ImageFont.truetype(f_greatvibes, 56)
font_ceremony = ImageFont.truetype(f_jost_semi, 16)
font_date = ImageFont.truetype(f_garamond_bold, 24)
font_venue = ImageFont.truetype(f_jost_med, 14)
font_url = ImageFont.truetype(f_jost_med, 13)

text_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
t_draw = ImageDraw.Draw(text_layer)

center_x = 860
curr_y = 96

def draw_tracked_text(draw_ctx, text, y, font, color, letter_spacing=0):
    chars = list(text)
    char_widths = [
        draw_ctx.textbbox((0, 0), c, font=font)[2] - draw_ctx.textbbox((0, 0), c, font=font)[0]
        for c in chars
    ]
    total_w = sum(char_widths) + (len(chars) - 1) * letter_spacing
    start_x = center_x - total_w // 2
    cur_x = start_x
    for c, cw in zip(chars, char_widths):
        draw_ctx.text((cur_x, y), c, font=font, fill=color)
        cur_x += cw + letter_spacing
    bbox = draw_ctx.textbbox((0, 0), text, font=font)
    return bbox[3] - bbox[1]

# Header Line
pre_text = "TOGETHER WITH THEIR FAMILIES"
draw_tracked_text(t_draw, pre_text, curr_y, font_pre, (226, 183, 85, 235), letter_spacing=5)
# Side accent lines
t_draw.line(
    [(center_x - 204, curr_y + 8), (center_x - 164, curr_y + 8)],
    fill=(226, 183, 85, 120),
    width=1,
)
t_draw.line(
    [(center_x + 164, curr_y + 8), (center_x + 204, curr_y + 8)],
    fill=(226, 183, 85, 120),
    width=1,
)

curr_y += 34

def draw_lux_name(draw_ctx, name, y):
    bbox = draw_ctx.textbbox((0, 0), name, font=font_names)
    nw = bbox[2] - bbox[0]
    nh = bbox[3] - bbox[1]
    nx = center_x - nw // 2

    # Drop shadow
    draw_ctx.text((nx + 2, y + 3), name, font=font_names, fill=(0, 0, 0, 200))
    # Rich warm gold text
    draw_ctx.text((nx, y), name, font=font_names, fill=(238, 198, 98, 255))
    # Specular upper sheen
    draw_ctx.text((nx - 1, y - 1), name, font=font_names, fill=(255, 246, 214, 150))
    return nh

# Bride Name: Ranjitha (matches ranjitha-weds-koushik domain & photo order)
nh1 = draw_lux_name(t_draw, "Ranjitha", curr_y)
curr_y += nh1 + 6

# Calligraphic "&" in Great Vibes
amp_bbox = t_draw.textbbox((0, 0), "&", font=font_and)
amp_w = amp_bbox[2] - amp_bbox[0]
t_draw.text((center_x - amp_w // 2, curr_y - 12), "&", font=font_and, fill=(248, 228, 128, 240))
curr_y += 36

# Groom Name: Koushik
nh2 = draw_lux_name(t_draw, "Koushik", curr_y)
curr_y += nh2 + 18

# Royal Gold Geometric Divider with diamond
div_w = 145
t_draw.line(
    [(center_x - div_w, curr_y), (center_x - 18, curr_y)],
    fill=(226, 183, 85, 190),
    width=1,
)
t_draw.line(
    [(center_x + 18, curr_y), (center_x + div_w, curr_y)],
    fill=(226, 183, 85, 190),
    width=1,
)
# Center diamond ornament
d_size = 5
diamond_pts = [
    (center_x, curr_y - d_size),
    (center_x + d_size, curr_y),
    (center_x, curr_y + d_size),
    (center_x - d_size, curr_y),
]
t_draw.polygon(diamond_pts, fill=(248, 228, 128, 255))
curr_y += 18

# Subtitle: ENGAGEMENT CELEBRATION
draw_tracked_text(
    t_draw,
    "ENGAGEMENT CELEBRATION",
    curr_y,
    font_ceremony,
    (251, 248, 238, 255),
    letter_spacing=4,
)
curr_y += 36

# Date & Venue Glass Badge
box_w, box_h = 448, 86
box_x = center_x - box_w // 2
box_y = curr_y

badge_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
bg_draw = ImageDraw.Draw(badge_layer)
bg_draw.rounded_rectangle(
    [box_x, box_y, box_x + box_w, box_y + box_h],
    radius=16,
    fill=(6, 35, 27, 230),
    outline=(226, 183, 85, 170),
    width=1,
)
# Subtle interior glow line
bg_draw.rounded_rectangle(
    [box_x + 2, box_y + 2, box_x + box_w - 2, box_y + box_h - 2],
    radius=14,
    outline=(255, 255, 255, 22),
    width=1,
)
canvas = Image.alpha_composite(canvas, badge_layer)

draw_tracked_text(
    t_draw,
    "MONDAY, 21 SEPTEMBER 2026",
    box_y + 16,
    font_date,
    (248, 228, 128, 255),
    letter_spacing=2,
)
draw_tracked_text(
    t_draw,
    "SHANKARA KRUPA · SHIVAMOGGA · 10:00 AM ONWARDS",
    box_y + 50,
    font_venue,
    (251, 248, 238, 220),
    letter_spacing=2,
)

curr_y = box_y + box_h + 18

# Website URL Pill with updated production link
url_pill = "ranjitha-weds-koushik.invitingyou.top"
pill_w = 340
pill_h = 28
pill_x = center_x - pill_w // 2
pill_y = curr_y

pill_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
p_draw = ImageDraw.Draw(pill_layer)
p_draw.rounded_rectangle(
    [pill_x, pill_y, pill_x + pill_w, pill_y + pill_h],
    radius=14,
    fill=(4, 25, 19, 160),
    outline=(226, 183, 85, 110),
    width=1,
)
canvas = Image.alpha_composite(canvas, pill_layer)

draw_tracked_text(
    t_draw,
    url_pill,
    curr_y + 6,
    font_url,
    (226, 183, 85, 230),
    letter_spacing=2,
)

# Composite all text
canvas = Image.alpha_composite(canvas, text_layer)

# -----------------------------------------------------------------------------
# 7. Save High Quality JPG & PNG
# -----------------------------------------------------------------------------
final_rgb = canvas.convert("RGB")
final_rgb.save(output_path_jpg, "JPEG", quality=96, optimize=True)
final_rgb.save(public_jpg, "JPEG", quality=96, optimize=True)
canvas.save(output_path_png, "PNG")

print("Generated creative luxury couple OG image successfully!")
