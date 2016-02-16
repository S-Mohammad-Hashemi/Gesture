import os
import socket
import math


TCP_IP = '127.0.0.1'
TCP_PORT = 8889
BUFFER_SIZE = 200  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr
vmax=1.13781
vmin=-vmax
diff=vmax-vmin
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    lines=data.split('\n')
    for line in lines:
        tokens=line.split(', ')
    x_acc=float(tokens[0])
    vpercent=100*(x_acc-vmin)/diff
    vpercent=int(math.ceil(vpercent))
    os.system("pactl set-sink-volume 0 "+`vpercent`+"%")
    print vpercent
#     conn.send(data)  # echo
conn.close()
