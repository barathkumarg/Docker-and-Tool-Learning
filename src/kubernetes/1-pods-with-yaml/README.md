# Pods with YAML - deploy a pod in kubernetes

## Pre-requisite for kubectl
- Installation for kubectl
```
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```

- Install the the `minikube` since we are not rely on the cluster provided by cloud

## YAML file creation redis - basic beginner one
```
apiVersion: v1
kind: Pod
metadata:
  name: myredis-pod
  labels:
    app: myredis
    tier: frontend
spec:
  containers:
    - name: redis-container
      image: redis:latest

```

### Commands

- To start/restart after edit in yaml file
```
kubectl apply -f <yaml file>
```

- To delete
```
kubectl pod delete <name>
```

- To edit 
```
kubectl pod edit <name>
```