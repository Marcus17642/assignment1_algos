import random
import time
import statistics
import datetime
import csv

def fut(case):
    result = 0
    trials = ["1"]
    while True:
        result += 1
        if "".join(trials) == case:
            return result
        i = len(trials) - 1
        while trials[i] == "1":
            trials[i] = "0"
            i -= 1
        if i == -1:
            trials = ["1"] + trials
        else:
            trials[i] = "1"
        if result > 1e24:
            return "WAT"

def casemaker(size):
    return "1" + "".join(random.choices("10", k=size))

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
    with open('experiment_results_routine2.csv', 'w', newline='') as f:
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
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20
]  # Adjusted sizes for routine_2
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

# Write summary to CSV
with open('experiment_results_routine2.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Experiment started at", start_time])
    writer.writerow(["Experiment ended at", end_time])
    writer.writerow(["Total duration", duration])
