import sys

def guess (lower, upper):
    """Computes an estimate of the square root of a number between lower and upper.
    Args:
        lower (float): The lower bound of the range.
        upper (float): The upper bound of the range.
    """
    global counter
    counter += 1
    print (f"{counter}. Guessing between {lower} and {upper}")
    mid = (lower + upper) / 2.0
    mid_squared = mid * mid

    if abs(mid_squared - target) < tolerance:
        print(f"Estimated square root of {target} is approximately {mid}")
        return
    elif mid_squared < target:
        guess(mid, upper)
    else:
        guess(lower, mid)

###################################
# Start of main program logic
##################################
 
tolerance = 1e-7    # Accuracy of result is pre-defined here. More precision will require more iterations to converge.
counter = 0          # To track number of iterations

target = input("Enter an integer more than zero to find the square root of: ")
try:
    if len(target) > 18:
        raise ValueError(f"The input cannot be more than 18 characters long.")
    elif type(target) is not str or not target.isdigit():
        raise ValueError("The input must be a non-negative integer.")
    else:
        target = int(target)
        guess(0, target)
except ValueError as ve:
    print(f"Invalid input: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)
