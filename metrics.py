import matplotlib.pyplot as plt

###############################################################
# Application created to create the graphs for reseach purposes
###############################################################
tot_games = int(input('How many games were played? '))
blue_wins = int(input('How many games did blue win?'))
red_wins = int(input('How many games did red win?'))
yellow_wins = int(input('How many games did yellow win?'))

tot_blue_iterations = 0
tot_red_iterations = 0
tot_yellow_iterations = 0


for _ in range(blue_wins):
    tot_blue_iterations += int(input('Enter each win iteration counter for blue:' ))

for _ in range(red_wins):
    tot_red_iterations += int(input('Enter each win iteration counter for red:' ))
    
for _ in range(yellow_wins):
    tot_yellow_iterations += int(input('Enter each win iteration counter for yellow:' ))

 
avg_blue_iterations = tot_blue_iterations / blue_wins if blue_wins > 0 else 0
avg_red_iterations = tot_red_iterations / red_wins if red_wins > 0 else 0
avg_yellow_iterations = tot_yellow_iterations / yellow_wins if yellow_wins > 0 else 0

all_wins_count = [blue_wins, red_wins, yellow_wins]
all_win_iterations = [avg_blue_iterations, avg_red_iterations, avg_yellow_iterations]

plt.figure(figsize = (10, 5))
plt.bar(['blue', 'red', 'yellow'], all_win_iterations, alpha = 0.6, label = 'Average Iterations to win')
plt.ylabel('Average iterations', color = 'b')
plt.title('Average Iterations per Color')
plt.grid(axis = 'y')
plt.show


plt.figure(figsize = (10, 5))
plt.bar(['blue', 'red', 'yellow'], all_wins_count, label = 'Games Won')
plt.ylabel('Games Won', color = 'r')
plt.title('Games Won By Critters')
plt.tick_params(axis = 'y', labelcolor = 'r')
plt.show()