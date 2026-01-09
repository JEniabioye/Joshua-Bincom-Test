### README.md

# Bincom ICT Python Basic Developer Test

## Overview
This Python script analyzes the colors of dresses worn by staff for a week and answers all the questions in the preliminary online test.

The program:
1. Reads the HTML file (`python_class_question.html`) containing color data.
2. Extracts all color names using regex.
3. Computes:
   - Mean color (based on frequency)
   - Most worn color
   - Median color
   - Variance of colors (bonus)
   - Probability of choosing RED at random (bonus)
4. Saves the color frequencies into a PostgreSQL database.
5. Includes bonus tasks:
   - Recursive search
   - Random 4-digit binary → base 10 conversion
   - Sum of first 50 Fibonacci numbers

## Requirements
- Python 3.x
- Libraries: re, random, statistics, collections, psycopg2 (for PostgreSQL integration)
- PostgreSQL database setup

## How to Run
1. Ensure `python_class_question.html` is in the same folder as the script.

2. Install psycopg2 if not installed:
 ```bash
pip install psycopg2-binary
  ```
3. Update PostgreSQL credentials in the script if different from default:
   ```python
   host="localhost"
   database="bincom_test"
   user="postgres"
   password="postgres"

4. Run the script:
 ```bash
python bincom_python_test.py
  ```

The script will print the results for Questions 1–9 and save colour frequencies to PostgreSQL.
## Author

* Eniabioye Joshua A
* Jeniabioye@gmail.com



