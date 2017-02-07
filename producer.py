'''The producer'''
from kafka import KafkaProducer

SERVER = 'winsam1:9092'  #'10.161.169.142:9092' #10.152.29.38:9092

def main():
    '''The main function'''
    produce()

def produce():
    ''' Rroduces some messages '''
    print 'start connection..'
    producer = KafkaProducer(bootstrap_servers=SERVER)
    print 'connected.'
    for _ in range(10):
        producer.send('data-raw', b'some_message_content')

    producer.flush()
    print 'all messages sent.'

if __name__ == '__main__':
    main()
