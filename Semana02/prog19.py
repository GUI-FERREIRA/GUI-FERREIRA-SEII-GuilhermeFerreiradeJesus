li = [15,2,26,3,4,10]

l2 = sorted(li)
print(l2)
li.sort()
print(li)

s_li = sorted(li, reverse = True)
print(s_li)

class Employee():
    def __init__(self, name, age, salary):
        self.name =name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{}.${})'.format(self.name, self.age, self.salary)

e1 = Employee('Carl', 37,70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('Jonh', 43, 90000)

employees= [e1, e2, e3]
def e_sort(emp):
    return emp.age

s_employees = sorted(employees, key=e_sort)
print(s_employees)