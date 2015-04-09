import pandas as pd
from lib.classes import Population
import matplotlib.pyplot as plt
import numpy as np
import time

startTime = time.time()

# Open the data points
df = pd.read_csv('data/test.csv')
function = 'polynomial'

# Create the lookup table
lookupTable = {}
for i, record in df.iterrows():
    key = record['X']
    lookupTable[key] = record[function]

# Parameters
generations = 500
degrees = 5
variables = 1

# Initialize a population
polynomials = Population(degrees, variables)
polynomials.evaluate(lookupTable)

# Go through generations
polynomials.enhance(generations, lookupTable)

# Extract the best polynomial
best = polynomials.best[-1]

# Plot what the polynomial looks like
x = df['X']
y = df[function]

# Display the best polynomial
intercept = 0
print ('The best polynomial found is:')
for index, variable in enumerate(best.values):
    intercept += variable[0]
    for power, coefficient in enumerate(variable[1:]):
        print (str(coefficient) + ' * ' + 'x' + str(index) + \
               '**' + str(power+1) + ' + ')
print (intercept)
print ('------------------------------')
print (str(time.time() - startTime) + " seconds")

# And plot it
plt.subplot(1,2,1)
test = np.linspace(min(x) - 0.1, max(x) + 0.1)
values = [sum(c * x ** p
          for p, c in enumerate(variable))
          for variable in best.values
          for x in test]

plt.plot(test, values)
plt.scatter(x, y, c='red', s=100)
# Plot the evolution of the square errors
plt.subplot(1,2,2)
errors = [indi.fitness for indi in polynomials.best]
plt.plot(errors)
plt.show()
