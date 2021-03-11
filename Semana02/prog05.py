#dicionarios
student = {'name': 'Guilherme', 'age': 21, 'courses': ['Math', 'CompSci']}
print(student['name'])
student['phone'] = '111-111'
print(student.get('phone','not found'))
print(student.items())
print('\n')
for key, value in student.items():
    print(key, value)