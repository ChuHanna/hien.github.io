import pika, sys, os
import time

def main():
    # connect rabbitmq
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # khai bao queue dung
    channel.queue_declare(queue='diff',durable= True)

    # ham xu ly sau khi lay mess ve
    def callback(ch, method, properties, body):
        print(body.decode('utf-8'))
        mess = body.decode('utf-8')
        a,b = mess.split('|')
        diff_ = int(a) - int(b)
        print("diff:",diff_)
        ch.basic_ack(delivery_tag = method.delivery_tag)

    # lay mess ve
    channel.basic_consume(queue='diff', on_message_callback=callback, )

    print(' [*] Waiting for messages. To exit press CTRL+C')

    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)