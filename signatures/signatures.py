import os
from os import path
from PIL import Image, ImageFont, ImageDraw


def getPage(image, left, right, padding, pos, font, color, file):
    canvas = ImageDraw.Draw(image)

    w, h = image.size

    # Left Number
    width, height = canvas.textsize(str(left), font=font)

    x = padding
    y = padding
    if pos == 'bot':
        y = h - y - height

    canvas.text((x, y), str(left), fill=color, font=font)

    # Right Number

    width, height = canvas.textsize(str(right), font=font)

    x = w - width - padding
    y = padding
    if pos == 'bot':
        y = h - y - height

    canvas.text((x, y), str(right), fill=color, font=font)

    print(f"{file}: [{left}, {right}]")

    del canvas

    image.save(file)


def printSignature(image, start, size, padding, pos, font, color, folder):
    size *= 4
    for i in range(size // 2):
        left = start + i
        right = start + size - i - 1

        # Swap the left and the right numbering
        if not i % 2:
            left, right = right, left
        
        f = path.join(folder, f"{i + start // 2 + 1}.png")

        getPage(image.copy(), left, right, padding, pos, font, color, f)


def printBook(papers, signatures, image, pos, padding, size, font, output, color, **kwargs):
    image_file = image
    font_file = font

    f, f_ext = path.splitext(font_file)
    if not f_ext:
        f_ext = '.ttf'
    font_file = ''.join([f, f_ext])

    if output is None:
        output = path.splitext(image)[0]

    try:
        font = ImageFont.truetype(font=font_file, size=size)
    except IOError:
        print(f"Could not find the font '{font_file}'.")
        exit()

    try:
        image = Image.open(image_file)
    except IOError as e:
        print(e)
        exit()

    if not os.path.isdir(output):
        os.mkdir(output)

    for i in range(signatures):
        printSignature(image, i * papers * 4 + 1, papers, padding, pos, font, color, output)
