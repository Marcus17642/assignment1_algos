import random
import time
import statistics
import datetime
import csv


def fut(case):
    h, n = case  # Unpack the case: h is the sorted list, n is the number to find
    l = 0  # Left pointer for binary search
    r = len(h)  # Right pointer for binary search
    while r > l:
        time.sleep(0.0001)  # Artificial delay to make measurements easier
        m = (r + l) // 2  # Calculate the middle index
        if h[m] == n:  # If the middle element is the target
            return m  # Return the index
        elif h[m] > n:  # If the middle element is greater than the target
            r = m  # Move the right pointer to the middle
        else:  # If the middle element is less than the target
            l = m + 1  # Move the left pointer to just after the middle
    # If the loop completes without finding the element, it's not in the list


def casemaker(size):
    # Generate a random start value for the range
    start = random.randint(1, 10 * size) + size
    # Generate a random step size for the range
    step = random.randint(1, 10)
    # Create a range object with approximately 'size' elements
    oof = range(start, start + (size + 2) * step, step)
    # Return the range and a random element from it
    return [oof, oof[random.randint(1, len(oof)) - 1]]


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

#why is andrei running for so many hours?

def run_experiments(sizes, num_samples):
    results = []
    # Open a CSV file to write results
    with open('experiment_results_routine1.csv', 'w', newline='') as f:
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
    10000, 20000, 50000, 100000, 200000, 500000, 
    1000000, 2000000, 5000000, 10000000
]  # Adjusted sizes for routine_1
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
with open('experiment_results_routine1.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Experiment started at", start_time])
    writer.writerow(["Experiment ended at", end_time])
    writer.writerow(["Total duration", duration])
