import socket

def client_program():
    cs=socket.socket()
    host=socket.gethostname()
    port=5000
    cs.connect((host,port))
    message=input('->')

    while message.lower().strip()!='bye':
        cs.send(message.encode())
        data=cs.recv(1024).decode()
        print("Recieved from server :"+data)
        message=input('->')
    cs.close()

if __name__ == '__main__':
    client_program()