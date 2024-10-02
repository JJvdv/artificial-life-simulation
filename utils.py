import random

from critter import Critter

WINDOW_SIZE = 600

############################################################################################
# Simple function to check if there is only one gorup of critters alive - Stopping condition.
############################################################################################
def checkStopCondition(critters, iterations):
    blue_count = sum(critter.color == 'blue' and critter.health > 0 for critter in critters)
    red_count = sum(critter.color == 'red' and critter.health > 0 for critter in critters)
    yellow_count = sum(critter.color == 'yellow' and critter.health > 0 for critter in critters)
    
    alive_critters = [blue_count > 0, red_count > 0, yellow_count > 0]
    
    if sum(alive_critters) == 1:
        if blue_count > 0:
            print(f'The Blue Critters won! after {iterations} iterations!')
            return True, 'blue'
        elif red_count > 0:
            print(f'The Red Critters won! after {iterations} iterations!')
            return True, 'red'
        elif yellow_count > 0:
            print(f'The Yellow Critters won! after {iterations} iterations!')
            return True, 'yellow'
    return False, 'None'

######################################################################################################
# reproduction function.
# Evaluate the fitness of each critter by the amount of kills they have at the end of the generation.
# The critter with the highest amount of kills are allowed to evolve and create offspring.
# mutation_rate - The amount of mutation allowed for the specific characteristic of the critters.
# Red Critters - Evolves their health.
# Blue Critters - Evolves their damage.
# Yellow Critters - Evolves their speed.
#####################################################################################################
def reproduction(reproduce_list):
    highest_kills = 0
    offspring_list = []
    mutation_rate = 0.2
    
    # Find best critters of each
    for critter in reproduce_list:
        if critter.kills > 0 and critter.kills > highest_kills:
            highest_kills = critter.kills
            
    for critter in reproduce_list:
        if critter.kills == highest_kills and critter.kills > 0:
            offspring = Critter(critter.color, (random.randint(0, WINDOW_SIZE), random.randint(0, WINDOW_SIZE)))
            if offspring.color == 'red':
                if critter.health < 1000:
                    offspring.health = 1000 + (100 * mutation_rate)
                else:
                    offspring.health = critter.health + int(critter.health * mutation_rate)
                offspring.damage = 50
                offspring.speed = 10
                offspring.kills = 0
                offspring.heal_cooldown = 0
                
                offspring_list.append(offspring)
                break
            if offspring.color == 'blue':
                offspring.health = 1000 
                offspring.damage = critter.damage + int(critter.damage * mutation_rate)
                offspring.speed = 10
                offspring.kills = 0
                offspring.heal_cooldown = 0
                
                offspring_list.append(offspring)
                break
            if offspring.color == 'yellow':
                offspring.health = 1000
                offspring.damage = 50
                offspring.speed = critter.speed + int(critter.speed * mutation_rate)
                offspring.kills = 0
                offspring.heal_cooldown = 0
                
                offspring_list.append(offspring)
                break
        
    return offspring_list