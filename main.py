from algoritmo_v5 import algoritmo

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

DEBUG = 0

def solve_it(input_data):
    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])
    conflict_count = int(firstLine[2])

    items = []
    conflicts = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    for i in range(1, conflict_count+1):
        line = lines[item_count + i]
        parts = line.split()
        conflicts.append((int(parts[0]), int(parts[1])))


    if DEBUG >= 1:
        print(f"numero de itens = {item_count}")
        print(f"capacidade da mochila = {capacity}")
        print(f"numero de conflitos = {conflict_count}")

    if DEBUG >= 2:
        print("Itens na ordem em que foram lidos")
        for item in items:
            print(item)
        print()

    if DEBUG >= 2:
        print("Conflitos na ordem em que foram lidos")
        for conflict in conflicts:
            print(conflict)
        print()

    #if conflict_count == 0:
    # Modify this code to run your optimization algorithm
    return algoritmo(item_count, items, capacity, conflict_count, conflicts)

if __name__ == '__main__':
	with open('ks_30_0_wc', 'r') as input_data_file:
		input_data = input_data_file.read()
	output_data = solve_it(input_data)
	print(output_data)

	'''
	solution_file = open(file_location + ".sol", "w")
	solution_file.write(output_data)
	solution_file.close()
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')
        '''


