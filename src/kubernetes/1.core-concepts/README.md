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

## YAML Replication set 
-  Used to create a replicaset which manages the duplicate pods and ensure the desired number of replicas are running at all times.

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: myapp-rs
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myredis-pod-replica
      tier: frontend
  template:
    metadata:
      labels:
        app: myredis-pod-replica
        tier: frontend
    spec:
      containers:
        - name: redis-container
          image: redis:latest
          ports:
            - containerPort: 80
```

Commonly used commands for ReplicaSet:

```bash
# Create a ReplicaSet
kubectl apply -f replicaset.yaml  

# List ReplicaSets
kubectl get rs  

#Delete the Replcaset
kubectl delete rs myapp-rs
```

## Deployment YAML
- A Deployment provides declarative updates for Pods and ReplicaSets. It allows you to describe an application’s life cycle, such as which images to use for the app, the number of pod replicas, and the update strategy.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx-container
          image: nginx:latest
          ports:
            - containerPort: 80
```

Commands for Deployment:

```bash
# Create a Deployment
kubectl apply -f deployment.yaml    

# List Deployments
kubectl get deployments

# Describe a Deployment
kubectl describe deployment nginx-deployment  
```

Note that the nginx now cannot be accessed since it is not exposed to the outside world. We will learn about how to expose the deployment in the next section.

### Service YAML
We use the services - cluster IP/Load balancer to expose the deployment to the outside world. We will learn about it in the next section.

```
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx
  type: LoadBalancer        # exposes externally
  ports:
    - protocol: TCP
      port: 80              # external port
      targetPort: 80 
      nodeport: 30080         # node port for minikube (optional)
```

#### How to get the external ip

Use `kubectl get services` to get the external IP address of the service. If you are using minikube, you can use `minikube service nginx-service --url` to get the URL to access the service.


