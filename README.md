# ARMAN — Developer Portfolio

A personal developer portfolio built with **Python, Django, HTML, CSS and JavaScript**. It presents my technical skills, projects, certifications and professional background.

## About Me

I'm a Computer Science student passionate about Python development, web technologies and Artificial Intelligence.

I enjoy learning new technologies, building practical projects and continuously improving my development skills.

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

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a file named `.env` in the project root, alongside `manage.py`.

Add the following:

```env
SECRET_KEY=your-generated-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

Generate your own secret key:

```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the generated key into your `.env` file.

**Important:** Never upload your `.env` file or share your secret key publicly.

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Create an admin account

```bash
python manage.py createsuperuser
```

Follow the prompts to create your account.

### 7. Start the development server

```bash
python manage.py runserver
```

Open your browser:

http://127.0.0.1:8000/

The Django admin panel is available at:

http://127.0.0.1:8000/admin/

## Important Notes

- The SQLite database is not included in the repository. Migrations create a fresh local database.
- Certificate uploads stored in the `media/` directory are excluded from GitHub.
- After setting up a fresh database, use Django Admin to add your portfolio content and certificate files.

## Future Improvements

- Cloud deployment
- Cloud-based database and file storage
- Performance and accessibility improvements
- Additional development projects

## Author

**Mohammed Muneeb Arman Anzar**

- GitHub: [armananzer8-pixel](https://github.com/armananzer8-pixel)

---

*Built with curiosity, consistency and a passion for technology.*
