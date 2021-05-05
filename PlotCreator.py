import pandas
from matplotlib import pyplot as plt


def plot_learning_curve(file):
    dataframe = pandas.read_csv(file, usecols=['iteration', 'solutionvalue'])
    dataframe['solutionvalue'] = dataframe['solutionvalue'].rolling(20).mean()
    dataframe.plot('iteration', 'solutionvalue', marker='o', color='mediumvioletred')
    plt.show()


def plot_episode_comparison(file500, file1000, file2000):
    point500 = pandas.read_csv(file500, usecols='solutionvalue')[499]
    point1000 = pandas.read_csv(file1000, usecols='solutionvalue')[999]
    point2000 = pandas.read_csv(file2000, usecols='solutionvalue')[1999]
    dataframe = {'iterations': [500, 1000, 2000], 'last greedy iteration': [point500, point1000, point2000]}
    dataframe.plot('iterations', 'last greedy iteration', marker='o', color='mediumvioletred')
    plt.show()
