import socket
import os


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)

pids = []
try:
  print('Starting listening on port 2222...')
  while True:
    conn, addr = s.accept()
    print('New connection', addr)
    newpid = os.fork()
    print('Opening socket:', addr, os.getpid())
    while True:
        try:
          data = conn.recv(1024)
        except:
          continue

        if data == 'close':
          break
        else:
          conn.send(data)
      #
    print('Closing socket: ', addr, os.getpid())
    conn.close()
    print('Closed: ', addr)
    os._exit(0)
  #
  for pid in pids:
    print("Pid exited", pid)
    os.waitpid(pid, 0)
finally:
  print('Closing server socket...')
  s.close()
  print('Closed.')