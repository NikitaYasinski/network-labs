class Logger:
    def __init__(self):
        newFile = open('log.txt', 'w+')
        newFile.close()

    def log(self, text, title=''):
        file = open('log.txt', "a")
        if title != '':
            file.write(title + '\n')
            print(title)

        file.write(text + '\n')
        print(text)
        file.close()

    def log_response(self, response):
        file = open('log.txt', "a")
        status = f'\nHTTP/1.1 {response.status} {response.reason}'
        self.log(status)

        if response.headers:
            self.log('Headers: ')
            for key, value in response.headers.items():
                self.log(f'{key}: {value}\r\n')

        if response.body:
            self.log(response.body.decode('iso-8859-1'), 'Body:')

        file.close()
