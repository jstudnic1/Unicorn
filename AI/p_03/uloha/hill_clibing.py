import random
from constants import *
from utils import *

def count_conflicts(G, coloring):
	# Spočítá počet konfliktů – pro každou hranu, kde oba vrcholy mají stejnou barvu.

	conflicts = 0
	for u, v in G.edges():
		if coloring[u] == coloring[v]:
			conflicts += 1
	return conflicts

def local_conflict(G, coloring, vertex):
	# Vrátí počet konfliktů, které má daný vrchol se svými sousedy.

	return sum(1 for u in G.neighbors(vertex) if coloring[u] == coloring[vertex])

def hill_climbing(G, num_colors):
	# Hill climbing s optimalizací random walk
	# upřednostní nejnižší číslovanou barvu v případě stejného zlepšení

	n = G.number_of_nodes()

	# Inicializace: náhodné obarvení vrcholů
	coloring = [random.randint(0, num_colors - 1) for _ in range(n)]

	for iteration in range(MAX_ITER):
		improved = False

		for vertex in range(n):
			current_color = coloring[vertex]
			old_local = local_conflict(G, coloring, vertex)

			# best_delta < 0 znamená zlepšení (protože delta = new_local - old_local)
			best_delta = 0
			best_color = current_color

			for color in range(num_colors):
				if color == current_color:
					continue
				# Kolik konfliktů by měl vrchol s touto novou barvou
				new_local = sum(1 for u in G.neighbors(vertex) if coloring[u] == color)
				delta = new_local - old_local

				# Podmínka: pokud je delta menší, jde o zlepšení <=> menší # konfliktů <=> vhodnější barva
				# pokud je delta stejná a color < best_color, také to upřednostníme
				if delta < best_delta or (delta == best_delta and color < best_color):
					best_delta = delta
					best_color = color

			# Pokud jsme našli zlepšení (best_delta < 0) nebo rovnocenné řešení s menší barvou
			if best_color != current_color:
				coloring[vertex] = best_color
				improved = True

		# Zjistíme počet konfliktů v aktuálním obarvení
		current_conflicts = count_conflicts(G, coloring)
		print(f"Iterace {iteration}, konflikty: {current_conflicts}")

		# Pokud jsme dosáhli řešení bez konfliktů, končíme
		if current_conflicts == 0:
			break

		# Pokud nebyly provedeny žádné změny, zkoušíme random walk
		if not improved:
			# for _ in range(5):
				vertex = random.randrange(n)
				current_color = coloring[vertex]
				available_colors = [c for c in range(num_colors) if c != current_color]
				new_color = random.choice(available_colors)
				coloring[vertex] = new_color
				print(f"\t\t\t\t\tRandom walk: změna vrcholu {vertex} na barvu {new_color}")
				current_conflicts = count_conflicts(G, coloring)

	return coloring

def is_coloring(G, col):
    # Ověří, zda je dané obarvení korektní (žádné dva sousední vrcholy nemají stejnou barvu)
    for u, v in G.edges():
        if col[u] == col[v]:
            print(RED + "Nevalidní obarvení" + RESET)
            return False
    print(GREEN + "Validní obarvení" + RESET)
    return True
