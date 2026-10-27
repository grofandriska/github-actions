from http.server import BaseHTTPRequestHandler, HTTPServer


def greeting():
    return "Hello, CSK!"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = (greeting() + "\n").encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    HTTPServer(("", 8080), Handler).serve_forever()
