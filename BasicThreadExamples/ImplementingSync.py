import threading
import time

counter_lock = threading.Lock()
counter = 0
num_counter = 1000

def increment_counter():
    global counter
    for i in range(num_counter):
        with counter_lock:
            counter+=1
        # time.sleep(0.0001)


def main():
    global counter

    counter = 0

    thread1 = threading.Thread(target = increment_counter)
    thread2 = threading.Thread(target = increment_counter)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f"Program ended with counter : {counter}")

if __name__ == "__main__":
    main()



    