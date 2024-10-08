import threading

# Shared variable
counter = 0
lock = threading.Lock()

# Function to increment the counter
def increment():
    global counter, lock
    for _ in range(1000000):
        lock.acquire()
        counter += 1
        lock.release()

# Create multiple threads
threads = []
for _ in range(10):
    t = threading.Thread(target=increment)
    threads.append(t)

# Start the threads
for t in threads:
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

# Print the final value of the counter
print("Counter:", counter)