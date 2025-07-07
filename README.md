# 📝 Django Blog Application

A full-featured blog web application built with Django. It includes a separate Blog and User model, along with authentication functionality like user registration, login, logout, and post management.

---

## 🚀 Features

- User registration and login/logout (authentication)
- Separate User and Blog models
- Create, edit, and delete blog posts (with permissions)
- View published posts
- User dashboard with user-specific post management
- Flash messages for actions (e.g., post deleted, logged in)
- Clean and responsive UI using Bootstrap

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (default), can be replaced with PostgreSQL/MySQL
- **Version Control:** Git & GitHub

---

## 📂 Project Structure

**project-root/
- │
- ├── blog/ # Blog app (BlogModel, views, URLs, templates)
- ├── users/ # User app (custom user model or default, auth views)
- ├── templates/ # Shared templates
- ├── media/ # Uploaded images (ignored in Git)
- ├── static/ # Static files (CSS, JS, etc.)
- ├── django_blog_env/ # Virtual environment (ignored in Git)
- ├── db.sqlite3 # SQLite DB (optional to ignore)
- ├── manage.py
- ├── .gitignore
- └── README.md


---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/django-blogverse.git
cd django-blog-app
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the development server
```bash
python manage.py runserver
```

### 🔐 Authentication Features

- /register/ – Register a new user
- /login/ – Login as existing user
- /logout/ – Logout
- /dashboard/ – User-specific dashboard


### 📌 Notes
- Blog images are stored in media/ (add this to .gitignore)
- You can use Django’s default User model or a custom one as needed.
- Be sure to configure MEDIA_URL and MEDIA_ROOT in settings.py for image uploads.

## 📄 License
- This project is licensed under the MIT License.

## 🙌 Contribution
- Feel free to fork and contribute. Pull requests are welcome!

###
