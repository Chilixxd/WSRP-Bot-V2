from http.server import HTTPServer, BaseHTTPRequestHandler
import os
#super cool discord shit


class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            #TODO open 404 page!
            self.path = '/404.html'
            self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

httpd = HTTPServer(('localhost', 6969), Serv)
print("Server has started")
httpd.serve_forever()