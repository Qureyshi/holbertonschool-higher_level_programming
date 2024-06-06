#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    """ serialize"""
    with open(filename) as f:
        json.dump(data, f)
    pass

def load_and_deserialize(filename):
    """ deserialize data """
    with open(filename, 'r') as f:
        data = json.load(f)
        return data
    
