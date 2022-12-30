# import socket

# HOST = "127.0.0.1"
# PORT = 65432

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
# 	s.bind((HOST, PORT))
# 	s.listen()
# 	while True:
# 		conn, addr = s.accept()
# 		with conn:
# 			print(f"connected by{addr}")
# 			data = conn.recv(1024)
# 			print(data.decode())
# 			conn.send(b'HTTP/1.1 200 OK\nconnected')
# 			conn.send(b'Content-type: text/html\n')
# 			conn.send(b'\n')

# 			conn.send(b'<html><body><pre>')
# 			conn.send(data)
# 			conn.send(b'</pre></body></html>')
# 			conn.close()

# import urllib.request
# from urllib.parse import *

# parse_url = urlparse('https://www.geeksforgeeks.org / python-langtons-ant/')
# print(parse_url)
# print('\n')
# unparse_url = urlunparse(parse_url)
# print(unparse_url)
# request_url = urllib.request.urlopen('https://www.geeksforgeeks.org/')
# print(request_url.read())

# import logging

# logging.basicConfig(filename="newfile.log",format='%(asctime)s %(message)s',filemode='w')
# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
# logger.debug("Harmless debug message")
# logger.info("Just a information")
# logger.warning("It's a warning")
# logger.error("Error occured")
# logger.critical("Internet is down")

import ast

code = ast.parse("print('Hello Learner! Welcome to Python')")
print(code)
exec(compile(code,filename="",mode="exec"))

