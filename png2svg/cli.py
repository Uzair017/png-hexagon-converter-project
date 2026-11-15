import argparse

from png2svg.converter import convert


def main(args=None):
    parser = argparse.ArgumentParser(
        description="Convert a PNG image to an SVG using hexagons."
    )

    parser.add_argument("input_filename")
    parser.add_argument("output_filename")
    parser.add_argument(
        "--radius",
        type=float,
        default=15,
        help="Radius of the hexagons (default: 15)"
    )

    parsed_args = parser.parse_args(args)

    convert(
        parsed_args.input_filename,
        parsed_args.output_filename,
        parsed_args.radius
    )


if __name__ == "__main__":
    main()