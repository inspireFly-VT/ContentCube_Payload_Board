import machine
import time
from framebuf import FrameBuffer, RGB565

def rgb_to_hsv(r, g, b):
    r = r / 255.0
    g = g / 255.0
    b = b / 255.0
    max_val = max(r, g, b)
    min_val = min(r, g, b)
    diff = max_val - min_val

    # Calculate Hue
    if diff == 0:
        h = 0
    elif max_val == r:
        h = (60 * ((g - b) / diff) + 360) % 360
    elif max_val == g:
        h = (60 * ((b - r) / diff) + 120) % 360
    elif max_val == b:
        h = (60 * ((r - g) / diff) + 240) % 360

    # Calculate Saturation
    s = 0 if max_val == 0 else (diff / max_val)

    # Calculate Value
    v = max_val

    return h, s * 100, v * 100

def See_Blue(image_bytes, width, height):
    # Resize image manually
    scale_percent = 0.5
    new_width = int(width * scale_percent)
    new_height = int(height * scale_percent)

    blue_pixel_count = 0
    total_pixel_count = new_width * new_height

    lower_h, lower_s, lower_v = 100, 40, 40
    upper_h, upper_s, upper_v = 140, 255, 255

    # Loop through image pixels (assuming RGB565 format or similar)
    for y in range(0, height, 2):  # Skip every other row to scale down
        for x in range(0, width, 2):  # Skip every other column to scale down
            pixel_index = (y * width + x) * 2  # 2 bytes per pixel (RGB565 format)
            pixel = image_bytes[pixel_index:pixel_index+2]

            r = (pixel[0] & 0xF8)  # Extract red component
            g = ((pixel[0] & 0x07) << 5) | ((pixel[1] & 0xE0) >> 3)  # Extract green component
            b = (pixel[1] & 0x1F) << 3  # Extract blue component

            h, s, v = rgb_to_hsv(r, g, b)

            # Check if pixel falls within the blue range
            if lower_h <= h <= upper_h and lower_s <= s <= upper_s and lower_v <= v <= upper_v:
                blue_pixel_count += 1

    # Calculate percentage of blue pixels
    ratio_blue = blue_pixel_count / total_pixel_count
    color_percent = ratio_blue * 100

    # Decide on tag
    if color_percent >= 40:
        tag = "TRANSFER"
    else:
        tag = "NO TRANSFER"

    return color_percent, tag

# Example usage with a placeholder image byte array (adjust for your actual image source)
# Replace with code to read an actual image file in byte format

# Assuming 128x128 image size for testing
image_width = 128
image_height = 128
image_bytes = bytearray(image_width * image_height * 2)  # Simulating RGB565 format image data

percent_blue, tag = See_Blue(image_bytes, image_width, image_height)
print(f"Image has {percent_blue:.4f}% blue and is tagged as: {tag}")

