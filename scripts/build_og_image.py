import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
images_dir = os.path.join(base_dir, "public", "images")
output_path_png = os.path.join(images_dir, "og-image.png")
output_path_jpg = os.path.join(images_dir, "og-image.jpg")
public_jpg = os.path.join(base_dir, "public", "og-image.jpg")

W, H = 1200, 630

# 1. Base Canvas & Deep Emerald Luxurious Gradient
canvas = Image.new("RGBA", (W, H), (5, 26, 20, 255))
draw = ImageDraw.Draw(canvas)

for y in range(H):
    ratio = y / H
    # Gradient from rich forest emerald to dark night emerald
    r = int(10 * (1 - ratio) + 4 * ratio)
    g = int(46 * (1 - ratio) + 22 * ratio)
    b = int(36 * (1 - ratio) + 18 * ratio)
    draw.line([(0, y), (W, y)], fill=(r, g, b, 255))

# Ambient warm radial glows
glow_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
g_draw = ImageDraw.Draw(glow_layer)
# Glow behind couple (x=270, y=360)
for r in range(350, 0, -5):
    alpha = int(35 * (1 - r / 350))
    g_draw.ellipse([270 - r, 360 - r, 270 + r, 360 + r], fill=(235, 195, 100, alpha))

# Soft warm glow on text side (x=830, y=300)
for r in range(400, 0, -5):
    alpha = int(22 * (1 - r / 400))
    g_draw.ellipse([830 - r, 300 - r, 830 + r, 300 + r], fill=(245, 215, 120, alpha))

canvas = Image.alpha_composite(canvas, glow_layer)

# 2. Mandala Background Textures
mandala_path = os.path.join(images_dir, "mandala-texture.jpg")
if os.path.exists(mandala_path):
    mandala = Image.open(mandala_path).convert("RGBA")
    mw, mh = 680, 680
    mandala_resized = mandala.resize((mw, mh), Image.Resampling.LANCZOS)
    
    # Left background mandala
    m_left = mandala_resized.copy()
    m_alpha = m_left.split()[3].point(lambda p: int(p * 0.11))
    m_left.putalpha(m_alpha)
    canvas.paste(m_left, (-140, -40), m_left)

    # Right bottom background mandala
    m_right = mandala_resized.copy()
    m_alpha_r = m_right.split()[3].point(lambda p: int(p * 0.09))
    m_right.putalpha(m_alpha_r)
    canvas.paste(m_right, (W - 420, H - 420), m_right)

# 3. Double Gold Frame
border_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
b_draw = ImageDraw.Draw(border_layer)
# Outer solid gold line
b_draw.rectangle([18, 18, W - 18, H - 18], outline=(226, 183, 85, 160), width=2)
# Inner delicate line
b_draw.rectangle([25, 25, W - 25, H - 25], outline=(226, 183, 85, 80), width=1)
canvas = Image.alpha_composite(canvas, border_layer)

# 4. Corner Floral Lotus Ornaments
corner_path = os.path.join(images_dir, "floral-corner.png")
if os.path.exists(corner_path):
    corner = Image.open(corner_path).convert("RGBA")
    cw, ch = 120, 120
    corner = corner.resize((cw, ch), Image.Resampling.LANCZOS)
    r, g, b, a = corner.split()
    a = a.point(lambda p: int(p * 0.65))
    corner.putalpha(a)

    canvas.paste(corner, (26, 26), corner)
    tr = corner.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    canvas.paste(tr, (W - 26 - cw, 26), tr)
    bl = corner.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    canvas.paste(bl, (26, H - 26 - ch), bl)
    br = corner.transpose(Image.Transpose.ROTATE_180)
    canvas.paste(br, (W - 26 - cw, H - 26 - ch), br)

# 5. Garland along the top
garland_path = os.path.join(images_dir, "garland.png")
if os.path.exists(garland_path):
    garland = Image.open(garland_path).convert("RGBA")
    # Span across top with proper scale and offset so tassels don't clash with text
    gw = 620
    gh = int(garland.height * (gw / garland.width))
    garland = garland.resize((gw, gh), Image.Resampling.LANCZOS)
    # Position shifted slightly left towards the arch center, and top tucked up
    canvas.paste(garland, (60, -35), garland)

# 6. Left Side: Royal Arch Portrait Frame for Couple
arch_x, arch_y = 65, 60
arch_w, arch_h = 410, 520

arch_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
a_draw = ImageDraw.Draw(arch_layer)

# Create an elegant architectural arch mask (rounded dome top, straight sides, rounded base)
# We can draw it precisely:
arch_mask = Image.new("L", (W, H), 0)
m_draw = ImageDraw.Draw(arch_mask)
# Top dome ellipse
m_draw.ellipse([arch_x, arch_y, arch_x + arch_w, arch_y + arch_w], fill=255)
# Bottom body
m_draw.rounded_rectangle([arch_x, arch_y + arch_w // 2, arch_x + arch_w, arch_y + arch_h], radius=16, fill=255)

# Fill arch background
arch_bg = Image.new("RGBA", (W, H), (6, 35, 27, 235))
canvas.paste(arch_bg, (0, 0), arch_mask)

# Arch borders
# Top arc
a_draw.arc([arch_x, arch_y, arch_x + arch_w, arch_y + arch_w], start=180, end=0, fill=(226, 183, 85, 180), width=2)
# Side lines
a_draw.line([(arch_x, arch_y + arch_w // 2), (arch_x, arch_y + arch_h - 16)], fill=(226, 183, 85, 180), width=2)
a_draw.line([(arch_x + arch_w, arch_y + arch_w // 2), (arch_x + arch_w, arch_y + arch_h - 16)], fill=(226, 183, 85, 180), width=2)
# Bottom rounded corners & bottom line
a_draw.arc([arch_x, arch_y + arch_h - 32, arch_x + 32, arch_y + arch_h], start=90, end=180, fill=(226, 183, 85, 180), width=2)
a_draw.arc([arch_x + arch_w - 32, arch_y + arch_h - 32, arch_x + arch_w, arch_y + arch_h], start=0, end=90, fill=(226, 183, 85, 180), width=2)
a_draw.line([(arch_x + 16, arch_y + arch_h), (arch_x + arch_w - 16, arch_y + arch_h)], fill=(226, 183, 85, 180), width=2)

# Inner delicate arch outline (inset 6px)
ix, iy, iw, ih = arch_x + 6, arch_y + 6, arch_w - 12, arch_h - 12
a_draw.arc([ix, iy, ix + iw, iy + iw], start=180, end=0, fill=(226, 183, 85, 75), width=1)
a_draw.line([(ix, iy + iw // 2), (ix, iy + ih - 12)], fill=(226, 183, 85, 75), width=1)
a_draw.line([(ix + iw, iy + iw // 2), (ix + iw, iy + ih - 12)], fill=(226, 183, 85, 75), width=1)
a_draw.arc([ix, iy + ih - 24, ix + 24, iy + ih], start=90, end=180, fill=(226, 183, 85, 75), width=1)
a_draw.arc([ix + iw - 24, iy + ih - 24, ix + iw, iy + ih], start=0, end=90, fill=(226, 183, 85, 75), width=1)
a_draw.line([(ix + 12, iy + ih), (ix + iw - 12, iy + ih)], fill=(226, 183, 85, 75), width=1)

canvas = Image.alpha_composite(canvas, arch_layer)

# Couple Image inside Arch
couple_path = os.path.join(images_dir, "couple-hero.png")
if os.path.exists(couple_path):
    couple = Image.open(couple_path).convert("RGBA")
    
    target_h = 510
    target_w = int(couple.width * (target_h / couple.height))
    couple_resized = couple.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    # Soft fade at bottom 40px
    fade_mask = Image.new("L", (target_w, target_h), 255)
    f_draw = ImageDraw.Draw(fade_mask)
    for y in range(target_h - 40, target_h):
        val = int(255 * (1 - (y - (target_h - 40)) / 40))
        f_draw.line([(0, y), (target_w, y)], fill=val)
    
    orig_a = couple_resized.split()[3]
    final_a = Image.composite(orig_a, Image.new("L", (target_w, target_h), 0), fade_mask)
    couple_resized.putalpha(final_a)
    
    c_x = arch_x + (arch_w - target_w) // 2
    c_y = arch_y + arch_h - target_h + 10
    
    canvas.paste(couple_resized, (c_x, c_y), couple_resized)

# 7. Typography on Right Side (Center at x = 855)
fonts_dir = "C:\\Windows\\Fonts"
font_names = ImageFont.truetype(os.path.join(fonts_dir, "palab.ttf"), 66)
font_and = ImageFont.truetype(os.path.join(fonts_dir, "Gabriola.ttf"), 52)
font_pre = ImageFont.truetype(os.path.join(fonts_dir, "corbel.ttf"), 14)
font_ceremony = ImageFont.truetype(os.path.join(fonts_dir, "corbelb.ttf"), 17)
font_date = ImageFont.truetype(os.path.join(fonts_dir, "palab.ttf"), 18)
font_venue = ImageFont.truetype(os.path.join(fonts_dir, "corbel.ttf"), 14)
font_url = ImageFont.truetype(os.path.join(fonts_dir, "corbel.ttf"), 13)

text_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
t_draw = ImageDraw.Draw(text_layer)

center_x = 855
curr_y = 100

def draw_tracked_text(draw_ctx, text, y, font, color, letter_spacing=0):
    chars = list(text)
    char_widths = [draw_ctx.textbbox((0, 0), c, font=font)[2] - draw_ctx.textbbox((0, 0), c, font=font)[0] for c in chars]
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
# Accent side lines
t_draw.line([(center_x - 200, curr_y + 8), (center_x - 165, curr_y + 8)], fill=(226, 183, 85, 110), width=1)
t_draw.line([(center_x + 165, curr_y + 8), (center_x + 200, curr_y + 8)], fill=(226, 183, 85, 110), width=1)

curr_y += 32

def draw_lux_name(draw_ctx, name, y):
    bbox = draw_ctx.textbbox((0, 0), name, font=font_names)
    nw = bbox[2] - bbox[0]
    nh = bbox[3] - bbox[1]
    nx = center_x - nw // 2
    
    # Drop shadow
    draw_ctx.text((nx + 2, y + 3), name, font=font_names, fill=(0, 0, 0, 210))
    # Outer warm gold
    draw_ctx.text((nx, y), name, font=font_names, fill=(236, 195, 95, 255))
    # Soft specular sheen
    draw_ctx.text((nx - 1, y - 1), name, font=font_names, fill=(255, 245, 210, 160))
    return nh

# Groom Name
nh1 = draw_lux_name(t_draw, "Koushik", curr_y)
curr_y += nh1 + 8

# Calligraphic "&"
amp_bbox = t_draw.textbbox((0, 0), "&", font=font_and)
amp_w = amp_bbox[2] - amp_bbox[0]
t_draw.text((center_x - amp_w // 2, curr_y - 12), "&", font=font_and, fill=(246, 226, 122, 240))
curr_y += 36

# Bride Name
nh2 = draw_lux_name(t_draw, "Ranjitha", curr_y)
curr_y += nh2 + 20

# Elegant Gold Geometric Divider with diamond
div_w = 140
t_draw.line([(center_x - div_w, curr_y), (center_x - 18, curr_y)], fill=(226, 183, 85, 180), width=1)
t_draw.line([(center_x + 18, curr_y), (center_x + div_w, curr_y)], fill=(226, 183, 85, 180), width=1)
# Center diamond
d_size = 5
diamond_pts = [(center_x, curr_y - d_size), (center_x + d_size, curr_y), (center_x, curr_y + d_size), (center_x - d_size, curr_y)]
t_draw.polygon(diamond_pts, fill=(246, 226, 122, 255))
curr_y += 18

# Subtitle: ENGAGEMENT CELEBRATION
draw_tracked_text(t_draw, "ENGAGEMENT CELEBRATION", curr_y, font_ceremony, (251, 248, 238, 255), letter_spacing=4)
curr_y += 36

# Date & Venue Glass Badge
box_w, box_h = 440, 82
box_x = center_x - box_w // 2
box_y = curr_y

badge_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
bg_draw = ImageDraw.Draw(badge_layer)
bg_draw.rounded_rectangle([box_x, box_y, box_x + box_w, box_y + box_h],
                          radius=16,
                          fill=(6, 34, 26, 220),
                          outline=(226, 183, 85, 160), width=1)
# Subtle inner highlight
bg_draw.rounded_rectangle([box_x + 2, box_y + 2, box_x + box_w - 2, box_y + box_h - 2],
                          radius=14,
                          outline=(255, 255, 255, 20), width=1)
canvas = Image.alpha_composite(canvas, badge_layer)

draw_tracked_text(t_draw, "MONDAY, 21 SEPTEMBER 2026", box_y + 16, font_date, (246, 226, 122, 255), letter_spacing=2)
draw_tracked_text(t_draw, "SHIVAMOGGA, KARNATAKA · 10:00 AM ONWARDS", box_y + 46, font_venue, (251, 248, 238, 220), letter_spacing=2)

curr_y = box_y + box_h + 18

# Website URL Pill
url_pill = "ranjitha-weds-koushika.invitingyou.top"
draw_tracked_text(t_draw, url_pill, curr_y, font_url, (226, 183, 85, 210), letter_spacing=3)

# Composite all text
canvas = Image.alpha_composite(canvas, text_layer)

# 8. Save High Quality JPG & PNG
final_rgb = canvas.convert("RGB")
final_rgb.save(output_path_jpg, "JPEG", quality=96, optimize=True)
final_rgb.save(public_jpg, "JPEG", quality=96, optimize=True)
canvas.save(output_path_png, "PNG")

print("Regenerated refined OG images successfully!")
