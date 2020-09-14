
# EPAI Session 8 Assignment by Sachin Dangayach

This assignment is based on the concepts of "Scopes and Closures". We have created four different closures for different tasks of the assignment.

# Below are key functions in session8.py file.

### A) Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable

### 1. length_check
Outer function called to create a closure. str_len will be free variable.

### 2. check_docstr_len
Function to check if the given input function is callable and if yes, get the docstring length of given function by "func.\_\_doc__" and check it is greater than 50.
For eg: for print function, docstring length by print.\_\_doc__ is 392 and thus function should return true for this.

### B) Write a closure that gives you the next Fibonacci number
### 3. fib_generator
Outer function called to create a closure. a and b are non local variables
### 4. next_fib
Returns the next fibonacci number considering first two numbers as 0 and 1 on every subsequent call. output =  1,2,3,5... Function generates the next fibonacci number by adding the last two Fibonacci
numbers. To start the series, it uses non-local variables a and b
For eg: as initial numbers are 0 and 1, next number will be 0+1 =1 then 1+1 = 2
then 1+2=3 then 2+3 = 5 then 3+5= 8 (summing the last two to generate the next number)

### C) Write a closure that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts
### 5. add
returns sum of 2 numbers
### 6. mul
returns products of 2 number
### 7. div
returns division of 2 number
### 8. operator_counter
operator_counter function called to create a closure. cntr is a non local variable and along with func which will take the function name.
### 9. op_cntr
calls function add, mul or div with input parameters and update a global dictionary "operation" having add, mul and div as its keys while calling the respective function
Function call updates the global dictionary named operation and output the result showing how many times this function has been called It also calls respective function(non local variable fn) with given input and returns the output string.
For eg: on calling closure for add function with 1,2 as input for 1st time, the output will be: add has been called 1 times, Result: 1 + 2 = 3

### D) Modify above such that now we can pass in different dictionary variables to update different dictionaries
### 10.     counter_for_user
counter_for_user function called to create a closure for user specific function call counters update through user specific global dictionaries. cntr is a non local variable and along with func which will take the function name. As every closure has its own scope, the counter for each dictionary will be different each closure and hence same counter can be used to update count of function call
### 11. op_countr
Calls function add, mul or div with input parameters and update a global dictionary "operation" having add, mul and div as its keys while calling the respective function. Function call updates the user specific dictionary and output the result showing how many times this function has been called.
It also calls respective function(non local variable fn) with given input and returns the output string.
For eg: on calling closure for add function with 1,2 as input for 1st time, the output will be: add has been called 1 times, Result: 1 + 2 = 3
### E) Modify above such that now we can pass in different dictionary variables to update different dictionaries - Alternative approach
### 12. counter_for_user_alt
counter_for_user_alt function called to create a closure for user specific function call counters update through user specific global dictionaries. cntr is a non local variable and along with func which will take the function name.  As every closure has its own scope, the counter for each dictionary will be different each closure and hence same counter can be used to update count of function call
 ### 13. op_countr_alt
 calls function add, mul or div with input parameters and update a global dictionary "operation" having add, mul and div as its keys while calling the respective function. For eg: on calling closure for add function with 1,2 as input for 1st time, the output will be: add has been called 1 times,
 Result: 1 + 2 = 3

# Below are test cases functions in test_session8.py file.

### 13. test_readme_exists :
Test for readme exists

### 14. test_readme_contents :
Test for readme contents are more than 500 words

### 15. test_readme_proper_description :
Test for all important functions/class described well in your README.md file

### 16. test_readme_file_for_formatting :
Test for readme formatting

### 17. test_indentations :
Test for source code formatting. No tabs but four spaces are used for indentation

### 18. test_function_name_had_cap_letters :
Test for no function is with capitals in source code

### 19. test_docstr_len_check_is_closure:
Test to check the docstr_len_check is a closure

### 20. test_docstr_gt50_invalid_func :
Test to check function can handle invalid function call like a non callable input passed

### 21. test_docstr_gt50_valid_func :
Test to check the doc string is greater than 50 characters for a callable function.

### 22. test_next_fib_num_is_closure :
Test to check the next_fib_num is a closure

### 23. test_next_fib_num_is_valid :
Test to check the numbers generated by next_fib_num is valid

### 24. test_func_counter_is_closure :
Test to check the add_cntr, mul_cntr and div_cntr are valid closure

### 25. test_func_counter_correct_update :
Test to check the valid update for counters in dictionary

### 25. test_func_counter_is_closure :
Test to check the add_cntr, mul_cntr and div_cntr are valid closure

### 26. test_by_user_func_counter_correct_update :
Test to check the valid update for counters in user specific dictionary

### 27. test_func_counter_is_closure_alt :
Test to check the add_cntr, mul_cntr and div_cntr are valid closure for alternative approach

### 28 .test_by_user_func_counter_correct_update_alt :
Test to check the valid update for counters in user specific dictionary for alternative approach
