# Pygame Circle Drawing with Progress Bar

![Python with circles](python_out.png)

This Python project uses Pygame and Pillow libraries to draw random circles on a window, based on an input image's non-transparent pixels. The script also provides a real-time console progress bar to indicate the completion status.

## Requirements

- Python 3.7 or higher
- Pygame library
- Pillow (PIL) library

## Installation

1. Install Python from [python.org](https://www.python.org/).
2. Install the required libraries:

```bash
pip install pygame
pip install Pillow
```

## Usage

1. Place your input image in the same directory as the script and rename it to `image_in.png`.
2. Run the script:

```bash
python filling.py
```

1. The program will open a Pygame window and start drawing random circles on non-transparent pixels of the input image.
2. The console will display a progress bar showing the completion status.
3. Once the process is complete, an output image `image_out.png` will be saved in the same directory.

## Features

- Draws random circles on a Pygame window.
- Uses non-transparent pixels from an input image.
- Displays a real-time progress bar in the console.
- Saves the final image with drawn circles.

## Code Overview

- **Pillow** is used to read the image and determine pixel transparency.
- **Pygame** is used to create a window and draw circles.
- A progress bar function updates in the console to show progress.

## Customization

- Modify the `image_path` variable to use a different input image.
- Adjust circle radius range in the `radius` variable.
- Change the color of the circles by updating the `pygame.draw.circle` call.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
