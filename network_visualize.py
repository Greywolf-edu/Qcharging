import pickle
import numpy as np
import matplotlib.pyplot as plt

def energy_distribution(network_file = 'networkvisualiztion.pkl'):
    network = None
    with open(network_file, 'rb') as f:
        network = pickle.load(f)

    
