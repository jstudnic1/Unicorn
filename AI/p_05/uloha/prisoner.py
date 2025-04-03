import random
from deap import base, creator, tools, algorithms

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

def sneaky_bastard_gen(my_history, opponent_history):
    rounds = len(my_history) + 1
    if rounds % 10 == 0:
        return 1  # Backstab every 10th round

    if len(opponent_history) < 2:
        return 0  # Not enough data to train

    toolbox = base.Toolbox()
    toolbox.register("attr_float", random.uniform, -1, 1)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, 3)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    def eval_ind(ind):
        correct = 0
        for i in range(1, len(opponent_history)):
            opp_last = opponent_history[i - 1]
            my_last = my_history[i - 1] if i - 1 < len(my_history) else 0
            x = ind[0] + ind[1] * opp_last + ind[2] * my_last
            pred = 0 if x >= 0 else 1
            if pred == opponent_history[i]:
                correct += 1
        return (correct,)

    toolbox.register("evaluate", eval_ind)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=0.5, indpb=0.2)
    toolbox.register("select", tools.selTournament, tournsize=3)

    pop = toolbox.population(n=10)
    algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=5, verbose=False)
    best = tools.selBest(pop, k=1)[0]

    opp_last = opponent_history[-1]
    my_last = my_history[-1] if my_history else 0
    x = best[0] + best[1] * opp_last + best[2] * my_last
    pred = 0 if x >= 0 else 1

    return pred

def sneaky_bastard(my_history, opponent_history):
    rounds = len(my_history) + 1

    if not opponent_history:
        return 0

    if rounds % 10 == 0:
        return 1

    if opponent_history[-1] == 1:
        if random.random() < 0.1:
            return 0

    return opponent_history[-1]

def random_strategy(my_history, opponent_history):
    return random.choice([0, 1])

def tit_for_tat(my_history, opponent_history):
    if not opponent_history:
        return 0

    return opponent_history[-1]

def pavlov(my_history, opponent_history):
    if not opponent_history:
        return 0  # První tah: spolupráce
    if my_history[-1] == opponent_history[-1]:
        return my_history[-1]  # Pokud oba hráli stejně, zopakuj tah
    else:
        return 1 - my_history[-1]  # Jinak změň tah

def adaptive(my_history, opponent_history, cooperation_threshold=0.5):
      if not opponent_history:
          return 0  # První tah: spolupráce
      cooperation_rate = opponent_history.count(0) / len(opponent_history)
      if cooperation_rate > cooperation_threshold:
          return 0  # Pokud soupeř často spolupracuje, spolupracuj také
      else:
          return 1  # Jinak zrazuj

def grim_trigger(my_history, opponent_history):
        if not opponent_history:
            return 0  # První tah: spolupráce
        if 1 in opponent_history:
            return 1  # Pokud soupeř někdy zradil, trvale zrazuj
        return 0  # Jinak pokračuj ve spolupráci
# Definice strategií

# Funkce pro výpočet skóre na základě tahů obou hráčů
def rozdej_skore(tah1, tah2):
    # 1 = zradi, 0 = nezradi

    skores = (0, 0)

    if (tah1 == 1) and (tah2 == 1):
        skores = (2, 2)

    if (tah1 == 1) and (tah2 == 0):
        skores = (0, 3)

    if (tah1 == 0) and (tah2 == 1):
        skores = (3, 0)

    if (tah1 == 0) and (tah2 == 0):
        skores = (1, 1)

    return skores

# Funkce pro simulaci hry mezi dvěma strategiemi
def play(f1, f2, stepsnum):

    skore1 = 0
    skore2 = 0

    historie1 = []
    historie2 = []

    for i in range(stepsnum):
        tah1 = f1(historie1, historie2)
        tah2 = f2(historie2, historie1)

        s1, s2 = rozdej_skore(tah1, tah2)
        skore1 += s1
        skore2 += s2

        historie1.append(tah1)
        historie2.append(tah2)

    return skore1, skore2, historie1, historie2

# Hlavní část programu
ucastnici = [sneaky_bastard_gen, tit_for_tat] * 3

# funkce se mohou v seznamu i opakovat
#ucastnici = [always_cooperate, always_cooperate, random_answer, random_answer, random_answer]



STEPSNUM = 10


l = len(ucastnici)
skores = [0 for i in range(l)]

print("=========================================")
print("Turnaj")
print("hra délky:", STEPSNUM)
print("-----------------------------------------")


for i in range(l):
    for j in range(i+1, l):
        f1 = ucastnici[i]
        f2 = ucastnici[j]
        skore1, skore2, historie1, historie2 = play(f1, f2, STEPSNUM)
        print(f1.__name__, "x", f2.__name__, " ", skore1, ":", skore2)
        print(f"historie: {historie1} \n\n {historie2}")
        skores[i] += skore1
        skores[j] += skore2


print("=========================================")
print("= Výsledné pořadí")
print("-----------------------------------------")


# setrideni indexu vysledku
index = sorted(range(l), key=lambda k: skores[k])

poradi = 1
for i in index:
    f = ucastnici[i]
    print(poradi, ".", f.__name__, ":", skores[i])
    poradi += 1
