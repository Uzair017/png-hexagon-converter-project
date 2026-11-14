from PIL import Image


def load_image(filename):
    image = Image.open(filename)
    image.load()

    return image