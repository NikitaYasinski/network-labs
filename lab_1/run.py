import sys
from MyHTTPServer import MyHTTPServer
import argparse


def get_args():
    argument_parser = argparse.ArgumentParser(description=f'Server settings')

    argument_parser.add_argument('-p', '--port', help='Server port', type=int, default=8000)
    argument_parser.add_argument('-ht', '--host', help='Server host', type=str, default='127.0.0.1')
    argument_parser.add_argument('-n', '--name', help='Server name', type=str, default='example.local')

    args = argument_parser.parse_args()

    return args


if __name__ == '__main__':
    args = get_args()

    serv = MyHTTPServer(args.host, args.port, args.name)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
