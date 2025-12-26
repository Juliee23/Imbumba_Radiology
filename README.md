# Imbumba Radiology Imaging Website

## 📌 Project Overview

This project is a professional medical website developed for **Imbumba Radiology Imaging**, a diagnostic imaging practice offering services such as **General X-Rays, CT Scans, Ultrasound, and Theatre Imaging**.

The website is designed to be **clean, responsive, and patient-friendly**, with a strong focus on clarity, accessibility, and trust. It uses modern web technologies while remaining simple to maintain and extend.

---

## 🏗️ Tech Stack

* **Backend Framework:** Django
* **Frontend Styling:** Tailwind CSS (via CDN)
* **Templating Engine:** Django Templates
* **Static Assets:** Django Static Files
* **Responsive Design:** Mobile-first, fully responsive layouts

---

## 📂 Project Structure

```text
project_root/
│
├── home/
│   ├── templates/
│   │   └── home/
│   │       ├── base.html        # Main layout (navbar + footer)
│   │       ├── index.html       # Home page
│   │       ├── services.html    # Services page
│   │       └── contact.html     # Contact page
│   │
│   ├── static/
│   │   └── home/
│   │       └── images/          # Website images
│   │
│   └── views.py
│
├── templates/
├── static/
├── manage.py
└── README.md
```

---

## 🧭 Pages Included

### 🏠 Home Page

* Custom hero section
* About Us section
* Vision & Mission
* Clean medical layout

### 🩻 Services Page

* Distinct hero section (different from home page)
* Services displayed in responsive columns
* Services include:

  * General X-Rays
  * CT Scans
  * Ultrasound
  * Theatre Imaging

### 📍 Contact Page

* Branch locations displayed in responsive columns
* Multiple branches supported
* Clean card-based layout

---

## 🎨 Design Principles

* Clean and minimal medical aesthetic
* Consistent spacing and alignment
* Responsive grid-based layouts
* High readability for patients
* Accessible color contrast

---

## 🧱 Base Layout (base.html)

The `base.html` file includes:

* Fixed navigation bar
* Mobile-responsive menu
* Footer section
* `{% block content %}` for page injection

All pages extend from this base template to ensure consistency.

---

## 📸 Static Files

Images are stored in:

```
home/static/home/images/
```

Images are loaded using Django’s static tag:

```django
{% load static %}
<img src="{% static 'home/images/example.jpg' %}" alt="Description">
```

---

## 🚀 How to Run the Project Locally

1. Clone the repository
2. Navigate into the project directory
3. Install dependencies (if applicable)
4. Run migrations:

   ```bash
   python manage.py migrate
   ```
5. Start the development server:

   ```bash
   python manage.py runserver
   ```
6. Open your browser at:

   ```
   http://127.0.0.1:8000/
   ```

---

## 🔮 Future Enhancements

* Online appointment booking
* Patient portal integration
* CMS-based content editing
* SEO optimization
* Performance enhancements

---

## 👩‍⚕️ Client

**Imbumba Radiology Imaging**
Professional diagnostic imaging services with compassion, accuracy, and trust.

---

## 🧑‍💻 Developer Notes

This project was structured for **easy scalability** and **long-term maintenance**, making it suitable for future integrations and growth.

---

© 2025 Imbumba Radiology Imaging. All rights reserved.
