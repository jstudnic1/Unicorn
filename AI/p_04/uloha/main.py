import random
import numpy as np
import matplotlib.pyplot as plt
from deap import base, creator, tools, algorithms

# Definice fitness funkce - maximalizace
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
# Definice jedince jako seznamu s fitness atributem
creator.create("Individual", list, fitness=creator.FitnessMax)

# Velikost jedince (délka terénu)
IND_SIZE = 100

toolbox = base.Toolbox()
# Atribut - reálné číslo mezi 0 a 1
toolbox.register("attr_float", random.uniform, 0, 1)
# Jedinec - seznam reálných čísel
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=IND_SIZE)
# Populace - seznam jedinců
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Definice fitness funkce s nezápornými hodnotami
def evaluate(individual):
    # Různorodost terénu - směrodatná odchylka
    s_odchylka = np.std(individual)
    # Hladkost terénu
    smoothness = -np.mean(np.abs(np.diff(individual)))
    fitness_value = s_odchylka + smoothness
    return max(fitness_value, 0),

# Registrace operátorů
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutUniformInt, low=0, up=1, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evaluate)

def plotterrain(t):
    fig, ax = plt.subplots()
    x = range(len(t))
    sea = [0.5 for _ in range(len(t))]
    ax.fill_between(x, sea, color="turquoise")
    ax.fill_between(x, t, color="sandybrown")
    ax.axis("off")
    plt.show()

def main():
    random.seed(42)
    pop = toolbox.population(n=300)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)
    hof = tools.HallOfFame(1)
    # křížení 50%, mutace 20%, 40 generací
    cxpb, mutpb, ngen = 0.5, 0.2, 40

    algorithms.eaSimple(pop, toolbox, cxpb, mutpb, ngen, stats=stats, halloffame=hof, verbose=True)

    return pop, stats, hof

if __name__ == "__main__":
    pop, stats, hof = main()
    # Vizualizace nejlepšího jedince
    plotterrain(hof[0])
