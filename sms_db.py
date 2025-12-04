import sqlite3
import pandas as pd
import streamlit as st

# Page config
st.set_page_config(page_title="Students management", layout="wide")
st.title("Student Management System")

# Initialize database
def init_db():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    
    # Create tables if not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            birth_date DATE,
            email TEXT UNIQUE,
            department_id INTEGER
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            course_id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT NOT NULL,
            department_id INTEGER,
            professor_id INTEGER
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS enrollments (
            enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            course_id INTEGER,
            enrollment_date DATE,
            grade TEXT,
            FOREIGN KEY(student_id) REFERENCES students(student_id),
            FOREIGN KEY(course_id) REFERENCES courses(course_id)
        )
    ''')
    conn.commit()
    return conn

# Initialize DB
conn = init_db()
cursor = conn.cursor()

# Sidebar menu
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a section", [
    "Add Student", "View Students", "Update/Delete Student",
    "Add Course", "View Courses", "Update/Delete Course",
    "Enroll Student", "View Enrollments"
])

# ===================== STUDENTS =====================
if page == "Add Student":
    st.header("Add New Student")
    with st.form("add_student_form"):
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        birth_date = st.date_input("Birth Date")
        email = st.text_input("Email")
        department_id = st.number_input("Department ID", min_value=1, step=1)
        submit = st.form_submit_button("Add Student")

        if submit:
            try:
                cursor.execute('''
                    INSERT INTO students (first_name, last_name, birth_date, email, department_id)
                    VALUES (?, ?, ?, ?, ?)
                ''', (first_name, last_name, birth_date, email, department_id))
                conn.commit()
                st.success("Student added successfully!")
            except sqlite3.IntegrityError:
                st.error("Email already exists!")

elif page == "View Students":
    st.header("All Students")
    df = pd.read_sql_query("SELECT * FROM students", conn)
    if df.empty:
        st.info("No students found.")
    else:
        st.dataframe(df, use_container_width=True)

elif page == "Update/Delete Student":
    st.header("Update or Delete Student")
    student_id = st.number_input("Student ID", min_value=1, step=1)
    action = st.selectbox("Action", ["Update Email", "Delete Student"])

    if action == "Update Email":
        new_email = st.text_input("New Email")
        if st.button("Update"):
            cursor.execute("UPDATE students SET email = ? WHERE student_id = ?", (new_email, student_id))
            if cursor.rowcount > 0:
                conn.commit()
                st.success("Updated successfully!")
            else:
                st.error("Student not found!")

    elif action == "Delete Student":
        if st.button("Delete", type="primary"):
            cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
            if cursor.rowcount > 0:
                conn.commit()
                st.success("Student deleted!")
            else:
                st.error("Student not found!")

# ===================== COURSES =====================
elif page == "Add Course":
    st.header("Add New Course")
    with st.form("add_course"):
        course_name = st.text_input("Course Name")
        dept_id = st.number_input("Department ID", min_value=1)
        prof_id = st.number_input("Professor ID", min_value=1)
        if st.form_submit_button("Add Course"):
            cursor.execute("INSERT INTO courses (course_name, department_id, professor_id) VALUES (?, ?, ?)",
                           (course_name, dept_id, prof_id))
            conn.commit()
            st.success("Course added!")

elif page == "View Courses":
    st.header("All Courses")
    df = pd.read_sql_query("SELECT * FROM courses", conn)
    st.dataframe(df if not df.empty else "No courses yet.", use_container_width=True)

elif page == "Update/Delete Course":
    st.header("Update/Delete Course")
    course_id = st.number_input("Course ID", min_value=1)
    action = st.selectbox("Action", ["Update Name", "Delete"])

    if action == "Update Name":
        new_name = st.text_input("New Course Name")
        if st.button("Update"):
            cursor.execute("UPDATE courses SET course_name = ? WHERE course_id = ?", (new_name, course_id))
            conn.commit()
            st.success("Updated!" if cursor.rowcount else "Not found!")

    if action == "Delete":
        if st.button("Delete Course", type="primary"):
            cursor.execute("DELETE FROM courses WHERE course_id = ?", (course_id,))
            conn.commit()
            st.success("Deleted!" if cursor.rowcount else "Not found!")

# ===================== ENROLLMENTS =====================
elif page == "Enroll Student":
    st.header("Enroll Student in Course")
    with st.form("enroll_form"):
        student_id = st.number_input("Student ID", min_value=1)
        course_id = st.number_input("Course ID", min_value=1)
        enrollment_date = st.date_input("Enrollment Date")
        grade = st.text_input("Grade (optional)", placeholder="e.g. A-, B+")
        if st.form_submit_button("Enroll"):
            cursor.execute('''
                INSERT INTO enrollments (student_id, course_id, enrollment_date, grade)
                VALUES (?, ?, ?, ?)
            ''', (student_id, course_id, enrollment_date, grade or None))
            conn.commit()
            st.success("Enrollment successful!")

elif page == "View Enrollments":
    st.header("All Enrollments")
    df = pd.read_sql_query('''
        SELECT e.*, s.first_name, s.last_name, c.course_name 
        FROM enrollments e
        JOIN students s ON e.student_id = s.student_id
        JOIN courses c ON e.course_id = c.course_id
    ''', conn)
    st.dataframe(df if not df.empty else "No enrollments yet.", use_container_width=True)

# Close connection when done (optional, Streamlit keeps script running)
# conn.close()