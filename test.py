from functools import partial

def hello(prenom):
	print(f"coucou {prenom}")

list_prenom = ["Antoine", "Valentin", "Sandrine", "Solangia", "Hakim"]


list_function_problem = []
list_functions_1 = []
list_functions_2 = []

for prenom in list_prenom:
	list_function_problem.append(hello(prenom))
	list_functions_1.append(lambda : hello(prenom))
	list_functions_2.append(partial(hello, prenom))


for func in list_function_problem:
	print(func)
print("_"*30)
for func in list_functions_1:
	func()
print("_"*30)
for func in list_functions_2:
	func()