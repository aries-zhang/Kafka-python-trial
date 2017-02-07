'''The producer'''
from kafka import KafkaProducer

SERVER = 'winsam1:9092'  #'10.161.169.142:9092' #10.152.29.38:9092

def main():
    '''The main function'''
    produce(SERVER)

def produce(server_address):
    ''' Rroduces some messages '''
    print 'start connection..'
    producer = KafkaProducer(bootstrap_servers=server_address)
    print 'connected.'
    for _ in range(10):
        producer.send('data-raw', b'Hello kitty!!')

    producer.flush()
    print 'all messages sent.'

if __name__ == '__main__':
    main()
