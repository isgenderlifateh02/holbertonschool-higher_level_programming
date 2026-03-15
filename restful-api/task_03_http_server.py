#!/usr/bin/python3
"""
A simple HTTP server using http.server module to handle
different endpoints and serve JSON data.
"""
import http.server
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    HTTP Request Handler for our simple API.
    """

    def do_GET(self):
        """
        Handles GET requests and routes them to specific endpoints.
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == '/info':
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode("utf-8"))

        else:
            # DİQQƏT: Əgər "404 Not Found" keçmədisə, mətni buna çeviririk:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run_server():
    """Starts the HTTP server on port 8000."""
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    print("Starting server on port 8000...")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
