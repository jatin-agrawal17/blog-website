# 📝 Role-Based Content Management & Blogging Platform

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.x-green?style=flat-square&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightblue?style=flat-square&logo=sqlite&logoColor=white)
![CKEditor](https://img.shields.io/badge/Editor-CKEditor%205-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

A full-stack blogging platform built with **Django** that enables role-based content management, rich-text publishing, secure user administration, and media-rich blog creation through a structured permission system.

---

## 🚀 Features

- 🔐 **Role-Based Access Control** — User, Editor, and Manager permission tiers
- 🛡️ **Secure Authentication** — Login, logout, and authorization using Django's built-in Auth system
- ✍️ **Blog CRUD Operations** — Full create, read, update, delete with ownership-based access restrictions
- 📝 **Rich Text Editor** — Powered by [CKEditor 5](https://ckeditor.com/ckeditor-5/) for a modern writing experience
- 🖼️ **Image Upload & Media Management** — Upload and manage images inside blog posts
- 🏷️ **Category Management** — SEO-friendly slug-based URLs for organized content discovery
- 👤 **Profile Dashboard** — Manage personal blogs and account information in one place
- 🛠️ **User Administration Panel** — Permission-controlled actions for Managers
- ⚙️ **Automatic Profile Creation** — Profiles are auto-created on user registration
- 📄 **Responsive Blog Listing** — Clean listing and detailed article pages
- ✅ **Server-Side Validation** — Secure, validated forms with access protection
- 📊 **Role-Specific Dashboards** — Separate views for content management and user management

---

## 📁 Project Structure

```
blog-website/
├── blog_main/          # Core Django project settings & URLs
├── account/            # User authentication, registration & profile management
├── blogs/              # Blog posts, categories, comments models & views
├── dashboards/         # Role-specific dashboard views (Manager/Editor/User)
├── social/             # Social features (likes, follows, interactions)
├── media/              # Uploaded media files (images, etc.)
├── static/             # Static files (CSS, JS, images)
├── templates/          # HTML templates for all views
├── db.sqlite3          # SQLite development database
├── manage.py           # Django management entry point
├── requirements.txt    # Python dependencies
└── .gitignore
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | [Django 4.x](https://www.djangoproject.com/) |
| Language | [Python 3.10+](https://www.python.org/) |
| Database | [SQLite](https://www.sqlite.org/) (dev) / PostgreSQL (prod) |
| Rich Text Editor | [CKEditor 5](https://ckeditor.com/ckeditor-5/) via [django-ckeditor](https://pypi.org/project/django-ckeditor/) |
| Frontend | HTML5, CSS3, Bootstrap |
| Media Handling | Django `ImageField` + `Pillow` |
| Auth | Django Built-in Auth + Custom Permissions |

---

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.10+
- pip
- virtualenv (recommended)
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/jatin-agrawal17/blog-website.git
cd blog-website
```

### 2. Create & Activate a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---


### 7. Live Demo:
[https://jatin17.pythonanywhere.com/](https://jatin17.pythonanywhere.com/)


## 🔑 User Roles & Permissions

| Role | Capabilities |
|---|---|
| **User** | Register, login, create & manage own blogs, update profile |
| **Editor** | All User permissions + edit/review content |
| **Manager** | All Editor permissions + manage users, assign roles, admin panel access |

Role assignment is handled through Django's permission system and the **User Administration Panel**.

---

## 📦 Key Dependencies

```txt
Django>=4.0
Pillow
django-ckeditor
```

> Full list available in [`requirements.txt`](./requirements.txt)

---

## 🌐 URLs & Routes

| URL Pattern | View | Description |
|---|---|---|
| `/` | `blog_list` | Homepage — all blog posts |
| `/blogs/<slug>/` | `blog_detail` | Single blog article |
| `/account/register/` | `register` | User registration |
| `/account/login/` | `login` | User login |
| `/account/profile/` | `profile` | User profile dashboard |
| `/blogs/create/` | `create_blog` | Create a new blog post |
| `/blogs/<slug>/edit/` | `edit_blog` | Edit existing blog post |
| `/dashboards/manager/` | `manager_dashboard` | Manager admin view |
| `/admin/` | Django Admin | Superuser admin panel |

---

## 🧑‍💻 Author

**Jatin Agrawal**
- GitHub: [@jatin-agrawal17](https://github.com/jatin-agrawal17)
- Linkedin: [jatin-agrawal](https://www.linkedin.com/in/jatin-agrawal-b80092367/)

---

## 📄 License

This project is licensed under the [MIT License](./LICENSE).

---

## 🙌 Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/)
- [CKEditor 5](https://ckeditor.com/ckeditor-5/)
- [Bootstrap](https://getbootstrap.com/)
- [Pillow (PIL Fork)](https://pillow.readthedocs.io/)
