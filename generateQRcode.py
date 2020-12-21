#!/usr/bin/env python3
from io import BytesIO
import qrcode

def getQRBytes(content):
    img = qrcode.make(content)
    buf = BytesIO()
    img.save(buf, "PNG")
    contents = buf.getvalue()
    return contents

def printHexFromBytes(byteContent):
    print("".join("{:02x}".format(x) for x in byteContent))

def run(content):
    qrCode = getQRBytes(content)
    printHexFromBytes(qrCode)

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(content=argv[1])
    else:
        print("No content provided")
