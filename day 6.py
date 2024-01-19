def is_sorted_ascending(array):
    
    for i in range(len(array) - 1):
        
        if array[i] > array[i + 1]:
           
            return False
    
    return True

user_input = input("Enter the array elements separated by spaces: ")

try:
    user_array = [int(x) for x in user_input.split()]
except ValueError:
    print("Invalid input. Please enter integers separated by spaces.")
    exit()

result = is_sorted_ascending(user_array)

if result:
    print("The array is sorted in ascending order.")
    print()
    print("True")
else:
    print("The array is not sorted in ascending order.")
    print()
    print("False")
