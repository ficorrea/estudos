import time
import json

class Treat:
    def __init__(self, data):
        self.data = data

    def add_time(self):
        self.data['time'] = int(time.time())

    def convert_json(self):
        self.data = json.dumps(self.data)
    
    def print_data(self):
        print(self.data)