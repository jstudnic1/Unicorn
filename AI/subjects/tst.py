from utils import *

def iscoloring(G, coloring):
    for edge in G.edges():
        if coloring[edge[0]] == coloring[edge[1]]:
            return False
    return True

def tabu_color(G, k, max_iterations, tabu_tenure=10):
    # začínáme s obarvením pomocí greedy algoritmu
    coloring = initial_greedy_coloring(G, k)

    # vytváříme tabu list a nejlepší řešení
    tabu_list = {}
    node_conflicts, total_conflicts = compute_conflicts(G, coloring)
    best_coloring = coloring.copy()
    best_conflicts = total_conflicts

    # pro obarvení grafu
    colormap = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'brown', 'cyan', 'lime', 'gray', 'black', 'white', 'gold', 'silver', 'teal', 'maroon', 'navy', 'olive', 'lime', 'gray', 'black', 'white', 'gold', 'silver', 'teal', 'maroon', 'navy', 'olive'] #počet barev je 35
    extended_colormap = colormap * (k // len(colormap) + 1)

    start_time = time.time()

    for iteration in range(max_iterations):
        # Tiskneme progress
        if iteration % 10000 == 0:
            elapsed = time.time() - start_time
            print(f"Iterace {iteration}: konflikty = {total_conflicts}, best = {best_conflicts}, čas = {elapsed:.2f}s")

        # Pokud nemáme žádné konflikty, našli jsme řešení
        if total_conflicts == 0:
            break

        # Vybereme náhodný node s konflikty
        conflict_nodes = [node for node, conf in node_conflicts.items() if conf > 0]
        if not conflict_nodes:
            break

        # Vybereme node s nejvíce konflikty
        node = max(conflict_nodes, key=lambda n: node_conflicts[n])

        # Zkoušíme všechny barvy a vybereme nejlepší ne-tabu move
        current_color = coloring[node]
        best_move = None
        best_move_conflicts = float('inf')

        for color in range(k):
            if color == current_color:
                continue

            # kontola tabu listu
            if (node, color) in tabu_list and tabu_list[(node, color)] > iteration:
                continue

            # vyhodnotíme změnu barvy
            # vypočítáme konflikty, pokud změníme barvu
            new_conflicts = 0
            for neighbor in G.neighbors(node):
                if color == coloring[neighbor]:
                    new_conflicts += 1
                if current_color == coloring[neighbor]:
                    new_conflicts -= 1

            new_total_conflicts = total_conflicts + new_conflicts

            # aktualizujeme nejlepší změnu barvy
            if new_total_conflicts < best_move_conflicts:
                best_move = color
                best_move_conflicts = new_total_conflicts

        # pokud není žádná platná změna barvy, vybereme náhodnou barvu
        if best_move is None:
            possible_colors = [c for c in range(k) if c != current_color]
            best_move = random.choice(possible_colors)

            # přepočítáme konflikty
            new_conflicts = 0
            for neighbor in G.neighbors(node):
                if best_move == coloring[neighbor]:
                    new_conflicts += 1
                if current_color == coloring[neighbor]:
                    new_conflicts -= 1

            best_move_conflicts = total_conflicts + new_conflicts

        # Provedeme změnu barvy
        coloring[node] = best_move

        # Aktualizujeme tabu list
        tabu_list[(node, current_color)] = iteration + tabu_tenure + random.randint(0, 5)

        # Aktualizujeme konflikty
        for neighbor in G.neighbors(node):
            if current_color == coloring[neighbor]:
                node_conflicts[node] -= 1
                node_conflicts[neighbor] -= 1
                total_conflicts -= 1
            if best_move == coloring[neighbor]:
                node_conflicts[node] += 1
                node_conflicts[neighbor] += 1
                total_conflicts += 1

        # Aktualizujeme nejlepší řešení
        if total_conflicts < best_conflicts:
            best_coloring = coloring.copy()
            best_conflicts = total_conflicts

    # použijeme nejlepší obarvení
    coloring = best_coloring
    total_conflicts = best_conflicts

    # nakreslíme graf s konečným obarvením
    plt.figure(figsize=(12, 8))
    nx.draw(G, with_labels=True, node_color=[extended_colormap[coloring[node]] for node in G.nodes()])
    plt.title(f'Graph Coloring ({total_conflicts} Conflicts)')
    plt.savefig('graph_coloring_{}.png'.format(k))
    plt.show()

    return f"Počet konfliktů: {total_conflicts}"

def main():
    # načteme graf
    start_time = time.time()
    print("Čtení grafu...")
    Gd = readdimacs('dsjc250.5.col.txt')
    print(f"Graf má {Gd.number_of_nodes()} vrcholů a {Gd.number_of_edges()} hran")

    k = 60 # počet barev
    max_iterations = 1000000000
    print(f"Začínáme obarvování s {k} barvami...")

    result = tabu_color(Gd, k, max_iterations)
    print(result)

    elapsed = time.time() - start_time
    print(f"Total execution time: {elapsed:.2f} seconds")

if __name__ == "__main__":
    main()

