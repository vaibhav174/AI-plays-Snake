

"""
main.py
~~~~~~~~~~

Main file for this project

Here I provide some examples for you to run easily,
you just need to uncomment the part you want and comment what you don't want,
each part is independent of others
"""

from game import*
from genetic_algorithm import *


"""
Watch games of snake played by my best neural nets !

Only 3 games are played here but you can load more networks from the saved folder if you wish
"""
net = NeuralNetwork()
game = Game()


# model 5 is safe and precise
net.load(filename_weights='saved/model5_weights.npy', filename_biases='saved/model5_biases.npy')
game.start(display=True, neural_net=net)
