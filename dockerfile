FROM python:3.12-slim-bookworm

RUN apt update && apt install -y libpq-dev gcc

WORKDIR /app

COPY requirements_prod.txt .

RUN pip install --no-cache-dir -r requirements_prod.txt

COPY . . 

EXPOSE 8000

RUN apt install -y dos2unix

# Convert the script's line endings to Unix format
RUN dos2unix entrypoint.sh

RUN chmod +x entrypoint.sh

ENTRYPOINT [ "/app/entrypoint.sh" ]

