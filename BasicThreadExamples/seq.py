import time

def method1():
    for i in range(5):
        print(f"Execution 1: {i}")
        time.sleep(1)

def method2():
    for i in range(5):
        print(f"Execution 2: {i}")
        time.sleep(1)
def main():
    print(" First method execution")
    method1()

if __name__ == "__main__":
    main()
