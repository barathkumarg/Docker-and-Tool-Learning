# Kubernetes Scheduling Examples

This folder contains runnable examples for Kubernetes scheduling features. See the core examples and basics in [src/kubernetes/1.core-concepts/README.md](src/kubernetes/1.core-concepts/README.md).

Files:

- `taint-toleration-pod.yaml` — Pod tolerates a node taint.
- `node-selector-pod.yaml` — Pod uses a node selector to bind to a labeled node.
- `node-affinity-pod.yaml` — Pod uses node affinity for scheduling onto nodes with matching labels.
- `pod-anti-affinity.yaml` — Pod uses pod anti-affinity to avoid colocating pods with the same `app` label on the same node.

## Setup

To use scheduling features effectively, you may want to create additional nodes in minikube:

```bash
# Create additional nodes in minikube
minikube node add
minikube node add --name minikube-m2
minikube node add --name minikube-m3

# List all nodes
kubectl get nodes

# Check minikube node status
minikube node list
```

## Concepts covered

- Taints and Tolerations
- Node Selectors
- Node Affinity
- Pod Anti-Affinity

---

## Taints and Tolerations

Purpose: Prevent pods from being scheduled on certain nodes unless they have matching tolerations.

Example YAML:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-taint-toleration
  labels:
    app: nginx-taint
spec:
  containers:
    - name: nginx
      image: nginx:stable
      ports:
        - containerPort: 80
  tolerations:
    - key: "special"
      operator: "Equal"
      value: "true"
      effect: "NoSchedule"
```

Commands:

```bash
# Add a taint to the first node
kubectl taint nodes $(kubectl get nodes -o name | head -n 1) special=true:NoSchedule

# Apply the toleration Pod manifest
kubectl apply -f taint-toleration-pod.yaml

# Inspect the pod and verify it was scheduled
kubectl get pods -o wide
kubectl describe pod nginx-taint-toleration
```

Cleanup:

```bash
kubectl delete -f taint-toleration-pod.yaml
kubectl taint nodes $(kubectl get nodes -o name | head -n 1) special=true:NoSchedule-
```

---

## Node Selectors

Purpose: Simple required scheduling filter based on node labels.

Example YAML:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-node-selector
  labels:
    app: nginx-node-selector
spec:
  nodeSelector:
    disktype: ssd
  containers:
    - name: nginx
      image: nginx:stable
      ports:
        - containerPort: 80
```

Commands:

```bash
# Label the first node for the selector example
kubectl label nodes $(kubectl get nodes -o name | head -n 1) disktype=ssd --overwrite

# Apply the nodeSelector Pod manifest
kubectl apply -f node-selector-pod.yaml

# Verify scheduling
kubectl get pods -o wide
kubectl describe pod nginx-node-selector
```

Cleanup:

```bash
kubectl delete -f node-selector-pod.yaml
kubectl label nodes $(kubectl get nodes -o name | head -n 1) disktype-
```

---

## Node Affinity

Purpose: More expressive rules for scheduling based on node attributes; supports required or preferred rules.

Example YAML:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-node-affinity
  labels:
    app: nginx-node-affinity
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
          - matchExpressions:
              - key: disktype
                operator: In
                values:
                  - ssd
  containers:
    - name: nginx
      image: nginx:stable
      ports:
        - containerPort: 80
```

Commands:

```bash
# Ensure the node is labeled (same label used by the manifest)
kubectl label nodes $(kubectl get nodes -o name | head -n 1) disktype=ssd --overwrite

# Apply the node affinity Pod manifest
kubectl apply -f node-affinity-pod.yaml

# Verify scheduling
kubectl get pods -o wide
kubectl describe pod nginx-node-affinity
```

Notes:

- If no node matches requiredDuringSchedulingIgnoredDuringExecution, the pod remains in Pending.

Cleanup:

```bash
kubectl delete -f node-affinity-pod.yaml
kubectl label nodes $(kubectl get nodes -o name | head -n 1) disktype-
```

---

## Pod Anti-Affinity

Purpose: Prevent pods with matching labels from running on the same topology domain (for example, the same node), improving availability.

Example YAML:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod-anti-affinity
  labels:
    app: nginx
spec:
  affinity:
    podAntiAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        - labelSelector:
            matchExpressions:
              - key: app
                operator: In
                values:
                  - nginx
          topologyKey: "kubernetes.io/hostname"
  containers:
    - name: nginx
      image: nginx:stable
      ports:
        - containerPort: 80
```

Commands:

```bash
# Apply an example pod that requests anti-affinity
kubectl apply -f pod-anti-affinity.yaml

# Verify scheduling and where pods are placed
kubectl get pods -o wide
kubectl describe pod nginx-pod-anti-affinity
```

Cleanup:

```bash
kubectl delete -f pod-anti-affinity.yaml
```

---

## General notes

- Start Minikube if you are running locally:

```bash
minikube start
```

- See [src/kubernetes/1.core-concepts/README.md](src/kubernetes/1.core-concepts/README.md) for basic pod/deployment/service examples and kubectl pre-requisites.

