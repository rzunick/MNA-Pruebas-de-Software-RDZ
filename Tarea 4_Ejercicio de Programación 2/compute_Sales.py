"""
This calculates the total sales from product catalog and sales records provided as JSON files.
"""

import json
import sys
import time

def load_json_file(filename):
    """
    Load JSON data from a file.
    Args:
        filename (str): The path to the file to be loaded.  
    Returns:
        dict or None: The loaded JSON data, or None if an error occurs.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except json.JSONDecodeError:
        print(f"Error: File '{filename}' contains invalid JSON.")
    return None

def calculate_total_sales(prices, sales):
    """
    Calculate the total sales cost.
    Args:
        prices (dict): A dictionary of product prices.
        sales (list): A list of sales records.
    Returns:
        float: The total sales cost.
    """
    total_cost = 0
    prices_dict = {product["title"]: product["price"] for product in prices}
    for sale in sales:
        product_title = sale.get('Product')
        quantity = sale.get('Quantity', 0)
        product_price = prices_dict.get(product_title)
        if product_price is not None:
            total_cost += product_price * quantity
        else:
            print(f"Warning: Product '{product_title}' not found in the catalogue.")
    return total_cost

def write_results_to_file(filename, total_cost, elapsed_time):
    """
    Write the sales results to a file.
    Args:
        filename (str): The name of the file where results will be saved.
        total_cost (float): The total sales cost.
        elapsed_time (float): The time elapsed during the calculation.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"Total Sales Cost: ${total_cost:.2f}\n")
        file.write(f"Time Elapsed: {elapsed_time:.2f} seconds\n")

def main():
    """
    Main function to orchestrate the calculation of total sales from provided JSON files.
    """
    if len(sys.argv) != 3:
        print("Usage: python compute_sales.py priceCatalogue.json salesRecord.json")
        sys.exit(1)
    prices_file_path = sys.argv[1]
    sales_file_path = sys.argv[2]
    start_time = time.time()
    prices_data = load_json_file(prices_file_path)
    sales_data = load_json_file(sales_file_path)

    if prices_data is None or sales_data is None:
        return

    total_cost = calculate_total_sales(prices_data, sales_data)
    elapsed_time = time.time() - start_time

    print(f"Total Sales Cost: ${total_cost:.2f}")
    print(f"Time Elapsed: {elapsed_time:.2f} seconds")

    write_results_to_file('SalesResults.txt', total_cost, elapsed_time)

if __name__ == '__main__':
    main()
