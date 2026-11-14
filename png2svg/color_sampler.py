import math


def sample_color(image, coordinate, radius):
    center_x, center_y = coordinate

    red_total = 0
    green_total = 0
    blue_total = 0
    pixel_count = 0

    for x in range(image.width):
        for y in range(image.height):
            dx = x - center_x
            dy = y - center_y

            if (
                abs(dx) <= radius
                and abs(dy) <= (math.sqrt(3) * radius / 2)
                and (math.sqrt(3) * abs(dx) + abs(dy)) <= math.sqrt(3) * radius
            ):
                red, green, blue = image.getpixel((x, y))

                red_total += red
                green_total += green
                blue_total += blue
                pixel_count += 1

    if pixel_count == 0:
        return (0, 0, 0)

    average_red = round(red_total / pixel_count)
    average_green = round(green_total / pixel_count)
    average_blue = round(blue_total / pixel_count)

    return (average_red, average_green, average_blue)