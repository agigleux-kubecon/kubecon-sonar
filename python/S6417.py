def create_dict():
   return {'a': 1, 'b': 2, 'c': 3}

def dict_retrieved_from_function_call():
    my_dict = create_dict()
    for key in my_dict:
        print(key)
        if key == 'b':
            my_dict.update(key, 0) # Noncompliant
            