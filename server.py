import socket
from _thread import *
import sys

"""
Server script always has to be running.
Server script has to be running on the machine, whose IP address is given below.
Then you can run multiple client scripts from wherever on the same local network as the server. 
"""

# currently for local network only. (... inner IP not outer facing one ...?)
server = "192.168.1.35"
port = 5555

# TODO: WIT
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

# only two people should be able to connect to the server
s.listen(2)
print("Waiting for connection, server started.")


def threaded_client(conn):
    reply = ""

    while True:
        try:
            # TODO: why 2048bit? s.ab. certain error mean you need to increase the size but the larger it is,
            #  the longer it will take to take in the data
            #  (so I should expect the program to get slower at some large size, I guess).
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            # TODO: WIT. s.ab. prevents infinite loops, but I thought data wouldn't be constant? Or will they always be
            #  exchanging info?
            if not data:
                print("Disconnected.")
                break
            else:
                print("Received:", reply)
                print("Sending:", reply)

            conn.sendall(str.encode(reply))
        # s.ab. make sure we don't end up in an infinite loop / break the program...
        except:
            break


while True:
    conn, adr = s.accept()
    print("Connected to:", adr)
    start_new_thread(threaded_client, (conn, ))
