import threading
import time

class Method1(threading.Thread):
    def run(self):
        for i in range(5):
            print(f"Execution 1: {i}")
            time.sleep(1)

class Method2(threading.Thread):
    def run(self):
        for i in range(5):
            print(f"Execution 2: {i}")
            time.sleep(1)

def main():
    print("first method")
    thread1 = Method1()
    print("Second method")
    thread2 = Method2()

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()






