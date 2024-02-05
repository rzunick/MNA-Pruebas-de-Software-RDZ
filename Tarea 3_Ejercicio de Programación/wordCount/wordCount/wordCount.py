import sys
import time

def count_words(filename):
    """
    Count the frequency of words in the given file.
    Args:
        filename (str): The name of the file to process.  
    Returns:
        dict: A dictionary containing the frequency of each word.
    """
    word_count = {}
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.split()
                for word in words:
                    word = word.strip()
                    if word:
                        word_count[word] = word_count.get(word, 0) + 1
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as error:
        print(f"An error occurred: {error}")
        return None
    return word_count

def write_results(word_count, elapsed_time):
    """
    Write the word count results to a file.
    Args:
        word_count (dict): A dictionary containing the frequency of each word.
        elapsed_time (float): The time elapsed during the execution.
    """
    with open('WordCountResults.txt', 'w', encoding='utf-8') as result_file:
        for word, count in word_count.items():
            result_file.write(f"{word}: {count}\n")
        result_file.write(f"Time elapsed: {elapsed_time} seconds\n")

def main():
    """
    Main function to execute the word count program.
    """
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        return
    filename = sys.argv[1]
    start_time = time.time()
    word_count = count_words(filename)
    end_time = time.time()
    if word_count is not None:
        for word, count in word_count.items():
            print(f"{word}: {count}")
        elapsed_time = end_time - start_time
        print(f"Time elapsed: {elapsed_time} seconds")
        write_results(word_count, elapsed_time)

if __name__ == "__main__":
    main()
