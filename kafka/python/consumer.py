"""
A very simple Kafka consumer
"""
import kafka

HOST = "localhost:9092"
TOPIC = "mercury"


def main():
    consumer = kafka.KafkaConsumer(TOPIC, bootstrap_servers=HOST)

    for message in consumer:
        print(message.value.decode("utf-8"))


if __name__ == "__main__":
    main()
