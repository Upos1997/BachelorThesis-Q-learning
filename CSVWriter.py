import csv

# / save_to_CSV
# Input: dataset(String), seed(Int), solutions(array(array(Int))), solutionvalues(array(Float)),
#        time(Float in seconds), datasize(Float in MB)
# Output: None
# Explanation: Creates a CSV file with name [dataset]@[seed]@[time]s@[datasize]MB.csv
#              and saves the given learning data to it.
def save_to_CSV(dataset, seed, solutions, solutionvalues, time, datasize):
    filename = (str(dataset) + '@' + str(seed) + '@' + str(time) + 's@' + str(datasize) + 'mb').replace(".",
                                                                                                              ",") + ".csv"
    with open(filename, 'x') as save_file:
        fieldnames = ['iteration', 'solution', 'solutionvalue']
        save_writer = csv.DictWriter(save_file, fieldnames=fieldnames)
        save_writer.writeheader()
        for iteration in range(len(solutions)):
            solution = solutions[iteration]
            value = solutionvalues[iteration]
            save_writer.writerow({'iteration': iteration, 'solution': solution, 'solutionvalue': value})
