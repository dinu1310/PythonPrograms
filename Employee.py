class Employee:
    noOfLeaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def print_details(self):
        return f" the name is {self.name} and salary is {self.salary} and role is {self.role} and no of leaves {self.noOfLeaves}"

    @classmethod  # Alternate constructor
    def ChangeNoOfLeaves(cls, nol):
        cls.noOfLeaves = nol

    @classmethod  # Alternate constructor
    def FromStr(cls, string):
        return cls(*string.split("-"))
        # param=string.split("-")
        # return cls(param[0],param[1],param[2])

    @staticmethod
    def printfile(str):  # can be called by class as well as object
        print("this is good ", str)
        return "Thenga"


class Programmer(Employee):  # Single level Inheritance
    def printProg(self):
        return f" The Programmer's name is {self.name} and salary is {self.salary} and role is {self.role} and no of leaves {self.noOfLeaves}"


# pass--> it is used to paas console if there is no argument in if block or in class
harry = Employee("harry", 13000, "data engineer")
# harry.ChangeNoOfLeaves(23)
# print(harry.print_details())
# print(harry.noOfLeaves)
# karan = Employee.FromStr("karan-1700-UI/UX")
# print(karan.salary)
# print(karan.printfile("dinu"))
karan = Programmer("karan", "6754", "python developer")
print(karan.printProg())
