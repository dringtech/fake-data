'''Module containing generators'''
from factory import make_factory
from pandas import DataFrame


class Generator:
    '''Generator class'''

    def __init__(self, **kwargs):
        self.factory = make_factory(dict, **kwargs)
        self.data = None

    def build_batch(self, count):
        '''Generate a new batch'''
        self.data = self.factory.build_batch(count)

    def save_csv(self, filename):
        '''Write generated data to file'''
        data_frame = DataFrame.from_records(self.data)
        data_frame.to_csv(filename)

    def __repr__(self):
        return repr(self.data)
