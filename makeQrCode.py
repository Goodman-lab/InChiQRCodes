#!/usr/bin/env python3

import sys
sys.path.append('/home/jmg11/.local/lib/python3.5/site-packages')
import qrcode
from pathlib import Path

def makeQrCode(InChiCode):
    #Get the path to write the image to, based of the content of the qr code,
    #to avoid duplication problems
    prefix = "./qr/"
    qrPath = "{}{}.png".format(prefix, InChiCode)
    txtPath = "{}{}.txt".format(prefix, InChiCode)

    if Path(qrPath).exists():
        #If it exists, update the date, but don't remake it
        Path(qrPath).touch()
        os.remove(txtPath)
    else:
        #If it doesn't exist, generate and save it
        img = qrcode.make("https://pubchem.ncbi.nlm.nih.gov/#query=inchikey="+InChiCode)
        img.save(qrPath, "PNG")
        os.remove(txtPath)






if __name__ == "__main__":
    from sys import argv

    if len(argv) >= 2:
        #If there are enough arguments, make the qr code, and exit with cleanly
        #print("creating qrinchi")
        #print('\n'.join(sys.path))
        #print('\n')
        #with open("qr/"+argv[1]+".ttt","w+") as f:
        #    f.write(argv[1]);

        makeQrCode(argv[1])
        exit(0)
    else:
        #If there aren't enough arguments, make the qr code, and exit
        #with an error code
        print("No content provided")
        exit(1)
