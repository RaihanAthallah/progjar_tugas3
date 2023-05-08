import sys
import socket
import logging
import threading
from multiprocessing import Process


def kirim_data():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.warning("membuka socket")

    server_address = ('localhost', 45000)
    logging.warning(f"opening socket {server_address}")
    sock.connect(server_address)

    try:
        # Send data
        message = 'TIME\r\n'
        logging.warning(f"[CLIENT] sending {message}")
        sock.sendall(message.encode('utf-8'))
        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(1024).decode('utf-8')
            amount_received += len(data)
            logging.warning(f"[DITERIMA DARI SERVER] {data}")
    finally:
        logging.warning("closing")
        sock.close()
    return

if __name__=='__main__':
    # Membuat 5 process untuk mengirim request ke server
    processes = []
    for i in range(5):
        p = Process(target=kirim_data)
        processes.append(p)
        p.start()
    
    # tampilkan jumlah thread aktif
    print(f"Jumlah thread yang terpakai =>  {threading.active_count()}")
    
    # Menunggu semua process selesai
    for p in processes:
        p.join()
        
     