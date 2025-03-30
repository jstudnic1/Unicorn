import random as rd
from constants import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def is_same_color(agent1, agent2):
    return (agent1 in PURPLE and agent2 in PURPLE) or (agent1 in BLUE and agent2 in BLUE)

def display_grid(happy_agents, num_happy_agents):
    cmap = mcolors.ListedColormap(['white', 'darkorange', 'green', 'darkorange', 'darkblue'])
    bounds = [0, 1, 2, 3, 4, 5]
    norm = mcolors.BoundaryNorm(bounds, cmap.N)

    # Display grids and graph side by side
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(happy_agents, cmap=cmap, norm=norm)
    axs[0].set_title('Happy Agents')
    axs[1].plot(range(len(num_happy_agents)), num_happy_agents)
    axs[1].set_title('Happy Agents Over Time')
    axs[1].set_xlabel('Iterations')
    axs[1].set_ylabel('Number of Happy Agents')
    axs[1].grid(True)

    plt.tight_layout()
    plt.show()

def calc_rat(agents, x, y):
    # Calculate ratio of neighbors with the same color as the current agent.
    current = agents[x, y]
    # Build a list of valid neighbor values (skipping self and empty cells)
    neighbors = [
        agents[i % N, j % N]
        for i in range(x - 1, x + 1 + 1)
        for j in range(y - 1, y + 1 + 1)
        if not (i == x and j == y) and agents[i % N, j % N] != EMPTY
    ]
    if not neighbors:
        return 0
    return sum(is_same_color(n, current) for n in neighbors) / len(neighbors)

def update_agents(agents):
    sad_agents = []
    null_agents = []
    for i in range(N):
        for j in range(N):
            if agents[i, j] == EMPTY:
                null_agents.append([i, j])
            else:
                rat = calc_rat(agents, i, j)
                if rat < UNTOL:
                    agents[i, j] = PURPLE_SAD if agents[i, j] in PURPLE else BLUE_SAD
                    sad_agents.append([i, j])
                else:
                    agents[i, j] = PURPLE_HAPPY if agents[i, j] in PURPLE else BLUE_HAPPY
    return agents, sad_agents, null_agents

def change_agent_mood(agents, pos, sad_agents):
    x, y = pos
    if agents[x, y] == EMPTY:
        return
    rat = calc_rat(agents, x, y)
    if rat < UNTOL:
        agents[x, y] = PURPLE_SAD if agents[x, y] in PURPLE else BLUE_SAD
        if pos not in sad_agents:
            sad_agents.append(pos)
    else:
        agents[x, y] = PURPLE_HAPPY if agents[x, y] in PURPLE else BLUE_HAPPY
        if pos in sad_agents:
            sad_agents.remove(pos)

def update_one_agent(agents, pos, sad_agents):
    # Update the mood of an agent and all its neighbors.
    x, y = pos
    change_agent_mood(agents, pos, sad_agents)
    for i in range(x - 1, x + 1 + 1):
        for j in range(y - 1, y + 1 + 1):
            if (i % N, j % N) != (x, y):
                change_agent_mood(agents, [i % N, j % N], sad_agents)
    return agents

def update_agents_in_1(agents, sad_agents, x, y):
    # Update every agent in the neighborhood (using periodic boundaries).
    for i in range(x - 1, x + 1 + 1):
        for j in range(y - 1, y + 1 + 1):
            i_mod, j_mod = i % N, j % N
            if agents[i_mod, j_mod] != EMPTY:
                update_one_agent(agents, [i_mod, j_mod], sad_agents)
    return agents

def make_happy(agents, sad_agents, null_agents):
    num_happy_agents = []
    while sad_agents and null_agents:
        sad = rd.choice(sad_agents)
        empty = rd.choice(null_agents)
        # Move the sad agent to the empty cell.
        agents[empty[0], empty[1]] = agents[sad[0], sad[1]]
        agents[sad[0], sad[1]] = EMPTY
        # Update lists: mark the old position as empty.
        null_agents.append(sad)
        # Update neighbors for both affected cells.
        update_agents_in_1(agents, sad_agents, sad[0], sad[1])
        update_agents_in_1(agents, sad_agents, empty[0], empty[1])
        null_agents.remove(empty)
        sad_agents.remove(sad)
        num_happy_agents.append(N*N - len(sad_agents) - len(null_agents))
        print(len(sad_agents))
    return agents, num_happy_agents

if __name__ == "__main__":
	grid = np.random.randint(0, 3, (N, N))

	updated_grid, sad_agents, null_agents = update_agents(grid)

	happy_grid, num_happy_agents = make_happy(updated_grid, sad_agents, null_agents)

	display_grid(happy_grid, num_happy_agents)
