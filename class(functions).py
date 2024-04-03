#functions
#def func_11():
 #   print("welcome to python")
  #  print("python is damn easy")  

#nt("start\n")
#func_11("noori")
#print("finish") 

#wap to create a function that does arithmatic addtion substraction mulitipication and division
def reverse_string(input_string):
    """
    Function to reverse a string.
    
    Parameters:
        input_string (str): The string to be reversed.
    
    Returns:
        str: The reversed string.
    """
    return input_string[::-1]

def main():

    input_string = input("Enter a string: ")
    reversed_string = reverse_string(input_string)

    print("Reversed string:", reversed_string)

if __name__ == "__main__":
    main()
      
