# ALX Travel App 🌍

A Django-based backend application for managing and listing travel destinations. This project is designed to implement scalable project structure, integrate MySQL as the database engine, and document APIs using Swagger (drf-yasg). Built as part of the ALX milestone task to reflect real-world practices in backend development.

---

## 🚀 Features

- Django REST Framework for API development
- MySQL database integration using environment variables
- Swagger UI (`drf-yasg`) for API documentation
- CORS support via `django-cors-headers`
- Environment configuration via `django-environ`
- Modular app structure (`listings` app)
- Git version control

---

## 🧠 Learning Objectives

This project demonstrates how to:

- Initialize a Django project with scalable, production-ready settings
- Manage secure environment variables with `.env` files
- Use MySQL as the database backend
- Integrate Swagger for clean API documentation
- Apply version control using Git and GitHub

---

## 🛠️ Tech Stack

| Tool/Framework     | Purpose                                 |
|--------------------|------------------------------------------|
| Django             | Backend web framework                   |
| Django REST Framework | API development                     |
| MySQL              | Relational database                     |
| drf-yasg           | Swagger documentation                   |
| django-environ     | Environment variable management         |
| django-cors-headers| Cross-Origin Resource Sharing (CORS)    |
| Git + GitHub       | Version control and code hosting        |

---

## 🧩 Project Structure
```
alx_travel_app/
├── alx_travel_app/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── listings/
│ ├── init.py
│ ├── models.py
│ ├── views.py
│ └── urls.py
├── manage.py
├── .env
└── requirements.txt
```

---

## ⚙️ Installation and Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/alx_travel_app.git
cd alx_travel_app
```
### 2. Create virtual environment and activate it
```
python3 -m venv venv
source venv/bin/activate
```
### 3. Install dependencies
```
pip install -r requirements.txt
```
### 4. Create and configure .env file
```
DEBUG=True
SECRET_KEY=your-secret-key
DB_NAME=yourdbname
DB_USER=yourdbuser
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=3306
```
### 5. Apply migrations
```
python manage.py makemigrations
python manage.py migrate
```
### 6. Run development server
```
python manage.py runserver
```
- Access your API docs at: http://127.0.0.1:8000/swagger/

### 📄 API Documentation
- This project uses Swagger to auto-document all API endpoints. Once the server is running, open:
```
http://127.0.0.1:8000/swagger/
```
- You'll see a UI listing all endpoints, request methods, parameters, and responses.

### 🗃️ GitHub Repository
### 🔗 GitHub: alx_travel_app

### 🤝 Contribution
Feel free to fork the repository, raise issues or submit pull requests. Your contributions are welcome.

