import pika, sys, os
import time


def main():
    # connect rabbitmq
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # khai bao queue dung
    channel.queue_declare(queue='total', durable= True)

    # ham xu ly sau khi lay mess ve
    def callback(ch, method, properties, body):
        # time.sleep(10)

        print(body.decode('utf-8'))
        mess = body.decode('utf-8')
        name, a, b = mess.split('|')
        if name != 'consumer1':
            exit(0)
        sum_ = int(a) + int(b)
        print("sum:", sum_)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    # lay mess ve
    channel.basic_consume(queue='total', on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')

    channel.start_consuming()


if __name__ == '__main__':
    main()