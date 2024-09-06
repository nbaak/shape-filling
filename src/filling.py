#!/usr/bin/env python3
import argparse
import os
import pygame
import random
from PIL import Image

def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█'):
    """
    Prints a progress bar to the console.

    Parameters:
    - iteration (int): Current iteration (0-based)
    - total (int): Total iterations
    - prefix (str): Prefix string
    - suffix (str): Suffix string
    - decimals (int): Positive number of decimals in percent complete
    - length (int): Character length of the bar
    - fill (str): Bar fill character
    """
    percent = f"{100 * (iteration / float(total)):.{decimals}f}"
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% [{iteration}/{total}] {suffix}', end='\r')
    # Print a new line when complete
    if iteration == total: 
        print()

def black_to_alpha(surface):
    """Convert black pixels to transparent on a Pygame surface."""
    surface = surface.convert_alpha()  # Ensure the surface has an alpha channel
    width, height = surface.get_size()
    
    for x in range(width):
        for y in range(height):
            pixel = surface.get_at((x, y))
            # If the pixel is black or near black, make it transparent
            if pixel.r < 20 and pixel.g < 20 and pixel.b < 20:
                surface.set_at((x, y), pygame.Color(0, 0, 0, 0))
    
    return surface

def generate_image(image_path, new_file_path, convert_black_to_alpha):
    """Generate the image with random circles and optionally convert black pixels to transparent."""
    image = Image.open(image_path)
    image_width, image_height = image.size

    # Initialize Pygame
    pygame.init()
    size = width, height = image_width, image_height
    window = pygame.display.set_mode(size)

    # Convert the PIL image to a format Pygame can use
    mode = image.mode
    size = image.size
    data = image.tobytes()
    image_in = pygame.image.fromstring(data, size, mode)

    # Create a mask from the non-transparent pixels of the PIL image
    mask = [(x, y) for x in range(image_width) for y in range(image_height)
            if image.getpixel((x, y))[0]]
    
    random.shuffle(mask)
    mask_length = len(mask)

    drawn_circles = []
    running = True
    clock = pygame.time.Clock()
    iteration = 0
    
    # Circle Radii
    circle_min_radius = 5
    circle_max_radius = 20

    while running and mask:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                running = False
            
        pos = pygame.Vector2(mask.pop())
        radius = random.randint(circle_min_radius, circle_max_radius)

        overlap = False
        for pos2, rad2 in drawn_circles:
            if pos.distance_to(pos2) - radius - rad2 < 0:
                overlap = True
                break

        if not overlap:
            pygame.draw.circle(window, pygame.Color('green'), pos, radius, 3)
            drawn_circles.append((pos, radius))
        
        pygame.display.flip()
        print_progress_bar(iteration, mask_length, prefix='Progress:', suffix='Complete', length=50)
        iteration += 1
        clock.tick(60)

    pygame.display.flip()

    # Apply black to alpha if the flag is set
    if convert_black_to_alpha:
        window = black_to_alpha(window)
        
    pygame.image.save(window, new_file_path)
    print(f"Output image saved as {new_file_path}")

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description='Process an image and create a new image with circles drawn.')
    parser.add_argument('-f', '--file', required=True, help='Path to the input image file')
    parser.add_argument('-n', '--name', help='Optional new file name. Defaults to <input_file>_out.png if not provided.')
    parser.add_argument('-bta', '--black_to_alpha', action='store_true', help='Convert black pixels to alpha (transparent) in the output image.')
    
    return parser.parse_args()

def main():
    args = parse_arguments()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    image_path = os.path.join(script_dir, args.file)
    if not os.path.isfile(image_path):
        print(f"Error: The file '{image_path}' does not exist.")
        return
    
    if args.name:
        new_file_path = os.path.join(script_dir, args.name)
    else:
        suffix = '_out'
        directory, filename = os.path.split(image_path)
        base, ext = os.path.splitext(filename)
        new_filename = f"{base}{suffix}{ext}"
        new_file_path = os.path.join(directory, new_filename)

    generate_image(image_path, new_file_path, args.black_to_alpha)

if __name__ == "__main__":
    main()
