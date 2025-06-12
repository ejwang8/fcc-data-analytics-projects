import numpy as np

def calculate(list):
    
    numbers = list # just so name list doesn't override
    
    if len(numbers) < 9:
        raise ValueError("List must contain nine numbers.")
    
    flat_array = np.array(numbers)
    square_array = flat_array.reshape(3,3)

    calculations = {
        'mean' : [
            square_array.mean(axis=0).tolist(), # of columns
            square_array.mean(axis=1).tolist(), # of rows
            flat_array.mean().tolist()          # of flattened
        ],
        'variance' : [
            square_array.var(axis=0).tolist(), 
            square_array.var(axis=1).tolist(), 
            flat_array.var().tolist()
        ],
        'standard deviation' : [
            square_array.std(axis=0).tolist(), 
            square_array.std(axis=1).tolist(), 
            flat_array.std().tolist()
        ],
        'max' : [
            square_array.max(axis=0).tolist(), 
            square_array.max(axis=1).tolist(), 
            flat_array.max().tolist()
        ],
        'min' : [
            square_array.min(axis=0).tolist(), 
            square_array.min(axis=1).tolist(), 
            flat_array.min().tolist()
        ],
        'sum' : [
            square_array.sum(axis=0).tolist(), 
            square_array.sum(axis=1).tolist(), 
            flat_array.sum().tolist()
        ],
    }

    return calculations
