import threading
import time

# Global counter
counter = 0

# Number of increments per thread
num_increments = 10000

def increment_counter():
    global counter
    for _ in range(num_increments):
        current_value = counter
        time.sleep(0.00001)  # Small delay to increase chance of race condition
        counter = current_value + 1

def main():
    global counter

    # Reset the counter
    counter = 0

    # Create multiple threads
    threads = []
    for _ in range(10):  # Increase the number of threads
        thread = threading.Thread(target=increment_counter)
        threads.append(thread)

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Print the final value of the counter
    print(f"Final counter value: {counter}")
    print(threads)

if __name__ == "__main__":
    main()
