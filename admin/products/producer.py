import pika, json

params = pika.URLParameters('amqps://rzaaydbx:qlNdlhM24-VFwNP8FvB5vQzevotFLVid@rattlesnake.rmq.cloudamqp.com/rzaaydbx')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)