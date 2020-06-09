from __future__ import print_function
from ortools.linear_solver import pywraplp


'''
def create_data_model():
    """Create the data for the example."""
    data = {}
    weights = [48, 30, 42, 36, 36, 48, 42, 42, 36, 24, 30, 30, 42, 36, 36]
    values = [10, 30, 25, 50, 35, 30, 15, 40, 30, 35, 45, 10, 20, 30, 25]
    data['weights'] = weights
    data['values'] = values
    data['items'] = list(range(len(weights)))
    data['num_items'] = len(weights)
    num_bins = 5
    data['bins'] = list(range(num_bins))
    data['bin_capacities'] = [100, 100, 100, 100, 100]
    return data
'''



def algoritmo(num_items, items, capacity, num_conflicts, conflicts):

	values = [i.value for i in items]
	weights = [i.weight for i in items]
	print('values',values, '\nweights', weights, '\nconflicts', conflicts)

	indices = list(range(num_items))

    # Create the mip solver with the CBC backend.
	solver = pywraplp.Solver('multiple_knapsack_mip',
                             pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

    # Variables
    # x[i, j] = 1 if item i is packed in bin j.
	x = {}
	for i in indices:
		x[i] = solver.IntVar(0, 1, 'x_%i' % i)

    # Constraints
    # The amount packed in each bin cannot exceed its capacity.
	solver.Add(
		sum(x[i] * weights[i]
			for i in indices) <= capacity)
	# ---------------------------------------------------------
	if num_conflicts > 0:
		for a in range(4):
			for i in indices:
				if verifica_conflitos(i, x, indices, conflicts, num_conflicts):
					solver.Add(x[i] == 0)
				else:
					solver.Add(x[i] == 1)
	# ---------------------------------------------------------
    # Objective
	objective = solver.Objective()
	
	for i in indices:
		objective.SetCoefficient(x[i], values[i])
	objective.SetMaximization()
	
	status = solver.Solve()
	
	if status == pywraplp.Solver.OPTIMAL:
		print(f'\nValor total: {objective.Value()}\n')
		for i in indices:
			if x[i].solution_value() > 0:
				print('Item', i, '- weight:', weights[i], ' value:',
						values[i])
				print()
	else:
		print('The problem does not have an optimal solution.')


def verifica_conflitos(i, x, indices, conflicts, num_conflicts):
	for c in range(num_conflicts):
		if i == conflicts[c][0]:
			for j in indices:
				if j == conflicts[c][1] and x[j]==1 and j != i:
					print('sim, elimina', c)
					return True
	print('nop, mantém', c)
	return False


def verifica_conflitos2(i, x, indices, conflicts, num_conflicts):
	out = False
	print('entrada', i)
	for c in range(num_conflicts):
		if i == conflicts[c][0]:
			for j in indices:
				if j == conflicts[c][1] and x[j]==1 and j != i:
					print('sim, elimina', c)
					out = True
				else:
					out = False	
		elif i == conflicts[c][1]:
			for j in indices:
				if j == conflicts[c][0] and x[j]==1 and j != i:
					print('sim, elimina', c)
					out = True
				else:	
					out = False				
		else:
			pass		
	print('saida', out)
	return out