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

    x = padding[0]
    y = padding[1]
    if pos == 'bot':
        y = h - y - height

    if mask is not None:
        canvas.rectangle([(x, y), (x + width, y + height)], fill=mask)
    canvas.text((x, y), left, fill=color, font=font)

    # Right Number

    width, height = canvas.textsize(right, font=font)

    x = w - width - padding[0]
    y = padding[1]
    if pos == 'bot':
        y = h - y - height

    if mask is not None:
        canvas.rectangle([(x, y), (x + width, y + height)], fill=mask)
    canvas.text((x, y), right, fill=color, font=font)

    print(f"{file}: [{left}, {right}]")

    del canvas

    image.save(file)


def printSignature(image, start, size, file, **kwargs):
    size *= 4
    for i in range(size // 2):
        left = start + i
        right = start + size - i - 1

        # Swap the left and the right numbering for double sided printing
        if not i % 2:
            left, right = right, left
        
        f = file % (i + start // 2 + 1)

        getPage(image.copy(), left, right, f, **kwargs)


def printBook(papers, signatures, image, size, font, output, padding: str, **kwargs):
    image_file = image
    font_file = font
    padding_str = padding

    # Padding Size

    try:
        if 'x' in padding_str.lower():
            padding = [int(i) for i in padding_str.lower().split('x')]
        else:
            padding = [int(padding_str)] * 2
    except ValueError:
        print(f"{padding_str} is not valid.  You can use either axb or a where a and b are integers.")
        exit()

    # Font

    f, f_ext = path.splitext(font_file)
    if not f_ext:
        f_ext = '.ttf'
    font_file = ''.join([f, f_ext])

    # Output Format

    if output is None:
        output_dir = path.splitext(image)[0]
        o_f = "%03d.png"
    else:
        o_f = path.basename(output)
        output_dir = path.dirname(output)

        if not o_f:
            o_f = "%03d.png"
    
    output = path.join(output_dir, o_f)

    try:
        output % 5
    except TypeError:
        print(f"{output} is not formatted properly.  the filename should include a string formatter like '%02d'")
        exit()

    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    # Font

    try:
        font = ImageFont.truetype(font=font_file, size=size)
    except IOError:
        print(f"Could not find the font '{font_file}'.")
        exit()

    # Image

    try:
        image = Image.open(image_file)
    except IOError as e:
        print(e)
        exit()

    # Process

    for i in range(signatures):
        printSignature(image, i * papers * 4 + 1, papers, output, font=font, padding=padding, **kwargs)
