# ARMAN — Developer Portfolio

A personal developer portfolio built with Django, HTML, CSS and JavaScript. It showcases my technical skills, projects, certifications and professional background.

## About Me

I'm a Computer Science student passionate about Python development, web technologies and Artificial Intelligence.

I'm continuously learning, building practical projects and improving my development skills.

## Features

- Responsive portfolio design
- Personal introduction and about section
- Technical skills showcase
- Projects portfolio
- Certifications section
- Resume download
- Contact information and social links
- Interactive elements and subtle animations
- Django-powered backend

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| HTML5 | Page structure |
| CSS3 | Styling and responsive design |
| JavaScript | Interactive functionality |
| SQLite | Local database |
| Git & GitHub | Version control |

## Project Structure

```text
arman-portfolio/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── portfolio/
│   ├── migrations/
│   ├── static/
│   │   └── portfolio/
│   │       ├── css/
│   │       ├── js/
│   │       └── files/
│   ├── templates/
│   ├── models.py
│   └── views.py
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/armananzer8-pixel/Arman-Developer-Portfolio.git
cd Arman-Developer-Portfolio
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-new-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

Generate a secret key using:

```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Keep your `.env` file private.

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open:

http://127.0.0.1:8000/

## Future Improvements

- Cloud deployment
- Cloud-based database and file storage
- Improved performance and accessibility
- Additional development projects

## Author

**Mohammed Muneeb Arman Anzar**

- GitHub: [armananzer8-pixel](https://github.com/armananzer8-pixel)

---

*Built with curiosity, consistency and a passion for technology.*
