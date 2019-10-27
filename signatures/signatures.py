counter = 1


def getPage(left, right):
    global counter
    print(f"{counter}: {{{left}, {right}}}")
    counter += 1


def printSignature(start, size):
    size *= 4
    for i in range(size // 2):
        if i % 2:
            getPage(start + i, start + size - i - 1)
        else:
            getPage(start + size - i - 1, start + i)


def printBook(signatures, sig_size):
    for i in range(signatures):
        printSignature(i * sig_size * 4 + 1, sig_size)
