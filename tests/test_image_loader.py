from png2svg.image_loader import load_image
import pytest
from PIL import UnidentifiedImageError


def test_load_image():
    image = load_image("tests/sample.png")

    assert image.size == (100, 100)

def test_load_invalid_image(tmp_path):
    invalid_file = tmp_path / "invalid.png"
    invalid_file.write_text("This is not an image")

    with pytest.raises(UnidentifiedImageError):
        load_image(invalid_file)

def test_load_missing_image():
    with pytest.raises(FileNotFoundError):
        load_image("tests/nonexistent.png")