"""
    Examples of Recursion ...

    @ Author: Dr. Romas James Hada
"""


def fact(i):
    if i == 1:
        return 1  # base condition
    else:
        return i * fact(i - 1)  # recursive case


'''
    1. Predict the output for the line shown below. You must show the content of the
    call stack in each functional call (20 Points).
'''
print(fact(7))


def pattern(symbol, numSymbols):
    if numSymbols == 1:
        return symbol
    else:
        return symbol + pattern(symbol, numSymbols - 1)


'''
   2. Predict the output for the line shown below. You must show the content of the
    call stack in each functional call (20 Points).
'''
print(pattern('*', 7))

"""
    Tail Vs. Non-Tail Recursion
    
    A recursive function is said to be Tail-Recursive if the recursive call is the last thing 
    done in the function before returning.
    
    A recursive function is said to be Non-Tail Recursive 
    if the recursive call is not the last thing done in the function before returning.
"""
def fact(i):
    if i==1:
        return 1
    else:
        return i*fact(i-1)

fact(5)
"""
    This function accumulates the result in the 'factorial' parameter 
    and only performs the recursive call at the end. This is an example of a Tail Recursion.
"""


def fact(i, factorial=1):
    if i == 1:
        return factorial  # base condition
    else:
        return fact(i - 1, i * factorial)  # recursive case


'''
    3. Predict the output for the line shown below. You must show the content of the
    call stack in each functional call (20 Points).
'''
print(fact(8))

"""
    This function performs a multiplication after each recursive call, 
    requiring more stack space for deep recursion. 
    
     This is an example of a Non-Tail Recursion.
"""


def fact(i):
    if i == 1:
        return 1  # base condition
    else:
        return i * fact(i - 1)  # recursive case


'''
    4. Predict the output for the line shown below. You must show the content of the
    call stack in each functional call (20 Points).
'''
print(fact(8))

"""
    5. Write a non-tail recursive algorithm to find a sum of the series shown below (20 Points). 
    
    1 + 4 + 9 + 16 + 25 + ...
"""


def nonTailSumOfSeries(n):
    pass


print(nonTailSumOfSeries(6))

"""
    6. Write a tail recursive algorithm to find a sum of the series shown below (100 BP). 
    
    1 + 4 + 9 + 16 + 25 + ...
"""


def TailSumOfSeries(n, mySum=1):
    pass


print(TailSumOfSeries(6))

"""
    7. Write and implement a recursive algorithm to reverse a string provided by a user (200 BP). 
    
"""