"""Main program for the Student Performance Analytics System."""

from pathlib import Path
import pandas as pd
from functions import (
    SUBJECTS,
    calculate_student_results,
    get_class_summary,
    get_subject_summary,
    get_top_performers,
    load_student_data,
)


def print_heading(title):
    """Print a clear section heading."""
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def main():
    # Locate the CSV relative to this Python file so the program works from any folder.
    dataset_path = Path(__file__).parent / "data" / "students.csv"

    try:
        students = load_student_data(dataset_path)
    except (FileNotFoundError, ValueError) as error:
        print(f"Could not load student data: {error}")
        return

    print_heading("STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print(f"Dataset loaded successfully: {len(students)} student records")
    print("\nPreview of student data:")
    print(students.head().to_string(index=False))
    print(f"\nDataset shape: {students.shape[0]} rows × {students.shape[1]} columns")

    results = calculate_student_results(students)

    print_heading("INDIVIDUAL STUDENT RESULTS")
    display_columns = [
        "Student_ID", "Name", "Department", "Total_Marks",
        "Average_Marks", "Grade", "Result", "Attendance"
    ]
    print(results[display_columns].to_string(index=False))

    summary = get_class_summary(results)
    print_heading("CLASS SUMMARY")
    print(f"Number of students      : {summary['student_count']}")
    print(f"Overall class average   : {summary['class_average']} / 100")
    print(f"Highest student average : {summary['highest_average']} / 100")
    print(f"Lowest student average  : {summary['lowest_average']} / 100")
    print(f"Students passed         : {summary['pass_count']}")
    print(f"Students failed         : {summary['fail_count']}")
    print(f"Pass percentage         : {summary['pass_percentage']}%")
    print(f"Average attendance      : {summary['attendance_average']}%")

    print_heading("SUBJECT-WISE PERFORMANCE")
    subject_summary = get_subject_summary(students)
    print(subject_summary.to_string(index=False))
    best_subject = subject_summary.loc[subject_summary["Average"].idxmax(), "Subject"]
    weakest_subject = subject_summary.loc[subject_summary["Average"].idxmin(), "Subject"]
    print(f"\nBest-performing subject   : {best_subject}")
    print(f"Lowest-average subject    : {weakest_subject}")

    print_heading("TOP 3 PERFORMING STUDENTS")
    top_students = get_top_performers(results, count=3)
    print(top_students[["Student_ID", "Name", "Department", "Average_Marks", "Grade"]].to_string(index=False))

    print_heading("DEPARTMENT-WISE AVERAGE")
    department_summary = (
        results.groupby("Department")["Average_Marks"]
        .mean()
        .round(2)
        .sort_values(ascending=False)
    )
    print(department_summary.to_string())

    # Save the enriched student results so they can be inspected after running the project.
    output_path = Path(__file__).parent / "student_results.csv"
    results.to_csv(output_path, index=False)
    print(f"\nDetailed results saved to: {output_path.name}")
    print("\nAnalysis completed successfully.")


if __name__ == "__main__":
    main()
