# Hotel Management System

This is a Django-based Hotel Management System that utilizes Python, HTML, CSS, Bootstrap, PostgreSQL, Django Rest API, and Vue.js for the backend, frontend, and API functionalities.

## Features

- **Django Backend:** The server-side logic is implemented using Django, providing a robust and scalable backend for managing hotel operations.

- **Vue.js Frontend:** The client-side of the application is built using Vue.js, a progressive JavaScript framework, for a dynamic and responsive user interface.

- **Poetry Package Management:** Poetry is used for package management, ensuring consistency and reproducibility of the project's dependencies.

- **PostgreSQL Database:** The application uses PostgreSQL as the database to store and manage hotel-related data efficiently.

- **Django Rest API:** RESTful API endpoints are implemented using Django Rest Framework, allowing for seamless communication between the frontend and backend.

## Installation

### Prerequisites

- Python 3.x
- Node.js and npm
- PostgreSQL

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/hotel-management-system.git
   cd hotel-management-system

2. Install Python dependencies using Poetry:
- poetry install

3. Create and apply database migrations:
- python manage.py makemigrations app
- python manage.py migrate app

4. Install Node.js dependencies for the frontend:
- cd frontend
- npm install

5. Build the frontend assets:
- npm run build

6. Run the development server:
- python manage.py runserver
