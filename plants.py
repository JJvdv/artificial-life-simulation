import pygame
import math

######################################################################################
# Plant class
# Plants are spawned randomly throughout the simulation space.
# Plants are used to heal critters in the simulation.
# The more critters heals from the plants the smaller they get till they are depleted.
# Respawns randomly once depleted.
######################################################################################
class Plant:
    def __init__(self, position):
        self.position = list(position)
        self.size = 10
        self.heal_amount = 10
        self.life = 10 
    
    # Function to make sure that only critters that are next to the plant can heal    
    def collision(self, critter):
        distance = math.sqrt((self.position[0] - critter.position[0]) **2 + (self.position[1] - critter.position[1])** 2)
        
        return distance < self.size + critter.size
    
    # Function used heal critters
    def heal(self, critter):
        if self.collision(critter):
            critter.health = critter.health + self.heal_amount
            self.size = self.size - 1
            self.life = self.life - 1
            
            if critter.health > 1000 and critter.color != 'red':
                critter.health = 1000

    # Function to display the plants in the simulation            
    def draw(self, window):
        pygame.draw.circle(window, 'green', (int(self.position[0]), int(self.position[1])), self.size)
    
    # Function to check if the plant is depleted and can not be used to heal anymore
    def depleted(self):
        return self.size <= 0 or self.life <= 0
    
    
    
    