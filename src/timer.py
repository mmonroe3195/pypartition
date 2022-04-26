import datetime
from partitioning import *
import random
NUM_ITERATIONS = 3

def average_time(algorithm, points):
    """call hull_algorithm on points repeatedly and return average time"""
    time_diff = None

    for iteration in range(0, NUM_ITERATIONS):
        points_copy = points[:]
        start = datetime.datetime.now()
        algorithm(points_copy, 28)
        end = datetime.datetime.now()
        if time_diff == None:
            time_diff = end - start
        else:
            time_diff = time_diff + end - start

    time_ms = time_diff.microseconds // 1000
    time_ms = time_ms + time_diff.seconds * 1000
    time_ms = time_ms + time_diff.days * 24 * 60 * 60 * 1000

    return time_ms

def get_table_entry(num_points, item):
    """get the appropriate table entry, which is either a number of points
       or a running time"""
    points = [(random.random(), random.random()) for i in range(num_points)]
    if item == "n":
        return num_points

    elif item == "chan":
        return average_time(chan_partitions2, points)

    return -1

def build_header_and_legend(option):
    """construct the header entries, which are also used to fill table entries"""
    # always print n (number of vertices)
    header = ["n", "chan"]

    print("Legend:")
    print("    n      : the number of points")
    print("    chan   : the running time of the chan algorithm (in ms)")

    if option == "hullsize":
        header.append("h")
        print("    h      : the number of points on the convex hull")

    print("")

    return header

def run_experiment(option):
    """run the timing experiement according to the user-supplied option"""
    header = build_header_and_legend(option)

    for item in header:
        print("{:>15} ".format(item), end="")
    print("")

    for i in range(4,35):
        size = 2**i
        for item in header:
            print("{:>15} ".format(get_table_entry(size, item)), end="")
        print("")

def main():
    """Get user input and run appropriate timing experiment."""
    print("Welcome to Chan Timer! Press Ctrl+C at any time to end...")

    option = input("Type same to start the experiment. ")
    while option != "same":
        print("Unrecognized option '", option, "'")
        option = input("Type same to start the experiment: ")

    if option == "same":
        print("Running algorithm with n points.")

    else:
        print("This shouldn't happen...")

    run_experiment(option)

if __name__ == "__main__":
    main()
