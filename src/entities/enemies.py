from src.entities.entity import *
from src.entities.item import Soul
from src.constants import *
from itertools import permutations
import random as rand


class Enemy(Entity):
    def __init__(self, inmate=None):
        super(Enemy, self).__init__(name=inmate['name'], symbol=SYMBOLS['enemy'])
        self.color = COLORS['enemy']
        self.type = 'enemy'

        self.picture = inmate['mugshot']
        self.charges = inmate['charges']
        self.level = (len(self.charges) // 2)

        for key in self.stats:
            self.update_stat(key, self.level)

        self.current_hp = self.total_hp
        self.inventory.append(Soul(self.stats, self.name, self.pos))

    def __repr__(self):
        print("Name: ", self.name)
        print("Level: ", self.level)
        print("Charges: ", self.charges)
        return ""

    def __lt__(self, other):
        return self.level < other.level

    def turn(self, map):
        player_x, player_y = map.player.pos
        self.update_fov(map.tcod_map)
        if self.view[player_y, player_x]:
            if self.current_hp / self.total_hp >= 0.25:
                self.move_rel_player(map, 'towards')
            else:
                self.move_rel_player(map, 'away')
        else:
            move = (rand.choice([-1, 0, 1]), rand.choice([-1, 0, 1]))
            if map.check_move(move, self):
                self.move(move)

    def move_rel_player(self, map, direction):
        path = map.astar.get_path(self.y, self.x, map.player.y, map.player.x)
        if path:
            move = (path[0][1] - self.x, path[0][0] - self.y)
            if direction is 'towards':
                if map.check_move(move, self):
                    self.move(move)
            else:
                # move in random direction that is not towards player
                possible_moves = list(permutations([-1, 0, 1], 2))
                if move in possible_moves:
                    possible_moves.remove(move)
                rand.shuffle(possible_moves)
                move = possible_moves.pop()
                while not map.check_move(move, self):
                    if not possible_moves:
                        return
                    move = possible_moves.pop()
                self.move(move)

    def move(self, move):
        super(Enemy, self).move(move)
