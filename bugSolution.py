def function_with_uncommon_error(x):
    if x == 0:
        return float('inf')  # Or raise a more descriptive exception
    else:
        return x + 5

#Alternative solution with exception handling
def function_with_uncommon_error(x):
    try:
        if x == 0:
            return 1/x
        else:
            return x + 5
    except ZeroDivisionError:
        return float('inf') # Or handle the exception in a more appropriate manner