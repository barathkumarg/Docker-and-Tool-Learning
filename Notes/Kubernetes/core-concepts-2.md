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

-  