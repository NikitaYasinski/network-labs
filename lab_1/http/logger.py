import logging


class Logger:
    def __init__(self):
        new_file = open('log.txt', 'w+')
        new_file.close()

        log_format = '%(message)s'
        logging.basicConfig(filename='log.txt', filemode='a', format=log_format, level=logging.INFO)

        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter(log_format)
        console.setFormatter(formatter)

        logging.getLogger('').addHandler(console)

    def log_response(self, response):
        status = f'\nHTTP/1.1 {response.status} {response.reason}'
        logging.info(status)

        if response.headers:
            logging.info('Headers: ')
            for key, value in response.headers.items():
                logging.info(f'{key}: {value}\r\n')

        if response.body:
            logging.info('Body:')
            logging.info(response.body.decode('iso-8859-1'))
