import pygame
import random

from plants import Plant
from critter import Critter
from utils import checkStopCondition, reproduction

# Window size
WINDOW_SIZE = 600

#############################################
# main function to start the simulation
#############################################

def main():
    pygame.init()
    pygame.display.set_caption('Artificial Life Simulation')
    
    window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 18)
    
    running = True
    paused = False
    count = 0
    iteration = 0
    all_critters = []
    all_plants = []
    
    # Initialise population at the start of the simulation
    for _ in range(10):
        blue_critter = Critter('blue', (random.randint(0, WINDOW_SIZE), random.randint(0, WINDOW_SIZE)))
        blue_critter.damage = 50
        blue_critter.health = 1000
        all_critters.append(blue_critter)
    for _ in range(10):
        red_critter = Critter('red', (random.randint(0, WINDOW_SIZE), random.randint(0, WINDOW_SIZE)))
        red_critter.speed = 10
        red_critter.health = 1000
        red_critter.damage = 50
        all_critters.append(red_critter)
    for _ in range(10):
        yellow_critter = Critter('yellow', (random.randint(0, WINDOW_SIZE), random.randint(0, WINDOW_SIZE)))
        yellow_critter.speed = 10
        yellow_critter.damage = 50
        yellow_critter.health = 1000
        all_critters.append(yellow_critter)
    
    for _ in range(random.randint(0, 6)):
        all_plants.append(Plant((random.randint(0, WINDOW_SIZE), random.randint(0, WINDOW_SIZE))))
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = True
                elif event.key == pygame.K_RETURN:
                    paused = False
                    
        if paused == False:
            window.fill(0)
            count += 1
            for critter in all_critters:
                critter.draw(window)
                critter.move()

                # stops critters from getting stuck.
                if count % 10 == 0:
                    critter.position[0] = random.randint(0, WINDOW_SIZE)
                    critter.position[1] = random.randint(0, WINDOW_SIZE)
                    
                
                if critter.health > 0 and critter.health > critter.low_health:
                    critter.attack(all_critters)
                    critter.chaseCritters(all_critters)
                else:
                    critter.searchForClosestPlant(all_plants)


                        
                for plant in all_plants:
                    plant.heal(critter)

            
            for plant in all_plants:
                plant.draw(window)

            all_critters = [critter for critter in all_critters if critter.health > 0]
            
            # Create offspring
            reproduction_critters = reproduction(all_critters)
            
            if len(reproduction_critters) > 0:
                iteration += 1
            
            # Reset population kills after each generation
            for critter in all_critters:
                critter.kills = 0
            
            # Update population with offspring    
            for reproduced_critter in reproduction_critters:
                all_critters.append(reproduced_critter)
                    
            reproduction_critters = []
            
            all_plants = [plant for plant in all_plants if plant.depleted() == False]
            
            if len(all_plants) == 0:
                for _ in range (random.randint(0, 6)):
                    all_plants.append(Plant((random.randint(0, WINDOW_SIZE), random.randint(0, WINDOW_SIZE))))
            
            stop = checkStopCondition(all_critters, iteration)[0]
            if stop:
                print("Game Over!!!")
                running = False  # End the game if only one group is alive
            
            
            # Print the current generation and population to the screen
            iterations_text = font.render(f'Current iteration: {iteration}', True, pygame.Color(255, 255, 255))
            population_text = font.render(f'Current population: {len(all_critters)}', True, pygame.Color(255, 255, 255))
            window.blit(iterations_text, (10, 20))
            window.blit(population_text, (10, 30))
            
            pygame.display.update()
            clock.tick(30)
           
    pygame.quit()
    

    
if __name__ == "__main__":
    main()