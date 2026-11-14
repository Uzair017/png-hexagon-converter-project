from png2svg.svg_generator import generate_hexagon


def test_generate_hexagon():
    svg = generate_hexagon((15, 15), 10, (255, 0, 0))

    assert "<polygon" in svg
    assert 'fill="#ff0000"' in svg