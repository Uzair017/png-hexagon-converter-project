from PIL import Image


def load_image(filename):
    image = Image.open(filename)
    image.load()
    image = image.convert("RGBA").convert("RGB")
    return image