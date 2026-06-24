import random
from faker import Faker
from db.connection import get_connection

fake = Faker()

def main():
    conn = get_connection()
    cur = conn.cursor()

    # GROUPS
    groups = []
    for i in range(3):
        cur.execute("INSERT INTO groups(name) VALUES (%s) RETURNING id", (f"Group-{i+1}",))
        groups.append(cur.fetchone()[0])

    # TEACHERS
    teachers = []
    for _ in range(5):
        cur.execute("INSERT INTO teachers(fullname) VALUES (%s) RETURNING id", (fake.name(),))
        teachers.append(cur.fetchone()[0])

    # SUBJECTS
    subjects = ["Math", "SQL", "Python", "Algorithms", "Networks"]

    subject_ids = []
    for s in subjects:
        teacher_id = random.choice(teachers)
        cur.execute(
            "INSERT INTO subjects(name, teacher_id) VALUES (%s, %s) RETURNING id",
            (s, teacher_id)
        )
        subject_ids.append(cur.fetchone()[0])

    # STUDENTS
    students = []
    for _ in range(40):
        cur.execute(
            "INSERT INTO students(fullname, group_id) VALUES (%s, %s) RETURNING id",
            (fake.name(), random.choice(groups))
        )
        students.append(cur.fetchone()[0])

    # GRADES
    for student_id in students:
        for _ in range(random.randint(10, 20)):
            cur.execute(
                """
                INSERT INTO grades(student_id, subject_id, grade, grade_date)
                VALUES (%s, %s, %s, %s)
                """,
                (
                    student_id,
                    random.choice(subject_ids),
                    random.randint(50, 100),
                    fake.date_between(start_date="-1y", end_date="today")
                )
            )

    conn.commit()
    cur.close()
    conn.close()

    print("DATA SEEDED SUCCESSFULLY")

if __name__ == "__main__":
    main()