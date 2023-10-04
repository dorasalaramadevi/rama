# Use an official Python runtime as a parent image
FROM python:3.8-slim
RUN pip install flask
ENV FLASK_APP rest_get_api.py
# Set the working directory in the container
WORKDIR /testwork


# Copy the Python script to the container
COPY rest_get_api.py /testwork/
COPY data.json /testwork/

EXPOSE 5000

# Run the Python script when the container launches
CMD ["flask","run","--host","0.0.0.0"]
