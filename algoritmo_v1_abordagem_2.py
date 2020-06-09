from __future__ import print_function
from ortools.linear_solver import pywraplp



def algoritmo(num_items, items, capacity, num_conflicts, conflicts):

	print('----- algoritmo v5 ------')

	values = [i.value for i in items]
	weights = [i.weight for i in items]
	print('values: ',values, '\nweights: ', weights, '\nconflitos: ', conflicts, '\ncapacidade: ', capacity)

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
		
		# Esse foi + ou -
		for a, b in conflicts:
			#print(a,b)
			solver.Add(x[a] == 0 or x[b] == 0)
		

		'''	
		solver.Add(
			sum(x[i] * x[j]
				for i in conflicts
					for j in conflicts) == 0)
		'''		
		#solver.Add((x[i]*x[j]for i,j in conflicts) == 0)
	# ---------------------------------------------------------
    # Objective
	objective = solver.Objective()
	
	for i in indices:
		objective.SetCoefficient(x[i], values[i])

	objective.SetMaximization()
	
	status = solver.Solve()
	
	solution = [0]*num_items    # lista com todas os objetos em zero. ex: [0, 0, 0, 0]
	
	if status == pywraplp.Solver.OPTIMAL:
		total_weight = 0
		print(f'\nValor total: {int(objective.Value())}\n')
		for i in indices:
			solution[i] = int(x[i].solution_value())
			if x[i].solution_value() > 0:
				total_weight += weights[i]
				print('Item', i, '- weight:', weights[i], ' value:',
						values[i])
				print()
		print('Peso total', total_weight)		
	else:
		print('The problem does not have an optimal solution.')

    # prepare the solution in the specified output format
	output_data = str(int(objective.Value())) + '\n'
	output_data += ' '.join(map(str, solution))
	
	return output_data
