// Mock database
let students = [];
let courses = [];
let enrollments = [];

// Student Form
document.getElementById("student-form").addEventListener("submit", function(event) {
    event.preventDefault();

    const firstName = document.getElementById("first-name").value;
    const lastName = document.getElementById("last-name").value;
    const email = document.getElementById("email").value;
    const birthDate = document.getElementById("birth-date").value;
    const departmentId = document.getElementById("department-id").value;

    const student = {
        id: students.length + 1,
        firstName,
        lastName,
        email,
        birthDate,
        departmentId
    };

    students.push(student);
    displayStudents();
});

// Display Students
function displayStudents() {
    const tableBody = document.getElementById("students-table").getElementsByTagName('tbody')[0];
    tableBody.innerHTML = "";

    students.forEach(student => {
        const row = tableBody.insertRow();
        row.innerHTML = `
            <td>${student.id}</td>
            <td>${student.firstName}</td>
            <td>${student.lastName}</td>
            <td>${student.email}</td>
            <td>${student.birthDate}</td>
            <td>${student.departmentId}</td>
            <td><button class="delete" onclick="deleteStudent(${student.id})">Delete</button></td>
        `;
    });
}

// Delete Student
function deleteStudent(id) {
    students = students.filter(student => student.id !== id);
    displayStudents();
}

// Course Form
document.getElementById("course-form").addEventListener("submit", function(event) {
    event.preventDefault();

    const courseName = document.getElementById("course-name").value;
    const departmentId = document.getElementById("department-id-course").value;
    const professorId = document.getElementById("professor-id").value;

    const course = {
        id: courses.length + 1,
        courseName,
        departmentId,
        professorId
    };

    courses.push(course);
    displayCourses();
});

// Display Courses
function displayCourses() {
    const tableBody = document.getElementById("courses-table").getElementsByTagName('tbody')[0];
    tableBody.innerHTML = "";

    courses.forEach(course => {
        const row = tableBody.insertRow();
        row.innerHTML = `
            <td>${course.id}</td>
            <td>${course.courseName}</td>
            <td>${course.departmentId}</td>
            <td>${course.professorId}</td>
            <td><button class="delete" onclick="deleteCourse(${course.id})">Delete</button></td>
        `;
    });
}

// Delete Course
function deleteCourse(id) {
    courses = courses.filter(course => course.id !== id);
    displayCourses();
}

// Enrollment Form
document.getElementById("enrollment-form").addEventListener("submit", function(event) {
    event.preventDefault();

    const studentId = document.getElementById("student-id").value;
    const courseId = document.getElementById("course-id").value;
    const enrollmentDate = document.getElementById("enrollment-date").value;
    const grade = document.getElementById("grade").value;

    const enrollment = {
        id: enrollments.length + 1,
        studentId,
        courseId,
        enrollmentDate,
        grade
    };

    enrollments.push(enrollment);
    displayEnrollments();
});

// Display Enrollments
function displayEnrollments() {
    const tableBody = document.getElementById("enrollments-table").getElementsByTagName('tbody')[0];
    tableBody.innerHTML = "";

    enrollments.forEach(enrollment => {
        const row = tableBody.insertRow();
        row.innerHTML = `
            <td>${enrollment.id}</td>
            <td>${enrollment.studentId}</td>
            <td>${enrollment.courseId}</td>
            <td>${enrollment.enrollmentDate}</td>
            <td>${enrollment.grade}</td>
            <td><button class="delete" onclick="deleteEnrollment(${enrollment.id})">Delete</button></td>
        `;
    });
}

// Delete Enrollment
function deleteEnrollment(id) {
    enrollments = enrollments.filter(enrollment => enrollment.id !== id);
    displayEnrollments();
}
