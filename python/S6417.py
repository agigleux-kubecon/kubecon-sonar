def my_fun(my_dict: dict[str, int]):
    for key in my_dict:
        if key == 'foo':
            my_dict.pop(key) # Noncompliant

def get_dict():
    return {'foo': 1, 'bar': 2}

my_fun(get_dict())         

def my_fun2():
    my_dict = {'foo': 1, 'bar': 2}
    for key in my_dict:
        if key == 'foo':
            my_dict.pop(key) # Noncompliant

def my_fun3():
    my_dict = get_dict()
    for key in my_dict:
        if key == 'foo':
            my_dict.pop(key) # Noncompliant

my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(key)
    if key == 'b':
        my_dict.pop(key) # Noncompliant            


def create_dict():
   return {'a': 1, 'b': 2, 'c': 3}

def dict_retrieved_from_function_call():
    my_dict_from_function_call = create_dict()
    for key in my_dict_from_function_call:
        print(key)
        if key == 'b':
            my_dict_from_function_call.update(key, 0) # Noncompliant       