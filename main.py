#Calculator: Define functions for each operations
#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2
#Multiply
def multiply(n1, n2):
  return n1 * n2
#Divide
def divide(n1, n2):
  return n1 / n2

#Store the operators in a dictionary
operators = {
  "+": add,
  "-":subtract,
  "*":multiply,
  "/":divide,}

#Take user number inputs for first number
num1 = int(input("What's the first number? "))

#Print the list of operation that can be performed
for key_symbol in operators:
  print(key_symbol)

#Take user for operation they would like to perform
operation = input("What operation would you like to perform? ")

#User input for second number
num2 = int(input("What's the second number? "))

#operation is taken by the operator variable to find the matching operator
operation_function = operators[operation]
#Calculate the answer based on the operator symbol entered
answer = operation_function(num1, num2)
#print out result and voila!
print(f"{num1}{operation}{num2} = {answer}")
