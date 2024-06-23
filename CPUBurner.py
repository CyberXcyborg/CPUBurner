import multiprocessing
import time

class CPUBurner:
    def __init__(self):
        self.running = False
        self.num_processes = multiprocessing.cpu_count()  # Get number of CPU cores

    def burn_cpu(self):
        self.running = True
        while self.running:
            processes = []
            for _ in range(self.num_processes):
                p = multiprocessing.Process(target=self.compute_task)
                p.start()
                processes.append(p)
            
            for p in processes:
                p.join()

    def compute_task(self):
        start_time = time.time()
        prime_count = 0
        num = 2
        while time.time() - start_time < 5:  # Simulate intensive computation for 5 seconds
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_count += 1
            num += 1

    def start(self):
        multiprocessing.Process(target=self.burn_cpu).start()

    def stop(self):
        self.running = False

def main():
    burner = CPUBurner()
    burner.start()

    input("Press Enter to stop burning CPU...")

    burner.stop()
    print("CPU burning stopped.")

if __name__ == '__main__':
    main()
