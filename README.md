# ASCII Art Generator

This Python script converts an image into ASCII art. It resizes the image, converts it to grayscale, maps the grayscale values to ASCII characters, and outputs the resulting ASCII art.

## Features

- Resize the image while maintaining the aspect ratio.
- Convert the image to grayscale.
- Map pixels to ASCII characters for a visual representation.
- Output the ASCII art to the console.
- Save the ASCII art to a text file.

## Requirements

- Python 3.x
- Pillow library

## Installation

1. Ensure you have Python 3 installed. You can download it from [python.org](https://www.python.org/downloads/).

2. Install the Pillow library using pip:

    ```bash
    pip install Pillow
    ```

## Usage

1. Download or clone this repository.

2. Place the image you want to convert into the same directory as the script or provide the full path to the image when prompted.

3. Run the script:

    ```bash
    python ascii_art.py
    ```

4. Enter the path to your image when prompted.

5. The ASCII art will be printed to the console and saved to `ascii_image.txt`.

## Example

Here is an example of how to use the script:

```bash
$ python ascii_art.py
Enter a valid pathname for the image: path/to/your/image.jpg
Processing image...
