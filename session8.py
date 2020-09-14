"""Assignment for session 8 based on Scopes and Closures"""


# TODO: 1 Write a closure that takes a function and then check whether the function passed
# has a docstring with more than 50 characters. 50 is stored as a free variable
def length_check():
    """
    Outer function called to create a closure. str_len will be free variable
    """
    str_len = 50
    def check_docstr_len(func)-> bool:
        """
        # Inputs:
            func   : function

        # Returns  : bool

        # Functionality:
            Check if the given function is callable and if yes, get the docstring
            length of given function by func.__doc__ and check it is greater than 50

        For eg: for print function, docstring length by print.__doc__ is 392 and thus
        function should retrun true for this.
        """
        if not hasattr(func, '__call__'):
            raise NameError(f"{func} is not a valid function")
        return(True if func.__doc__ and len(func.__doc__) > str_len else False)
    return (check_docstr_len)

# Calling length_check returns inner check_docstr_len function which refers non local variable
# stn_len and thus resulting into a closure
docstr_len_check = length_check()

# TODO: 2 Write a closure that gives you the next Fibonacci number
def fib_generator():
    """
    Outer function called to create a closure. a and b are non local variables
    """
    a = 0
    b = 1
    dummy = 0 # for first two numbers (0 and 1)
    def next_fib()-> int:
        """
        returns the next fibonacci number considering first two numbers as 0 and 1
        on every subsequent call. output =  1,2,3,5...

        # Inputs:

        # Returns  : int

        # Functionality:
            Function generates the next fibonacci number by adding the last two fibonacci
            numbers. To start the series, it uses non-local variables a and b

        For eg: as initial numbers are 0 and 1, next number will be 0+1 =1 then 1+1 = 2
        then 1+2=3 then 2+3 = 5 then 3+5= 8 (summing the last two to generate the next number)
        """
        nonlocal a
        nonlocal b
        nonlocal dummy
        if dummy == 0:
            dummy +=1
            return(a)
        elif dummy == 1:
            dummy +=1
            return(b)
        else:
            a,b = b,a+b
        return(b)
    return(next_fib)

# Calling fib_generator returns inner next_fib function which refers non local variable a & b
# and results in next fibonacci number for each subsequent call as a and b are Part
next_fib_num = fib_generator()


# TODO: 3  Write a closure that can keep a track of how many times add/mul/div functions
#  were called, and update a global dictionary variable with the counts
def add(a:int, b:int)->int:
    """returns sum of 2 numbers"""
    return(f'Result: {a} + {b} = {a + b} ')
def mul(a:int, b:int)->int:
    """returns multiplication of 2 numbers"""
    return(f'Result: {a} * {b} = {a * b} ')
def div(a:int, b:int)->int:
    """returns division of 2 numbers"""
    if b==0:
        raise ValueError(f"division by 0 is not possible")
    return(f'Result: {a} / {b} = {a / b} ')

operation = {'add':0, 'mul':0, 'div':0} # Global dictionary

def operator_counter(func):
    """
    operator_counter function called to create a closure. cntr is a non local variable
    and along with func which will take the function name.
    Inputs:
        func: function name
    Returns:
        op_cntr: function
    """

    cntr = 0

    def op_cntr(*args:int, **kwargs:int)->str:
        """
        calls function add, mul or div with input parameters and update a global dictionary
        "operation" having add, mul and div as its keys while calling the respective function

        # Inputs:
            *args: expects input parameters a and b

        # Returns:
            Returns string output of function call with given input

        # Functionality:
            Function call updates the global dictionary named operation and output the result
            showing how many times this function has been called
            It also calls respective function(non local variable fn) with given input and returns
            the output string.

        For eg: on calling closure for add function with 1,2 as input for 1st time, the output
        will be: add has been called 1 times, Result: 1 + 2 = 3
        """
        # Check for a valid  function is passed to create a closure
        if not hasattr(func, '__call__'):
            raise NameError(f"{func} is not a valid function")

        nonlocal cntr
        cntr +=1 # update the counter
        operation[func.__name__] = cntr # update the global dictionary
        print(f'{func.__name__} has been called {operation[func.__name__]} times')
        return(func(*args, **kwargs))
    return(op_cntr)

# Closures for add, mul and div functions
add_cntr = operator_counter(add)
mul_cntr = operator_counter(mul)
div_cntr = operator_counter(div)

# TODO 4: Modify above such that now we can pass in different dictionary variables to update different dictionaries
user1 = {'add':0, 'mul':0, 'div':0} # Global dictionary for user 1
user2 = {'add':0, 'mul':0, 'div':0} # Global dictionary for user 2
def counter_for_user(func,dictn):
    """
    counter_for_user function called to create a closure for user specific function call
    counters udpate through user specific global dictionaries.
    cntr is a non local variable and along with func which will take the function name.
    As every closure has its own scope, the counter for each dictionary will be different
    each closure and hence same counter can be used to update count of function call
    Inputs:
        func: function name
        dictn: User specific global dictionary
    Returns:
        op_cntr: function
    """
    cntr = 0
    def op_countr(*args:int, **kwargs:int)->str:
        """
        calls function add, mul or div with input parameters and update a global dictionary
        "operation" having add, mul and div as its keys while calling the respective function

        # Inputs:
            *args: expects input parameters a and b

        # Returns:
            Returns string output of function call with given input

        # Functionality:
            Function call updates the user specific dictionary and output the result
            showing how many times this function has been called.
            It also calls respective function(non local variable fn) with given input and returns
            the output string.

        For eg: on calling closure for add function with 1,2 as input for 1st time, the output
        will be: add has been called 1 times, Result: 1 + 2 = 3
        """
        nonlocal cntr
        nonlocal dictn
        cntr +=1
        dictn[func.__name__] = cntr
        print(f'{func.__name__} has been called {dictn[func.__name__]} times')
        return func(*args, **kwargs)
    return(op_countr)

# Closures for add, mul and div functions for user 1
add_cntr1 = counter_for_user(add,dictn = user1)
mul_cntr1 = counter_for_user(mul,dictn = user1)
div_cntr1 = counter_for_user(div,dictn = user1)

# Closures for add, mul and div functions for user 2
add_cntr2 = counter_for_user(add,dictn = user2)
mul_cntr2 = counter_for_user(mul,dictn = user2)
div_cntr2 = counter_for_user(div,dictn = user2)


# TODO 5: Modify above such that now we can pass in different dictionary variables
# to update different dictionaries - another approach
user1_alt = {'add':0, 'mul':0, 'div':0}
user2_alt = {'add':0, 'mul':0, 'div':0}

def counter_for_user_alt(usr_dict):
    """
    counter_for_user_alt function called to create a closure for user specific function call
    counters update through user specific global dictionaries.
    cntr is a non local variable and along with func which will take the function name.
    As every closure has its own scope, the counter for each dictionary will be different
    each clousure and hence same counter can be used to update count of function call

    Inputs:
        usr_dict: User specific global dictionary
    Returns:
        op_countr_alt: function
    """
    cntr = {'add':0, 'mul':0, 'div':0}
    def op_countr_alt(*args, **kwargs):
        """
        calls function add, mul or div with input parameters and update a global dictionary
        "operation" having add, mul and div as its keys while calling the respective function

        # Inputs:
            *args: expects input parameters a and b

        # Returns:
            Returns string output of function call with given input

        # Functionality:
            Function call updates the user specific dictionary and output the result
            showing how many times this function has been called.
            It also calls respective function(non local variable fn) with given input and returns
            the output string.

            For eg: on calling closure for add function with 1,2 as input for 1st time, the output
            will be: add has been called 1 times, Result: 1 + 2 = 3
        """
        arg = args[0]
        args = args[1:]
        if arg.__name__ not in {'add','mul','div'}:
            raise NameError(f"{arg} is not a valid function")
        nonlocal cntr
        nonlocal usr_dict
        cntr[arg.__name__]+=1
        usr_dict[arg.__name__] = cntr[arg.__name__]
        print(f'{arg.__name__} has been called {usr_dict[arg.__name__]} times')
        return(arg(*args, **kwargs))
    return(op_countr_alt)

optr1 = counter_for_user_alt(user1_alt)
optr2 = counter_for_user_alt(user2_alt)
