FROM python:3.9
RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
#CMD ["python3" ,"manage.py" ,"runserver", "0.0.0.0:8000"]
#CMD ["/bin/bash"]



