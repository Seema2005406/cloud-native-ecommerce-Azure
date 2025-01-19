# Flask eCommerce Application

## Overview
This is a cloud-native eCommerce application built with Python Flask. It uses a microservices architecture and supports containerized deployment.

## Features
- User authentication with JWT
- Product catalog management
- Modular architecture with Blueprints
- Dockerized setup with PostgreSQL
- CI/CD pipeline with GitHub Actions
- Kubernetes deployment with Terraform, Ansible, and Helm

## Setup

### Prerequisites
- Docker and Docker Compose
- Kubernetes cluster
- Terraform and Ansible installed
- Helm CLI installed

### Steps
1. Clone the repository.
2. Run `docker-compose up` to start the services.
3. Access the application at `http://localhost:5000`.

## Deployment

### CI/CD Pipeline
The CI/CD pipeline uses GitHub Actions. It builds, tests, and pushes the Docker image to Docker Hub.
