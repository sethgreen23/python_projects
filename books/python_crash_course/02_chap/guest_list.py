persons_dinner = ["Mariouma", "Habiba", "Naima"]
def invite_diner(ps):
	for p in ps:
		print(f"{p.title():<10s}, I would like to invite you to dinner.")
def program(persons_dinner):
	invite_diner(persons_dinner)
	out_guest = "Habiba"
	in_guest = "Kabil"
	print(f"\n{out_guest} can't make is i will invide {in_guest} instead.\n")
	persons_dinner.remove(out_guest)
	persons_dinner.append(in_guest)
	invite_diner(persons_dinner)
	new_persons = ["Habil", "Ali", "Abraham"]
	print("\nI found a bigger table i will invite 3 more people.\n")
	print("These people are :")
	for name in new_persons:
		print(f"{name}.")
	for i, name in enumerate(new_persons):
		if (i == 0):
			persons_dinner.insert(0, name)
		elif (i == 1):
			persons_dinner.insert((len(persons_dinner)+1)//2, name)
		else:
			persons_dinner.append(name)
	print("\n")
	invite_diner(persons_dinner)
	print("\nSorry i can invite just two people for dinner.\nThe big table wont arrive on time.\n")

	while (len(persons_dinner) > 2):
		guest_sorry = persons_dinner.pop()
		print(f"{guest_sorry}, Im sorry i can't invite anymore to the dinner.")

	print("\n")
	invite_diner(persons_dinner)

def delete_lst(lst):
	while (len(lst) > 0):
		del lst[0]
def prin_lst(lst):
	print(lst)

