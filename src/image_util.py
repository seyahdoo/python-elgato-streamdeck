
from PIL import Image, ImageDraw, ImageFont


# Custom tiles with run-time generated text and custom image via the PIL module
def get_key_image(image_path, text):
    # Get the required key image dimensions
    width = 72
    height = 72

    # Create new key image of the correct dimensions, black background
    image = Image.new("RGB", (width, height), 'black')

    # Add image overlay, rescaling the image asset if it is too large to fit the
    # requested dimensions via a high quality Lanczos scaling algorithm
    icon = Image.open(get_key_image()).convert("RGBA")
    icon.thumbnail((width, height - 20), Image.LANCZOS)
    image.paste(icon, (0, 0), icon)

    # Load a custom TrueType font and use it to overlay the key index, draw key
    # number onto the image
    font = ImageFont.truetype("Assets/Roboto-Regular.ttf", 14)
    draw = ImageDraw.Draw(image)
    draw.text((10, height - 20), text=text, font=font, fill=(255, 255, 255, 128))

    # Get the raw r, g and b components of the generated image (note we need to
    # flip it horizontally to match the format the StreamDeck expects)
    r, g, b = image.transpose(Image.FLIP_LEFT_RIGHT).split()

    # Recombine the B, G and R elements in the order the display expects them,
    # and convert the resulting image to a sequence of bytes
    return Image.merge("RGB", (b, g, r)).tobytes()

