import AI
import time
import tracemalloc
import Environment
import MinizincConverter
import CSVWriter
import PlotCreator

tracemalloc.start()
start_time = time.time()
training = AI.train()
time = round(time.time() - start_time, 2)
print("--- %s seconds ---" % time)
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 1000000}MB; Peak was {peak / 1000000}MB")
tracemalloc.stop()
#MinizincConverter.create_datafile()
CSVWriter.save_to_CSV(Environment.coordinates, AI.seed, training[1], training[2], time, peak / 1000000)
#PlotCreator.plot_learning_curve("Tests/Dataset d1-50/Seed 1/Episodes 500/belgium-d1-n50@1@1320,14s@39,436195mb.csv")
