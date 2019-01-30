"""
Roll dice based on user input parameters
"""
import random
import argparse

def Stats(dieMultiplier, dieSides, Timesrolled):
    for i in range (Timesrolled):
        atts = [random.randint(1,dieSides) for x in range (dieMultiplier)]
        yield(atts) #creates a generator function that you need to iterate over

def main(**kwargs):
    """
    Main control function for the script
    """
    multiplier = kwargs.pop('multiplier', 1)
    sides = kwargs.pop('sides', 20)
    times = kwargs.pop('times', 1)

    for att in Stats(dieMultiplier = multiplier, dieSides = sides,
                    Timesrolled = times):
                print (att)

def parse():
    """
    parses script args
    """
    parser = argparse.ArgumentParser(description='Rolls dice to return random values')
    parser.add_argument("-m," "--multiplier", default = 1, type=int,
                        dest = 'multiplier', help="Die Multiplier")
    parser.add_argument("-s", "--sides", default = 20, type=int,
                        dest = 'sides', help="Number of sides on each die")
    parser.add_argument("-t", "--times", default = 1, type=int,
                        dest = 'times', help = "Number of times to roll the dice")
    args = parser.parse_args()

    main(**vars(args))

if __name__== '__main__':
        parse()
