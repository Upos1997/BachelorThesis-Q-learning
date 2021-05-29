# Convert the current environment to a minzinc datafile
import Environment


def create_datafile():
    k = Environment.max_vehicles
    n = len(Environment.environment) - 1
    print("N = " + str(n) + ";")
    print("K = " + str(k) + ";")
    print(('Distance = [|' + '\n|'.join([', '.join(['{:4}'.format(item) for item in row])
                                         for row in Environment.environment]) + '|];').replace(" ", ""))
