from __future__ import absolute_import, print_function, unicode_literals

import itertools
from streamparse.spout import Spout
from pykafka import KafkaClient
from pykafka.common import OffsetType

import sys  

reload(sys)  
sys.setdefaultencoding('utf8')


class WordSpout(Spout):

    def initialize(self, stormconf, context):
        client = KafkaClient(hosts='0.0.0.0:9092')
        self.topic = client.topics[b'twitterstream']
 
    def next_tuple(self):
        consumer = self.topic.get_balanced_consumer(consumer_group=b'group1',
                                                    auto_commit_enable=True,
                                                    reset_offset_on_start=True,             
                                                    auto_offset_reset=OffsetType.LATEST)

        for message in consumer:
            if message is not None:
                self.emit([message.value])
