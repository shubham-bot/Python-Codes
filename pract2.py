"""name = input("Please enter your name: ")
age = int(input("How old are you? {}".format(name))

if (18 <= age < 31):
	print("Wellcome to our holiday program, {}".format(name))
else:
	print("You age is out of range")



for i in range(1,13):
	for j in range(1,13):
		print("{0} times {1} is {2}".format(i, j, i*j))
	print("--------------------------")"""

shopping_list = ["Bread", "pasta", "eggs", "spam", "bread", "rice"]

for item in shopping_list:
	if (item == "spam"):
		continue

	print("Buy " + item)


for item in shopping_list:
	if(item!= "spam"):

		print("Buy " + item)
