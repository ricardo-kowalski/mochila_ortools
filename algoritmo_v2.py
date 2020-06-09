"""
Adaptação do exemplo do OR-Tools docs
"""

from __future__ import print_function
from ortools.algorithms import pywrapknapsack_solver


def algoritmo(num_items, items, capacity, num_conflicts, conflicts):

	values = [i.value for i in items]
	weights = [i.weight for i in items]
	print(values, '\n', weights)
    # Create the solver.
	solver = pywrapknapsack_solver.KnapsackSolver(pywrapknapsack_solver.KnapsackSolver.
        KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')
		
	solver.Init(values, [weights], [capacity])
	computed_value = solver.Solve()

	packed_items = []
	packed_weights = []
	total_weight = 0
	print('Total value =', computed_value)
	for i in range(len(values)):
		if solver.BestSolutionContains(i):
			packed_items.append(i)
			packed_weights.append(items[i].weight)
			total_weight += items[i].weight
	print('Total weight:', total_weight)
	print('Packed items:', packed_items)
	print('Packed_weights:', packed_weights)


'''
    values = [
        360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600, 38, 48, 147,
        78, 256, 63, 17, 120, 164, 432, 35, 92, 110, 22, 42, 50, 323, 514, 28,
        87, 73, 78, 15, 26, 78, 210, 36, 85, 189, 274, 43, 33, 10, 19, 389, 276,
        312
    ]
    weights = [[
        7, 0, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 0, 36, 3, 8, 15, 42, 9, 0,
        42, 47, 52, 32, 26, 48, 55, 6, 29, 84, 2, 4, 18, 56, 7, 29, 93, 44, 71,
        3, 86, 66, 31, 65, 0, 79, 20, 65, 52, 13
    ]]
    capacities = [850]
'''