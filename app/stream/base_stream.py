from abc import ABC


class BaseStream(ABC):

    def process_event(self, event):
        pass

    def read_from_source(self, source):
        pass
