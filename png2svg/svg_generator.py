import math


def generate_hexagon(coordinate, radius, color):
    center_x, center_y = coordinate
    red, green, blue = color

    points = [
        (center_x + radius, center_y),
        (center_x + radius / 2, center_y + math.sqrt(3) * radius / 2),
        (center_x - radius / 2, center_y + math.sqrt(3) * radius / 2),
        (center_x - radius, center_y),
        (center_x - radius / 2, center_y - math.sqrt(3) * radius / 2),
        (center_x + radius / 2, center_y - math.sqrt(3) * radius / 2),
    ]

    points_string = " ".join(
        f"{x},{y}" for x, y in points
    )

    fill_color = f"#{red:02x}{green:02x}{blue:02x}"

    return f'<polygon points="{points_string}" fill="{fill_color}" />'