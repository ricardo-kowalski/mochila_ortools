from __future__ import print_function
from ortools.linear_solver import pywraplp
from collections import namedtuple
import time

time_limit = 1000000
'''

values = [
    8, 10, 15, 4
]
weights = [
    4, 5, 8, 3
]
capacity = 11

num_items = len(values)

conflicts = [(2,1), (2, 0), (2, 3), (1, 0)]
'''

def algoritmo(num_items, items, capacity, num_conflicts, conflicts):


	solver = pywraplp.Solver('SolverPLI',pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)


	solver.SetTimeLimit(time_limit)


	print(*items, sep='\n')

	solver.SetTimeLimit(time_limit)

	x = []

	for j in range(0, num_items):
		x.append(solver.IntVar(0, 1, 'x[%d]' % j))

	
	
	if num_conflicts != 0:
				
		Item_wc = namedtuple("Item_wc", ['index', 'value', 'weight', 'restrictions'])
		items_wc = []

		for i in items:
			restrictions = set()
			for tupla in conflicts:
				#print(cur_confl)
				if i.index in tupla:
					if tupla[0] == i.index:
						elem_tupla = tupla[1]
						restrictions.add(elem_tupla)
					else:
						elem_tupla = tupla[0]
						restrictions.add(elem_tupla)
					#print('tupla',tupla)
					continue
			restrictions = list(restrictions)
			# --------------------------------------------------------------------
			items_wc.append(Item_wc(i.index, i.value, i.weight, restrictions))

		
		constraintType0 = solver.Constraint(-solver.infinity(), capacity)
		
		for i in items_wc:
			constraintType0.SetCoefficient(x[i.index], i.weight)
		
		'''
		constraintType1 = []
		for i in range(num_conflicts):
			constraintType1.append(solver.Constraint(1, solver.infinity()))

		for s in items_wc:
			for i in s.restrictions:
				constraintType1[i].SetCoefficient(x[s.index], 0)

		

		for s in items_wc:
			print('\n',s)
			for i in s.restrictions:
				constraintType1[s.index].SetCoefficient(x[i], 0)
		'''
		constraintType1 = []
		for i in items_wc:
			constraintType1.append(solver.Constraint(1, solver.infinity()))

		for c in range(len(conflicts)):
			for i in items_wc:
				for el in i.restrictions:
					if el == conflicts[c][0] and any((j == conflicts[c][1])for j in range(num_items) if x[j] == 1):
						if el == conflicts[c][0]:
							print('sim, elimina', c)
							constraintType1[i.index].SetCoefficient(x[int(conflicts[c][1])], 0)
						if el == conflicts[c][1]:
							print('sim, elimina', c)	
							constraintType1[i.index].SetCoefficient(x[int(conflicts[c][0])], 0)

		objective = solver.Objective()
		objective.SetMaximization()
		for j in range(0, num_items):
			objective.SetCoefficient(x[j], items_wc[j].value)

		result_status = solver.Solve()

		if result_status == solver.OPTIMAL:
			print(solver.Objective().Value())

		for variable in x:
			print(f'{variable.name()} = {variable.solution_value()}')
