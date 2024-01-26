import socket
import sys
import random
import os
import time
import threading
import multiprocessing
import json

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224
NUM_WORKERS = 15

def genera_richieste(address, port):
    start_time_thread=time.time()
    try:
        s=socket.socket()
        s.connect((address,port))
        print(f"\n{threading.current_thread().name}{num+1} Connessione al server:{address}:{port}")
    except:
        print(f"\n{threading.current_thread().name}Qualcosa è andato storto \n")
        sys.exit

    comandi=['+','-','*','%']
    primoNumero=random.randint(1,100)
    operazione=comandi[random.randint(0,3)]
    secondoNumero=random.randint(1,100)
    messaggio={'primoNumero':primoNumero,
               'operazione':operazione,
               'secondoNumero':secondoNumero}
    messaggio=json.dumps(messaggio)
    s.sendall(messaggio.encode("UTF-8"))
    data=s.recv(1024)
    if not data:
        print(f"{threading.current_thread().name}:Server non risponde")
    else:
        print(f"{threading.current_thread().name}:Risultato:{data.decode()}")
    s.close()
    end_time_thread=time.time()
    print(f"{threading.current_thread().name} execution time=", end_time_thread - start_time_thread)


if __name__=='___main__':
    # Run tasks using threads
    start_time = time.time()
    threads = [threading.Thread(target=genera_richieste,args=(SERVER_ADDRESS, SERVER_PORT,)) for _ in range(NUN_WORKERS)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    end_time = time.time()

print("Total threads time=", end_time - start_time)

