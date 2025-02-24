from http.server import SimpleHTTPRequestHandler, HTTPServer

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With, Content-Type")
        SimpleHTTPRequestHandler.end_headers(self)

if __name__ == "__main__":
    port = 8000
    httpd = HTTPServer(("localhost", port), CORSRequestHandler)
    print(f"Serving HTTP on localhost, port {port} (http://localhost:{port}/)...")
    httpd.serve_forever()
