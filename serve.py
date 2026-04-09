import http.server, socketserver, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(('', 8091), handler) as httpd:
    print("Serving on http://localhost:8091")
    httpd.serve_forever()
