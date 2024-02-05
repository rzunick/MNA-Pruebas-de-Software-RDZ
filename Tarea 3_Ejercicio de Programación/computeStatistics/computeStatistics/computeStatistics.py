import sys
import time

class ComputeStatistics:
    """
    This class computes descriptive statistics from a file containing numbers.
    """

    def __init__(self, filename):
        """
        Initializes ComputeStatistics object with the given filename.
        """
        self.filename = filename
        self.data = []
        self.mean = None
        self.median = None
        self.mode = None
        self.std_dev = None
        self.variance = None

    def read_file(self):
        """
        Reads data from the file and populates the data list.
        """
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                for line in file:
                    try:
                        num = float(line.strip())
                        self.data.append(num)
                    except ValueError:
                        print(f"Invalid data found: {line.strip()}")
        except FileNotFoundError:
            print("File not found.")
            sys.exit(1)

    def compute_statistics(self):
        """
        Computes descriptive statistics.
        """
        start_time = time.time()
        num_items = len(self.data)
        self.mean = sum(self.data) / num_items
        sorted_data = sorted(self.data)
        mid = num_items // 2
        if num_items % 2 == 0:
            self.median = (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            self.median = sorted_data[mid]
        counts = {}
        for num in self.data:
            counts[num] = counts.get(num, 0) + 1
        max_freq = max(counts.values())
        self.mode = [num for num, freq in counts.items() if freq == max_freq]
        self.std_dev = (sum((x - self.mean) ** 2 for x in self.data) / num_items) ** 0.5
        self.variance = self.std_dev ** 2
        end_time = time.time()
        return end_time - start_time

    def display_results(self, elapsed_time):
        """
        Displays descriptive statistics.
        """
        print("Descriptive Statistics:")
        print(f"Mean: {self.mean}")
        print(f"Median: {self.median}")
        print(f"Mode: {self.mode}")
        print(f"Standard Deviation: {self.std_dev}")
        print(f"Variance: {self.variance}")
        print(f"Time elapsed: {elapsed_time} seconds")

    def save_results_to_file(self, elapsed_time):
        """
        Saves descriptive statistics to a file.
        """
        with open("StatisticsResults.txt", 'w', encoding='utf-8') as file:
            file.write("Descriptive Statistics:\n")
            file.write(f"Mean: {self.mean}\n")
            file.write(f"Median: {self.median}\n")
            file.write(f"Mode: {self.mode}\n")
            file.write(f"Standard Deviation: {self.std_dev}\n")
            file.write(f"Variance: {self.variance}\n")
            file.write(f"Time elapsed: {elapsed_time} seconds\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python compute_statistics.py fileWithData.txt")
        sys.exit(1)
    filename = sys.argv[1]
    compute_stats = ComputeStatistics(filename)
    compute_stats.read_file()
    elapsed_time = compute_stats.compute_statistics()
    compute_stats.display_results(elapsed_time)
    compute_stats.save_results_to_file(elapsed_time)
    