# 🌐 Django Translator App

A simple yet powerful **Django-based web application** that allows authenticated users to **create notes** and **translate** them between **English and Hindi** using a third-party translation API.  
The project demonstrates clean backend design, REST API implementation, caching, and integration with external services — all packaged into a Dockerized deployment for AWS EC2.

---

## 🚀 Project Overview

The **Django Translator App** helps users manage multilingual notes and translate text seamlessly between English ↔ Hindi.  
It showcases how Django REST Framework, authentication, external APIs, and caching can be combined to build a scalable backend system.

**Core Features:**
- 🔐 User registration and authentication  
- 📝 CRUD operations for personal notes  
- 🌍 Translation between English ↔ Hindi  
- 💾 Caching to optimize repeated notes  
- 📊 User statistics and usage insights  

---

## 🧰 Tech Stack

| Category | Technology |
|-----------|-------------|
| **Backend Framework** | Django, Django REST Framework |
| **Database** | PostgreSQL / SQLite (for local setup) |
| **Authentication** | Token / JWT Authentication |
| **Caching** | Django cache framework (Redis) |
| **Containerization** | Docker |
| **Deployment** | AWS EC2, Render |
| **Programming Language** | Python 3.x |
| **Third-party API** | Translator API (configurable via `.env`) |

---

## ⚙️ Setup Instructions

### 🧑‍💻 Local Development Setup

Follow these steps to run the Django Translator App on your local machine:

1. **Clone the repository**
   ```bash
   git clone https://github.com/Anjali0739/Django-Translator-App.git
   cd Django-Translator-App
2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate     # on Windows: venv\Scripts\activate
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
4. **Create a `.env` file (in the root directory)**
   ```bash
   # .env file
    SECRET_KEY=your_django_secret_key
    DEBUG=True
    TRANSLATOR_URL=https://api.example.com/translate
    DATABASE_URL=sqlite:///db.sqlite3
5. **Run migrations**
    ```bash
    python manage.py migrate 
6. **Start the development server**
   ```bash
   python manage.py runserver
7. **Access the API**
   Open your browser or Postman and visit:
   ```bash
   http://127.0.0.1:8000/


### 🐳 Docker Setup

You can run both Django and Redis from within the same Docker container using your provided Dockerfile.

1. **Build the Docker image**
   ```bash
   docker build -t translatorapp:latest .
2. **Run the container**
   ```bash
   docker run -p 8000:8000 translatorapp:latest
3. **Verify Redis and Django are running**
   - Django server: http://localhost:8000
   - Redis server runs inside the same container (port 6379)
4. **Stop and remove the container**
   ```bash
   docker ps
   docker stop <container_id>
   docker rm <container_id>


### ☁️ AWS EC2 Deployment

To deploy the app on AWS EC2 using Docker:

1. **Launch an EC2 Instance**
   - Use Ubuntu 22.04 or Amazon Linux 2
   - Allow inbound ports: 22 (SSH), 8000 (App), and optionally 6379 (Redis)
2. **SSH into your instance**
   ```bash
    ssh -i your-key.pem ubuntu@<EC2-PUBLIC-IP>
3. **Install dependencies**
   ```bash
   sudo apt update
   sudo apt install docker.io git -y
   sudo systemctl enable docker
   sudo systemctl start docker
4. **Clone your repository**
   ```bash
   git clone https://github.com/Anjali0739/Django-Translator-App.git
   cd Django-Translator-App
5. **Create your `.env` file** - 
  Add the same environment variables used locally but with `DEBUG=False`.
6. **Build and run the Docker container**
   ```bash
   sudo docker build -t translatorapp:latest .
   sudo docker run -d -p 8000:8000 translatorapp:latest
7. **Access your app**
   ```cpp
   http://<EC2-PUBLIC-IP>:8000

---

## 📬 API Documentation (Postman)

### 🔹 **Base URL**
`http://127.0.0.1:8000/`  
> Replace with your EC2 public IP or domain after deployment.


### 🧾 **User APIs**
| Method | Endpoint | Description |
|---------|-----------|-------------|
| `POST` | `user/register/` | Register a new user |
| `POST` | `api/token/` | Obtain JWT access |
| `POST` | `api/token/refresh/` |  refresh tokens for authentication |


### 📝 **Notes APIs**
| Method | Endpoint | Description |
|---------|-----------|-------------|
| `GET` | `notes/` | Get all notes of the authenticated user |
| `POST` | `notes/` | Create a new note |
| `GET` | `notes/<id>/` | Retrieve a specific note by ID (cached via Redis) |
| `PUT` | `/notes/<id>/` | Update a specific note by ID |
| `DELETE` | `/notes/<id>/` | Delete a specific note by ID |


### 🌐 **Translation APIs**
| Method | Endpoint | Description |
|---------|-----------|-------------|
| `GET` | `/translate/<id>/` | Translate a note text based on its language (English ↔ Hindi) |


### 📊 **Stats APIs**
| Method | Endpoint | Description |
|---------|-----------|-------------|
| `GET` | `/stats/` | Get user’s translation statistics (total notes, translations, and breakdown by language) |


---

## 🧩 Design Overview

### 🏗️ High-Level Design (HLD)

 - User interacts via REST API → DRF views
 - Each user can have multiple notes
 - Each note can have a translated version (1-to-1 via Translating model)
 - Translator API handles text translation
 - Cache layer optimizes repeated translations
 - Stats endpoint aggregates usage metrics

### ⚙️ Low-Level Design (LLD)

 - Models: `User`, `Note`, `Translating`, `Stats`
 - Relationships: One-to-Many (User → Notes), One-to-One (Note → Translating)
 - Translation Flow:
      - Check cache → Use existing translation → Update count
      - Else call external API → Store → Return response
 - Error Handling:
      - All views wrapped in try-except blocks for safety

---

## 🧩 Design Decisions
   - **Django REST Framework (DRF):** Provides robust, flexible API support.
   - **Redis Cache:** Reduces API latency by caching note details and translations.
   - **JWT Authentication:** Ensures secure token-based access.
   - **Docker:** Simplifies deployment and local testing.
   - **SQLite → PostgreSQL Ready:** Easily extendable to production-grade database.

---
## ⚠️ Known Limitations / Next Steps
   - Currently supports only English ↔ Hindi translations
   - Basic error messages; can be improved for UX
   - Caching logic can be expanded for translated text
   - Add more language support (via configurable API targets)
   - Add frontend (React/Vue) for better interactivity
   - Add unit tests for translation and stats endpoints



    


