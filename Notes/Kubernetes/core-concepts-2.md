# Kubernetes Core concepts -Part 2


## Pods
- Containers are encapsulated in a deployable object called **Pods**
- In Kubernetes, the hierarchy is: Cluster → Node → Pod (Pod is the smallest deployable unit)
- Two applications can run in two different pods
- Pods have a 1:1 relationship with containers — to scale up, you create more pods
- We can create multi-container pods — two or more containers (helper containers) in a single pod


### Usage of Pods - A Scenario-Based Example

- Consider a Docker Python application with a helper container. Previously, you would need to run two separate commands:
```
docker run python-app
docker run helper --link app1
```

- When using **Pods**, Kubernetes handles the container linking automatically. When you run a pod, two containers are spawned together. This removes the need to run helper and main app separately. Pods encapsulate the image, network, and volumes in a single unit. 


### Deploy a Pod

```bash
kubectl run nginx --image nginx
```

- Get pods — initially will be in `Pending` state, then transform to `Running` state

```bash
kubectl get pods
```


### Pods with YAML

- Example pod manifest (`pod-definition.yaml`):

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
  labels:
    app: myapp
    tier: frontend
spec:
  containers:
    - name: nginx-container
      image: nginx:latest
      ports:
        - containerPort: 80
```

- `apiVersion`: API version for this resource type (`v1` for Pod).
- `kind`: Kubernetes object type (`Pod`).
- `metadata`: Identifying data such as name and labels.
- `spec`: Desired state of the pod, including container definitions.

### Kubectl commands
Generate a pod YAML quickly using dry-run (client-side only):

```bash
kubectl run myapp-pod \
  --image=nginx:latest \
  --dry-run=client -o yaml > pod-definition.yaml
```

Create or update the pod from the manifest:

```bash
kubectl apply -f pod-definition.yaml
```

Check pod status:

```bash
kubectl get pods
```

View detailed pod information:

```bash
kubectl describe pod myapp-pod
```

Why `kubectl edit` is important:

- If you edit the local YAML and run `kubectl create -f ...` again, you may accidentally create a new pod (for example, after changing `metadata.name`), which means another container is started.
- `kubectl edit pod <pod-name>` updates the existing live object instead of creating a second pod.

Example:

```bash
# Existing pod
kubectl get pods
# myapp-pod   1/1   Running

# Risky flow: change name in YAML to myapp-pod-v2, then create again
kubectl create -f pod-definition.yaml
kubectl get pods
# myapp-pod      1/1   Running
# myapp-pod-v2   1/1   Running   <-- extra pod/container created
```

Safer update flow:

```bash
# Edit the running pod directly
kubectl edit pod myapp-pod
```

- For file-based changes, prefer `kubectl apply -f pod-definition.yaml` instead of running `create` repeatedly.

Run/restart example (standalone Pod):

```bash
# Re-apply config (create if missing, update if exists)
kubectl apply -f pod-definition.yaml

# If you need a clean restart for a standalone pod
kubectl delete pod myapp-pod
kubectl apply -f pod-definition.yaml
```

## Pods - Replication

Replication means running multiple copies of the same Pod so your app stays available and can handle more traffic.

- If one Pod fails, Kubernetes creates a new one (self-healing).
- If traffic increases, you can increase the number of replicas (scaling).
- For modern workloads, use **ReplicaSet** (usually managed by a **Deployment**).
- **ReplicationController** is older and kept here for basics/legacy understanding.

### Option 1: ReplicationController (Legacy)

```yaml
apiVersion: v1
kind: ReplicationController
metadata:
  name: myapp-rc
spec:
  replicas: 3
  selector:
    app: myapp
    tier: frontend
  template:
    metadata:
      labels:
        app: myapp
        tier: frontend
    spec:
      containers:
        - name: nginx-container
          image: nginx:latest
          ports:
            - containerPort: 80
```

### Option 2: ReplicaSet (Recommended over RC)

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: myapp-rs
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
      tier: frontend
  template:
    metadata:
      labels:
        app: myapp
        tier: frontend
    spec:
      containers:
        - name: nginx-container
          image: nginx:latest
          ports:
            - containerPort: 80
```

### Labels and Selectors (Important)

- Labels are key-value tags on Pods.
- Selectors tell RC/RS which Pods they should manage.
- The labels in `template.metadata.labels` must match the selector.

### Common Commands (Organized)

```bash
# 1) Create resources
kubectl apply -f replication-controller.yaml
kubectl apply -f replicaset.yaml

# 2) List resources
kubectl get rc
kubectl get rs
kubectl get pods

# 3) Inspect details
kubectl describe rc myapp-rc
kubectl describe rs myapp-rs

# 4) Scale replicas
kubectl scale --replicas=5 -f replicaset.yaml
kubectl scale --replicas=5 rs myapp-rs

# 5) Delete resources
kubectl delete -f replication-controller.yaml
kubectl delete -f replicaset.yaml
```

### Quick Note

In real projects, you usually create a **Deployment**, and Deployment manages the ReplicaSet for you.

## Deployments

- A higher-level abstraction that manages ReplicaSets and Pods.
- Provides declarative updates, rollbacks, and scaling.

- It acts as the top layer for the replcaset and pod management. You create a deployment, and it creates the ReplicaSet, which in turn creates the Pods.

- The syntax is more similar to ReplicaSet, but with `kind: Deployment` and `apiVersion: apps/v1`.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
      tier: frontend
  template:
    metadata:
      labels:
        app: myapp
        tier: frontend
    spec:
      containers:
        - name: nginx-container
          image: nginx:latest
          ports:
            - containerPort: 80
```

Commands
```bash
# Create deployment
kubectl apply -f deployment.yaml  

#List deployments
kubectl get deployments

# Describe deployment
kubectl describe deployment myapp-deployment

# GET all the info
kubectl get all
```



