import os
import wsgiref.simple_server
import urllib.parse
import json

ASSETS_DIR = 'assets'
CSS_DIR = 'css'
req = {}

def application(environ, start_response):
    # get requested path
    path = environ["PATH_INFO"]
    # get requested method
    method = environ["REQUEST_METHOD"]

    # content type of response
    content_type = "text/html"

    if path == "/":
        if method == "POST":
            # getting wsgi.input obj
            input_obj = environ["wsgi.input"]
            # length of body
            input_length = int(environ["CONTENT_LENGTH"])
            # getting body of wsgi.input obj
            # decoding to string
            body = input_obj.read(input_length).decode()

            # parsing body of form
            data = urllib.parse.parse_qs(body, keep_blank_values=True)
            # data of body in format
            ### personal note: that's a dictionary
            req = {
                "razao-social" : data["razao-social"][0],
                "nome-fantasia" : data["nome-fantasia"][0],
                "natureza-juridica" : data["natureza-juridica"][0]
            }
            # # adding to submission
            # forms_data.append(req)dd

            encode_data = json.dumps(req).encode('utf-8')

            response = b"Enviado com sucesso.\n"
            status = "200 OK"

        else:
            # read html file
            with open("form.html","r") as f:
                response = f.read().encode()
            status = "200 OK"

    elif path == "/favicon.ico":
        favicon_path = os.path.join(ASSETS_DIR, 'favicon.ico')
        if os.path.exists(favicon_path):
            with open(favicon_path, 'rb') as f: # rb = read in binary
                response = f.read()
            status = "200 OK"
            content_type = "image/x-icon"

    elif path == "/logo.png":
        logo_path = os.path.join(ASSETS_DIR, 'logo.png')
        if os.path.exists(logo_path):
            with open(logo_path, 'rb') as f:
                response = f.read()
            content_type = "image/x-icon"
            status = "200 OK"

    elif path == "/style.css":
        css_path = os.path.join(ASSETS_DIR, CSS_DIR, 'style.css')
        if os.path.exists(css_path):
            with open(css_path, 'rb') as f:
                response = f.read()
            content_type = "text/css"
            status = "200 OK"

    else:
        response = b"<h1>Page not found</h1>"
        status = "404 not found"

    headers = [
        ("Content-Type", content_type),
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
