'''Consumer module'''
from kafka import KafkaConsumer

SERVER = 'winsam1:9092'  #'10.161.169.142:9092' #10.152.29.38:9092

def main():
    '''The main function'''
    startconsume(SERVER)

def startconsume(server_address):
    '''The consume function'''
    print 'start consumption..'
    consumer = KafkaConsumer(bootstrap_servers=server_address, auto_offset_reset='earliest')
    consumer.subscribe(['data-raw'])
    print 'connected.'
    for msg in consumer:
        print 'received message: ' + msg.value

    print 'consume done.'

if __name__ == '__main__':
    main()
