﻿# Attendance Management System (Mark Attendance With Location & Image of Employee) 
This project is an Attendance Management System built with Django. It allows organizations to manage employee attendance efficiently. The app captures employee images and their current location while marking attendance. Admins can view all employee attendance details, including location, while employees can only see their own attendance records.

# WebApp Images
![image](https://github.com/user-attachments/assets/b7f9527b-d17f-4bfe-b5a8-8cb70d0925f0)
![image](https://github.com/user-attachments/assets/4a712077-6a96-4561-a0fd-73acde9e6851)
![image](https://github.com/user-attachments/assets/d63e0cb6-1091-4ab4-847d-e76c366f550c)
![image](https://github.com/user-attachments/assets/4ff06824-6087-4f41-a465-d15e83061b28)






# Features
1) User Authentication: Users can log in with their credentials. New organizations can create an account and add team members.
2) Employee Attendance: Employees can mark their attendance by clicking "I am present," which captures their image and location.
3) Admin Dashboard: Admins can view attendance records of all employees, along with their captured images and locations.
4) Email Notification: Passwords for new employees are sent via email when added to the platform.
Google Login: The app supports Google login for easy access.

# Technologies Used
1) Backend: Django
2) Frontend: HTML, CSS, Bootstrap 4, JavaScript
3) Database: SQLite (default, can be changed)
4) Authentication: Google OAuth2 and Django's built-in authentication system
5) Email Service: Django's Email backend (for sending passwords)

# Installation
1) git clone https://github.com/mudassirzeya/attendace_management_system.git
2) pip install django pillow
3) python manage.py migrate
4) Set Up Email Backend
   1) Update the email configuration in the settings.py file to use your preferred email service for sending passwords.
5) Create Superuser (Admin Account): python manage.py createsuperuser
6) Run Server: python manage.py runserver

