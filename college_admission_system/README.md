# College Admission Seat Allocation System

A complete web-based system to manage college admissions and automate seat allocation based on merit and category.

## Features
- **Seat Allocation Algorithm**: Merit-based allocation (highest marks first), checking category availability, and falling back to OC (Open Competition) seats.
- **Admin Dashboard**: Real-time reports on total students, gender distribution, category counts, and seat utilization.
- **Student Management**: Full CRUD (Create, Read, Update, Delete) operations for student records.
- **Dynamic Settings**: Admin can adjust category-wise seat counts at any time, triggering a complete reallocation.
- **Responsive UI**: Built with Bootstrap 5 for mobile and desktop compatibility.

## Tech Stack
- **Backend**: Python Flask
- **Database**: MySQL (PyMySQL)
- **Frontend**: HTML5, CSS3, Bootstrap 5, FontAwesome

## Project Structure
```
college_admission_system/
├── app.py              # Main Flask application
├── database.sql        # SQL schema and initial data
├── static/
│   └── css/
│       └── style.css   # Custom styling
├── templates/          # Jinja2 HTML templates
│   ├── base.html
│   ├── dashboard.html
│   ├── students.html
│   ├── add_student.html
│   ├── edit_student.html
│   └── settings.html
└── README.md           # Documentation
```

## Setup Instructions

### 1. Database Setup
1. Open your MySQL client (e.g., phpMyAdmin, MySQL Workbench, or CLI).
2. Create a database named `college_admission`.
3. Import the `database.sql` file or run its content to create the necessary tables and initialize seat counts.

### 2. Python Environment Setup
1. Ensure you have Python installed.
2. Install the required dependencies:
   ```bash
   pip install Flask PyMySQL
   ```

### 3. Database Configuration
Open `app.py` and update the `db_config` dictionary with your MySQL credentials:
```python
db_config = {
    'host': 'localhost',
    'user': 'root',       # Your MySQL username
    'password': '',       # Your MySQL password
    'database': 'college_admission'
}
```

### 4. Running the Application
1. Navigate to the project directory.
2. Run the Flask app:
   ```bash
   python app.py
   ```
3. Open your browser and go to `http://127.0.0.1:5000`.

## Seat Allocation Rules
1. All students are sorted by Marks (Descending).
2. For each student:
   - First, try to allocate a seat in their specific category (BC, MBC, SC, PC).
   - If no seats are available in their category, try to allocate a seat in the **OC (Open Competition)** category.
   - If both are full, the student is placed on the **Waiting List**.
3. Any change to student marks, category, or seat availability triggers a full reallocation based on the current merit list.
