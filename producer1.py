import pika

# connect RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='total', durable=True)
channel.queue_declare(queue='diff', durable=True)
channel.queue_declare(queue='mul', durable=True)
channel.queue_declare(queue='div', durable=True)

# khai bao exchange direct log, type = direct
channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

# tao bind giua exchange va queue
channel.queue_bind(exchange='direct_logs', queue='total')
channel.queue_bind(exchange='direct_logs', queue='diff')
channel.queue_bind(exchange='direct_logs', queue='mul')
channel.queue_bind(exchange='direct_logs', queue='div')
a = int(input())
b = int(input())
dau = input()
mess = '|'.join([str(a), str(b)])

routing_key = ' '

if dau == '+':
    routing_key = 'total'
elif dau == '-':
    routing_key = 'diff'
elif dau == '*':
    routing_key = 'mul'
elif dau == '/':
    routing_key = 'div'

channel.basic_publish(exchange='direct_logs', routing_key=routing_key, body=mess)
print("[x] Sent a = ", a,", b = ", b, "\n operator = ", dau)
connection.close()