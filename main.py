import AI
import time
import tracemalloc
import Environment
import MinizincConverter
import CSVWriter

from Environment import max_vehicles, environment

tracemalloc.start()
start_time = time.time()
training = AI.train()
time = round(time.time() - start_time, 2)
print("--- %s seconds ---" % time)
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 1000000}MB; Peak was {peak / 1000000}MB")
tracemalloc.stop()
# MinizincConverter.create_datafile()
#CSVWriter.save_to_CSV(Environment.coordinates, AI.seed, training[1], training[2], time, peak / 1000000)
