# Python base image use karein
FROM python:3.10

# Work directory set karein
WORKDIR /app

# Dependencies copy karein aur install karein
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Project files copy karein
COPY . .

# Default port expose karein
EXPOSE 8000

# Command to run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
