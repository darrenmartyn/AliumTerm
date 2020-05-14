from stem.control import Controller
import socket
import telnetlib

def listener(port):
    print " + listening on port %d" % port
    t = telnetlib.Telnet()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", port))
    s.listen(1)
    conn, addr = s.accept()
    print  " ! got a connection"
    t.sock = conn
    t.interact()

print(' * Connecting to tor')
with Controller.from_port() as controller:
  controller.authenticate("my_password")
  response = controller.create_ephemeral_hidden_service({80: 5000}, await_publication = True)
  print(" * Our service is available at %s.onion, press ctrl+c to quit" % response.service_id)
  try:
    listener(port=5000)
  finally:
    print(" * Shutting down our hidden service")
