import random, threading, time

def print_numbers():
    for i in range(1, 11):
        print(f"print_numbers: {i}")
        time.sleep(random.randint(1, 10) / 100)

def print_letters():
    for letter in 'ABCDEFGHIJ':
        print(f"print_letters: {letter}")
        time.sleep(random.randint(1, 10) / 100)

# Create two threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Done")
