data={
    'name' : 'Ashrit',
    'age' : '18',
    'gender' : 'male',
    'dob' : '29/01/2004'
}

print(data)

print('\n')

x=data.get('dob')
print(x)

print('\n')

print(data['name'])





string={
    "name"   :    "My name is Ashrit",
    'gender' :    "i am Male",
    'dob'    :  'I was born on 29 Jan 2004'
}

print(string['name'])
print(string)
y=data["dob"]
print(y)
data= input("Enter a word: ")
print("Data:", string.get(data, "not found"))