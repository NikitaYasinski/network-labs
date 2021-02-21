import socket
from http.request import Request
from http.response import Response
from http.httpError import HTTPError
from http.logger import Logger
from email.parser import Parser
import os
import re

MAX_LINE = 64 * 1024
MAX_HEADERS = 100
DIRECTORY_WITH_FILES_PATH = './files'

class MyHTTPServer:
    def __init__(self, host, port, server_name):
        self._host = host
        self._port = port
        self._server_name = server_name
        self._logger = Logger()

    def serve_forever(self):
        serv_sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
            proto=0
        )

        try:
            serv_sock.bind((self._host, self._port))
            serv_sock.listen()

            while True:
                conn, _ = serv_sock.accept()
                try:
                    self.serve_client(conn)
                except Exception as e:
                    if e.errno not in (errno.ECONNRESET, errno.ECONNABORTED, errno.EPIPE):
                        raise
                    print('Client serving failed', e)
        finally:
            serv_sock.close()

    def serve_client(self, conn):
        try:
            req = self.parse_request(conn)
            resp = self.handle_request(req)
            self.send_response(conn, resp)
        except ConnectionResetError:
            conn = None
        except Exception as e:
            self.send_error(conn, e)

        if conn:
            req.rfile.close()
            conn.close()

    def parse_request(self, conn):
        rfile = conn.makefile('rb')

        method, target, ver = self.parse_request_line(rfile)
        headers = self.parse_headers(rfile)
        host = headers.get('Host')
        if not host:
            raise HTTPError(400, 'Bad request', 'Host header is missing')
        if host not in (self._server_name, f'{self._host}:{self._port}'):
            raise HTTPError(404, 'Not found')

        return Request(method, target, ver, headers, rfile)

    def parse_headers(self, rfile):
        headers = []
        while True:
            line = rfile.readline(MAX_LINE + 1)
            if len(line) > MAX_LINE:
                raise HTTPError(494, 'Request header too large')

            if line in (b'\r\n', b'\n', b''):
                break

            headers.append(line)
            if len(headers) > MAX_HEADERS:
                raise HTTPError(494, 'Too many headers')

        sheaders = b''.join(headers).decode('iso-8859-1')
        return Parser().parsestr(sheaders)

    def parse_request_line(self, rfile):
        raw = rfile.readline(MAX_LINE + 1)
        if len(raw) > MAX_LINE:
            raise HTTPError(400, 'Bad request', 'Request line is too long')

        req_line = str(raw, 'iso-8859-1')
        words = req_line.split()
        if len(words) != 3:
            raise HTTPError(400, 'Bad request', 'Malformed request line')

        method, target, ver = words
        if ver != 'HTTP/1.1':
            raise HTTPError(505, 'HTTP Version Not Supported')
        return method, target, ver

    def handle_request(self, req):
        if req.method == 'GET':
            return self.handle_get(req)

        if req.method == 'POST':
            return self.handle_post(req)

        if req.method == 'OPTIONS':
            return self.handle_options(req)

    def handle_get(self, req):
        filename = req.target
        file_path = 'files/' + filename

        if not os.path.isfile(file_path):
            raise HTTPError(404, 'Not found')

        try:
            fin = open(file_path)
            body = fin.read()
            fin.close()

            body = body.encode('utf-8')
            headers = {'Content-Length': len(body)}
            return Response(200, 'OK', headers, body)

        except FileNotFoundError:
            raise HTTPError(404, 'Not found')

    def get_property(self, rfile, separator):
        decoded_separator = separator.decode('iso-8859-1').strip().replace('-', '')
        property = []
        while True:
            line = rfile.readline(MAX_LINE + 1)
            decoded_line = line.decode('iso-8859-1')
            if decoded_separator.strip() == decoded_line.replace('-', '').strip():
                return property
            else:
                property.append(line)

    def handle_post(self, req):
        separator = req.rfile.readline(MAX_LINE + 1)
        data = []

        try:
            property = self.get_property(req.rfile, separator)
            data.append(property)

            for item in data:
                content_disposition = item[0].decode('iso-8859-1')
                content_type = item[1].decode('iso-8859-1')
                file_data = b''.join(item[3:]).decode('iso-8859-1')

                pattern = "\"(.*?)\""
                filename_string = content_disposition.split('filename=')[1]
                parsed_filename = re.search(pattern, filename_string).group(1)

                try:
                    file = open(f'{DIRECTORY_WITH_FILES_PATH}/{parsed_filename}', "w+")
                    file.write(file_data)
                    file.close()
                except CreateFileError:
                    raise HTTPError(500, 'Internal Server Error')

            return Response(201, 'OK')
        except Error:
            raise HTTPError(403, 'Post error')

    def handle_options(self, req):
        pass

    def send_response(self, conn, resp):
        wfile = conn.makefile('wb')
        status_line = f'HTTP/1.1 {resp.status} {resp.reason}\r\n'
        wfile.write(status_line.encode('iso-8859-1'))
        self._logger.log_response(resp)

        if resp.headers:
            for key, value in resp.headers.items():
                header_line = f'{key}: {value}\r\n'
                wfile.write(header_line.encode('iso-8859-1'))

        wfile.write(b'\r\n')

        if resp.body:
            wfile.write(resp.body)

        wfile.flush()
        wfile.close()

    def send_error(self, conn, err):
        try:
            status = err.status
            reason = err.reason
            body = (err.body or err.reason).encode('utf-8')
        except:
            status = 500
            reason = b'Internal Server Error'
            body = b'Internal Server Error'
        resp = Response(status, reason, {'Content-Length': len(body)}, body)
        self.send_response(conn, resp)
