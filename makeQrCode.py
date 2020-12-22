#!/usr/bin/env python3
import qrcode

from pathlib import Path

def makeQrCode(InChiCode):
    #Get the path to write the image to, based of the content of the qr code,
    #to avoid duplication problems
    prefix = "qr/"
    qrPath = "{}{}.png".format(prefix, InChiCode)

    if Path(qrPath).exists():
        #If it exists, update the date, but don't remake it
        Path(qrPath).touch()
    else:
        #If it doesn't exist, generate and save it
        img = qrcode.make(InChiCode)
        img.save(qrPath, "PNG")

if __name__ == "__main__":
    from sys import argv

    if len(argv) >= 2:
        #If there are enough arguments, make the qr code, and exit with cleanly
        makeQrCode(argv[1])
        exit(0)
    else:
        #If there aren't enough arguments, make the qr code, and exit
        #with an error code
        print("No content provided")
        exit(1)
