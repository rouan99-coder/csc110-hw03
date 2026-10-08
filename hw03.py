"""
Name: Rouan Chen
Peers: (add any collaborators)
References: (anything you checked to solve this)
"""

# imported modules
import statistics # let's us use mean, median, mode

# This is a global variable (seen by all local scopes)
grades = [0,0,0,0,0] # initialized with five zeros

# Task 1:
#  Complete the function "read_five_ints" below:
def read_five_ints():
    """ Reads five grades from the user, verifies they are valid integers within [0,10],
    and updates the global grades list. Exits with an error message if input is invalid.
    """
    for idx in range ( len(grades) ):
        in_str = input("Give me the next grade in [0 to 10]:")
        if not in_str.isdigit():
            print("Error in read_five_ints: input string is not for an integer")
            exit()
        num = int(in_str)
        if num < 0 or num > 10 :
            print("Error in read_five_ints: input integer outside of range")
            exit()

        grades[idx] = num


# Task 2:
#  Complete the function "pick_averaging_method" below:
def pick_averaging_method():
    """ returns an average depending on the user's selection

    Obtains an average using either mean, median or mode,
    depending on user input.
    User should pick 'a' for mean, 'b' for median, 'c' for mode.
    Any other input prints
    'Error in pick_averaging_method: incorrect option picked'.
    """
    
    choice = input("Pick 'a' for mean, 'b' for median, 'c' for mode: ")
    
    if choice == "a":
        print("picked: Mean")
        avg = statistics.mean(grades)
        return avg
    
    elif choice == "b":
        print("picked: Median")
        avg = statistics.median(grades)
        return avg
    
    elif choice == "c":
        print("picked: Mode")
        avg = statistics.mode(grades)
        return avg
    
    else:
        print("Error in pick_averaging_method: incorrect option picked")
        exit()

# Task 3:
#  Complete the function "pick_visualization" below:
def pick_visualization(average):
    """ prints the result in a format that depends on the user's selection

    Prints the numeric average or prints in a special way
    depending on user input.
    User should pick '1' for print average, or '2' for plot average.
    Any other input prints
    'Error in pick_visualization: incorrect option picked'.
    """
    choice = input("Pick '1' for print average, or '2' for plot average:")
    
    if choice == "1":
        print_list_and_average(average)
    
    elif choice == "2":
        plot_grades(average)
    
    else:
        print( " Error in pick_visualization: incorrect option picked " )
        exit()


# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

# Do not modify this function
def print_list_and_average(average):
    print(f"The average of {grades} is {average}")

def plot_grades(average):
    print ("Annotated grades: ")
    prev = -1
    for g in grades:
        if prev < average < g:
            print("^", end="")
        if average > g:
            print(" ", end="")
        if average == g:
            print(f"({g})", end="")
        else:
            print(f"{g} ", end="")
        prev = g
    print()

# Do not modify this function
def main ():
    # calls the function and updates the grades
    read_five_ints()
    # this reorders the values in grades in increasing order
    grades.sort()
    print(f"Sorted grades: {grades}")
    # gets avg depending on selection
    avg = pick_averaging_method()
    # prints or 'plots' result
    pick_visualization(avg)
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
