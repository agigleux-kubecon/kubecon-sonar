def my_fun_inside_function():
    my_dict = {'foo': 1, 'bar': 2}
    for key in my_dict:
        if key == 'foo':
            my_dict.pop(key) # Noncompliant
       
def create_dict():
   return {'a': 1, 'b': 2, 'c': 3}

def dict_retrieved_from_function_call():
    my_dict = create_dict()
    for key in my_dict:
        print(key)
        if key == 'b':
            my_dict.update(key, 0) # Noncompliant       

def my_fun_as_parameter(my_dict: dict[str, int]):
    for key in my_dict:
        if key == 'b':
            my_dict.pop(key) # Noncompliant (soon)

my_fun_as_parameter(create_dict())     
