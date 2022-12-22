# import pika

# def on_open(connection):
# 	pass
# connection = pika.SelectConnection(on_open_callback=on_open)
# try:
# 	connection.ioloop.start()
# except KeyboardInterrupt:
# 	connection.close()
# 	connection.ioloop.start()

# channel = None
# def on_connected(connection):
# 	connection.channel(on_open_callback=on_channel_open)
# def on_channel_open(new_channel):
# 	global channel
# 	channel = new_channel
# 	channel.queue_declare(
# 		queue="test",
# 		durable=True,
# 		exclusive=False,
# 		autodelete=False,
# 		callback=on_queue_declared
# 		)
# def on_queue_declared(frame):
# 	channel.basic_consume('test', handle_delivery)
# def handle_delivery(channel,header,body):
# 	print(body)
# parameters = pika.ConnectionParameters()
# connection = pika.SelectConnection(parameters,on_open_callback=on_connected)
# try:
# 	connection.ioloop.start()
# except KeyboardInterrupt:
# 	connection.close()
# 	connection.ioloop.start()

import js2py
f = js2py.eval_js("function $(a,b) {sum = a+b;return sum}")
print(f(3,4))