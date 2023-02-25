import json
import time
import logging

from kafka import KafkaProducer
from kafka import KafkaConsumer

from kafka.admin import KafkaAdminClient, NewTopic
from faker import Faker

logging.basicConfig(level=logging.INFO)


def my_serializer(data: dict) -> bytes:
    return json.dumps(data).encode()


def fake_data() -> dict:
    fake = Faker()

    return {
        'name': fake.name(),
        'address': fake.address(),
        'created_at': fake.year()
    }


class Producer:
    TOPIC_NAME = 'anttop1'

    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092', ],
                                      value_serializer=my_serializer)
        self.client = KafkaAdminClient(bootstrap_servers='localhost:9092',
                                       client_id='1')

    def show_topics(self):
        return self.client.list_topics()

    def ensure_topic(self):
        if self.TOPIC_NAME in self.show_topics():
            logging.info(f'already have topit {self.TOPIC_NAME}')
        else:
            topic_list = []
            topic_list.append(NewTopic(name=self.TOPIC_NAME, num_partitions=1, replication_factor=1))
            self.client.create_topics(new_topics=topic_list, validate_only=False)
            logging.info(f'topic created {self.TOPIC_NAME}')

    def send_message(self, mess: dict):
        logging.info('[Producer] sending message to kafka server')
        self.producer.send(self.TOPIC_NAME, mess).get(timeout=10)
        self.producer.flush()


class Consumer:
    TOPIC_NAME = 'anttop1'

    def __init__(self):
        self.consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                                      value_deserializer=lambda v: json.loads(v.decode()),
                                      auto_offset_reset='earliest')

    def read_msg(self):
        self.consumer.subscribe(topics=[self.TOPIC_NAME, ])
        for message in self.consumer:
            print("%d:%d: v=%s" % (message.partition,
                                   message.offset,
                                   message.value))
        self.consumer.close()

"""
see this 
https://github.com/lemoncode21/fastapi-kafka/blob/master/kafka/docker-compose.yml
https://www.youtube.com/watch?v=l5NOe3jTEso&ab_channel=lemoncode21
"""

if __name__ == '__main__':
    p = Producer()

    print(p.show_topics())
    p.ensure_topic()
    print(p.show_topics())

    # produce massage every 5 sec
    for i in range(2):
        p.send_message(fake_data())
        time.sleep(5)

    c = Consumer()
    c.read_msg()
