#!/usr/bin/env python3

if __name__ == "__main__":
    from sys import argv

    if len(argv) >= 2:
        #If there are enough arguments, make the qr code, and exit with cleanly
        with open("qr/"+argv[1]+".txt","w+") as f:
            f.write("Hello");
        exit(0)
    else:
        #If there aren't enough arguments, make the qr code, and exit
        #with an error code
        print("No content provided")
        exit(1)
