'''Module providing model-related helpers'''
import json


class AutoModel:
    '''Class which just instantiates anything passed to it'''
    def __init__(self, **props):
        self.props = props

    def __repr__(self):
        return json.dumps(self.props)
