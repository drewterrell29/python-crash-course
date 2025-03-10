person = {'first_name': 'Drew', "last_name":"Terrell","age":33,"city":"Dallas","foods":["pizza","hamburger","pasta"]}
person_2 = {'first_name': "John", "last_name":"Calvin","age":33,"city":"Geneva","foods":["pizza","hamburger","pasta"]}
person_3 = {'first_name': "James", "last_name":"Smith","age":45,"city": "New York","foods":["pizza","hamburger","pasta"]}

people = [person, person_2, person_3]

for person in people:
    print(person["first_name"])
    print(f"{person['first_name']}, favorite foods are:")
    for food in person["foods"]:
        print(food)