from http.server import HTTPServer, BaseHTTPRequestHandler

class echoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write('Hai, Selamat Datang di Website Kevin'.encode())


def main():
    PORT = 9000
    server = HTTPServer(('', PORT), echoHandler)
    print('Server Running on port %s' % PORT)
    server.serve_forever()


if __name__ == '__main__':
    main()