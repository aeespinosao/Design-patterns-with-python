"""
Builder Coding Exercise
You are asked to implement the Builder design pattern for rendering simple chunks of code.
Sample use of the builder you are asked to create:
cb = CodeBuilder('Person').add_field('name', '""') \
                          .add_field('age', '0')
print(cb)
The expected output of the above code is:
class Person:
  def __init__(self):
    self.name = ""
    self.age = 0
Please observe the same placement of spaces and indentation.
"""
class CodeBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.fields = []

    def add_field(self, type, name):
        self.fields.append((type, name))
        return self

    def __str__(self):
        response = "class {}:\n".format(self.root_name)
        if self.fields:
            response += "  def __init__(self):\n"
            for field in self.fields:
                print(field)
                response += "    self.{} = {}\n".format(field[0], field[1])
        else:
            response += "  pass"
        return response