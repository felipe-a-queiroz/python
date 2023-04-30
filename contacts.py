contacts = {
    'number': 4,
    'students': 
        [
            {'name': 'Sarah Holderness', 'email': 'sarah@example.com'},
            {'name': 'Harry Potter', 'email': 'harry@example.com'},
            {'name': 'Hermione Granger', 'email': 'hermione@example.com'},
            {'name': 'Ron Wasley', 'email': 'ron@example.com'}
        ]
}

print('Student emails:')
for student in contacts['students']:
    print(student.get('email'))