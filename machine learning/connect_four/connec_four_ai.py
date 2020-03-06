from random import randint
import pickle
from numpy import linalg

class Connect_four_ai():

    def __init__(self):
        self.training_data = set()
        self.add_data(([[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],3))
        self.load()
        print("Loaded {} training examples".format(len(self.training_data)))

    def make_move(self, game):
        n = self.find_nearest(game.grid)
        return n[1]

    def add_data(self, move):
        v = [item for sublist in move[0] for item in sublist]
        self.training_data.add((tuple(v),move[1]))

    def load(self):
        self.training_data = pickle.load(open("training_data.p", "rb"))

    def save(self):
        pickle.dump(self.training_data, open("training_data.p", "wb"))

    def find_nearest(self, state):
        flat = [item for sublist in state for item in sublist]
        n = min(self.training_data, key=lambda x:linalg.norm([flat[i] - x[0][i] for i in range(len(flat))]))
        return n
