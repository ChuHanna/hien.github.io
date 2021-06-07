import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='total', durable=True)
channel.queue_declare(queue='diff', durable=True)
channel.queue_declare(queue='mul', durable=True)
channel.queue_declare(queue='div', durable=True)

channel.exchange_declare(exchange='fanout_logs',
                         exchange_type='fanout')
# tao bind giua exchange va queue
# channel.queue_bind(exchange='fanout_logs', queue='total')
channel.queue_bind(exchange='fanout_logs', queue='diff')
channel.queue_bind(exchange='fanout_logs', queue='mul')
channel.queue_bind(exchange='fanout_logs', queue='div')

a = int(input())
b = int(input())
dau = input()
mess = '|'.join(['consumer1', str(a), str(b)])

routing_key = ' '

channel.basic_publish(exchange='fanout_logs', routing_key=routing_key, body=mess)
print("[x] Sent a = ", a,", b = ", b, "\n operator = ", dau)
connection.close()
