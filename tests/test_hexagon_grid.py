
import math
import pytest

from png2svg.hexagon_grid import compute_next_coordinate
from png2svg.hexagon_grid import generate_hexagon_coordinates

def test_first_coordinate():
    coordinate = compute_next_coordinate(900, 506, 15, 0, 0)

    assert coordinate == (0, 0)


def test_next_column_coordinate():
    coordinate = compute_next_coordinate(900, 506, 15, 1, 0)

    expected = (22.5, (math.sqrt(3) * 15) / 2)

    assert coordinate == pytest.approx(expected)


def test_next_row_coordinate():
    coordinate = compute_next_coordinate(900, 506, 15, 0, 1)

    expected = (0, math.sqrt(3) * 15)

    assert coordinate == pytest.approx(expected)


def test_coordinate_outside_image():
    coordinate = compute_next_coordinate(900, 506, 15, 100, 100)

    assert coordinate == (-1, -1)




def test_generate_hexagon_coordinates():
    coordinates = list(generate_hexagon_coordinates(30, 30, 10))

    expected = [
        (0, 0),
        (0, math.sqrt(3) * 10),
        (15, (math.sqrt(3) * 10) / 2),
        (15, (math.sqrt(3) * 10) * 1.5),
        (30, 0),
        (30, math.sqrt(3) * 10),
    ]

    assert len(coordinates) == len(expected)

    for actual, expected_coordinate in zip(coordinates, expected):
        assert actual == pytest.approx(expected_coordinate)
