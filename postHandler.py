#!/usr/bin/env python3



from http.server import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep


class Handler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        BaseHTTPRequestHandler.__init__(self, request, client_address, server)
        self.request_id = ""


    def _setPngResponse(self):
        self.send_response(200)
        self.send_header("Content-type", "image/png")
        self.end_headers()

    def do_GET(self):

        try:
            #We only ever want to serve these pages, so close ourselves from
            #attacks to view other files by explicit enumeration, and ignoring
            #every other path
            if self.path == "index.html" or self.path == "/":
                print(self.path)
                #Make headers
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                #Read content to serve
                with open("./index.html","r") as indexFile:
                    content = indexFile.read()
            elif self.path == "styles.css":
                #Make headers
                self.send_response(200)
                self.send_header("Content-type", "text/css")
                #Read content to serve
                with open("./styles.css","r") as stylesFile:
                    content = stylesFile.read()
            else:
                #Requested file not of a valid format, so 404
                raise IOError

            self.end_headers()
            self.wfile.write(content.encode("utf-8"))

        except IOError:
            self.send_error(404,"File Not Found: {}".format(self.path))

    #def do_POST(self):
        #content_length = int(self.headers["Content-Length"]) # <--- Gets the size of data
        #post_data = self.rfile.read(content_length) # <--- Gets the data itself
        #self._setHtmlResponse()
        #self.wfile.write("POST request for {}".format(self.path).encode("utf-8"))



def run(port=8080):
    serverAddress = ("", port)
    httpd = HTTPServer(serverAddress, Handler)
    print("Starting server on port {}".format(port))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    print("Killing server due to keyboard interrupt")
    httpd.server_close()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
