import os
import wsgiref.simple_server

STATIC_DIR = 'static'

def application(environ, start_response):
    path = environ["PATH_INFO"]

    if path == "/":
        with open("login.html","r") as f:
            response = f.read().encode()
        status = "200 OK"
    elif path == "/favicon.ico":
        favicon_path = os.path.join(STATIC_DIR, 'favicon.ico')
        if os.path.exists(favicon_path):
            with open(favicon_path, 'rb') as f: # rb = read in binary
                favicon_content = f.read()
            status = "200 OK"
            headers = [("Content-Type", "image/x-icon")]
            start_response(status, headers)
            return [favicon_content]
    else:
        response = b"<h1>Page not found</h1>"
        status = "404 not found"

    headers = [
        ("Content-Type", "text/html"),
        ("Content-Length", str(len(response)))
    ]

    start_response(status, headers)

    return [response]

if __name__ == "__main__":
    w_s = wsgiref.simple_server.make_server(
        host="localhost",
        port=8024,
        app=application
    )
    w_s.serve_forever()
