# Stage 1: Build
FROM python:3.11-slim as builder
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --user --no-cache-dir -r requirements.txt

FROM python:3.11-slim
WORKDIR /app

RUN groupadd -g 999 python && \
    useradd -r -u 999 -g python python

COPY --from=builder /root/.local /home/python/.local
COPY main.py .

# Ensure the app can find the installed packages
ENV PATH=/home/python/.local/bin:$PATH
RUN chown -R python:python /app

USER python

EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]