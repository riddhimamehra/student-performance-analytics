"""Reusable functions for the Student Performance Analytics System."""

import numpy as np
import pandas as pd

SUBJECTS = ["Math", "Python", "English", "Science"]


def load_student_data(file_path):
    """Load student records from a CSV file into a Pandas DataFrame."""
    df = pd.read_csv(file_path)
    required_columns = ["Student_ID", "Name", "Department", *SUBJECTS, "Attendance"]
    missing_columns = [column for column in required_columns if column not in df.columns]
    if missing_columns:
        raise ValueError(f"Dataset is missing required columns: {missing_columns}")
    if df.empty:
        raise ValueError("The student dataset is empty.")
    return df


def calculate_student_results(df):
    """Add total, average, grade, and pass/fail columns to a copy of the data."""
    results = df.copy()
    results["Total_Marks"] = results[SUBJECTS].sum(axis=1)
    results["Average_Marks"] = np.round(results[SUBJECTS].mean(axis=1), 2)

    def assign_grade(average):
        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        elif average >= 40:
            return "E"
        return "F"

    results["Grade"] = results["Average_Marks"].apply(assign_grade)
    # A student passes only if every subject mark is at least 40.
    results["Result"] = results[SUBJECTS].ge(40).all(axis=1).map(
        {True: "Pass", False: "Fail"}
    )
    return results


def get_subject_summary(df):
    """Return average, highest, and lowest marks for each subject."""
    summary = pd.DataFrame({
        "Subject": SUBJECTS,
        "Average": [round(df[subject].mean(), 2) for subject in SUBJECTS],
        "Highest": [int(df[subject].max()) for subject in SUBJECTS],
        "Lowest": [int(df[subject].min()) for subject in SUBJECTS],
    })
    return summary


def get_class_summary(results):
    """Calculate overall class statistics using Pandas and NumPy."""
    averages = results["Average_Marks"].to_numpy()
    pass_count = int((results["Result"] == "Pass").sum())
    fail_count = int((results["Result"] == "Fail").sum())
    return {
        "student_count": int(len(results)),
        "class_average": round(float(np.mean(averages)), 2),
        "highest_average": round(float(np.max(averages)), 2),
        "lowest_average": round(float(np.min(averages)), 2),
        "pass_count": pass_count,
        "fail_count": fail_count,
        "pass_percentage": round((pass_count / len(results)) * 100, 2),
        "attendance_average": round(float(np.mean(results["Attendance"].to_numpy())), 2),
    }


def get_top_performers(results, count=3):
    """Return the top students ranked by average marks."""
    return results.sort_values(
        by=["Average_Marks", "Name"], ascending=[False, True]
    ).head(count)
