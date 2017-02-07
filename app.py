'''The entrance module'''
from threading import Thread
import time
import consumer
import producer

SERVER = 'winsam1:9092'

def main():
    '''The main function'''
    consume_thread = Thread(target=consume)
    consume_thread.start()

    producer.produce(SERVER)
    time.sleep(5)

def consume():
    '''Wrapper'''
    consumer.startconsume(SERVER, 10)

if __name__ == '__main__':
    main()
