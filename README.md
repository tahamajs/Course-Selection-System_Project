# Course Selection System

## Overview

This project is a Course Selection System designed for university students. It allows students to register for courses, manage their academic information, and communicate with university staff. The system is built using Django, Django Rest Framework, and PostgreSQL as the database. Docker is used for containerization to ensure easy deployment and scalability.

## Features

* User Authentication: Secure login and logout functionality with token-based authentication.
* Course Management: Students can view available courses, enroll, drop, and manage their course load.
* Faculty Management: Admins can manage faculty information and assign them to specific courses.
* Student Information: Detailed student profiles with academic history, course enrollment status, and more.
* Term Management: Admins can manage academic terms, including course offerings and schedules.
* Emergency Course Drop: Students can apply for emergency course drops with proper justification.
* Grade Appeal: A system for students to appeal their grades and for professors to review and respond to these appeals.
* Document Management: Storage and retrieval of important academic documents using MinIO.
* Role-Based Access Control: Different levels of access for students, faculty, and admins.

## Project Structure

* /accounts/: Handles user accounts and authentication
* /apply/: Manages the course application process
* /college/: Manages college-specific information
* /config/: Configuration files and environment settings
* /course/: Core functionality for course management
* /description/: Contains project descriptions and documentation
* /nginx/: Configuration for Nginx reverse proxy
* /shared/: Shared resources and utilities
* .env: Main environment variables
* .dockerignore: Files and directories to ignore in Docker builds
* .gitignore: Files and directories to ignore in Git
* Dockerfile: Dockerfile for building the application
* docker-compose.yml: Docker Compose configuration
* manage.py: Django management script
* README.md: Project documentation (you're reading it!)



## Project Overview

### Purpose and Scope

The project is a comprehensive university course selection system designed to facilitate the process of course registration, management, and academic tracking for students. The system is built to support various academic activities such as course enrollment, managing student grades, handling emergency course drops, and allowing students to appeal their grades. Additionally, it supports administrative functions like managing faculty, departments, and academic terms.

### Technology Stack

The system is developed using the Django web framework with Django Rest Framework (DRF) to build RESTful APIs. PostgreSQL is used as the primary database to store and manage all academic records, including student information, course details, and faculty data. Docker is employed for containerization, enabling consistent deployment across different environments. The system also utilizes Nginx as a reverse proxy for secure and efficient handling of HTTP requests.

### Key Features

1. **User Management** :

* **Accounts Module** : Manages user authentication and profile management, including the creation of user accounts, handling login/logout operations, and ensuring secure access through token-based authentication. It supports different user roles such as students, professors, and administrators.

1. **Course Management** :

* **Course Module** : Handles the creation, updating, and deletion of courses. It manages course details like prerequisites, co-requisites, and credit information. The module also supports the scheduling of classes and exams, and the assignment of instructors to specific courses.

1. **Student Enrollment and Registration** :

* **Apply Module** : Facilitates student course registration, including the selection and dropping of courses. It supports emergency drop requests and course substitutions. The module ensures that students can manage their course loads effectively, adhering to academic regulations.

1. **Academic Records** :

* **Grades and Transcripts** : Allows students to view their grades and academic history. Professors can enter and update student grades, which are then reflected in the student’s transcript. The system also supports grade appeals, allowing students to request a review of their grades, which professors can respond to.

1. **Administrative Functions** :

* **College and Department Management** : Manages the structure and data related to colleges, faculties, and departments within the university. It includes functionalities for handling academic terms, course offerings, and scheduling.
* **Faculty Management** : Admins can manage faculty profiles, including their departmental affiliations, teaching assignments, and academic credentials.

1. **API and System Architecture** :

* The system’s architecture is designed to be modular, with each functionality accessible through RESTful APIs. This design allows for easy integration with other systems and scalability. Pagination is implemented in API responses to efficiently handle large datasets.

1. **Documentation and Configuration** :

* **Config Module** : Contains all necessary configurations for running the system in different environments (development, testing, production). This includes environment variables and settings files.
* **Nginx Configuration** : Manages the reverse proxy settings to ensure secure and efficient routing of requests to the appropriate backend services.
* **Shared Utilities** : Provides common functions and middleware that are used across various modules, ensuring code reusability and consistency.

### Project Workflow

* **Development and Version Control** : The project is managed using Git, with a structured workflow for branching, committing, and merging code changes. Pull requests are reviewed before being merged into the main branch, ensuring code quality.
* **Deployment** : The system is containerized using Docker, with Docker Compose managing multi-container setups for the web server, database, and other services. This ensures that the application can be deployed consistently across different environments.
* **Continuous Integration and Testing** : The project includes a pipeline for continuous integration (CI) using GitHub Actions or another CI tool. This pipeline automatically runs tests, checks code formatting, and builds Docker images for deployment.

### Additional Features

* **Logging and Error Management** : The system includes comprehensive logging and error management, following standards like RFC 7231. Logs are maintained at different levels (info, warning, error) to facilitate troubleshooting and system monitoring.
* **File Management** : The system supports file storage using MinIO, allowing the secure handling of documents and media associated with students and courses.
* **Internationalization and Localization** : The system includes support for multiple languages, with translations managed through Django’s translation framework. This ensures that the system can be used in different linguistic and cultural contexts.



 ## Installation Guide

   To set up the project locally, follow these steps:

   ### 1. Clone the Repository

   First, you need to clone the project repository to your local machine. Use the following commands:


   <pre><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><div class="flex items-center"><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" class="icon-sm"><path fill="currentColor" fill-rule="evenodd" d="M7 5a3 3 0 0 1 3-3h9a3 3 0 0 1 3 3v9a3 3 0 0 1-3 3h-2v2a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3v-9a3 3 0 0 1 3-3h2zm2 2h5a3 3 0 0 1 3 3v5h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1h-9a1 1 0 0 0-1 1zM5 9a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-9a1 1 0 0 0-1-1z" clip-rule="evenodd"></path></svg>Copy code</button></span></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">git clone <repository_url>
   cd <repository_directory>
   </code></div></div></pre>

   Replace** **`<repository_url>` with the actual URL of the repository and** **`<repository_directory>` with the desired directory name.

   ### 2. Set Up Environment Variables

   Next, you need to configure the environment variables that the Django project will use. These variables are essential for the project to connect to the database, manage API keys, and handle other sensitive information.

   * Create a** **`.env` file in the project root directory. This file should be based on the provided** **`.env.example` file.
   * Ensure that you set up the following additional environment files:
     * `.db.env`: Contains environment variables specific to the database configuration.
     * `.dev.env`: Contains development-specific environment variables.
     * `minio.env`: Contains configuration for MinIO, which is used for file storage.

   ### 3. Build and Run the Application Using Docker

   Once the environment variables are set, you can build and run the application using Docker. Docker simplifies the setup by ensuring that all dependencies and services are correctly configured and running in isolated containers.

   To build and start the application, run the following command:

   <pre><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><div class="flex items-center"><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" class="icon-sm"><path fill="currentColor" fill-rule="evenodd" d="M7 5a3 3 0 0 1 3-3h9a3 3 0 0 1 3 3v9a3 3 0 0 1-3 3h-2v2a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3v-9a3 3 0 0 1 3-3h2zm2 2h5a3 3 0 0 1 3 3v5h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1h-9a1 1 0 0 0-1 1zM5 9a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-9a1 1 0 0 0-1-1z" clip-rule="evenodd"></path></svg>Copy code</button></span></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">docker-compose up --build
   </code></div></div></pre>

   This command uses Docker Compose to build the Docker images and start the containers as defined in the** **`docker-compose.yml` file.

   ### 4. Apply Migrations

   Django uses migrations to apply changes to the database schema. After starting the application, you need to apply these migrations:

   <pre><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><div class="flex items-center"><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" class="icon-sm"><path fill="currentColor" fill-rule="evenodd" d="M7 5a3 3 0 0 1 3-3h9a3 3 0 0 1 3 3v9a3 3 0 0 1-3 3h-2v2a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3v-9a3 3 0 0 1 3-3h2zm2 2h5a3 3 0 0 1 3 3v5h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1h-9a1 1 0 0 0-1 1zM5 9a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-9a1 1 0 0 0-1-1z" clip-rule="evenodd"></path></svg>Copy code</button></span></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">docker-compose exec web python manage.py migrate
   </code></div></div></pre>

   This command runs the Django migration scripts, which will create the necessary database tables and apply any schema changes.

   ### 5. Create a Superuser for Accessing the Admin Panel

   To access the Django admin interface, you'll need to create a superuser account. This account will have full access to the admin panel:

   <pre><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><div class="flex items-center"><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" class="icon-sm"><path fill="currentColor" fill-rule="evenodd" d="M7 5a3 3 0 0 1 3-3h9a3 3 0 0 1 3 3v9a3 3 0 0 1-3 3h-2v2a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3v-9a3 3 0 0 1 3-3h2zm2 2h5a3 3 0 0 1 3 3v5h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1h-9a1 1 0 0 0-1 1zM5 9a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-9a1 1 0 0 0-1-1z" clip-rule="evenodd"></path></svg>Copy code</button></span></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">docker-compose exec web python manage.py createsuperuser
   </code></div></div></pre>

   Follow the prompts to set a username, email, and password for the superuser.

   ### 6. Access the Application

   Finally, you can access the running application through your web browser:

   * The application should be available at** **`http://localhost:8000`.
   * The Django admin panel can be accessed at** **`http://localhost:8000/admin`.

## API Documentation

API endpoints are available for different user roles (Admin, Faculty, Students). The documentation is auto-generated and accessible via Swagger at** **`http://localhost:8000/swagger/`.

## Testing

* Unit tests are implemented for all major components.
* To run tests, execute:
  <pre><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><div class="flex items-center"><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" class="icon-sm"><path fill="currentColor" fill-rule="evenodd" d="M7 5a3 3 0 0 1 3-3h9a3 3 0 0 1 3 3v9a3 3 0 0 1-3 3h-2v2a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3v-9a3 3 0 0 1 3-3h2zm2 2h5a3 3 0 0 1 3 3v5h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1h-9a1 1 0 0 0-1 1zM5 9a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-9a1 1 0 0 0-1-1z" clip-rule="evenodd"></path></svg>Copy code</button></span></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">docker-compose exec web python manage.py test
  </code></div></div></pre>

## Deployment

* The application is containerized using Docker.
* Use the provided** **`docker-compose.yml` for production deployments.
* Configure CI/CD pipelines using GitHub Actions for automated testing and deployment.

## Contributing

* Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
* Follow the branching and commit message conventions as defined in the project guidelines.

## License

This project is licensed under the MIT License - see the** **`LICENSE.md` file for details.

## Acknowledgements

* Django Rest Framework
* PostgreSQL
* Docker
* MinIO for storage management

## Contact

For further details, please contact the project maintainers.
