import http.server
import socketserver

PORT = 8000
DIRECTORY = "."

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

# Imposta il server
handler = MyHttpRequestHandler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Server avviato su http://localhost:{PORT}")
    httpd.serve_forever()
