import random
import time
import statistics
import datetime
import csv

def fut(case):
    i = 1
    while i < len(case):
        if i == 0 or case[i] >= case[i - 1]:
            i += 2
        else:
            case[i], case[i - 1] = case[i - 1], case[i]
        i -= 1
    return case

def casemaker(size):
    return [random.randint(0, 1e9) for _ in range(size)]

def measure_performance(size, num_samples):
    times = []
    for _ in range(num_samples):
        case = casemaker(size)  # Generate a case of the given size
        start_time = time.perf_counter()  # Start timing
        fut(case)  # Run the function under test
        end_time = time.perf_counter()  # End timing
        times.append(end_time - start_time)  # Record the elapsed time
    
    # Calculate statistics
    mean_time = statistics.mean(times)
    
    return mean_time

def run_experiments(sizes, num_samples):
    results = []
    # Open a file to write results
    with open('experiment_results_routine3.txt', 'w') as f:
        # Write header
        f.write("Size,Samples,Mean Time (s)\n")
        
        for size in sizes:
            # Measure performance for each size
            mean_time = measure_performance(size, num_samples)
            # Record results
            results.append((size, num_samples, mean_time))
            # Format result string
            result_str = f"Size: {size}, Mean time: {mean_time:.6f}s"
            # Print results to console
            print(result_str)
            # Write results to file
            f.write(f"{size},{num_samples},{mean_time:.6f}\n")
            # Flush the file to ensure it's written immediately
            f.flush()
    return results

#this does take a while to run
# Example usage
sizes = [
    100, 200, 500, 1000, 2000, 5000, 
    10000, 20000, 50000, 100000, 200000, 500000
]  

"""
sizes = [
    100, 200, 300, 400, 500, 600, 700, 800, 900, 
    1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 
    5000, 7500, 10000, 15000, 20000, 25000, 30000, 
    40000, 50000, 75000, 100000, 150000, 200000, 
    250000, 300000, 400000, 500000, 750000, 1000000, 
    1500000, 2000000, 2500000, 3000000, 4000000, 5000000, 
    7500000, 10000000, 15000000, 20000000, 30000000, 
    40000000, 50000000, 75000000, 100000000, 
    
]
"""
# Adjusted sizes for routine_3
num_samples = 100  # Number of samples to take for each size

# Record start time
start_time = datetime.datetime.now()
print(f"Experiment started at: {start_time}")

results = run_experiments(sizes, num_samples)

# Record end time and calculate duration
end_time = datetime.datetime.now()
duration = end_time - start_time
print(f"Experiment ended at: {end_time}")
print(f"Total duration: {duration}")

# Write summary to file
with open('experiment_results_routine3.txt', 'a') as f:
    f.write(f"\nExperiment started at: {start_time}\n")
    f.write(f"Experiment ended at: {end_time}\n")
    f.write(f"Total duration: {duration}\n")
