# Server Health Monitoring Dashboard

## Overview

A Flask-based monitoring dashboard to display server health metrics in real time.

The application tracks:

- CPU Usage
- Memory Usage
- Disk Usage
- System Uptime
- Hostname
- OS Details
- Running Process Count

---

## Tech Stack

- Python
- Flask
- psutil
- Docker
- GitHub
- Docker Hub
- GitHub Actions
- Kubernetes
- AWS EC2

---

## Project Structure

```bash
server-health-monitoring-dashboard/
├── app.py
├── requirements.txt
├── Dockerfile
├── templates/
│   └── index.html
├── .github/workflows/docker.yml
└── k8s/
    ├── deployment.yaml
    └── service.yaml
```

---

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run app:

```bash
python app.py
```

Open:

```text
http://localhost:5000
```

---

## Run Using Docker

Build image:

```bash
docker build -t server-health-monitoring-dashboard .
```

Run container:

```bash
docker run -d -p 5000:5000 server-health-monitoring-dashboard
```

Open:

```text
http://localhost:5000
```

---

## Docker Hub Image

```bash
docker pull ashishkarad5566/server-health-monitoring-dashboard:latest
```

---

## CI/CD

GitHub Actions is used to:

- Build Docker image
- Push image to Docker Hub
- Automate container delivery

Workflow file:

```text
.github/workflows/docker.yml
```

---

## Kubernetes Deployment

Deploy application:

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

Check:

```bash
kubectl get pods
kubectl get svc
```

Access application:

```text
http://<EC2-IP>:30080
```

---

## Features

- Containerized monitoring dashboard
- Automated image build and push
- Kubernetes deployment
- Self-healing through replicas
- NodePort service exposure

---

## Future Enhancements

- Prometheus integration
- Grafana dashboards
- Alerting
- Kubernetes autoscaling
