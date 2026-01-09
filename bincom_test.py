import re
import random
import statistics
from collections import Counter
import psycopg2

# Extracting colours

def extract_colours(html_file):
    with open(html_file, "r") as file:
        content = file.read()

    colours = re.findall(r'\b[A-Z]+\b', content)

    ignore = {
        "DAY", "COLOURS", "MONDAY", "TUESDAY",
        "WEDNESDAY", "THURSDAY", "FRIDAY"
    }

    return [c for c in colours if c not in ignore]


def get_colour_frequency(colours):
    return Counter(colours)


# 1. MEAN COLOUR

def mean_colour(freq):
    mean_value = sum(freq.values()) / len(freq)
    return [c for c, f in freq.items() if f == round(mean_value)]


# 2. MOST WORN COLOUR (Mode)

def most_worn_colour(freq):
    return freq.most_common(1)[0]


# 3. MEDIAN COLOUR

def median_colour(freq):
    sorted_items = sorted(freq.items(), key=lambda x: x[1])
    return sorted_items[len(sorted_items) // 2]


# 4. VARIANCE
def colour_variance(freq):
    return statistics.variance(freq.values())


# 5. PROBABILITY OF RED

def probability_of_red(freq):
    return freq.get("RED", 0) / sum(freq.values())


# 6. SAVING TO POSTGRESQL

def save_to_postgres(freq):
    conn = psycopg2.connect(
        host="localhost",
        database="bincom_test",
        user="postgres",
        password="Flamesyaga"
    )

    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS colour_frequency (
            id SERIAL PRIMARY KEY,
            colour VARCHAR(20),
            frequency INT
        )
    """)

    cur.execute("DELETE FROM colour_frequency")

    for colour, count in freq.items():
        cur.execute(
            "INSERT INTO colour_frequency (colour, frequency) VALUES (%s, %s)",
            (colour, count)
        )

    conn.commit()
    cur.close()
    conn.close()


# 7. RECURSIVE SEARCH

def recursive_search(numbers, target, index=0):
    if index == len(numbers):
        return False
    if numbers[index] == target:
        return True
    return recursive_search(numbers, target, index + 1)


# 8. BINARY TO DECIMAL

def binary_to_decimal():
    binary = ''.join(str(random.randint(0, 1)) for _ in range(4))
    return binary, int(binary, 2)


# 9. SUM OF FIRST 50 FIBONACCI NUMBERS

def sum_fibonacci(n=50):
    a, b = 0, 1
    total = 0
    for _ in range(n):
        total += a
        a, b = b, a + b
    return total


# Main

if __name__ == "__main__":
    html_file = "python_class_question.html"

    colours = extract_colours(html_file)
    freq = get_colour_frequency(colours)

    print("Colour Frequencies:", freq)
    print("1. Mean Colour:", mean_colour(freq))
    print("2. Most Worn Colour:", most_worn_colour(freq))
    print("3. Median Colour:", median_colour(freq))
    print("4. Variance:", colour_variance(freq))
    print("5. Probability of RED:", probability_of_red(freq))

    save_to_postgres(freq)
    print("6. Colours saved to PostgreSQL")

    print("7. Recursive Search:", recursive_search([1, 2, 3, 4, 5], 4))

    binary, decimal = binary_to_decimal()
    print(f"8. Binary: {binary} → Decimal: {decimal}")

    print("9. Sum of first 50 Fibonacci numbers:", sum_fibonacci())
