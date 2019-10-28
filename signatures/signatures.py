import os
from os import path
from PIL import Image, ImageFont, ImageDraw


def getPage(image, left, right, file, padding, pos, font, color, mask, format):
    canvas = ImageDraw.Draw(image)

    left = format % left
    right = format % right

    w, h = image.size

    # Left Number
    width, height = canvas.textsize(left, font=font)

    x = padding
    y = padding
    if pos == 'bot':
        y = h - y - height

    if mask is not None:
        canvas.rectangle([(x, y), (x + width, y + height)], fill=mask)
    canvas.text((x, y), left, fill=color, font=font)

    # Right Number

    width, height = canvas.textsize(right, font=font)

    x = w - width - padding
    y = padding
    if pos == 'bot':
        y = h - y - height

    if mask is not None:
        canvas.rectangle([(x, y), (x + width, y + height)], fill=mask)
    canvas.text((x, y), right, fill=color, font=font)

    print(f"{file}: [{left}, {right}]")

    del canvas

    image.save(file)


def printSignature(image, start, size, folder, **kwargs):
    size *= 4
    for i in range(size // 2):
        left = start + i
        right = start + size - i - 1

        # Swap the left and the right numbering
        if not i % 2:
            left, right = right, left
        
        f = path.join(folder, f"{i + start // 2 + 1}.png")

        getPage(image.copy(), left, right, f, **kwargs)


def printBook(papers, signatures, image, size, font, output, **kwargs):
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
        printSignature(image, i * papers * 4 + 1, papers, output, font=font, **kwargs)
