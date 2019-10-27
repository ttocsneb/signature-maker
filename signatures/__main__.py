import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('papers', help="Papers per Signature", type=int)
parser.add_argument('signatures', help="Number of Signatures", type=int)

args = parser.parse_args()

from signatures import printBook

printBook(args.signatures, args.papers)
