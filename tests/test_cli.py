from png2svg.cli import main


def test_cli_conversion(tmp_path):
    input_file = "tests/sample.png"
    output_file = tmp_path / "output.svg"

    main([input_file, str(output_file)])

    assert output_file.exists()

    content = output_file.read_text()

    assert "<svg" in content
    assert "<polygon" in content
    assert "</svg>" in content

def test_cli_custom_radius(tmp_path):
    input_file = "tests/sample.png"
    output_file = tmp_path / "output.svg"

    main([input_file, str(output_file), "--radius", "25"])

    assert output_file.exists()