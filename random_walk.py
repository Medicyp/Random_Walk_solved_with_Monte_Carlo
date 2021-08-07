# You live in a city. In this city, all the streets are organized in a perfect grid. You go for a walk.
# At each intersection, you choose between going North, South, East or West, randomly.
# And then you walk a block until the next intersection.
# What is the longest random walk you can take so that on average you will end up 4 blocks or fewer from home?

# Position on the grid is (x, y)

import random

def random_walk(n):

    x, y = 0, 0

    for i in range(n):
        step = random.choice(['North', 'South', 'East', 'West'])

        if step == 'North':
            y += 1
        elif step == 'South':
            y += -1
        elif step == 'East':
            x += 1
        else:
            x += -1

    return (x,y)

number_of_walks = 100000

for walk_length in range(1, 31):
    no_transport = 0
    for i in range(number_of_walks):
        (x, y) = random_walk(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport += 1

    no_transport_percentage = float(no_transport) / number_of_walks
    print('Walk size = ', walk_length, ' / % of no tranport = ', 100*no_transport_percentage)

