import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from png2svg.converter import convert

    return convert, mo


@app.cell
def _(mo):
    file_picker = mo.ui.file(
        filetypes=[".png"],
        multiple=False,
        label="Select a PNG image"
    )

    file_picker
    return (file_picker,)


@app.cell
def _(convert, file_picker):
    import os

    if file_picker.value:
        uploaded_file = file_picker.value[0]

        if not os.path.exists("output images"):
            os.mkdir("output images")

        with open("input.png", "wb") as file:
            file.write(uploaded_file.contents)

        convert("input.png", "output images/result.svg")

        os.remove("input.png")

        message = "successfully converted! svg saved in `output images/result.svg`."

    print(message)
    return


if __name__ == "__main__":
    app.run()
