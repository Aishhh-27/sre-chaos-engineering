# Self-Healing and Autoscaling Kubernetes Application

This project demonstrates a Kubernetes-based application that is capable of self-healing, handling failures, and automatically scaling based on load.

The goal was to simulate real-world SRE scenarios such as pod failures and traffic spikes, and observe how the system reacts.

## Tech Stack

- Kubernetes (Minikube)
- Docker
- Python (Flask)
- Prometheus & Grafana
- Horizontal Pod Autoscaler (HPA)

---

## Features

### 1. Self-Healing

The application is deployed with multiple replicas.  
If a pod crashes or is deleted, Kubernetes automatically recreates it to maintain the desired state.

### 2. Health Checks

Liveness and readiness probes are configured to ensure:
- Unhealthy containers are restarted
- Traffic is only routed to healthy pods

### 3. Chaos Testing

A simple script is used to continuously delete pods:

while true; do kubectl delete pod -l app=sre-app; sleep 30; done


This helps verify that the system recovers automatically without downtime.

### 4. Monitoring

Prometheus and Grafana are used to monitor:
- CPU usage
- Pod health
- Cluster behavior

### 5. Autoscaling (HPA)

Horizontal Pod Autoscaler is configured based on CPU usage.

- Min replicas: 2  
- Max replicas: 5  
- Target CPU: 50%

Under load, the application scales up automatically.  
When the load drops, it scales back down.

---
## Architecture

The application is deployed on Kubernetes with the following components:

- Flask application running in multiple pods
- Kubernetes Deployment managing replicas
- Service exposing the application internally
- Metrics Server providing CPU metrics
- Horizontal Pod Autoscaler for scaling
- Prometheus and Grafana for monitoring

Traffic is generated internally using a load generator pod, and scaling decisions are made based on CPU utilization.

## How It Works

1. Deploy the application with 2 replicas
2. Apply resource requests for CPU
3. Configure HPA
4. Generate load using a busybox container
5. Observe scaling behavior

---

## Results

- Pods automatically restarted when deleted (self-healing)
- System handled continuous failures without crashing
- Application scaled from 2 → 5 pods under load
- Scaled back from 5 → 2 when load stopped

---

## Learnings

- HPA requires CPU requests to function correctly
- Metrics Server is required for autoscaling
- Kubernetes does not scale down immediately due to stabilization windows
- Proper labeling is critical for services and autoscaling

---

## Folder Structure


sre-chaos-engineering/
│── app/
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
│
│── k8s/
│ ├── deployment.yaml
│ ├── service.yaml
│ └── hpa.yaml
│
│── chaos/
│ └── chaos.sh


---

## How to Run

```bash
# Build image
docker build -t sre-app .

# Load into minikube
minikube image load sre-app

# Deploy
kubectl apply -f k8s/

# Create HPA
kubectl autoscale deployment sre-app --cpu-percent=50 --min=2 --max=5

## Screenshots

### Autoscaling in action
![HPA Scaling](screenshots/hpa-scale.png)
### Pods scaling up
![Pods](screenshots/pods.png)


Conclusion

This project simulates real production scenarios where systems must handle failures and varying load conditions. It demonstrates practical understanding of Kubernetes, monitoring, and autoscaling.


---

