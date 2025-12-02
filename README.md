# Containerized Microservice with AWS

[![Continuous Integration Test](https://github.com/AbdulDD/Containerized-Microservice-with-AWS/actions/workflows/makefile.yml/badge.svg)](https://github.com/AbdulDD/Containerized-Microservice-with-AWS/actions/workflows/makefile.yml)

This project contains a **containerized Python microservice** that provides NLP functionality, including **Named Entity Recognition (NER)** and **Sentiment Analysis**, and is prepared for deployment on **AWS** using **Docker** and **Elastic Container Registry (ECR)** / **Elastic Container Service (ECS)**.

---

## Features

- **NER Endpoint:** Extract entities from input text
- **Sentiment Endpoint:** Analyze text sentiment
- Built with **Flask**, **PyTorch**, **Transformers**
- Fully containerized with **Docker**
- Ready for cloud deployment on **AWS**

---

## Requirements

- Docker ≥ 20.x  
- Python 3.12 (for local development)  
- Optional: AWS CLI (for ECR/ECS deployment)

---

## Quickstart with Docker

1. Build docker image

```bash
docker build -t containerized-microservice:latest .
```

2. Run docker image

```bash
docker run -it -p 5000:5000 containerized-microservice:latest
```

3. Test the Endpoints

NER Endpoint

```bash
curl -X POST http://localhost:5000/ner -H 'Content-Type: application/json' -d '{"text": "Meta is a tech giant"}'
```

Sentiment Endpoint

```bash
curl -X POST http://localhost:5000/sentiment -H 'Content-Type: application/json' -d '{"text": "I love mathematics"}'
```