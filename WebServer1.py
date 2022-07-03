import http.server
from logging import Handler
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("",PORT), Handler)
print("Server at PORT   ", PORT)
httpd.serve_forever()