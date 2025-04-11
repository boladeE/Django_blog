FROM python:3.11

RUN apt update && apt install -y libpq-dev gcc

WORKDIR /app

COPY requirements_prod.txt .
RUN pip install --no-cache-dir -r requirements_prod.txt

COPY . . 

EXPOSE 8000

RUN chmod +x entrypoint.sh

ENTRYPOINT [ "/app/entrypoint.sh" ]

