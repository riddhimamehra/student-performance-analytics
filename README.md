# Student Performance Analytics System

A beginner-friendly Python data-analysis project that uses **Python, NumPy, and Pandas** to summarize student marks, assign grades, determine pass/fail status, and compare student and subject performance.

## Features

- Reads a CSV dataset into a Pandas DataFrame.
- Checks that required columns are present.
- Calculates each student's total and average marks.
- Assigns grades using a documented grading scale.
- Identifies pass/fail status using a clear rule.
- Reports class averages, highest/lowest averages, pass count, fail count, pass percentage, and attendance average.
- Compares subject-wise averages, highest marks, and lowest marks.
- Lists the top three students.
- Calculates department-wise average performance.
- Saves enriched results to `student_results.csv`.

## Technologies and concepts

- Python: variables, data types, functions, loops/iteration, conditions, exception handling, file paths.
- Pandas: CSV loading, DataFrames, row/column calculations, filtering, grouping, sorting, and summaries.
- NumPy: numerical arrays, mean, maximum, and minimum.
- CSV: stores the sample student dataset.

## Project structure

```text
student-performance-analytics/
├── data/
│   └── students.csv
├── main.py
├── functions.py
├── requirements.txt
├── README.md
├── Project_Documentation.md
└── .gitignore
```

`student_results.csv` is generated when you run the program and is excluded from Git by `.gitignore`.

## Dataset

The included sample dataset has 20 fictional students. Columns:

- `Student_ID`: unique student identifier
- `Name`: student name
- `Department`: CSE, AI-ML, IT, or ECE
- `Math`, `Python`, `English`, `Science`: marks out of 100
- `Attendance`: attendance percentage

The records are sample data for educational use, not real student records.

## Grading and pass/fail rules

**Grade based on average marks:**

| Average marks | Grade |
|---:|:---|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| 40–49.99 | E |
| Below 40 | F |

**Pass rule:** a student passes only when their marks are **at least 40 in every subject**. If any subject is below 40, the result is Fail. Attendance is reported separately and does not change the pass/fail result.

## Setup and run

Python 3.10 or newer is recommended.

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Install the required libraries:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Run the program:

   ```bash
   python main.py
   ```

The program prints its analysis in the terminal and writes detailed calculated results to `student_results.csv`.
