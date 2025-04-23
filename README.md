# 🛠️ Django Client & Project Management System

This project was developed as part of a Django Internship Assignment. It is a backend system designed to handle **Users**, **Clients**, and **Projects** with appropriate relationships, validations, and functionalities using Django and Django REST Framework.

> 👨‍💻 **Developer:** R. Akhildev Reddy  
> 📅 **Date:** 23 April 2025  
> 💼 **Role Applied For:** Django Developer Intern

---

## 📌 Agenda

Design a backend system that:
- Manages Users, Clients, and Projects
- Maintains proper data relationships
- Supports full CRUD operations via APIs
- Provides authentication-based filtering
- Leverages Django Admin for data management

---

## ⚙️ Tech Stack

- **Framework:** Django, Django REST Framework (DRF)
- **Language:** Python
- **Database:** MySQL / PostgreSQL
- **Tools:** 
  - Postman (API testing)
  - Django Admin (User and data management)

---

## 🚀 Project Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/django-internship-project.git
   cd django-internship-project
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Update your database settings in settings.py to match your MySQL/PostgreSQL credentials.

Run migrations:

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
Create a superuser:

bash
Copy
Edit
python manage.py createsuperuser
Start the development server:

bash
Copy
Edit
python manage.py runserver
🧱 Models Structure
👤 User
Default Django auth.User model

🏢 Client

Field	Type
id	AutoField
client_name	CharField
created_by	ForeignKey(User)
created_at	DateTimeField
updated_at	DateTimeField
📦 Project

Field	Type
id	AutoField
project_name	CharField
client	ForeignKey(Client)
users	ManyToManyField(User)
created_by	ForeignKey(User)
created_at	DateTimeField
🌐 API Endpoints
🔹 Clients
GET /clients/ → List all clients

POST /clients/ → Create a new client

GET /clients/<id>/ → Get client details and their projects

PUT /clients/<id>/ → Update client details

DELETE /clients/<id>/ → Delete a client

🔸 Projects
POST /projects/ → Create a new project with client ID and user assignments

GET /projects/ → List all projects assigned to the logged-in user

DELETE /projects/<id>/ → Delete a project

🛠 Code Structure
plaintext
Copy
Edit
├── api/
│   ├── admin.py         # Register models in admin panel
│   ├── models.py        # Contains Client and Project models
│   ├── serializers.py   # DRF serializers for models
│   ├── views.py         # API logic and endpoint handling
│   └── urls.py          # Routes for API endpoints
│
├── client_project_manager/
│   ├── settings.py      # Main configuration file
│   └── urls.py          # Root project URLs
│
├── requirements.txt     # Dependencies
