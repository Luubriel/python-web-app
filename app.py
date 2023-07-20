import os
import wsgiref.simple_server

ASSETS_DIR = 'assets'
CSS_DIR = 'css'

def application(environ, start_response):
    path = environ["PATH_INFO"]

    if path == "/":
        with open("form.html","r") as f:
            response = f.read().encode()
        status = "200 OK"

    elif path == "/favicon.ico":
        favicon_path = os.path.join(ASSETS_DIR, 'favicon.ico')
        if os.path.exists(favicon_path):
            with open(favicon_path, 'rb') as f: # rb = read in binary
                favicon_content = f.read()

            status = "200 OK"
            headers = [("Content-Type", "image/x-icon")]
            start_response(status, headers)
            return [favicon_content]

    elif path == "/logo.png":
        logo_path = os.path.join(ASSETS_DIR, 'logo.png')
        if os.path.exists(logo_path):
            with open(logo_path, 'rb') as f: # rb = read in binary
                logo_content = f.read()

            status = "200 OK"
            headers = [("Content-Type", "image/x-icon")]
            start_response(status, headers)
            return [logo_content]

    elif path == "/style.css":
        css_path = os.path.join(ASSETS_DIR, CSS_DIR, 'style.css')
        if os.path.exists(css_path):
            with open(css_path, 'rb') as f:
                css_content = f.read()

            status = "200 OK"
            headers = [("Content-Type", "text/css")]
            start_response(status, headers)
            return [css_content]

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
