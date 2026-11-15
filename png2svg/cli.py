import sys

from png2svg.converter import convert


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    if len(args) != 2:
        raise SystemExit("Usage: python -m png2svg.cli input.png output.svg")

    input_filename = args[0]
    output_filename = args[1]

    convert(input_filename, output_filename)


if __name__ == "__main__":
    main()