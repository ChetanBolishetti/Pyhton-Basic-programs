import  socket
def server_program():
    s=socket.socket()
    host=socket.gethostname()
    port=5000
    s.bind((host,port))

    s.listen(2)
    conn,address=s.accept()
    print("Connection From :"+str(address))
    while True:
        data=conn.recv(1024).decode()
        if not data:
            break
        print("From connected User :"+str(data))
        data = input('->')
        conn.send(data.encode())
    conn.close()

if __name__ == '__main__':
    server_program()