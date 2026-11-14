from PIL import Image

from png2svg.color_sampler import sample_color


def test_sample_color():
    image = Image.new("RGB", (30, 30), (255, 0, 0))

    color = sample_color(image, (15, 15), 10)

    assert color == (255, 0, 0)

def test_sample_average_color():
    image = Image.new("RGB", (30, 30), (0, 0, 0))

    image.putpixel((15, 15), (255, 0, 0))
    image.putpixel((16, 15), (0, 0, 255))

    color = sample_color(image, (15.5, 15), 0.5)

    assert color == (128, 0, 128)