import threading
import time

def some_long_func(name):
    print(f"hey oh, {name}")
    time.sleep(10)
    print(f"bye, {name}!")

def main():
    print("Starting the program!")
    t = threading.Thread(target=some_long_func, args=["stranger"])
    t.start()
    print("Finishing the program!")

if __name__ == "__main__":
    main()
