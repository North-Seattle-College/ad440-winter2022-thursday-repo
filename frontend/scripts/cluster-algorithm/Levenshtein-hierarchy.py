import Levenshtein
import numpy as np
import scipy.cluster.hierarchy
import matplotlib.pyplot as plt

# USING TEST JSON FILE
import json
with open('test-teacher-comments.json', 'r') as f:
    masterList = json.load(f)
# USING TEST JSON FILE

# Returns the distance between words i and j using the Levenshtein distance formula
def distance(coord):
    i, j = coord
    return Levenshtein.distance(masterList[i], masterList[j])

# Clusters the data of the given string list
def cluster(StringList):
    # Use "numpy.triu_indices" to get the coordinates of the upper triangle. (numbers in the brackets [])
    #         │String1 String2 String3  String4 ...
    # ────────┼────────────────────────────────────
    # String1 │   0      [1]      [2]     [3]  [...]
    # String2 │   1       0       [4]     [5]  [...]
    # String3 │   2       4        0      [6]  [...]
    # String4 │   3       6        5       0   [...]
    #   ...   |  ...     ...      ...     ...    0   
    trianlge = np.triu_indices(len(StringList), 1)

    # Use "numpy.apply_along_axis" to apply the distance function to the coordinates of the upper triangle
    distanceData = np.apply_along_axis(distance, 0, trianlge)

    # Pass this data array to "scipy.cluster.hierarchy.linkage" to create the cluster
    rawClusterData = scipy.cluster.hierarchy.linkage(distanceData)

    # return the raw cluster data
    return rawClusterData

# Returns the original list in the order according to the raw clustered data
def orderedList(order):
    newList = []
    for s in order:
        newList.append(masterList[s].replace('$','')) # String that end wiht "$" crash matplotlib
    return newList

# Plot and graph the cluster data into a visual representation  
def plotData(rawClusterData):
    dn = scipy.cluster.hierarchy.dendrogram(rawClusterData)
    locs, labels = plt.xticks()  # Get the current locations and labels.
    plt.xticks(locs, orderedList(dn['leaves']))  # Set text labels and properties.
    plt.xlabel('Teacher Comments')
    plt.ylabel('Distance Level')
    plt.title("Hierarchy Cluster Plot")
    plt.show()

# main fucntion of script
def main():
    plotData(cluster(masterList))

main()