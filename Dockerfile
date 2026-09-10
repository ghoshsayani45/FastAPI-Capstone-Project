FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY . .

# Install the dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]