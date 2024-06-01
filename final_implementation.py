import sys
import argparse
import math
from collections import deque

# Function to get the data from the file
def load_file(f):
    file = open(f, 'r')
    data = file.readline()
    values = data.strip().split()
    for i in range(len(values)):
        values[i] = float(values[i])
    return values
# Viterbi algorithm to identify states
def find_states_viterbi(t, rate=2, penalty=1, debug_mode=False):
    num_points = len(t) - 1
    total_time = t[-1]
    intervals = []
    for i in range(num_points):
        intervals.append(t[i+1] - t[i])

    num_states = math.ceil(1 + math.log(total_time, rate) + math.log(1 / min(intervals), rate))
    avg_interval = total_time / num_points
    lambdas = []
    for i in range(num_states):
        lambdas.append(rate**i / avg_interval)

    cost_matrix = []
    for i in range(num_points + 1):
        cost_row = []
        for j in range(num_states):
            cost_row.append(float('inf'))
        cost_matrix.append(cost_row)
    back_pointer = []
    for i in range(num_states):
        pointer_row = []
        for j in range(num_points + 1):
            pointer_row.append(0)
        back_pointer.append(pointer_row)
    cost_matrix[0][0] = 0
