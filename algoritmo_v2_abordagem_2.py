from __future__ import print_function
from ortools.linear_solver import pywraplp
from collections import namedtuple
import time

time_limit = 1000000


def algoritmo(num_items, items, capacity, num_conflicts, conflicts):


	solver = pywraplp.Solver('SolverPLI',pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)


	solver.SetTimeLimit(time_limit)


	print(*items, sep='\n')

	solver.SetTimeLimit(time_limit)

	x = []

	for j in range(0, num_items):
		x.append(solver.IntVar(0, 1, 'x[%d]' % j))


	constraintType0 = solver.Constraint(-solver.infinity(), capacity)
		
	for i in items:
		constraintType0.SetCoefficient(x[i.index], i.weight)


	if num_conflicts > 0:
		print(conflicts)
		for a,b in conflicts:	
			solver.Add(x[a] + x[b] <= 1)
	
		#solver.Add(sum(x[i] for i in range(num_items)) >= 1)
		'''
		c = []
		for i in range(num_conflicts):
			a,b = int(conflicts[i][0]), int(conflicts[i][1])	
			c.append(solver.Constraint(-solver.infinity(), 0, 'c_%d' % i))
			c[i].SetCoefficient(x[a], 1)
			c[i].SetCoefficient(x[b], 1)
		'''	
	
		'''
		constraintType1 = []
		for i in range(num_conflicts):
			constraintType1.append(solver.Constraint(-solver.infinity(), 0))
		#constraintType1 = solver.Constraint(-solver.infinity(), 0)

		n = 0
		for c in conflicts:
			constraintType1.SetCoefficient(x[c[0]], x[c[1]])
			n += 1
		'''
		
		'''
		constraintType1 = []
		constraintType1 = solver.Constraint(-solver.infinity(),0)
		constraintType1 = solver.Constraint(0, solver.infinity())	
		for a, b in conflicts:
			constraintType1.SetCoefficient(x[a], x[b])	
		'''
		'''
		for a,b in conflicts:
			#print(a,b)
			solver.Add(x[a]*x[b] == 0)
		'''
	
	objective = solver.Objective()

	objective.SetMaximization()

	for j in range(0, num_items):
		objective.SetCoefficient(x[j], items[j].value)

	result_status = solver.Solve()

	solution = [0]*num_items    # lista com todas os objetos em zero. ex: [0, 0, 0, 0]

	if result_status == pywraplp.Solver.OPTIMAL:
		total_weight = 0
		print(f'\nValor total: {int(objective.Value())}\n')
		for i in items:
			solution[i.index] = int(x[i.index].solution_value())
			if x[i.index].solution_value() > 0:
				total_weight += i.weight
				print('Item', i.index, '- weight:', i.weight, ' value:', i.value)
				print()
		print('Peso total', total_weight)		
	else:
		print('The problem does not have an optimal solution.')

    # prepare the solution in the specified output format
	output_data = str(int(objective.Value())) + '\n'
	output_data += ' '.join(map(str, solution))
	
	return output_data	