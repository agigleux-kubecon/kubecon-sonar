class A:
    def foo(self):
        print("A")

def cross_procedural():
    d = dict(**create_A()) # Noncompliant

def create_A():
    return A()