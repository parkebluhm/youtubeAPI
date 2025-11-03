# Define build arguments
ARG AIRFLOW_VERSION=2.9.2
ARG PYTHON_VERSION=3.10

# Use the official Airflow image for that version
FROM apache/airflow:${AIRFLOW_VERSION}-python${PYTHON_VERSION}

# Set Airflow home
ENV AIRFLOW_HOME=/opt/airflow

# Copy your requirements file into the container
COPY requirements.txt ${AIRFLOW_HOME}/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r ${AIRFLOW_HOME}/requirements.txt
