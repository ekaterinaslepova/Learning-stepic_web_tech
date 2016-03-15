
def application(environ, start_response):
    response_body = '\n'.join(environ['QUERY_STRING'].split('&'))

    status = '200 OK'

    response_headers = [('Content-Type', 'text/plain')]

    start_response(status, response_headers)

    return [response_body]

