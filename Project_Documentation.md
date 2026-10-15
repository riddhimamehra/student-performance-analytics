# Project Documentation: Student Performance Analytics System

## 1. Project Title and Student Details

**Project title:** Student Performance Analytics System  
**Student name:** Riddhima Mehra  
**Course:** Python with AI  
**Institute/training provider:** EWB Courses  
**GitHub repository:** https://github.com/riddhimamehra/student-performance-analytics
**Submission date:** 15 October 2026

## 2. Objective

The objective of this project is to build a Python-based system that reads student marks and attendance from a CSV file and turns the records into clear, useful summaries. It helps identify individual performance, grades, pass/fail status, subject strengths and areas needing improvement, and top-performing students.

## 3. Technologies Used

- **Python:** program logic, variables, conditions, functions, loops/iteration, and error handling.
- **Pandas:** reads the CSV file into a DataFrame and performs tabular calculations, sorting, grouping, and summaries.
- **NumPy:** performs numerical calculations such as mean, maximum, and minimum.
- **CSV:** stores the sample dataset.

## 4. Dataset Description

The project includes 20 fictional student records in `data/students.csv`. Each row represents one student. The columns are:

| Column | Description |
|---|---|
| Student_ID | Unique student identifier |
| Name | Student name |
| Department | Student's department |
| Math | Marks out of 100 |
| Python | Marks out of 100 |
| English | Marks out of 100 |
| Science | Marks out of 100 |
| Attendance | Attendance percentage |

The dataset uses fictional names and values for demonstration. It can be replaced with a trainer-approved dataset that follows the same column structure.

## 5. Implementation

1. **Load the dataset:** `load_student_data()` reads the CSV file with `pandas.read_csv()` and checks that required columns exist.
2. **Calculate marks:** `calculate_student_results()` adds total marks and average marks for the four subjects.
3. **Assign grades:** a function applies the grading scale to each student's average.
4. **Determine pass/fail:** the student passes only if marks are at least 40 in every subject. Pandas checks the condition across the subject columns.
5. **Calculate class statistics:** NumPy calculates the class average, highest and lowest student averages, and average attendance. Pandas counts pass/fail students and calculates pass percentage.
6. **Analyze subjects:** `get_subject_summary()` calculates each subject's average, highest mark, and lowest mark. The program identifies the highest- and lowest-average subjects.
7. **Find top performers:** `get_top_performers()` sorts students by average marks and returns the top three.
8. **Analyze departments:** Pandas `groupby()` calculates average marks for each department.
9. **Save results:** the final DataFrame is written to `student_results.csv` so the calculated results can be reviewed later.

## 6. Grading and Pass/Fail Rules

Grades are based on average marks across Math, Python, English, and Science:

| Average | Grade |
|---:|:---|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| 40–49.99 | E |
| Below 40 | F |

A student passes only if they score at least 40 marks in every subject. A mark below 40 in even one subject results in Fail. Attendance is summarized separately and does not affect the result.

## 7. Key Features

- CSV dataset loading and validation
- Student total and average calculation
- Grade assignment
- Pass/fail classification
- Class-level statistics and pass percentage
- Subject-wise performance comparison
- Top-three student ranking
- Department-wise average comparison
- Export of calculated results to CSV

## 8. Output / Screenshots

After running `python main.py`, capture screenshots of:
- the student data preview and individual student results;
- the class summary;
- subject-wise performance and top-three students;
- department-wise averages and the successful completion message.

**Note:** Insert your own screenshots here after running the program. Do not claim screenshots or results that you have not verified.

## 9. Final Outcome

The system processes a student dataset and presents readable information about marks, averages, grades, pass/fail status, class performance, subject performance, top students, and department averages. It also saves a results CSV file. The project demonstrates basic Python programming, NumPy numerical calculations, and Pandas-based data analysis without using advanced machine learning.

## 10. Challenges and Learning

**Challenges:** Keeping the calculations consistent, applying the grade rules correctly, checking the dataset structure, and presenting the results clearly.

**How they were handled:** The calculations were separated into reusable functions. The dataset columns are validated before analysis. The grading and pass/fail rules are documented so that the output is understandable.

**Learning outcomes:** I practiced loading CSV data, working with Pandas DataFrames, using NumPy for numerical calculations, writing functions, using conditions and iteration, sorting and grouping data, and documenting a Python project.
