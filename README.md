## ⚙️ Installation
### 1. Clone the repository
```bash
git clone git@github.com:AnnaKilimova/class_based_views.git
```
### 2. Navigate to the project folder:
```bash
cd class_based_views
```
### 3. Create and activate a virtual environment
#### For MacOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate    
```  
#### For Windows:
```bash
venv\Scripts\activate    
```
### 4. Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt    
```
This installs all required packages listed in requirements.txt, ensuring your environment matches the project dependencies.

### 5. Install PostgreSQL
Make sure PostgreSQL is installed and running locally:
- macOS: `brew install postgresql`
- Ubuntu: `sudo apt install postgresql`
- Windows: Download from [https://www.postgresql.org/download/](https://www.postgresql.org/download/)

### 6. Create a database and user
After installing PostgreSQL, create a database and a user for the project:
```bash
psql -U postgres
CREATE DATABASE myproject_db;
CREATE USER myproject_user WITH PASSWORD 'mypassword';
ALTER ROLE myproject_user SET client_encoding TO 'utf8';
ALTER ROLE myproject_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE myproject_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myproject_db TO myproject_user;
\q
```
### 7. Configure your .env file
Create a .env file in the project root and add your database configuration:
<br>⚠️ Do NOT commit this file to GitHub. Use .env.example as a template.
```bash
SECRET_KEY=secret_key
DEBUG=True
DATABASE_NAME=myproject_db
DATABASE_USER=myproject_user
DATABASE_PASSWORD=mypassword
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

### 8. Apply migrations:
```bash
python manage.py migrate
```
## 🧩 Task Description
Rewrite the existing views in the project to CBV, using at least 3 of the following:

- DetailView
- ListView
- CreateView
- UpdateView
- DeleteView

### 🧪 Running Tests
```bash
python manage.py test
```
Tests cover:
1. Course List View Tests
2. Course Detail View Tests
3. Course Creation Tests
4. Course Update Tests
5. Course Deletion Tests

### 🙋‍♂️ Create superuser
```bash
python manage.py createsuperuser
```
### 🚀 Running the Application
After tests pass, start the server:
```bash
python manage.py runserver
```
The project will be available at:
```bash
👉 http://127.0.0.1:8000/
```
Available route:
Available routes:
- [/admin/](http://127.0.0.1:8000/admin/) — Django admin panel
- [/courses/](http://127.0.0.1:8000/courses/) — List of all courses (ListView)
- [/courses/create/](http://127.0.0.1:8000/courses/create/) — Create a new course (CreateView)
- [/courses/2/](http://127.0.0.1:8000/courses/2/) — Course details (DetailView)
- [/courses/2/update/](http://127.0.0.1:8000/courses/2/update/) — Update existing course (UpdateView)
- [/courses/2/delete/](http://127.0.0.1:8000/courses/2/delete/) — Delete a course (DeleteView)

Stop the server:
```bash
^C
```