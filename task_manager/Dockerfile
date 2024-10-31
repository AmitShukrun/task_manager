# קובעים את התמונה הבסיסית
FROM python:3.9

# קובעים משתנים לספריית העבודה
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# יוצרים את ספריית העבודה
WORKDIR /app

# מעתיקים את קבצי הפרויקט
COPY requirements.txt /app/

# מתקינים את התלויות
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# פקודת התחלה
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "your_project_name.wsgi:application"]
