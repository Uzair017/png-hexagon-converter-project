from png2svg.svg_writer import write_svg


def test_write_svg(tmp_path):
    output_file = tmp_path / "output.svg"

    hexagons = [
        '<polygon points="10,10 20,10 15,20" fill="#ff0000" />'
    ]

    write_svg(hexagons, 100, 100, output_file)

    content = output_file.read_text()

    assert '<svg' in content
    assert 'width="100"' in content
    assert 'height="100"' in content
    assert '<polygon' in content
    assert '</svg>' in content