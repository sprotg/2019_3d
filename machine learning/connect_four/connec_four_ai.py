from random import randint
import pickle

class Connect_four_ai():

    def __init__(self):
        self.training_data = set()
        self.add_data(([[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],3))
        self.load()

    def make_move(self, game):
        return randint(0,5)

    def add_data(self, move):
        v = [item for sublist in move[0] for item in sublist]
        self.training_data.add((tuple(v),move[1]))
        print(self.training_data)

    def load(self):
        self.training_data = pickle.load(open("training_data.p", "rb"))

    def save(self):
        pickle.dump(self.training_data, open("training_data.p", "wb"))

    def find_nearest(self, state):
        pass
