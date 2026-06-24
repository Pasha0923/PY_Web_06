from db.connection import get_connection

SQL = """
DROP TABLE IF EXISTS grades CASCADE;
DROP TABLE IF EXISTS students CASCADE;
DROP TABLE IF EXISTS subjects CASCADE;
DROP TABLE IF EXISTS teachers CASCADE;
DROP TABLE IF EXISTS groups CASCADE;

CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100) NOT NULL
);

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100) NOT NULL,
    group_id INTEGER REFERENCES groups(id)
);

CREATE TABLE subjects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    teacher_id INTEGER REFERENCES teachers(id)
);

CREATE TABLE grades (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES students(id),
    subject_id INTEGER REFERENCES subjects(id),
    grade INTEGER CHECK (grade BETWEEN 1 AND 100),
    grade_date DATE NOT NULL
);
"""

def main():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(SQL)

    conn.commit()
    cur.close()
    conn.close()

    print("Tables created")

if __name__ == "__main__":
    main()