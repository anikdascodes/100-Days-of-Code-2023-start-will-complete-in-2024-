#Function with more than one input
def greet_with(name,location):
    print(f'Hello {name}')
    print(f'What is it like in {location}?')

#function with positional arguments
greet_with('Anik','India')

#Function with keyword arguments
greet_with(location='India',name='Anik')