def write_svg(hexagons, width, height, output_filename):
    svg_content = (
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}">\n'
    )

    for hexagon in hexagons:
        svg_content += f"    {hexagon}\n"

    svg_content += "</svg>"

    with open(output_filename, "w") as file:
        file.write(svg_content)