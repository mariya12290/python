

""" Here self refer to object or instance of class """
class Example:
    def __init__(self,emp):
        self.emp_name = emp

    def introduce(self):
        print("Hello I am "+self.emp_name)

emp = Example("Suri")
emp.introduce()

class ExampleChild(Example):
    def __init__(self, childName):
        Example.emp_name = childName
    def child_func(self):
        print("I am child of employee "+Example.emp_name)

emp_child = ExampleChild("sURI")
emp_child.introduce()
emp_child.child_func()