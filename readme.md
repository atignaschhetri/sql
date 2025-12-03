## Student Management System Database

## Project Overview

This project implements a complete Student Management System (SMS) database using SQLite.
It manages students, departments, professors, courses, enrollments, and grades in a well-structured relational database.

The system demonstrates how relationships work across multiple academic entities and provides real-world learning of SQL CRUD operations, joins, and constraints.

## Key Features

- Student demographic and academic information

- Department directory with unique IDs

- Professors linked to respective departments

- Courses offered under each department

- Enrollment tracking between students and courses (Many-to-Many)

- Grade recording for each enrolled course

- Foreign key relationships ensuring data integrity

## Sample dataset included for testing and learning

## Database Tables

The SMS database consists of six relational tables:

1. Students

Stores student personal data and department mapping.

2. Departments

Contains the list of all academic departments.

3. Professors

Stores professor details linked to departments.

4. Courses

Contains all available courses with assigned professors.

5. Enrollments

Tracks which student enrolled in which course.

6. Grades

Stores grades received by students in various courses.

## Setup & Installation

## Prerequisites

Ensure this is  installed:

- Python 3.7 or higher

- Jupyter Notebook / VS Code with Notebook support

- SQLite (auto-managed by Python)

- pip (Python package manager)





### Install the requirements .txt to install dependency

```
pip install -r requirements.txt
```

