from src.utils.hashing import convert_hash
from time import sleep
from random import choice

names = ['felipe', 'lavinia', 'lais', 
         'manuela', 'lilian', 'isabel', 
         'mateus']

def run():
    while True:
        name = choice(names)
        print(f'{name}: {convert_hash(name)}')
        sleep(10)

if __name__== "__main__":
    run()