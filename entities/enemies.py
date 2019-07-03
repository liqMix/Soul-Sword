from entities.entity import *
import json
import requests
import random


class Enemy(Entity):
    def __init__(self, inmate=None, symbol='E'):
        super(Enemy, self).__init__(name=inmate['name'], symbol='E')
        self.color = tcod.red
        self.type = 'enemy'
        
        self.height = inmate['height']
        self.weight = inmate['weight']
        self.sex = inmate['sex']
        self.race = inmate['race']
        self.eyes = inmate['eyes']
        self.hair = inmate['hair']
        self.image = inmate['image']
        self.charges = inmate['charges']
        self.level = len(self.charges)

    def __repr__(self):
        print("Name: ", self.name)
        print("Level: ", self.level)
        print("Charges: ", self.charges)
        return ""

    def __lt__(self, other):
        return self.level < other.level


class EnemyList:
    def __init__(self, source="https://web3.clackamas.us/roster/extract/inmates"):
        self.source = source
        self.enemy_list = []
        self.load_inmates()

    def load_inmates(self):
        response = requests.get("https://web3.clackamas.us/roster/extract/inmates")
        inmates = json.loads(response.text)['results']

        self.enemy_list = []
        for i in inmates:
            self.enemy_list.append(Enemy(inmate=i))
        self.enemy_list.sort()

    def generate_enemies(self, number_of_enemies=10):
        return random.sample(self.enemy_list, k=number_of_enemies)
