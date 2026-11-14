from png2svg.converter import convert


def test_convert_png_to_svg(tmp_path):
    input_file = "tests/sample.png"
    output_file = tmp_path / "output.svg"

    convert(input_file, output_file)

    assert output_file.exists()

    content = output_file.read_text()

    assert "<svg" in content
    assert "<polygon" in content
    assert "</svg>" in content