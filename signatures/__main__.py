import argparse

parser = argparse.ArgumentParser(description='Number Pages for a book')

parser.add_argument('papers', help="Papers per Signature", type=int)
parser.add_argument('signatures', help="Number of Signatures", type=int)
parser.add_argument('image', help="Background image for each paper", type=str)

parser.add_argument('-t', '--top', dest='pos', help='Place the numbering on the top of the page', action='store_const', const='top', default='bot')
parser.add_argument('-b', '--bottom', dest='pos', help='Place the numbering on the bottom of the page (default)', action='store_const', const='bot')
parser.add_argument('-p', '--padding', dest='padding', metavar='px', help='padding from the edge of the numbers', default="16")
parser.add_argument('-s', '--size', dest='size', metavar='pt', help='Size of the font', type=int, default=12)
parser.add_argument('-f', '--font', dest='font', metavar='font', help='Font to use', type=str, default="arial")
parser.add_argument('-o', '--output', dest='output', metavar='directory', help='output format ex: "out/%%03d.png"')
parser.add_argument('-c', '--color', dest='color', metavar='color', help='set the color of the text', default='rgb(0, 0, 0)')
parser.add_argument('-m', '--mask', dest='mask', metavar='color', help='Add a background to mask the image.')
parser.add_argument('--format', dest='format', metavar='fmt', help='Set the format string of the numbers', default="%d")

args = parser.parse_args()

from signatures import printBook

printBook(**vars(args))
