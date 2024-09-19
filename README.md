# Course Selection System

## Overview

The **Course Selection System** is a comprehensive web application designed for university students to manage their academic activities efficiently. Built using **Django**, **Django REST Framework**, and **PostgreSQL**, the system provides functionalities for course enrollment, academic tracking, faculty management, and administrative operations. The application is containerized using **Docker** to ensure easy deployment and scalability.

---

## Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [Deployment](#deployment)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

---

## Features

### User Authentication

- Secure login and logout functionality with token-based authentication.
- Role-based access control for **Students**, **Faculty**, and **Administrators**.
- Password hashing and secure session management.

### Course Management

- **View Available Courses**: Students can browse courses offered in the current term.
- **Enroll and Drop Courses**: Seamless enrollment and dropping of courses within allowed periods.
- **Course Load Management**: Validation to prevent overloading beyond credit limits.

### Faculty Management

- **Faculty Profiles**: Administrators can create and manage faculty profiles.
- **Course Assignment**: Assign faculty members to specific courses.
- **Communication**: Faculty can communicate with enrolled students.

### Student Information

- **Student Profiles**: Detailed profiles including academic history and personal information.
- **Academic Tracking**: View enrolled courses, grades, and GPA calculation.
- **Document Management**: Upload and access important academic documents.

### Term Management

- **Academic Terms**: Administrators can create and manage terms.
- **Course Offerings**: Define courses available each term with schedules and capacities.
- **Scheduling**: Manage class times, exam schedules, and room assignments.

### Emergency Course Drop

- **Application for Emergency Drop**: Students can apply with justifications.
- **Approval Workflow**: Requests are reviewed and approved by faculty and administrators.

### Grade Appeal

- **Appeal Submission**: Students can submit grade appeals with supporting documents.
- **Review Process**: Faculty can review, comment, and make decisions on appeals.
- **Notification System**: Automated notifications for status updates.

### Document Management

- **MinIO Integration**: Secure storage and retrieval of academic documents.
- **File Uploads**: Supports various file types with size restrictions.
- **Access Control**: Permissions based on user roles and ownership.

### Role-Based Access Control

- **Students**: Course enrollment, view grades, manage profiles.
- **Faculty**: Manage courses, enter grades, respond to appeals.
- **Administrators**: Full access to manage users, courses, terms, and system settings.

---

## Technology Stack

- **Backend Framework**: [Django](https://www.djangoproject.com/) and [Django REST Framework](https://www.django-rest-framework.org/)
- **Database**: [PostgreSQL](https://www.postgresql.org/)
- **Containerization**: [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/)
- **Web Server**: [Nginx](https://www.nginx.com/) as a reverse proxy
- **Storage**: [MinIO](https://min.io/) for object storage
- **Authentication**: Token-based authentication using Django's built-in mechanisms
- **Version Control**: [Git](https://git-scm.com/)

---

## Project Structure

```
├── accounts/             # Handles user accounts and authentication
├── apply/                # Manages the course application process
├── college/              # Manages college-specific information
├── config/               # Configuration files and environment settings
├── course/               # Core functionality for course management
├── description/          # Project descriptions and documentation
├── nginx/                # Configuration for Nginx reverse proxy
├── shared/               # Shared resources and utilities
├── Dockerfile            # Dockerfile for building the application
├── docker-compose.yml    # Docker Compose configuration
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables
├── .gitignore            # Git ignore rules
├── LICENSE.md            # License information
└── README.md             # Project documentation (you're reading it!)
```

---

## Installation

### Prerequisites

- **Docker** and **Docker Compose** installed on your machine.
- **Git** for version control.

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/course-selection-system.git
   cd course-selection-system
   ```

2. **Create Environment Variables**

   - Copy the sample environment file and modify it according to your setup.

     ```bash
     cp .env.example .env
     ```

   - Update the `.env` file with your configurations.

3. **Build and Run the Containers**

   ```bash
   docker-compose up -d --build
   ```

4. **Apply Migrations**

   ```bash
   docker-compose exec web python manage.py migrate
   ```

5. **Create Superuser (Admin Account)**

   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

6. **Collect Static Files**

   ```bash
   docker-compose exec web python manage.py collectstatic --no-input
   ```

7. **Access the Application**

   - The application should now be running at `http://localhost:8000/`.
   - Access the admin panel at `http://localhost:8000/admin/`.

---

## Usage

### For Students

- **Register and Login**: Create an account or log in using your credentials.
- **Browse Courses**: View available courses for the current term.
- **Enroll in Courses**: Add desired courses to your schedule.
- **Manage Enrollments**: Drop courses or apply for emergency drops if needed.
- **View Grades**: Check your grades and academic progress.
- **Submit Grade Appeals**: If necessary, submit appeals for grade reviews.

### For Faculty

- **Login**: Access your faculty account.
- **Manage Courses**: View and edit course information.
- **Enter Grades**: Submit grades for enrolled students.
- **Respond to Appeals**: Review and respond to grade appeals.

### For Administrators

- **Login**: Access the admin dashboard.
- **Manage Users**: Create, update, or delete student and faculty accounts.
- **Configure Terms**: Set up academic terms and course offerings.
- **Oversee Operations**: Monitor system activities and handle administrative tasks.

---

## API Documentation

- **Swagger UI**: Access the interactive API documentation at `http://localhost:8000/swagger/`.
- **Endpoints**: Detailed information about available endpoints for different user roles.
- **Authentication**: Use token-based authentication for secure API access.

---

## Testing

- **Unit Tests**: Comprehensive tests are implemented for all major components.

### Running Tests

```bash
docker-compose exec web python manage.py test
```

- **Test Coverage**: Generate coverage reports to ensure code quality.

---

## Deployment

### Production Deployment

- **Docker Compose**: Use the provided `docker-compose.yml` file configured for production.
- **Environment Variables**: Ensure all production variables are set in the `.env` file.
- **Reverse Proxy**: Nginx is configured to handle HTTPS and serve static files.

### Continuous Integration/Continuous Deployment (CI/CD)

- **CI Pipelines**: Set up pipelines using tools like GitHub Actions, GitLab CI/CD, or Jenkins.
- **Automated Testing**: Tests are automatically run during the CI process.
- **Automated Deployment**: Successful builds can be deployed to production environments.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE.md](LICENSE.md) file for details.

---

## Acknowledgements

- **Django**: High-level Python Web framework.
- **Django REST Framework**: Powerful toolkit for building Web APIs.
- **PostgreSQL**: Robust relational database system.
- **Docker**: Platform for developing, shipping, and running applications in containers.
- **MinIO**: High-performance, S3 compatible object storage.
- **Nginx**: High-performance HTTP server and reverse proxy.

---

## Contact

For further details or inquiries:

- **Project Maintainer**: [taha majlesi](mailto:tahamaj4@gmail.com)
- **GitHub Repository**: [Course Selection System](https://github.com/tahamajs/Course-Selection-System_Project)

Feel free to open an issue or submit a pull request if you have suggestions or improvements.

---

## Additional Information

### Logging and Error Management

- **Logging**: The system implements comprehensive logging at various levels (DEBUG, INFO, WARNING, ERROR, CRITICAL).
- **Error Handling**: Custom error pages and messages for better user experience.

### Security Measures

- **Input Validation**: All user inputs are validated to prevent SQL injection and XSS attacks.
- **Secure Passwords**: Passwords are hashed using strong algorithms.
- **HTTPS Support**: Configuration supports SSL/TLS for secure communication.

### Internationalization and Localization

- **Language Support**: The application is built with internationalization in mind, supporting multiple languages.
- **Translation**: Easily add translations for different languages using Django's built-in i18n framework.

### Pagination and Filtering

- **Efficient Data Handling**: API responses are paginated to handle large datasets efficiently.
- **Filtering and Searching**: Endpoints support filtering and searching for resources like courses and users.

### Documentation

- **Code Documentation**: Docstrings and comments are provided throughout the codebase.
- **Developer Guide**: Instructions for developers to contribute to the project are available in the `CONTRIBUTING.md` file.

