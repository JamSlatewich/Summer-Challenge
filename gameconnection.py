import socket
import json

class GameConnection:
	def __init__(self):
		self.sock =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def connect(self):
		self.sock.connect(("localhost", 2092))

	def run_command(self, command):
		dump = json.dumps(command)
		message = dump.encode("utf-8")
		self.sock.send(message)
		message = self.sock.recv(1000000)
		dump = message.decode("utf-8")
		return json.loads(dump)