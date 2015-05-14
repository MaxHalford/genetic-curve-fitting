import pandas as pd
from lib.classes import Population
import matplotlib.pyplot as plt
import numpy as np
import time
from pylab import savefig

plt.style.use('ggplot')

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
generations = 300
degrees = 4
variables = 1

# Initialize a population
polynomials = Population(degrees, variables)
polynomials.evaluate(lookupTable)
polynomials.sort()

# Iterate through generations
for g in range(generations):
    # Enhance the population
    polynomials.enhance(lookupTable)
    # Display the improvement
    polynomials.plot2D(df['X'], df[function], g)
    #savefig('gif/{0}'.format(g))

# Display the final best polynomial



