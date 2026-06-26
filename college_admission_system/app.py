from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql
import pymysql.cursors
import os

app = Flask(__name__)
app.secret_key = "college_admission_secret_key"

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'college_admission',
    'cursorclass': pymysql.cursors.DictCursor,
    'autocommit': True
}

def get_db_connection():
    try:
        return pymysql.connect(**db_config)
    except Exception as e:
        # If database does not exist, try connecting without it to create it
        conn = pymysql.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            autocommit=True
        )
        with conn.cursor() as cursor:
            cursor.execute("CREATE DATABASE IF NOT EXISTS college_admission")
        conn.close()
        return pymysql.connect(**db_config)

def init_db():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        # Create tables
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                student_id VARCHAR(20) UNIQUE NOT NULL,
                name VARCHAR(100) NOT NULL,
                gender ENUM('Male', 'Female') NOT NULL,
                category VARCHAR(20) NOT NULL,
                mark FLOAT NOT NULL,
                status VARCHAR(20) DEFAULT 'Waiting',
                allocated_category VARCHAR(20) DEFAULT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS settings (
                category_name VARCHAR(20) PRIMARY KEY,
                seat_count INT NOT NULL DEFAULT 0
            )
        """)
        # Default seat counts (Total 30 for MCA)
        cursor.execute("SELECT COUNT(*) as count FROM settings")
        if cursor.fetchone()['count'] == 0:
            default_seats = [
                ('OC', 10),
                ('BC', 8),
                ('MBC', 6),
                ('SC', 4),
                ('PC', 2)
            ]
            cursor.executemany("INSERT INTO settings (category_name, seat_count) VALUES (%s, %s)", default_seats)
    conn.close()

def allocate_seats():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        # Reset all allocations
        cursor.execute("UPDATE students SET status = 'Waiting', allocated_category = NULL")
        
        # Get all students sorted by marks desc
        cursor.execute("SELECT * FROM students ORDER BY mark DESC, created_at ASC")
        students = cursor.fetchall()
        
        # Get seat counts
        cursor.execute("SELECT * FROM settings")
        settings = cursor.fetchall()
        seats_available = {s['category_name']: s['seat_count'] for s in settings}
        
        for student in students:
            allocated = False
            cat = student['category']
            
            # 1. Try to allocate in student's category
            if seats_available.get(cat, 0) > 0:
                cursor.execute(
                    "UPDATE students SET status = 'Allocated', allocated_category = %s WHERE id = %s",
                    (cat, student['id'])
                )
                seats_available[cat] -= 1
                allocated = True
            
            # 2. If not allocated, try OC (Open Competition)
            if not allocated and seats_available.get('OC', 0) > 0:
                cursor.execute(
                    "UPDATE students SET status = 'Allocated', allocated_category = 'OC' WHERE id = %s",
                    (student['id'],)
                )
                seats_available['OC'] -= 1
                allocated = True
                
    conn.close()

@app.route('/')
def index():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        # Total students
        cursor.execute("SELECT COUNT(*) as count FROM students")
        total_students = cursor.fetchone()['count']
        
        # Boys and Girls count
        cursor.execute("SELECT gender, COUNT(*) as count FROM students GROUP BY gender")
        genders = cursor.fetchall()
        boys_count = next((g['count'] for g in genders if g['gender'] == 'Male'), 0)
        girls_count = next((g['count'] for g in genders if g['gender'] == 'Female'), 0)
        
        # Category-wise count
        cursor.execute("SELECT category, COUNT(*) as count FROM students GROUP BY category")
        category_counts = cursor.fetchall()
        
        # Allocated vs Waiting
        cursor.execute("SELECT status, COUNT(*) as count FROM students GROUP BY status")
        status_counts = cursor.fetchall()
        allocated_count = next((s['count'] for s in status_counts if s['status'] == 'Allocated'), 0)
        waiting_count = next((s['count'] for s in status_counts if s['status'] == 'Waiting'), 0)
        
        # Seat utilization
        cursor.execute("""
            SELECT s.category_name, s.seat_count, 
            (SELECT COUNT(*) FROM students WHERE allocated_category = s.category_name) as used_seats
            FROM settings s
        """)
        seat_utilization = cursor.fetchall()
        
    conn.close()
    return render_template('dashboard.html', 
                           total_students=total_students,
                           boys_count=boys_count,
                           girls_count=girls_count,
                           category_counts=category_counts,
                           allocated_count=allocated_count,
                           waiting_count=waiting_count,
                           seat_utilization=seat_utilization)

@app.route('/students')
def view_students():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM students ORDER BY mark DESC")
        students = cursor.fetchall()
    conn.close()
    return render_template('students.html', students=students)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        student_id = request.form['student_id']
        name = request.form['name']
        gender = request.form['gender']
        category = request.form['category']
        mark = float(request.form['mark'])
        
        conn = get_db_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO students (student_id, name, gender, category, mark) VALUES (%s, %s, %s, %s, %s)",
                    (student_id, name, gender, category, mark)
                )
            allocate_seats()
            flash("Student added successfully!", "success")
            return redirect(url_for('view_students'))
        except Exception as e:
            flash(f"Error: {e}", "danger")
        finally:
            conn.close()
            
    return render_template('add_student.html')

@app.route('/edit_student/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM students WHERE id = %s", (id,))
        student = cursor.fetchone()
        
    if request.method == 'POST':
        student_id = request.form['student_id']
        name = request.form['name']
        gender = request.form['gender']
        category = request.form['category']
        mark = float(request.form['mark'])
        
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE students SET student_id=%s, name=%s, gender=%s, category=%s, mark=%s WHERE id=%s",
                    (student_id, name, gender, category, mark, id)
                )
            allocate_seats()
            flash("Student updated successfully!", "success")
            return redirect(url_for('view_students'))
        except Exception as e:
            flash(f"Error: {e}", "danger")
        finally:
            conn.close()
            
    conn.close()
    return render_template('edit_student.html', student=student)

@app.route('/delete_student/<int:id>')
def delete_student(id):
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM students WHERE id = %s", (id,))
    allocate_seats()
    conn.close()
    flash("Student deleted successfully!", "success")
    return redirect(url_for('view_students'))

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    conn = get_db_connection()
    if request.method == 'POST':
        for category, count in request.form.items():
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE settings SET seat_count = %s WHERE category_name = %s",
                    (count, category)
                )
        allocate_seats()
        flash("Settings updated and seats reallocated!", "success")
        return redirect(url_for('settings'))
        
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM settings")
        settings = cursor.fetchall()
    conn.close()
    return render_template('settings.html', settings=settings)

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
