FROM python:3.11-slim-buster

WORKDIR /api

COPY . ./

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8000

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]