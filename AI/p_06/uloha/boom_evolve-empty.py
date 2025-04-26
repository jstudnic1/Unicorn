# -*- coding: utf-8 -*-


import pygame
import numpy as np
import random
import math


from deap import base
from deap import creator
from deap import tools


pygame.font.init()


#-----------------------------------------------------------------------------
# Parametry hry
#-----------------------------------------------------------------------------

WIDTH, HEIGHT = 900, 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)


TITLE = "Boom Master"
pygame.display.set_caption(TITLE)

FPS = 80
ME_VELOCITY = 5
MAX_MINE_VELOCITY = 3
SIMSTEPS = 1000   # přidáno: globální počet simulačních kroků



BOOM_FONT = pygame.font.SysFont("comicsans", 100)
LEVEL_FONT = pygame.font.SysFont("comicsans", 20)



ENEMY_IMAGE  = pygame.image.load("mine.png")
ME_IMAGE = pygame.image.load("me.png")
SEA_IMAGE = pygame.image.load("sea.png")
FLAG_IMAGE = pygame.image.load("flag.png")


ENEMY_SIZE = 50
ME_SIZE = 50

ENEMY = pygame.transform.scale(ENEMY_IMAGE, (ENEMY_SIZE, ENEMY_SIZE))
ME = pygame.transform.scale(ME_IMAGE, (ME_SIZE, ME_SIZE))
SEA = pygame.transform.scale(SEA_IMAGE, (WIDTH, HEIGHT))
FLAG = pygame.transform.scale(FLAG_IMAGE, (ME_SIZE, ME_SIZE))






# ----------------------------------------------------------------------------
# třídy objektů
# ----------------------------------------------------------------------------

# trida reprezentujici minu
class Mine:
    def __init__(self):

        # random x direction
        if random.random() > 0.5:
            self.dirx = 1
        else:
            self.dirx = -1

        # random y direction
        if random.random() > 0.5:
            self.diry = 1
        else:
            self.diry = -1

        x = random.randint(200, WIDTH - ENEMY_SIZE)
        y = random.randint(200, HEIGHT - ENEMY_SIZE)
        self.rect = pygame.Rect(x, y, ENEMY_SIZE, ENEMY_SIZE)

        self.velocity = random.randint(1, MAX_MINE_VELOCITY)




# trida reprezentujici me, tedy meho agenta
class Me:
    def __init__(self):
        self.rect = pygame.Rect(10, random.randint(1, 300), ME_SIZE, ME_SIZE)
        self.alive = True
        self.won = False
        self.timealive = 0
        self.sequence = []
        self.fitness = 0
        self.dist = 0


# třída reprezentující cíl = praporek
class Flag:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH - ME_SIZE, HEIGHT - ME_SIZE - 10, ME_SIZE, ME_SIZE)


# třída reprezentující nejlepšího jedince - hall of fame
class Hof:
    def __init__(self):
        self.sequence = []



# -----------------------------------------------------------------------------
# nastavení herního plánu
#-----------------------------------------------------------------------------


# rozestavi miny v danem poctu num
def set_mines(num):
    l = []
    for i in range(num):
        m = Mine()
        l.append(m)

    return l


# inicializuje me v poctu num na start
def set_mes(num):
    l = []
    for i in range(num):
        m = Me()
        l.append(m)

    return l

# zresetuje vsechny mes zpatky na start
def reset_mes(mes, pop):
    for i in range(len(pop)):
        me = mes[i]
        me.rect.x = 10
        me.rect.y = 10
        me.alive = True
        me.dist = 0
        me.won = False
        me.timealive = 0
        me.sequence = pop[i]
        me.fitness = 0





# -----------------------------------------------------------------------------
# senzorické funkce
# -----------------------------------------------------------------------------

def my_senzor(me, mines, flag):

    def mine_distance_and_direction(me, mine):
        x1, y1 = me.rect.center
        x2, y2 = mine.rect.center
        distance = math.hypot(x2 - x1, y2 - y1)
        direction = math.atan2(y2 - y1, x2 - x1)
        return distance, direction

    def finish_distance(me, flag):
        x1, y1 = me.rect.center
        x2, y2 = flag.rect.center
        return math.hypot(x2 - x1, y2 - y1)

    def finish_direction(me, flag):
        x1, y1 = me.rect.center
        x2, y2 = flag.rect.center
        return math.atan2(y2 - y1, x2 - x1)

    # compute nearest mine distance and direction
    max_dist = math.hypot(WIDTH, HEIGHT)
    # if no mines exist, skip mine sensing
    if not mines:
        fd = finish_distance(me, flag)
        fdir = finish_direction(me, flag)
        return [0.0, 0.0, fd / max_dist, fdir / math.pi]
    # gather distances and directions to all mines
    dists_dirs = [mine_distance_and_direction(me, mine) for mine in mines]
    # select nearest mine
    min_d, min_dir = min(dists_dirs, key=lambda x: x[0])
    # compute flag distance and direction
    finish_d = finish_distance(me, flag)
    finish_dir = finish_direction(me, flag)
    # normalize observations
    norm_mine_dist = min_d / max_dist
    norm_mine_dir = min_dir / math.pi
    norm_flag_dist = finish_d / max_dist
    norm_flag_dir = finish_dir / math.pi
    return [norm_mine_dist, norm_mine_dir, norm_flag_dist, norm_flag_dir]


# ---------------------------------------------------------------------------
# funkce řešící pohyb agentů
# ----------------------------------------------------------------------------


# konstoluje kolizi 1 agenta s minama, pokud je kolize vraci True
def me_collision(me, mines):
    for mine in mines:
        if me.rect.colliderect(mine.rect):
            #pygame.event.post(pygame.event.Event(ME_HIT))
            return True
    return False


# kolidujici agenti jsou zabiti, a jiz se nebudou vykreslovat
def mes_collision(mes, mines):
    for me in mes:
        if me.alive and not me.won:
            if me_collision(me, mines):
                me.alive = False


# vraci True, pokud jsou vsichni mrtvi Dave
def all_dead(mes):
    for me in mes:
        if me.alive:
            return False

    return True


# vrací True, pokud již nikdo nehraje - mes jsou mrtví nebo v cíli
def nobodys_playing(mes):
    for me in mes:
        if me.alive and not me.won:
            return False

    return True


# rika, zda agent dosel do cile
def me_won(me, flag):
    if me.rect.colliderect(flag.rect):
        return True

    return False


# vrací počet živých mes
def alive_mes_num(mes):
    c = 0
    for me in mes:
        if me.alive:
            c += 1
    return c



# vrací počet mes co vyhráli
def won_mes_num(mes):
    c = 0
    for me in mes:
        if me.won:
            c += 1
    return c



# resi pohyb miny
def handle_mine_movement(mine):

    if mine.dirx == -1 and mine.rect.x - mine.velocity < 0:
        mine.dirx = 1

    if mine.dirx == 1  and mine.rect.x + mine.rect.width + mine.velocity > WIDTH:
        mine.dirx = -1

    if mine.diry == -1 and mine.rect.y - mine.velocity < 0:
        mine.diry = 1

    if mine.diry == 1  and mine.rect.y + mine.rect.height + mine.velocity > HEIGHT:
        mine.diry = -1

    mine.rect.x += mine.dirx * mine.velocity
    mine.rect.y += mine.diry * mine.velocity


# resi pohyb min
def handle_mines_movement(mines):
    for mine in mines:
        handle_mine_movement(mine)


#----------------------------------------------------------------------------
# vykreslovací funkce
#----------------------------------------------------------------------------


# vykresleni okna
def draw_window(mes, mines, flag, level, generation, timer):
    WIN.blit(SEA, (0, 0))

    t = LEVEL_FONT.render("level: " + str(level), 1, WHITE)
    WIN.blit(t, (10  , HEIGHT - 30))

    t = LEVEL_FONT.render("generation: " + str(generation), 1, WHITE)
    WIN.blit(t, (150  , HEIGHT - 30))

    t = LEVEL_FONT.render("alive: " + str(alive_mes_num(mes)), 1, WHITE)
    WIN.blit(t, (350  , HEIGHT - 30))

    t = LEVEL_FONT.render("won: " + str(won_mes_num(mes)), 1, WHITE)
    WIN.blit(t, (500  , HEIGHT - 30))

    t = LEVEL_FONT.render("timer: " + str(timer), 1, WHITE)
    WIN.blit(t, (650  , HEIGHT - 30))






    WIN.blit(FLAG, (flag.rect.x, flag.rect.y))

    # vykresleni min
    for mine in mines:
        WIN.blit(ENEMY, (mine.rect.x, mine.rect.y))

    # vykresleni me
    for me in mes:
        if me.alive:
            WIN.blit(ME, (me.rect.x, me.rect.y))

    pygame.display.update()



def draw_text(text):
    t = BOOM_FONT.render(text, 1, WHITE)
    WIN.blit(t, (WIDTH // 2  , HEIGHT // 2))

    pygame.display.update()
    pygame.time.delay(500)







#-----------------------------------------------------------------------------
# funkce reprezentující neuronovou síť, pro inp vstup a zadané váhy wei, vydá
# čtveřici výstupů pro nahoru, dolu, doleva, doprava
#----------------------------------------------------------------------------


# <----- ZDE je místo vlastní funkci !!!!



# funkce reprezentující výpočet neuronové funkce
# funkce dostane na vstupu vstupy neuronové sítě inp, a váhy hran wei
# vrátí seznam hodnot výstupních neuronů
def nn_function(inp, wei):
    # multi-layer perceptron: one hidden layer of size 4
    H = 4
    inp_arr = np.array(inp)
    # layer1 weights (H x input_dim) and biases (H)
    w1 = np.array(wei[:16]).reshape((H, inp_arr.size))
    b1 = np.array(wei[16:16+H])
    # layer2 weights (output_dim x H) and biases (output_dim)
    start = 16 + H
    w2 = np.array(wei[start:start+H*4]).reshape((4, H))
    b2 = np.array(wei[start+H*4:start+H*4+4])
    # forward pass: tanh activation
    h = np.tanh(w1.dot(inp_arr) + b1)
    out = w2.dot(h) + b2
    return out.tolist()


# naviguje jedince pomocí neuronové sítě a jeho vlastní sekvence v něm schované
def nn_navigate_me(me, inp):


    out = np.array(nn_function(inp, me.sequence))
    # choose action with highest activation
    ind = int(np.argmax(out))
    #print(out)

    # nahoru, pokud není zeď
    if ind == 0 and me.rect.y - ME_VELOCITY > 0:
        me.rect.y -= ME_VELOCITY
        me.dist += ME_VELOCITY

    # dolu, pokud není zeď
    if ind == 1 and me.rect.y + me.rect.height + ME_VELOCITY < HEIGHT:
        me.rect.y += ME_VELOCITY
        me.dist += ME_VELOCITY

    # doleva, pokud není zeď
    if ind == 2 and me.rect.x - ME_VELOCITY > 0:
        me.rect.x -= ME_VELOCITY
        me.dist += ME_VELOCITY

    # doprava, pokud není zeď
    if ind == 3 and me.rect.x + me.rect.width + ME_VELOCITY < WIDTH:
        me.rect.x += ME_VELOCITY
        me.dist += ME_VELOCITY




# updatuje, zda me vyhrali
def check_mes_won(mes, flag):
    for me in mes:
        if me.alive and not me.won:
            if me_won(me, flag):
                me.won = True



# resi pohyb mes
def handle_mes_movement(mes, mines, flag):

    for me in mes:

        if me.alive and not me.won:

            inp = my_senzor(me, mines, flag)
            # debug log removed; sensors verified
            nn_navigate_me(me, inp)



# updatuje timery jedinců
def update_mes_timers(mes, timer):
    for me in mes:
        if me.alive and not me.won:
            me.timealive = timer



# ---------------------------------------------------------------------------
# fitness funkce výpočty jednotlivců
#----------------------------------------------------------------------------

def finish_distance(me, flag):
    x1, y1 = me.rect.center
    x2, y2 = flag.rect.center
    return math.hypot(x2 - x1, y2 - y1)

# funkce pro výpočet fitness všech jedinců
def handle_mes_fitnesses(mes, flag):
    max_dist    = math.hypot(WIDTH, HEIGHT)
    for me in mes:
        # 1) Normovaný čas přežití [0..1]
        survival_score = me.timealive / SIMSTEPS

        # 2) Normovaná uražená vzdálenost [0..1]
        #    předpokládáme max dist = SIMSTEPS * ME_VELOCITY
        max_move = SIMSTEPS * ME_VELOCITY
        move_score = me.dist / max_move

        # 3) Normovaná blízkost k cíli na konci [0..1]
        final_d = finish_distance(me, flag)
        closeness_score = 1 - (final_d / max_dist)

        # váhy pro jednotlivá kritéria
        w_surv    = 0.2
        w_move    = 0.2
        w_close   = 0.2

        fitness = w_surv * survival_score \
                + w_move * move_score \
                + w_close * closeness_score

        # 4) pokud agent vyhrál, přidej velký bonus + bonus za rychlost
        if me.won:
            # rychlejší dokončení = vyšší hodnota [0..1]
            speed_score = (SIMSTEPS - me.timealive) / SIMSTEPS
            w_win       = 1.0   # hlavní dosažený cíl
            w_speed     = 0.4   # jak moc oceníme rychlost
            fitness += w_win + w_speed * speed_score

        # ujistíme se, že fitness není záporné
        me.fitness = max(fitness, 0.0)



# uloží do hof jedince s nejlepší fitness
def update_hof(hof, mes):
    l = [me.fitness for me in mes]
    ind = np.argmax(l)
    hof.sequence = mes[ind].sequence.copy()


# ----------------------------------------------------------------------------
# main loop
# ----------------------------------------------------------------------------

def main():


    # =====================================================================
    # <----- ZDE Parametry nastavení evoluce !!!!!

    VELIKOST_POPULACE = 10
    EVO_STEPS = 5  # pocet kroku evoluce
    DELKA_JEDINCE = 40   # genome: (4x4 + 4) for hidden layer + (4x4 + 4) for output layer
    NGEN = 30        # počet generací
    CXPB = 0.6          # pravděpodobnost crossoveru na páru
    MUTPB = 0.2        # pravděpodobnost mutace

    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()

    toolbox.register("attr_rand", random.random)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_rand, DELKA_JEDINCE)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    # vlastni random mutace
    # <----- ZDE TODO vlastní mutace
    def mutRandom(individual, indpb):
        for i in range(len(individual)):
            if random.random() < indpb:
                individual[i] = random.random()
        return individual,

    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", mutRandom, indpb=0.05)
    toolbox.register("select", tools.selRoulette)
    toolbox.register("selectbest", tools.selBest)

    pop = toolbox.population(n=VELIKOST_POPULACE)

    # =====================================================================

    clock = pygame.time.Clock()



    # =====================================================================
    # testování hraním a z toho odvození fitness


    mines = []
    mes = set_mes(VELIKOST_POPULACE)
    flag = Flag()

    hof = Hof()


    run = True

    level = 5   # <--- ZDE nastavení obtížnosti počtu min !!!!!
    generation = 0

    evolving = True
    evolving2 = False
    timer = 0

    while run:

        clock.tick(FPS)


        # pokud evolvujeme pripravime na dalsi sadu testovani - zrestartujeme scenu
        if evolving:
            timer = 0
            generation += 1
            reset_mes(mes, pop) # přiřadí sekvence z populace jedincům a dá je na start !!!!
            mines = set_mines(level)
            evolving = False

        timer += 1

        check_mes_won(mes, flag)
        handle_mes_movement(mes, mines, flag)


        handle_mines_movement(mines)

        mes_collision(mes, mines)

        if all_dead(mes):
            evolving = True
            #draw_text("Boom !!!")"""


        update_mes_timers(mes, timer)
        draw_window(mes, mines, flag, level, generation, timer)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False






        # ---------------------------------------------------------------------
        # <---- ZDE druhá část evoluce po simulaci  !!!!!

        # druhá část evoluce po simulaci, když všichni dohrají, simulace končí 1000 krocích

        if timer >= SIMSTEPS or nobodys_playing(mes):

            # přepočítání fitness funkcí, dle dat uložených v jedinci
            handle_mes_fitnesses(mes, flag)   # <--------- ZDE funkce výpočtu fitness !!!!

            update_hof(hof, mes)
            print(f"Generation {generation}: best weights = {hof.sequence}")


            #plot fitnes funkcí
            #ff = [me.fitness for me in mes]

            #print(ff)

            # přiřazení fitnessů z jedinců do populace
            # každý me si drží svou fitness, a každý me odpovídá jednomu jedinci v populaci
            for i in range(len(pop)):
                ind = pop[i]
                me = mes[i]
                ind.fitness.values = (me.fitness, )


            # selekce a genetické operace
            offspring = toolbox.select(pop, len(pop))
            offspring = list(map(toolbox.clone, offspring))






            for child1, child2 in zip(offspring[::2], offspring[1::2]):
                if random.random() < CXPB:
                    toolbox.mate(child1, child2)

            for mutant in offspring:
                if random.random() < MUTPB:
                    toolbox.mutate(mutant)

            pop[:] = offspring


            evolving = True


    # po vyskočení z cyklu aplikace vytiskne DNA sekvecni jedince s nejlepší fitness
    # a ukončí se

    pygame.quit()


if __name__ == "__main__":
    main()
