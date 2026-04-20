from http.server import BaseHTTPRequestHandler, HTTPServer
import socket

PORT = 8080

print("STEP 1: File started")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("STEP 2: Request received")

        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()

        hostname = socket.gethostname()

        message = f"Hello from DevOps 🚀\nHostname: {hostname}"
        self.wfile.write(message.encode())


print("STEP 3: Before main")


if __name__ == "__main__":
    print("STEP 4: Inside main")

    server = HTTPServer(("0.0.0.0", PORT), Handler)

    print(f"STEP 5: Server running on port {PORT}")

    server.serve_forever()