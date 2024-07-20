import threading
import time

class BackgroundTask(threading.Thread):
    def run(self):
        while True:
            print("Background task is runnning")
            time.sleep(2)

def main():
    daemonThread = BackgroundTask()
    daemonThread.daemon = True
    daemonThread.start()

    for i in range(5):
        print(f"Iterations : {i}")
        time.sleep(1)
    print("Main program Finished")

if __name__ == "__main__":
    main()

