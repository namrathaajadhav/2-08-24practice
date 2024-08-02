#global
count = 0
def increase():
    global count 
    count+=1
increase()
increase()
print(count)

def calculate_averagr(numbers):
    return sum(numbers)
number_list = []
n = int(input("Enter the number of element: "))
for i in range(n):
    number = int(input(f"Enter number {i+1}: "))
    number_list.append(number)
averagr = calculate_averagr(number_list)
print("Average:", averagr)

#local
def modify_list(my_list):
  my_list.append(4)
my_list = [1,2,3]
modify_list=(my_list)
print(my_list)


def sum_of_square(numbers):
  total = 0 
  for number in numbers:
    square = number * number
    total += square
  return total
numbers = [1,2,3,4,5]
result = sum_of_square(numbers)
print(result)


#global keyword


def increase_global_count():
     global count 
     count += 1

count = 0
increase_global_count()
increase_global_count()
print(count)
