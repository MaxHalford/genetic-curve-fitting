import numpy as np

def degreesCounter(array):
    # Differences
    FO = [array[i] - array[i-1] for i in range(1, len(array))]
    # Differences of differences
    SO = [FO[i] - FO[i-1] for i in range(len(FO))]
    # Use the signs to compare the differences
    FO = np.sign(FO)
    SO = np.sign(SO)
    # Count changes
    degrees = [1 if FO[i] != FO[i-1] or SO[i] != SO[i-1] else 0 for i in range(1, len(SO))]
    return np.sum(degrees)
