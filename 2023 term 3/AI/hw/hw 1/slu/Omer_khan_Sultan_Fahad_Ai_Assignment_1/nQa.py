import random
import math
import time

def generateStartStat(n):
    # this function will genrate starting postion randomly depending on n value
    return [random.randint(0, n-1) for i in range(n)]

def computeConflicts(state):
    # this function will find conflit
    n = len(state) # size of problem
    conflicts = 0
    for i in range(n):  
        for j in range(i+1, n):
            if (state[i] == state[j]) or (abs(state[i] - state[j]) == j - i):
                # first if condition to find vertically, horizontally conflict
                # second if condition to find diagonally conflict 
                conflicts += 1
    return conflicts

# function to make next move
def move(state):
    n = len(state)
    i = random.randint(0, n-1)
    j = random.randint(0, n-1)
    new_state = state[:]
    new_state[i] = j
    # next state is genrated randomly 
    return new_state

# function to compute probability of acceptence for each state
# probability of acceptence i computed based on Metropolis–Hastings algorithm
def acceptanceProbability(delta, temperature):    
    if delta < 0:
        return 1.0
    else:
        return math.exp(-delta / temperature)

# function to solve the problem using simulated annealing 
def simulatedAnnealing(n, max_iter, initial_temperature, cooling_rate):
    # first state generated randomly
    current_state = generateStartStat(n)
    # energy is number of conflicts in stat
    current_energy = computeConflicts(current_state)
    # start tempature defined statcily
    temperature = initial_temperature
    for i in range(max_iter):
        # if there is no conflict
        if current_energy == 0:
            # sloution is found
            return current_state
        # generate new state 
        new_state = move(current_state)
        # compute conflict for new stat
        new_energy = computeConflicts(new_state)
        # delte is diffrent of conflict between old state and current
        delta = new_energy - current_energy
        # calclaute ap of current stat
        ap = acceptanceProbability(delta, temperature)
        # decide if new state is acceptable depending on Metropolis–Hastings algorithm
        if random.random() < ap:
            current_state, current_energy = new_state, new_energy
        temperature *= cooling_rate
    # if sloution doesnt find under 1000 loops
    return None

def displayBoard(array=[]):
    # function display queen in board
    board = []
    for row in range(len(array)):
        # create lines in number N
        line = ""
        for col in range(len(array)):
            if array[row] == col:
                # for each line 
                # if its place of queen 
                line += "|♛|"
            else:
                line += "| |"
        board.append(line)
    return board


start_time = time.perf_counter()



N = int(input("enter number of queens \n"))
solution = simulatedAnnealing(n=N, max_iter=1000, initial_temperature=1000, cooling_rate=0.95)
if solution:
    # if there is solution
    print("\nsolution as Row & postion")
    print("Row","Pos")
    for i in solution:
        print("{} , {}".format(solution.index(i),i))
    print("\nsolution as board\n")
    b = displayBoard(solution)
    for line in b:
        print(line)
else:
    # if there is no solution
    print("No solution found")

end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"\nThe execution time is: {execution_time}")
