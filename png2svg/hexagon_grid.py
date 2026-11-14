
import math


def compute_next_coordinate(image_width, image_height, radius, column, row):
    x = 1.5 * radius * column
    y = math.sqrt(3) * radius * (row + 0.5 * (column % 2))

    if x > image_width or y > image_height:
        return (-1, -1)

    return (x, y)



def generate_hexagon_coordinates(image_width, image_height, radius):
    column = 0

    while True:
        first_coordinate = compute_next_coordinate(
            image_width, image_height, radius, column, 0
        )

        if first_coordinate == (-1, -1):
            break

        row = 0

        while True:
            coordinate = compute_next_coordinate(
                image_width, image_height, radius, column, row
            )

            if coordinate == (-1, -1):
                break

            yield coordinate
            row += 1

        column += 1
