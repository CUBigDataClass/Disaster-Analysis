from __future__ import absolute_import, print_function, unicode_literals

import itertools
from streamparse.spout import Spout
from kafka.consumer import KafkaConsumer

class WordSpout(Spout):
    #outputs = ['sentence']
    def initialize(self, stormconf, context):
        #self.words = itertools.cycle(['dog', 'cat',
        #                              'zebra', 'elephant'])
        #self.sentences = [
        #    "She advised him to take a long holiday, so he immediately quit work and took a trip around the world",
        #    "I was very glad to get a present from her",
        #    "He will be here in half an hour",
        #    "She saw him eating a sandwich",
        #]
        #self.sentences = itertools.cycle(self.sentences)
        self.consumer = KafkaConsumer(b'twitterstream',
                            bootstrap_servers=['0.0.0.0:9092'])

    def next_tuple(self):
        #word = next(self.words)
        #self.emit([word])

        #sentence = next(self.sentences)
        #self.emit([sentence])

        for message in self.consumer:
            if message is not None:
                self.emit([message.value])

    def ack(self, tup_id):
        pass  # if a tuple is processed properly, do nothing

    def fail(self, tup_id):
        pass  # if a tuple fails to process, do nothing
