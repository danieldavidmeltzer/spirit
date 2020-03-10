import string

from PIL import Image


def print_ascii_art(binary_image):
    image = Image.open(binary_image)
    # resize the image
    width, height = image.size
    aspect_ratio = height / width
    width = 200
    height = int(aspect_ratio * width)
    image = image.resize((width, height))
    image = image.convert('L')
    pixels = image.getdata()

    # a-zA-Z
    chars = string.ascii_lowercase
    jumps = len(chars) / 255
    ascii_art = [chars[max(min(int(grey_value * jumps), len(chars) - 1), 0)]
                 for grey_value in pixels]
    lines_number = int(len(ascii_art) / width)
    ascii_lines = []
    for line in range(lines_number):
        char_index = line * width
        ascii_lines.append(''.join(ascii_art[char_index:char_index + width]))
    ascii_image = "\n".join(ascii_lines)
    print(ascii_image)
