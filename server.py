import socket

HOST = socket.gethostbyname(socket.gethostname())


def start_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST,8080))
        print(HOST)
        server.listen(4)
        while True:   
            print("Working...")
            users, address = server.accept()
            data = users.recv(1024).decode('utf-8')
            connect = load_request(data)
            users.send(connect)
            users.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        server.close()
        print('\n'+'shutdown this shit...')



def load_request(request_data):
    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    HDRS_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    path = request_data.split(' ')[1]
    response = ''
    try:    
        with open('/home/ivankovalenko/Документы/python-web'+path, 'rb') as file:
            response = file.read()
        return HDRS.encode('utf-8') + response
    except FileNotFoundError:
        return (HDRS_404 + 'Sorry bro...').encode('utf-8')
if __name__ == '__main__':
    start_server()
