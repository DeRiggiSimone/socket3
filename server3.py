import socket, json
from threading import Thread
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224

def ricevi_comandi (sock_service, addr_client):
    sock_service,addr_client=sock_server.accept()
        with sock_service as sock_client:
            while True:
                data=sock_client.recv(BUFFER_SIZE)
                print(data)
                if not data:
                    break
                data=data.decode()
                data=json.loads(data)
                primoNumero=data['primoNumero']
                operazione=data['operazione']
                secondoNumero=data['secondoNumero']
                print(primoNumero,secondoNumero,operazione)
                if operazione=="+":
                    ris=primoNumero+secondoNumero
                elif operazione=="-":
                    ris=primoNumero-secondoNumero
                elif operazione=="*":
                    ris=primoNumero*secondoNumero
                elif operazione=="/":
                    ris=primoNumero/secondoNumero
                ris=str(ris)
                print("risul:",ris)
                sock_client.sendall(ris.encode())
    sock_service.close()

def ricevi_connessioni (sock_listen):
    while True:
        sock_service, addr_client = sock_listen.accept()
        print("\nConnessione ricevuta da %s" % str(addr_client))
        print("Creo un thread per servire le richieste")
        try:
            Thread(target=ricevi_comandi, args=(sock_service, addr_client)).start()
        except:
            print("Il thread non si avvia") 
            sock_listen.close()
    
def avvia_server(indirizzo, porta):
    sock_listen.bind((SERVER_IP,SERVER_PORT))
    sock_listen.listen()
    ricevi_connessioni (sock_listen)
if __name__=='__main__':
    avvia_server(SERVER_ADDRESS, SERVER_PORT)
print("Termina")
