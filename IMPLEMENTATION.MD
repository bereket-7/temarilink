You are a senior Django architect. Build a production-ready backend for a SaaS project called **TemariLink**.

## 🎯 Project Goal

TemariLink is a school SaaS platform focused on:

* Student management
* Grade entry
* Report card generation
* SMS notifications to parents (core feature)
* Basic fee tracking

This is an MVP system that must be SIMPLE, scalable, and clean.

---

# 🏗️ ARCHITECTURE REQUIREMENTS

Use:

* Django
* Django REST Framework
* PostgreSQL
* UUID primary keys
* Multi-tenant (school-based isolation)

Follow a **modular app structure**:

temarilink/
config/
apps/
schools/
accounts/
students/
academics/
reports/
notifications/
billing/
common/

Each app MUST use **multi-file models**, not a single models.py.

---

# 🧱 BASE MODEL

Create a reusable abstract base model in:

common/models/base.py

Requirements:

* UUID primary key
* created_at timestamp
* abstract = True

---

# 📦 APPS + MODELS

Implement the following models EXACTLY:

---

## 🏢 schools

File: apps/schools/models/school.py

Model: School

* id (UUID)
* name (string)
* phone (string)
* created_at

---

## 👤 accounts

File: apps/accounts/models/user.py

Model: User (extend AbstractBaseUser)

* id
* school (FK → School)
* full_name
* phone (used as USERNAME_FIELD)
* role (ADMIN / TEACHER)
* is_active

Do NOT implement full permissions system.

---

## 🎓 students

Files:

* student.py
* guardian.py

Model: Student

* school (FK)
* full_name
* grade
* section

Model: Guardian

* student (FK)
* full_name
* phone

---

## 📚 academics

Files:

* subject.py
* term.py
* grade.py

Model: Subject

* school (FK)
* name

Model: Term

* school (FK)
* name

Model: Grade

* student (FK)
* subject (FK)
* term (FK)
* score (decimal)

---

## 📄 reports

File: report_card.py

Model: ReportCard

* student (FK)
* term (FK)
* pdf_url

---

## 📩 notifications

File: sms.py

Model: SMSMessage

* school (FK)
* phone
* message
* status (SENT / FAILED)

---

## 💰 billing

Files:

* fee.py
* payment.py

Model: Fee

* student (FK)
* amount
* status (PAID / UNPAID)
* due_date

Model: Payment

* fee (FK)
* amount
* paid_at

---

# 🔗 MODEL REGISTRATION

Each app must include:

models/**init**.py

Import all model files there.

---

# ⚙️ SETTINGS

* Add all apps to INSTALLED_APPS
* Configure PostgreSQL (placeholder config is fine)
* Set custom user model (AUTH_USER_MODEL)

---

# 🔐 ADMIN PANEL

Register ALL models in admin.py for each app.

---

# 📡 API (DRF)

For each main model, create:

* serializers.py
* views.py (ModelViewSet)

At minimum implement APIs for:

* Student
* Grade
* SMSMessage

Use DefaultRouter in urls.py.

---

# 📩 SMS SERVICE

Create:

apps/notifications/services/sms_service.py

Function:
send_sms(phone: str, message: str) -> bool

Mock external API (no real provider needed yet)

---

# 🔥 CORE BUSINESS LOGIC

When a Grade is created:

* Fetch student's guardian
* Automatically send SMS:
  "{student_name} scored {score} in {subject}"

Implement this using a **service or signal (preferred: service layer)**.

---

# 🧪 OUTPUT REQUIREMENTS

Generate:

* Full folder structure
* All model files (multi-file)
* serializers
* viewsets
* urls
* admin registrations
* sms service
* clean, readable, production-level code

Avoid:

* unnecessary complexity
* permissions system
* unused abstractions

---

# 🎯 PRIORITY

Focus on:

1. Clean architecture
2. Readable code
3. Working APIs
4. SMS trigger logic

This code should be ready to run with:

* makemigrations
* migrate
* runserver

---

Return complete code with proper file paths.
