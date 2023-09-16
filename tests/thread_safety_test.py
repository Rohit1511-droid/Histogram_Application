import pytest
import threading
from histogram import Histogram  # Import your Histogram class

def insert_samples(histogram, samples):
    histogram.insertSamples(samples)

def test_thread_safety():
    # Create a Histogram instance
    histogram = Histogram()
    histogram.check_consistency([[0, 1.1], [3, 4.1], [8.5, 8.7], [31.5, 41.27]])

    # Generate samples for testing
    samples = [i for i in range(1000)]

    # Define the number of threads for parallel insertions
    num_threads = 4

    # Create threads and start parallel insertions
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=insert_samples, args=(histogram, samples))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Calculate the expected total count of samples
    expected_count = len(samples) * num_threads

    # Check if the histogram contains the expected number of samples
    assert histogram.get_total_count() == expected_count
