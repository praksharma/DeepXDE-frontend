import configparser

"""
The code creates an ini file to store confgurations.
"""
config = configparser.ConfigParser()
config['DEFAULT'] = {'workdir': '$HOME/DeepXDE_simulations/'}

with open('config.ini', 'w') as configfile:
  config.write(configfile)

