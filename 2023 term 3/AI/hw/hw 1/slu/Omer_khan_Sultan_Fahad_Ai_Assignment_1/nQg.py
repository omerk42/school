import random
import time

start_time = time.perf_counter()
    
   
   

N = int(input("enter number of queens \n"))

# Population size
popSize = 100

# Mutation probability
mutProb = 0.1

# Fitness function
def fit(board):
    attacks = 0
    for i in range(N):
        for j in range(i+1, N):
            if board[i] == board[j] or board[i] - i == board[j] - j or \
               board[i] + i == board[j] + j:
                attacks += 1
    return N - attacks

# Generate initial population
def genPop():
    pop = []
    for i in range(popSize):
        indi = list(range(N))
        random.shuffle(indi)
        pop.append(indi)
    return pop

# Select parents for crossover
def selcPop(pop):
    fitns = [fit(board) for board in pop]
    # total fitness
    totFit = sum(fitns)
    # probabilities  
    porb = [f/totFit for f in fitns]
    parent1 = random.choices(pop, weights=porb)[0]
    parent2 = random.choices(pop, weights=porb)[0]
    return parent1, parent2

# Perform crossover on parents
def crossover(parent1, parent2):
    crossover_point = random.randint(1, N-1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutate an individual
def mutate(indi):
    if random.random() < mutProb:
        i, j = random.sample(range(N), 2)
        indi[i], indi[j] = indi[j], indi[i]

# Run the genetic algorithm
def geneticAlgorithm():
    pop = genPop()
    for i in range(1000):
        # Select parents and perform crossover
        parent1, parent2 = selcPop(pop)
        child1, child2 = crossover(parent1, parent2)

        # Mutate the children
        mutate(child1)
        mutate(child2)

        # Add the children to the population
        pop.extend([child1, child2])

        # Remove the worst individuals from the population
        pop = sorted(pop, key=fit, reverse=True)[:popSize]

        # Check if a solution has been found
        best_fit = fit(pop[0])
        if best_fit == N:
            return pop[0]

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


solution = geneticAlgorithm()
if solution:
    print("\nsolution as Row & postion\n")
    print("Row","Pos")
    for i in solution:
        print("{} , {}".format(solution.index(i),i))
    print("\nsolution as board\n")
    b = displayBoard(solution)
    for line in b:
        print(line)
else:
    print("No solution found")


end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"The execution time is: {execution_time}")