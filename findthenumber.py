import math

cards = [22, 18, 14, 9, 8, 6, 2, 0]
query = 9
output = 3

test = {
    'input': {
        'numbers': [22, 18, 14, 9, 8, 6, 2, 0],
        'query': 9
    },
    'output': 3
}

def find_the_number(numbers, query):
    # Create a variable which has a placement with the value 0
    placement = 0
    
    # Set up a loop for repetition
    while True:
        
        # Checks if element at the current position matches the query
        if numbers[placement] == query:
            
            # Gives an alert that the card is found! Return and exit the loop.
            return placement
        
        # Increment the position
        placement += 1
        
        # Check if we have reached the end of the array
        if placement == len(numbers):
            
            # Number not found return -1
            return -1


result = find_the_number(test['input']['numbers'], test['input']['query'])
result

result == output
