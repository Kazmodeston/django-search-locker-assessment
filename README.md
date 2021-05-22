# django-search-locker-assessment
Assessment to search for Locker in a specific Location (City/State) using **Python(Django) for backend and VueJS + Tailwind CSS**

## Installation Process

### django Installation Process (Backend)

**Make Sure you navigate to the source Directory where you have directories like `frontend` , `locker` , `lockersearch`**

 - #### 1. Clone the repository 
  - git clone https://github.com/<username>/<forked-repo>.git

 - #### 2. Create your own virtual environment
  - python3 -m venv venv
  - source venv/bin/activate

 - #### 3. Install your requirements
  - pip install -r requirements.txt

 - #### 4. Start Server to create Sqlite3 Database
  - python manage.py runserver

 - #### 5. Make your migrations
  - python manage.py makemigrations

  - python manage.py migrate



### Vue and Tailwind CSS Installation Process (Frontend)

**From the Source Directory, `cd frontend` (move into frontend directory)**

- #### Install your dependencies
 - npm install



## PLEASE NOTE
> Make Sure you have all the Applications installed on your machine before running the commands above
 - Python3
 - Django v3.2.3  (the `requirements.txt` in the source directory will help you with that)
 - Tailwind v2.1.2 (the `package.json` in directory frontend will help you with that as well)