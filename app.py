import wsgiref.simple_server

def application(environ, start_response):
    path = environ["PATH_INFO"]

    if path == "/":
        with open("login.html","r") as f:
            response = f.read().encode()
        status = "200 OK"
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
