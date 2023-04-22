# python with kafka

# lessons

- dockerizing -> <https://www.youtube.com/watch?v=WnlX7w4lHvM&t=270s&ab_channel=SelfTuts>
- <https://www.youtube.com/playlist?list=PLxoOrmZMsAWxXBF8h_TPqYJNsh3x4GyO4>
- <https://kafka.apache.org/documentation/>

# persist data

  <https://github.com/wurstmeister/kafka-docker/issues/360>

# comands inside

- if have controle (can be used as gui if JMX_PORT: 1099 is active)

``` shell
** inside kafka contener 
cd /opt/kafka/bin

** create new topic in container
./opt/kafka/bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 100 --topic ant_top1

** lost topics
./opt/kafka/bin/kafka-topics.sh --list --zookeeper zookeeper:2181

```

# kafka-manager gui

- <https://github.com/sheepkiller/kafka-manager-docker>

# Python

- using python as producer and consumer
  - <https://pypi.org/project/kafka-python/>
