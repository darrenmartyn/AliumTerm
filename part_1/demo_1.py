from stem.control import Controller

print(' * Connecting to tor')

with Controller.from_port() as controller:
  controller.authenticate("my_password") # my_password is example
  response = controller.create_ephemeral_hidden_service({80: 5000}, await_publication = True)
  print(" * Our service is available at %s.onion:80, pointing to localhost:5000" % response.service_id)
  try:
    raw_input(" ! hit enter, or ^C to quit")
  finally:
    print(" * Shutting down our hidden service")
