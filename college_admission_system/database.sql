CREATE DATABASE IF NOT EXISTS college_admission;
USE college_admission;

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
);

CREATE TABLE IF NOT EXISTS settings (
    category_name VARCHAR(20) PRIMARY KEY,
    seat_count INT NOT NULL DEFAULT 0
);

-- Initialize default seat counts for MCA (Total 30)
-- Example distribution: OC=10, BC=8, MBC=6, SC=4, PC=2
INSERT INTO settings (category_name, seat_count) VALUES 
('OC', 10),
('BC', 8),
('MBC', 6),
('SC', 4),
('PC', 2)
ON DUPLICATE KEY UPDATE seat_count = VALUES(seat_count);
