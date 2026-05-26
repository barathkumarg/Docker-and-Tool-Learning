# Topics

- Manual Scheduling
- Labels and Selectors
- Resource Limits
- DaemonSets
- Multiple Schedulers
- Scheduler Events


# Manual Scheduling
### What is Manual Scheduling?
  - Manually assigning a Pod to a specific node without relying on the Kubernetes scheduler.
### Use Cases for Manual Scheduling:
  - Testing and Debugging: Manually scheduling a Pod can help in testing specific node configurations or debugging issues related to node resources.
  - Specialized Workloads: Certain workloads may require specific hardware or software configurations that are only available on certain nodes.
  - Performance Optimization: Manually scheduling can help optimize performance by placing Pods on nodes with better resources or closer to data sources.
  - Pod will be in `Pending` state until the specified node is available and has sufficient resources to run the Pod.
### How to Manually Schedule a Pod:   
  - Create a Pod manifest with the `nodeName` field set to the desired node's name.
  - Use `nodeName` field in Pod spec to specify the node for scheduling.
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: my-container
    image: my-image
  nodeName: my-node
```
### Considerations for Manual Scheduling:
  - Manual scheduling bypasses the Kubernetes scheduler, so it may lead to resource contention if not managed carefully.
  - It is important to ensure that the specified node has sufficient resources to run the Pod.
  - Manual scheduling is not recommended for production environments as it can lead to maintenance challenges and reduced flexibility in workload management.

### Commands
```bash
# To view the status of a manually scheduled Pod:
kubectl get pods my-pod -o wide

# To view the status of the scheduler:
kubectl get pods --namespace kube-system
```

- **Why the kubectl apply not working for manual scheduling?**
  - When you use `kubectl apply` to create or update a Pod with a specified `nodeName`, the Kubernetes scheduler will not automatically assign the Pod to a node. Instead, the Pod will be in a `Pending` state until the specified node is available and has sufficient resources to run the Pod. This is because manual scheduling bypasses the Kubernetes scheduler, and it relies on the user to ensure that the specified node can accommodate the Pod's resource requirements.

# Labels and Selectors
### What are Labels and Selectors?
  - Labels are key-value pairs attached to Kubernetes objects (like Pods, Services, etc.) that are used to organize and select subsets of objects.
  - Selectors are queries that allow you to filter and select objects based on their labels.
### Use Cases for Labels and Selectors:
  - Organizing Resources: Labels help in categorizing and organizing resources based on attributes like environment

  - Can find the labels in the pod as below:
```bash
# To view the labels of a Pod:
kubectl get pods my-pod --show-labels

# Filter the pods with specific label:
kubectl get pods -l app=my-app

# To view the objects using the selector
kubectl get all --selector env=production
```
  - YAML example of labels and selectors:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
  labels:
    app: my-app
    environment: production
...
```
- **How to Use Labels and Selectors:**
  - You can use labels to group resources and selectors to query those groups. For example, you can create a Service that selects Pods with a specific label:
```yaml
apiVersion: v1
kind: ReplicaSet
metadata:
  name: my-replicaset
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
        function: backend
    spec:
      containers:
      - name: my-container
        image: my-image
```

- Here the `selector` is used to select Pods with the label `app: my-app`, and the `template` defines the labels that will be applied to the Pods created by the ReplicaSet. Hence the pod eith `app: my-app` and `function: backend` labels will be created as the replica set.

## Annotations  
### What are Annotations?
  - Annotations are key-value pairs that can be attached to Kubernetes objects to store arbitrary metadata. Unlike labels, annotations are not used for selection or grouping but can be used to store information that may be useful for tools and libraries.
### Use Cases for Annotations:
  - Storing Metadata: Annotations can be used to store additional information about an object, such as build information, deployment details, or any other custom data that may be relevant to the object
  e.g., `kubectl.kubernetes.io/last-applied-configuration` annotation stores the last applied configuration of an object when using `kubectl apply`.
  - Tooling and Automation: Annotations can be used by tools and automation scripts to store information that may be needed for processing or decision-making.
### How to Use Annotations:
  - You can add annotations to Kubernetes objects in the metadata section of the object definition. For example:
```yamlapiVersion: v1
kind: Pod
metadata:
  name: my-pod    
  annotations:
    description: "This is a sample pod for demonstration purposes."
    owner: "team-a"
spec:
```

# Taints and Tolerations
### What are Taints and Tolerations?  
  - Taints and tolerations are mechanisms in Kubernetes that allow you to control which Pods can be scheduled on which nodes. Taints are applied to nodes, while tolerations are applied to Pods.
### Use Cases for Taints and Tolerations:
  - Node Isolation: Taints can be used to isolate certain nodes for specific workloads, ensuring that only Pods with the appropriate tolerations can be scheduled on those nodes.
  - Resource Management: Taints can help manage resources by preventing certain Pods from being scheduled on nodes that are reserved for specific workloads or have limited resources.

  - `Taint` are applied on the nodes level, prevents the pods from scheduling on the node unless the pod has a matching `toleration`. Taints have three components: key, value, and effect. The effect can be `NoSchedule`, `PreferNoSchedule`, or `NoExecute`.
  - `Toleration` are applied on the pod level, allows the pod to be scheduled on nodes with matching taints. Tolerations have three components: key, operator, and value. The operator can be `Equal` or `Exists`.

### How to Use Taints and Tolerations:
  - To add a taint to a node, you can use the following
```bash
kubectl taint nodes <node-name> key=value:effect
```
  - To add a toleration to a Pod, you can include it in the Pod specification:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  tolerations:
  - key: "key"
    operator: "Equal"
    value: "value"
    effect: "NoSchedule"
```

- To view the taints on a node, you can use the following command:
```bash
kubectl describe node <node-name> | grep -i taints
```

- Command to untaint a node:
```bash
# `Add` minus sign (-) at the end of the taint to remove it from the node
kubectl taint nodes <node-name> key=value:effect-
```

### Important Notes:
  - It never guarantees that the pod will be scheduled on the node with the matching taint, it only allows the pod to be scheduled on that node if there are no other nodes available that do not have the taint.
  - `Master Node` is tainted by default to prevent scheduling of regular pods on it. The taint is `node-role.kubernetes.io/master:NoSchedule`, which means that only pods with a toleration for this taint can be scheduled on the master node. This is done to ensure that the master node is reserved for running critical control plane components and is not used for running regular application workloads.

# Node Selectors, Node Affinity, and Anti-Affinity

### What are Node Selectors, Node Affinity, and Anti-Affinity?
  - Node Selectors, Node Affinity, and Anti-Affinity are mechanisms in Kubernetes that allow you to control the scheduling of Pods based on node attributes and preferences.
### Use Cases for Node Selectors, Node Affinity, and Anti-Affinity:
  - Node Selectors:
    - Used for simple scheduling requirements where you want to schedule Pods on nodes with specific labels.
  - Node Affinity:
    - Used for more complex scheduling requirements where you want to specify rules for how Pods should be scheduled based on node attributes, such as preferred or required node labels.
  - Anti-Affinity:
    - Used to prevent Pods from being scheduled on the same node or in the same topology domain, which can help improve availability and reduce the risk of failure.
### How to Use Node Selectors, Node Affinity, and Anti-Affinity:
#### Node Selectors:

  - Pod yaml file with node selector:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec: 
  nodeSelector:
    disktype: ssd
```
  - Apply the label to the node:
```bash
kubectl label nodes <node-name> disktype=ssd `
```
  - Node yaml file with node selector:
```yaml
apiVersion: v1
kind: Node
metadata:
  name: my-node
  labels:
    disktype: ssd
```

#### Node Affinity:
  - Pod yaml file with node affinity:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
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
```
- Operators : `exists`, `doesNotExist`, `in`, `notIn`, `gt`, `lt`

- What if no Nodes match the Node Affinity rules? What if pod label changed ?

**Node Affnity Types**:
  - `requiredDuringSchedulingIgnoredDuringExecution`: The Pod will only be scheduled on nodes that match the specified affinity rules. If no nodes match, the Pod will remain in a `Pending` state until a suitable node becomes available. If the Pod is already running and the node's labels change such that it no longer matches the affinity rules, the Pod will continue to run on that node until it is evicted or deleted, but it will not be rescheduled to another node that matches the affinity rules.

  - `preferredDuringSchedulingIgnoredDuringExecution`: The scheduler will try to schedule the Pod on nodes that match the specified affinity rules, but if no such nodes are available, it will schedule the Pod on any available node. If the Pod is already running and the node's labels change such that it no longer matches the affinity rules, the Pod will continue to run on that node until it is evicted or deleted, but it will not be rescheduled to another node that matches the affinity rules.

#### Anti-Affinity:
  - Pod yaml file with anti-affinity:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  affinity:
    podAntiAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchExpressions:
          - key: app
            operator: In
            values:
            - my-app
        topologyKey: "kubernetes.io/hostname"
```