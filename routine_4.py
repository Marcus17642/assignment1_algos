import random
import time
import statistics
import datetime
import csv

def fut(case):
    fut2(case, 0, len(case) - 1)
    return case

def fut2(case, s, t):
    if t < s:
        return
    if case[s] > case[t]:
        case[s], case[t] = case[t], case[s]
    if t > s + 1:
        q = (t - s + 1) // 3
        fut2(case, s, t - q)
        fut2(case, s + q, t)
        fut2(case, s, t - q)

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
    # Open a CSV file to write results
    with open('experiment_results_routine4.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        # Write header
        writer.writerow(["Size", "Mean Time (s)"])
        
        for size in sizes:
            # Measure performance for each size
            mean_time = measure_performance(size, num_samples)
            # Record results
            results.append((size, mean_time))
            # Format result string
            result_str = f"Size: {size}, Mean time: {mean_time:.6f}s"
            # Print results to console
            print(result_str)
            # Write results to CSV
            writer.writerow([size, mean_time])
            # Flush the file to ensure it's written immediately
            f.flush()
    return results

# Example usage
sizes = [
    100, 200, 500, 1000, 2000, 5000, 
    10000, 20000, 50000, 100000, 200000, 500000
]  # Adjusted sizes for routine_4
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
with open('experiment_results_routine4.txt', 'a') as f:
    f.write(f"\nExperiment started at: {start_time}\n")
    f.write(f"Experiment ended at: {end_time}\n")
    f.write(f"Total duration: {duration}\n")
