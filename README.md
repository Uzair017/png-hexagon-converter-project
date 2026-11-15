# PNG to SVG Hexagon Converter

A Python project that converts low-resolution png images into svg images using a hexagonal grid.


The program takes a PNG image, goes through it using a hexagonal grid, and samples the pixels inside each hexagon. After that it calculates the average rgb colour of those pixels and uses that colour to generate a hexagon in the svg file.

At the end, all the generated hexagons are combined into one SVG image.
I have used marimo to make a simple interface where the user can select a png image and convert it into an svg file.


# Project Structure

`png2svg/` -> contains the main python files for image loading, hexagonal grid, colour sampling, svg generation and conversion.
`tests/` -> contains the test files for checking different parts of the project.
`.github/` -> contains the gitHub actions workflow for running the tests.
`app.py` -> marimo notebook for selecting a PNG image and converting it into an SVG file.


# Installation
First clone the repository from GitHub:

git clone https://github.com/Uzair017/png-hexagon-converter-project.git

Go inside the project folder:

cd png-hexagon-converter-project

Create and activate a virtual environment:

python -m venv .venv

.venv\Scripts\activate

Install the required libraries:

pip install pillow pytest marimo


# Usage
To convert a PNG image using the command line:

python -m png2svg.cli input.png output.svg

For marimo interface. Run it using:

marimo edit app.py

Select a png image, and the converted svg will be saved in the output images folder.


# Running Tests
To run the tests, use:

python -m pytest

This will run the test cases for the different parts of the project.


# GitHub Actions
I have used github Actions to automatically run the tests when code is pushed to the repository or a pull request is created.