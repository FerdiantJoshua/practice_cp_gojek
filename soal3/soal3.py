import sys


def check_existence_in_range(grid, w, i1, i2, j1, j2):
	n = len(grid)
	m = len(grid[0])
	
	i_distance = abs(i1-i2)
	i_direction = 0 if i_distance == 0 else (i2-i1) // i_distance
	j_distance = abs(j1-j2)
	j_direction = 0 if j_distance == 0 else (j2-j1) // j_distance
	if i2 < 0 or j2 < 0 or i2 >= n or j2 >= m:
		return 0
	else:
		is_equal = True
		k = 0
		while k < len(w) and is_equal:
			i_idx = i1 + k * i_direction
			j_idx = j1 + k * j_direction
			is_equal = w[k] == grid[i_idx][j_idx]
			k += 1
		if is_equal:
			return 1
		else:
			return 0
		

def count_occurence(grid, w):
	n = len(grid)
	m = len(grid[0])
	move_dist = len(w) - 1
	
	count = 0
	for i in range(n):
		for j in range(m):
			if grid[i][j] == w[0]:
				# Horizontal & vertical
				count += check_existence_in_range(grid, w, i, i+move_dist, j, j)
				count += check_existence_in_range(grid, w, i, i-move_dist, j, j)
				count += check_existence_in_range(grid, w, i, i, j, j+move_dist)
				count += check_existence_in_range(grid, w, i, i, j, j-move_dist)
				# Diagonal
				count += check_existence_in_range(grid, w, i, i+move_dist, j, j+move_dist)
				count += check_existence_in_range(grid, w, i, i+move_dist, j, j-move_dist)
				count += check_existence_in_range(grid, w, i, i-move_dist, j, j+move_dist)
				count += check_existence_in_range(grid, w, i, i-move_dist, j, j-move_dist)
	return count

if __name__ == '__main__':
	filename = sys.argv[1]
	with open(filename, 'r') as f_in:
		t = int(f_in.readline())
		answers = [0 for _ in range(t)]
		for i in range(t):
			print(i)
			n = int(f_in.readline())
			m = int(f_in.readline())
			grid = []
			for j in range(n):
				grid.append(f_in.readline().strip())
			w = f_in.readline().strip()
			answers[i] = count_occurence(grid, w)
		
	for i in range(len(answers)):
		print(f'Case {i+1}: {answers[i]}')