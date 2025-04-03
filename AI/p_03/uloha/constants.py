
MAX_ITER = 3_000_000

RED = "\033[1;31m"
GREEN = "\033[1;32m"
ORANGE = "\033[1;33m"
YELLOW = "\033[1;34m"
RESET = "\033[0m"

PATH0 = 'graphs/small_graph0.col' # licha kružnice
NUM_COLORS0 = 3

PATH1 = 'graphs/small_graph1.col' # random small graph
NUM_COLORS1 = 3

PATH2 = 'graphs/dsjc250.5.col'
NUM_COLORS2 = 28

PATH3 = 'graphs/dsjc500.1.col'
NUM_COLORS3 = 12
# pre 14
VALID_500_1 = [8, 11, 12, 6, 6, 6, 1, 5, 2, 10, 10, 1, 8, 10, 13, 5, 5, 5, 8, 3, 9, 3, 8, 12, 6, 1, 13, 6, 9, 4, 4, 0, 6, 2, 7, 3, 10, 11, 5, 6, 0, 3, 0, 3, 2, 5, 9, 4, 12, 0, 2, 9, 13, 6, 4, 7, 8, 6, 6, 6, 9, 3, 2, 7, 10, 12, 12, 9, 9, 0, 3, 9, 3, 0, 13, 2, 6, 0, 5, 0, 2, 2, 0, 7, 1, 9, 7, 12, 1, 12, 1, 9, 0, 6, 0, 4, 2, 2, 0, 2, 8, 3, 7, 8, 1, 6, 6, 12, 7, 0, 9, 3, 7, 10, 4, 11, 12, 11, 1, 8, 1, 5, 3, 1, 5, 7, 10, 4, 10, 8, 3, 1, 0, 5, 10, 2, 5, 5, 13, 11, 13, 11, 1, 3, 11, 1, 9, 13, 8, 6, 0, 12, 0, 7, 11, 0, 1, 3, 1, 4, 4, 1, 11, 4, 10, 7, 12, 1, 1, 9, 2, 7, 0, 10, 7, 4, 1, 6, 3, 11, 10, 7, 5, 2, 5, 0, 1, 8, 3, 6, 8, 10, 2, 5, 12, 0, 1, 11, 2, 0, 4, 2, 6, 9, 2, 3, 4, 7, 0, 0, 4, 0, 2, 0, 1, 6, 11, 3, 0, 9, 2, 0, 2, 4, 11, 7, 3, 3, 2, 3, 9, 10, 13, 1, 5, 1, 6, 1, 5, 7, 1, 10, 7, 3, 10, 8, 8, 4, 9, 11, 12, 4, 6, 4, 4, 8, 4, 4, 6, 2, 2, 5, 11, 1, 3, 2, 6, 3, 11, 4, 0, 1, 1, 2, 4, 10, 6, 2, 6, 2, 7, 10, 0, 2, 3, 4, 9, 3, 8, 2, 7, 13, 2, 12, 10, 3, 6, 4, 1, 7, 8, 5, 5, 3, 3, 6, 7, 13, 2, 10, 10, 3, 13, 10, 0, 10, 9, 1, 5, 5, 8, 4, 12, 1, 6, 6, 3, 4, 5, 11, 13, 8, 3, 3, 3, 9, 1, 7, 7, 1, 0, 7, 5, 5, 3, 4, 4, 1, 13, 2, 10, 1, 7, 0, 9, 7, 3, 11, 4, 5, 11, 10, 1, 4, 2, 13, 2, 3, 0, 3, 8, 8, 6, 7, 6, 5, 7, 5, 7, 9, 8, 11, 4, 8, 8, 8, 9, 13, 0, 7, 8, 0, 8, 5, 2, 10, 10, 11, 12, 7, 8, 13, 0, 6, 2, 13, 1, 0, 10, 6, 1, 4, 5, 4, 11, 8, 10, 11, 0, 7, 4, 12, 3, 1, 11, 13, 6, 1, 4, 12, 9, 10, 3, 12, 8, 0, 4, 1, 0, 2, 3, 4, 0, 5, 6, 11, 8, 2, 11, 12, 0, 0, 1, 5, 5, 2, 0, 1, 10, 2, 4, 1, 9, 10, 1, 13, 0, 1, 0, 5, 4, 1, 9, 0, 13, 1, 9, 5, 5, 7, 2, 7, 13, 7, 8, 2, 4, 9, 6, 0, 5, 2, 1, 9, 2, 3, 9, 5, 6, 7]

PATH4 = 'graphs/dsjc500.5.col'
NUM_COLORS4 = 48

PATH5 = 'graphs/star_graph.col' # hvězda
NUM_COLORS5 = 2

PATH6 = 'graphs/comple_graph.col' # kompletní graf
NUM_COLORS6 = 124

PATH7 = 'graphs/dsjc125.9.col'
NUM_COLORS7 = 44

PATH8 = 'graphs/dsjc125.1.col'
NUM_COLORS8 = 5
# pro 5
VALID_125_1_v0 = [1, 0, 0, 0, 0, 1, 1, 2, 3, 2, 2, 0, 3, 0, 0, 3, 4, 1, 1, 3, 0, 1, 1, 3, 3, 0, 4, 0, 0, 1, 0, 3, 1, 4, 1, 0, 2, 2, 1, 1, 2, 4, 3, 2, 2, 1, 2, 0, 4, 0, 3, 2, 3, 3, 2, 3, 4, 3, 0, 1, 1, 1, 4, 1, 4, 4, 3, 0, 2, 2, 0, 3, 2, 2, 3, 2, 4, 0, 3, 3, 1, 4, 1, 2, 2, 2, 1, 1, 0, 0, 2, 3, 3, 3, 0, 0, 1, 2, 1, 1, 0, 1, 1, 0, 4, 0, 0, 0, 0, 3, 4, 1, 2, 0, 4, 1, 2, 1, 4, 0, 4, 1, 0, 0, 0]
VALID_125_1_v1 = [1, 0, 2, 0, 0, 4, 4, 1, 3, 4, 1, 4, 2, 1, 0, 2, 2, 3, 4, 2, 0, 3, 1, 2, 0, 0, 1, 1, 3, 3, 2, 2, 1, 1, 1, 0, 4, 1, 1, 3, 0, 2, 4, 2, 1, 3, 1, 1, 2, 4, 3, 0, 0, 0, 1, 0, 2, 3, 0, 1, 4, 3, 4, 0, 2, 2, 0, 2, 1, 3, 2, 2, 0, 3, 1, 4, 2, 0, 4, 3, 3, 1, 3, 1, 1, 0, 0, 3, 2, 1, 1, 2, 2, 0, 3, 0, 4, 0, 3, 0, 0, 3, 3, 0, 4, 4, 0, 1, 0, 3, 2, 1, 3, 1, 4, 3, 2, 1, 4, 0, 4, 4, 0, 0, 0]

def choose_graph(p):
	if p == 0:
		path = PATH0
		num_colors = NUM_COLORS0
	elif p == 1:
		path = PATH1
		num_colors = NUM_COLORS1
	elif p == 2:
		path = PATH2
		num_colors = NUM_COLORS2
	elif p == 3:
		path = PATH3
		num_colors = NUM_COLORS3
	elif p == 4:
		path = PATH4
		num_colors = NUM_COLORS4
	elif p == 5:
		path = PATH5
		num_colors = NUM_COLORS5
	elif p == 6:
		path = PATH6
		num_colors = NUM_COLORS6
	elif p == 7:
		path = PATH7
		num_colors = NUM_COLORS7
	elif p == 8:
		path = PATH8
		num_colors = NUM_COLORS8
	return path, num_colors
