from png2svg.image_loader import load_image
from png2svg.hexagon_grid import generate_hexagon_coordinates
from png2svg.color_sampler import sample_color
from png2svg.svg_generator import generate_hexagon
from png2svg.svg_writer import write_svg


def convert(input_filename, output_filename, radius=15):
    image = load_image(input_filename)
    hexagons = []

    coordinates = generate_hexagon_coordinates(
        image.width, image.height, radius
    )

    for coordinate in coordinates:
        color = sample_color(image, coordinate, radius)

        hexagon = generate_hexagon(coordinate, radius, color)

        hexagons.append(hexagon)

    write_svg(hexagons, image.width, image.height, output_filename)