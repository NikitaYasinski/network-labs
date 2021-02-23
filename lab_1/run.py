import sys
from MyHTTPServer import MyHTTPServer
import argparse


def get_args():
    argument_parser = argparse.ArgumentParser(description=f'Server settings')

    argument_parser.add_argument('-p', '--port', help='Server port', type=int, default=8000)
    argument_parser.add_argument('-ht', '--host', help='Server host', type=str, default='127.0.0.1')
    argument_parser.add_argument('-n', '--name', help='Server name', type=str, default='example.local')
    argument_parser.add_argument('-head', '--header', help='Add default headers to response', type=bool, default=0)

    args = argument_parser.parse_args()

    return args


if __name__ == '__main__':
    args = get_args()
    headers = {}

    if args.header:
        with open("headers.txt") as f:
            for line in f:
                (key, val) = line.split()
                headers[key] = val

    serv = MyHTTPServer(args.host, args.port, args.name, headers)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
