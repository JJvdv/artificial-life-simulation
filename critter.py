import random
import pygame
import math


WINDOW_SIZE = 600

#############################################################################################################
# Critter class
# Attributes:
# - color: The group the critter belongs to (Red, Yellow, Blue)
# - position: xy-coordinates of the critter in the simulation
# - speed: how fast the critter moves
# - health: The amount of health each critter has, the critter dies when health is 0 or less
# - damage: The damage delt to other critters when they are attacking each other.
# - velocity: How far the critters move from their current position to another position in the simulation.
# - low_health: A threshold for critters to rather search for healing plants than attack.
# - kills: The amount of kills a critter has.
############################################################################################################
class Critter:
    def __init__(self, color, position, speed = 10, health = 1000, damage = 10):
        self.color = color
        self.position = list(position)
        self.size = 5
        self.speed = speed 
        self.velocity = [random.uniform(-self.speed, self.speed), random.uniform(-self.speed, self.speed)]
        self.health = health
        self.low_health = 30
        self.damage = damage
        self.kills = 0

    # Function to allows critters to attack each other if they are still alive
    def attack(self, critters):
        for critter in critters:
            curr_health = critter.health
            if critter.color != self.color and self.collision(critter) and critter.health > 0:
                critter.health = critter.health - self.damage
                if critter.health == curr_health:
                    break

            if critter.health <= 0:
                self.kills += 1                   
    
    # Function for the critters to move around in the boundaries of the simulation space (size of space)    
    def move(self):
        if self.health > 0:                 
            self.position[0] += self.velocity[0]
            self.position[1] += self.velocity[1]
            
            if self.position[0] < self.size:
                self.position[0] = self.size
                self.velocity[0] *= -1
            if self.position[1] < self.size:
                self.position[1] = self.size
                self.velocity[1] *= -1
            

            if self.position[0] > WINDOW_SIZE - self.size:
                self.position[0] = WINDOW_SIZE - self.size
                self.velocity[0] *= -1
            if self.position[1] > WINDOW_SIZE - self.size:
                self.position[1] = WINDOW_SIZE - self.size
                self.velocity[1] *= -1
    
    # Function for critters to chase other critters            
    def chase(self, target_position):
        dx = target_position[0] - self.position[0]
        dy = target_position[1] - self.position[1]
        
        distance = math.sqrt((dx **2) + (dy **2))
        
        if distance > 0:
            self.velocity[0] = self.speed * (dx / distance)
            self.velocity[1] = self.speed * (dy / distance)
    
    # Function for critters if they are in proximity of other critters to chase them so that they can attack        
    def chaseCritters(self, critters):
        for critter in critters:
            if self.color != critter.color and critter.health > 0:
                distance = math.sqrt((self.position[0] - critter.position[0]) **2 + (self.position[1] - critter.position[1]) **2)

                if distance <= 50:
                    self.chase(critter.position)

    # Function to check if critters are close enough to each other to be ablt to attack.
    # If critters are next to each other they are allowed to attack (melee attacks).
    def collision(self, colide_critter):
        distance = math.sqrt((self.position[0] - colide_critter.position[0]) **2 + (self.position[1] - colide_critter.position[1]) **2)

        if distance <= colide_critter.size:
            return True
        else:
            return False

    # Draw the critters on the board using pygame to display their positions as they move
    def draw(self, window):
        if self.health > 0:
            pygame.draw.circle(window, self.color, (int(self.position[0]), int(self.position[1])), self.size)
    
    # Function to search for the closest healing plants if the low_health threshold is reached        
    def searchForClosestPlant(self, plants):
        if self.health <= self.low_health and self.heal_cooldown == 0:
            closest_plant = None
            closest_distance = float('inf')
            
            for plant in plants:
                distance = math.sqrt((self.position[0] - plant.position[0]) **2 + (self.position[1] - plant.position[1]) **2)
                
                if distance < closest_distance:
                    closest_distance = distance
                    closest_plant = plant
                    
                if closest_plant:
                    self.chase(closest_plant.position)
                    self.heal_cooldown = 100