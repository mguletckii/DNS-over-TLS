from dnstlsgtw import dnstlsgtw
import socket, dns.query
import threading
import sys, logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

try:
    listen_addr = sys.argv[1]
    listen_port = int(sys.argv[2])
    host_name = sys.argv[3]
    host_port = int(sys.argv[4])
except:
    logging.error(f'In command line arguments! Config:{sys.argv[1:]}')
    exit(1)

connection_threads = list()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
sock.bind((listen_addr, listen_port))

while True:
    try:
        new_thread = threading.Thread(target=dnstlsgtw, args=(host_name, host_port, sock, \
            dns.query.receive_udp(sock)))
    except:
        logging.error(f'Craeting new thread!')
        exit(1)

    connection_threads.append(new_thread)
    new_thread.start()
