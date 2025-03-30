import random
import matplotlib.pyplot as plt
from deap import base, creator, tools, algorithms

TERRAIN_LENGTH = 20

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))  # minimalizujeme
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

toolbox.register("attr_float", random.uniform, 0, 1)

toolbox.register("individual", tools.initRepeat, creator.Individual,
                 toolbox.attr_float, n=TERRAIN_LENGTH)

toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evaluate(individual):
    diff_sum = sum(abs(individual[i] - individual[i+1]) for i in range(len(individual)-1))
    return diff_sum,

toolbox.register("evaluate", evaluate)

# === Operátory ===
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=0.1, indpb=0.2)
toolbox.register("select", tools.selRoulette)

def plotterrain(t):
    fig, ax = plt.subplots()
    x = range(len(t))
    sea = [0.5 for _ in t]
    ax.fill_between(x, sea, color="turquoise")
    ax.fill_between(x, t, color="sandybrown")
    ax.axis("off")
    plt.show()

def main():
    pop = toolbox.population(n=50)
    NGEN = 30
    CXPB, MUTPB = 0.5, 0.2

    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=CXPB, mutpb=MUTPB, ngen=NGEN, verbose=False)

    best = tools.selBest(pop, 1)[0]
    print("Fitness nejlepšího terénu:", best.fitness.values[0])

    plotterrain(best)

if __name__ == "__main__":
    main()
