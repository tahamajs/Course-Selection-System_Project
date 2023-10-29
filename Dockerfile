FROM python:3.9-slim

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /CourseSelectionSystem
WORKDIR /CourseSelectionSystem

EXPOSE 8000

ENTRYPOINT ["python", "CourseSelectionSystem/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]