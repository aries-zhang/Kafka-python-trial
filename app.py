'''The entrance module'''
import consumer
import producer

SERVER = 'winsam1:9092'

def main():
    '''The main function'''
    producer.produce(SERVER)
    consumer.startconsume(SERVER)

if __name__ == '__main__':
    main()
