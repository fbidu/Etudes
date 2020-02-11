"""
A very simple Kafka producer
"""
from itertools import count
from time import sleep

from kafka import KafkaProducer

HOST = "localhost:9092"
TOPIC = "mercury"


def success(record_metadata):
    """
    callback when sending message to Kafka succeeds.
    """
    print(f"tópico: \t{record_metadata.topic}")
    print(f"partição: \t{record_metadata.partition}")
    print(f"offset: \t{record_metadata.offset}")


def main():
    producer = KafkaProducer(bootstrap_servers=HOST)

    for i in count():
        producer.send(TOPIC, f"Message {i}".encode("utf-8")).add_callback(success)
        producer.send(TOPIC, key=b"Key!", value=f"value {i}".encode("utf-8"))
        sleep(2)
    producer.flush()


if __name__ == "__main__":
    main()
