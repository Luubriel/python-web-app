import wsgiref.simple_server

def application(environ, start_response):
    # response
    response = b"Hello world"
    # status of response
    status = "200 OK"
    # response header
    headers = [("Content-Type", "text/html")]
    # setting status and headers
    start_response(status, headers)

    return [response]

if __name__ == "__main__":
    w_s = wsgiref.simple_server.make_server(
        host="localhost",
        port=8024,
        app=application
    )
    w_s.serve_forever()
