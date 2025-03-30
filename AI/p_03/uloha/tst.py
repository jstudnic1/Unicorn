from utils import *

def tabu_color(G, k, max_iterations, tabu_tenure=7, diversification_threshold=1000):
    coloring = initial_greedy_coloring(G, k)
    tabu_list = {}
    node_conflicts, total_conflicts = compute_conflicts(G, coloring)
    best_coloring = coloring.copy()
    best_conflicts = total_conflicts

    # Paleta barev
    colormap = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'brown', 'cyan', 'lime']
    extended_colormap = colormap * (k // len(colormap) + 1)

    # Počítadlo pro diverzifikaci
    iterations_without_improvement = 0
    start_time = time.time()

    for iteration in range(max_iterations):
        # Výpis každých 10 000 iterací
        if iteration % 10000 == 0:
            elapsed = time.time() - start_time
            print(f"Iterace {iteration}: konflikty = {total_conflicts}, best = {best_conflicts}, čas = {elapsed:.2f}s")

        # Pokud nejsou konflikty, máme řešení
        if total_conflicts == 0:
            break

        # Výběr uzlu s konflikty
        conflict_nodes = [node for node, conf in node_conflicts.items() if conf > 0]
        if not conflict_nodes:
            break

        node = max(conflict_nodes, key=lambda n: node_conflicts[n])
        current_color = coloring[node]
        best_move = None
        best_move_conflicts = float('inf')

        # Hledání nejlepší změny barvy
        for color in range(k):
            if color == current_color:
                continue

            # Ignorujeme tabu pohyby, pokud nevedou k lepšímu řešení
            if (node, color) in tabu_list and tabu_list[(node, color)] > iteration:
                continue

            # Výpočet změny konfliktů
            new_conflicts = sum(1 for neighbor in G.neighbors(node) if coloring[neighbor] == color) - sum(1 for neighbor in G.neighbors(node) if coloring[neighbor] == current_color)
            new_total_conflicts = total_conflicts + new_conflicts

            # Aktualizace nejlepšího tahu
            if new_total_conflicts < best_move_conflicts:
                best_move = color
                best_move_conflicts = new_total_conflicts

        # Pokud žádný tah není vhodný, vybereme náhodnou barvu
        if best_move is None:
            possible_colors = [c for c in range(k) if c != current_color]
            best_move = random.choice(possible_colors)

            new_conflicts = sum(1 for neighbor in G.neighbors(node) if coloring[neighbor] == best_move) - sum(1 for neighbor in G.neighbors(node) if coloring[neighbor] == current_color)
            best_move_conflicts = total_conflicts + new_conflicts

        # Aplikujeme změnu barvy
        coloring[node] = best_move
        tabu_list[(node, current_color)] = iteration + tabu_tenure + random.randint(0, 5)

        # Aktualizace konfliktů
        total_conflicts = best_move_conflicts
        node_conflicts[node] = sum(1 for neighbor in G.neighbors(node) if coloring[neighbor] == best_move)

        # Aktualizace nejlepšího řešení
        if total_conflicts < best_conflicts:
            best_coloring = coloring.copy()
            best_conflicts = total_conflicts
            iterations_without_improvement = 0
        else:
            iterations_without_improvement += 1

        # Diverzifikace po dosažení prahu
        if iterations_without_improvement > diversification_threshold:
            for _ in range(int(len(G.nodes()) * 0.1)):
                random_node = random.choice(list(G.nodes()))
                old_color = coloring[random_node]
                new_color = random.randint(0, k-1)
                if new_color != old_color:
                    coloring[random_node] = new_color
            node_conflicts, total_conflicts = compute_conflicts(G, coloring)
            iterations_without_improvement = 0

    # Použijeme nejlepší nalezené obarvení
    coloring = best_coloring
    total_conflicts = best_conflicts

    # Vizualizace výsledku
    plt.figure(figsize=(12, 8))
    nx.draw(G, with_labels=True, node_color=[extended_colormap[coloring[node]] for node in G.nodes()])
    plt.title(f'Obarvení grafu ({total_conflicts} konfliktů)')
    plt.savefig(f'graph_coloring_{k}.png')
    plt.show()

    return f"Počet konfliktů: {total_conflicts}", coloring

def main():
    # Načtení grafu
    start_time = time.time()
    print("Čtení grafu...")
    Gd = readdimacs('DSJC125.9 col.txt')
    print(f"Graf má {Gd.number_of_nodes()} vrcholů a {Gd.number_of_edges()} hran")

    k = 60  # Počet barev
    max_iterations = 1000000
    print(f"Začínáme obarvování s {k} barvami...")

    result = tabu_color(Gd, k, max_iterations)
    print(result)

    elapsed = time.time() - start_time
    print(f"Celkový čas běhu: {elapsed:.2f} sekund")

if __name__ == "__main__":
    main()
