FROM python:3.9
WORKDIR /image_converter
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
EXPOSE 5000
# This Dockerfile sets up a Python environment for the image converter application.
