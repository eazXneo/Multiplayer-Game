import socket
from _thread import *
import sys

"""
Server script always has to be running.
Server script has to be running on the machine, whose IP address is given below.
Then you can run multiple client scripts from wherever on the same local network as the server. 
"""

# currently for local network only. (... inner IP not outer facing one ...?)
# server = "192.168.1.35"
server = "172.20.10.2"
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


def read_pos(str):
    """
    Args:
        str: Looks like the string of the tuple received from another machine

    Returns:
        Tuple of integers for the position of something.
    """
    str = str.split(",")
    return int(str[0]), int(str[1])  # WIT, this becomes a tuple?!


def make_pos(tup):
    """
    Args:
        tup: The tuple of ints holding a position

    Returns:
        String of the tuple passed as a parameter
    """
    return str(tup[0]) + "," + str(tup[1])


pos = [(0, 0), (100, 100)]  # starting positions for the two players.


def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""

    while True:
        try:
            # TODO: why 2048bit? s.ab. certain error mean you need to increase the size but the larger it is,
            #  the longer it will take to take in the data
            #  (so I should expect the program to get slower at some large size, I guess).
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data

            # TODO: WIT. s.ab. prevents infinite loops, but I thought data wouldn't be constant? Or will they always be
            #  exchanging info?
            if not data:
                print("Disconnected.")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print("Received:", data)
                print("Sending :", reply)

            conn.sendall(str.encode(make_pos(reply)))
        # s.ab. make sure we don't end up in an infinite loop / break the program...
        except:
            break

    print("Lost connection.")
    conn.close()


current_player = 0
while True:
    conn, adr = s.accept()
    print("Connected to:", adr)

    start_new_thread(threaded_client, (conn, current_player))
    current_player += 1
