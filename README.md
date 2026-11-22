ARMAN Developer Portfolio

My personal developer portfolio, built with Django and deployed on Render with a Neon PostgreSQL database.

Live site: https://arman-developer-portfolio.onrender.com

The site runs on Render's free tier, so the first visit after a period of inactivity can take up to a minute to wake up.

What's inside
Projects: featured work with descriptions, technologies, and GitHub / live links
Certifications: training and learning milestones, each with a viewable certificate PDF
Profile: introduction, about section, and links to GitHub and LinkedIn
Admin panel: content is managed through the Django admin, with no code changes needed
Featured projects
Arman DevHub
Library Management System
Arman Portfolio (this website)
Tech stack
Area	Technology
Backend	Python, Django
Database	PostgreSQL (Neon)
Hosting	Render
Static files	WhiteNoise
Web server	Gunicorn
Project structure
arman-portfolio/
├── config/        # Django project settings, URLs, WSGI
├── portfolio/     # Main app: models, views, templates, static files
├── manage.py
└── requirements.txt
Run it locally
Clone the repository and open the folder:
bash
git clone https://github.com/armananzer8-pixel/Arman-Developer-Portfolio.git
cd Arman-Developer-Portfolio
Create and activate a virtual environment:
bash
python -m venv venv
venv\Scripts\activate

On macOS or Linux, use source venv/bin/activate instead.

Install dependencies:
bash
pip install -r requirements.txt
Apply migrations and create an admin user:
bash
python manage.py migrate
python manage.py createsuperuser
Start the development server:
bash
python manage.py runserver

Then open http://127.0.0.1:8000/

Environment variables

The app reads its configuration from environment variables. Never commit real values to the repository.

Variable	Purpose
SECRET_KEY	Django secret key
DEBUG	Set to True only for local development (defaults to False)
ALLOWED_HOSTS	Comma-separated list of allowed hostnames
DATABASE_URL	PostgreSQL connection string
Deployment (Render)
Build command:
bash
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
Start command:
bash
gunicorn config.wsgi:application
Deploys automatically from the main branch.
Managing certificates

Render's filesystem is temporary, so certificate PDFs are stored in the repository as static files instead of being uploaded through the admin.

To add a new certificate:

Put the PDF in portfolio/static/certifications/
Commit and push to main
In the admin, create or edit the certification and set its file path to certifications/YourFile.pdf
About the certifications

Some certifications listed on the site are personal learning milestones and are not accredited qualifications. They are labeled as such on the certificates themselves.

Author

Arman

GitHub: armananzer8-pixel