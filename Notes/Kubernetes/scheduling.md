# Topics

- Manual Scheduling
- Labels and Selectors
- Annotations
- Taints and Tolerations
- Node Selectors, Node Affinity, and Anti-Affinity
- Node Affinity and Taint-Tolerations

# Manual Scheduling

## What is Manual Scheduling?

Manual scheduling means assigning a Pod to a specific node using the `nodeName` field, bypassing the default Kubernetes scheduler.

## Use Cases

- Testing and debugging node-specific behavior.
- Scheduling workloads on nodes with special hardware or software.
- Performance tuning by placing Pods on a node close to data or with better resources.
- Running a Pod on a node that already has a reserved environment.

## How to Manually Schedule a Pod

Create a Pod manifest with the `nodeName` field set to the target node name.

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

## Considerations

- Manual scheduling bypasses the Kubernetes scheduler.
- It may cause resource contention if the target node is already busy.
- The specified node must have enough resources for the Pod.
- Manual scheduling is generally not recommended for production workloads.
- If the node is unavailable or cannot accommodate the Pod, the Pod remains in `Pending`.

## Commands

```bash
# View a manually scheduled Pod
kubectl get pods my-pod -o wide

# View scheduler-related Pods in kube-system
kubectl get pods --namespace kube-system
```

## Notes

- `kubectl apply` does work for a Pod with `nodeName`, but the Pod will stay `Pending` until the specified node is available and has sufficient resources.
- Manual scheduling relies on the user to ensure the node can run the Pod.

# Labels and Selectors

## What are Labels and Selectors?

- Labels are key-value pairs attached to Kubernetes objects.
- Selectors are queries used to find objects based on labels.

## Use Cases

- Organize resources by environment, app, tier, or team.
- Filter objects for Services, ReplicaSets, and Deployments.
- Select subsets of Pods for management or monitoring.

## Examples

```bash
# View labels for a Pod
kubectl get pods my-pod --show-labels

# Filter Pods by label
kubectl get pods -l app=my-app

# View all objects matching a selector
kubectl get all --selector env=production
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
  labels:
    app: my-app
    environment: production
spec:
  containers:
  - name: my-container
    image: my-image
```

## ReplicaSet Example

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

The `selector` matches Pods with `app: my-app`, while the ReplicaSet template defines the labels assigned to new Pods.

# Annotations

## What are Annotations?

Annotations are key-value pairs attached to Kubernetes objects to store metadata that is not used for selection.

## Use Cases

- Store build, deployment, or audit metadata.
- Attach tool-specific or automation metadata.
- Preserve configuration details used by tools like `kubectl`.

## Example

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
  annotations:
    description: "This is a sample pod for demonstration purposes."
    owner: "team-a"
spec:
  containers:
  - name: my-container
    image: my-image
```

# Taints and Tolerations

## What are Taints and Tolerations?

- Taints are applied to nodes to repel Pods.
- Tolerations are applied to Pods to allow them onto tainted nodes.

## Use Cases

- Isolate nodes for special workloads.
- Reserve nodes for dedicated applications.
- Keep general workloads off control-plane or specialized nodes.

## Taint and Toleration Components

- Taint: `key`, `value`, `effect`
- Effects: `NoSchedule`, `PreferNoSchedule`, `NoExecute`
- Toleration: `key`, `operator`, `value`, `effect`
- Operators: `Equal`, `Exists`

## Commands

```bash
# Add a taint to a node
kubectl taint nodes <node-name> key=value:effect

# View taints on a node
kubectl describe node <node-name> | grep -i taints

# Remove a taint from a node
kubectl taint nodes <node-name> key=value:effect-
```

## Pod Toleration Example

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
  containers:
  - name: my-container
    image: my-image
```

## Notes

- A toleration does not guarantee scheduling on a node; it only allows the Pod to be eligible for matching tainted nodes.
- Control-plane nodes are typically tainted with `node-role.kubernetes.io/master:NoSchedule`.

# Node Selectors, Node Affinity, and Anti-Affinity

## What are Node Selectors, Node Affinity, and Anti-Affinity?

- Node Selector: simple label-based node selection.
- Node Affinity: expressive node selection rules.
- Anti-Affinity: rules to avoid scheduling Pods together.

## Use Cases

- Node Selector: schedule Pods on nodes with a specific label.
- Node Affinity: specify preferred or required node attributes.
- Pod Anti-Affinity: spread replicas across nodes or failure domains.

## Node Selector Example

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  nodeSelector:
    disktype: ssd
  containers:
  - name: my-container
    image: my-image
```

```bash
kubectl label nodes <node-name> disktype=ssd
```

## Node Affinity Example

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
  containers:
  - name: my-container
    image: my-image
```

## Node Affinity Operators

- `Exists`
- `DoesNotExist`
- `In`
- `NotIn`
- `Gt`
- `Lt`

## Behavior

- If no nodes match required affinity, the Pod stays `Pending`.
- If labels change after scheduling, the Pod continues running until evicted or deleted.

## Anti-Affinity Example

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
  containers:
  - name: my-container
    image: my-image
```

# Node Affinity and Taint-Tolerations

- Taints and node affinity both affect scheduling, but neither alone guarantees placement.
- A Pod must satisfy both the node affinity and the taint toleration to be scheduled on a matching tainted node.
- If no suitable node exists, the Pod remains `Pending`.

```bash
# Add a taint to the node
kubectl taint nodes <node-name> key=value:NoSchedule

# Label the node for affinity
kubectl label nodes <node-name> disktype=ssd
```

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
  - name: my-container
    image: my-image
```

# Resource Requirements

## What are Resource Requests and Limits?

Resource Requests and Limits let you specify the minimum and maximum CPU and memory a container can use.

- Requests: used by the scheduler to choose a node.
- Limits: enforce runtime usage constraints.

## Use Cases

- Requests ensure the Pod is scheduled on a node with enough resources.
- Limits prevent a container from using too much CPU or memory.

## Example

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: my-container
    image: my-image
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
```

## Constraints: CPU and Memory

- CPU is measured in CPU units where `1` CPU equals one core. A request of `0.5` means half a CPU core.
- Memory is measured in bytes, using units like `Mi` and `Gi`.

## Behavior of Resource Requests and Limits

- No requests or limits configured:
  - The container may use any available resources on the node, which can cause contention and instability.
- Only requests configured:
  - The scheduler reserves the requested resources, but the container may still use more if available.
- Only limits configured:
  - The container is limited at runtime but may be scheduled without guaranteed reserved capacity.
- Both requests and limits configured:
  - Preferred setup. The Pod is scheduled with reserved resources and limited to the configured maximum.

## Notes

- Exceeding the memory limit may trigger an OOM kill and terminate the container.
- Exceeding the CPU limit will throttle the container, reducing performance but not terminating it.
 

## LimitRange

LimitRange is a namespace-level object that defines default resource requests and limits for Pods and containers in that namespace.

- If a Pod does not specify requests or limits, Kubernetes may apply the defaults from the LimitRange.
- If a Pod specifies requests or limits, those values override the defaults.

### Example LimitRange

```yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: my-limit-range
spec:
  limits:
  - type: Container
    default:
      cpu: "500m"
      memory: "256Mi"
    defaultRequest:
      cpu: "250m"
      memory: "128Mi"
```

### Apply to a Namespace

```bash
kubectl apply -f limit-range.yaml -n my-namespace
```

## Resource Quota

ResourceQuota is a namespace-level object that limits the total resources consumed by all objects in the namespace.

- It can limit CPU, memory, number of Pods, and other resource types.
- If a Pod requests more resources than the quota allows, the API server rejects it.

### Example ResourceQuota

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: my-resource-quota
spec:
  hard:
    requests.cpu: "2"
    requests.memory: "4Gi"
    pods: "10"
```

# DaemonSets

A DaemonSet ensures that all (or selected) nodes run a copy of a Pod.

- As nodes are added, Pods are added.
- As nodes are removed, Pods are garbage collected.
- Deleting the DaemonSet removes the Pods it created.

### Example DaemonSet

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: my-daemonset
spec:
  selector:
    matchLabels:
      app: my-daemonset
  template:
    metadata:
      labels:
        app: my-daemonset
    spec:
      containers:
      - name: my-container
        image: my-image
```

### DaemonSet Notes

- A DaemonSet creates a Pod on each matching node.
- If a node does not match the selector, the DaemonSet does not schedule a Pod there.

### Commands

```bash
# List DaemonSets in the current namespace
kubectl get daemonsets

# Describe a specific DaemonSet
kubectl describe daemonset my-daemonset
```

# Static Pods

Static Pods are managed directly by the kubelet on a specific node, not by the Kubernetes control plane scheduler.

- Static Pods are defined by manifest files on the node, typically under `/etc/kubernetes/manifests`.
- The kubelet monitors that directory and creates or removes Pods based on manifest files.
- Static Pods are often used for critical control-plane components or system agents.

## Control Plane Note

The control plane includes the API server, controller manager, scheduler, and etcd. It maintains cluster state and schedules Pods.

## Kubelet Configuration

- `kube-service.yaml` typically includes `--pod-manifest-path=/etc/kubernetes/manifests`.
- `kubeconfig.yaml` typically includes `--kubeconfig=/etc/kubernetes/kubeconfig`.

## Mirror Pods

- When a static Pod is created by the kubelet, the API server creates a mirror Pod object with the same name.
- Mirror Pods are labeled with `kubernetes.io/config.mirror`.
- Mirror Pods provide visibility for static Pods through standard Kubernetes tools.

## Static Pod Behavior

- Static Pods are not managed by controllers such as ReplicaSet, DaemonSet, or StatefulSet.
- To run multiple static Pods, create separate manifest files with unique names.
- Delete a static Pod by removing its manifest file; the kubelet deletes the corresponding mirror Pod.

## Commands

```bash
# List static Pods on the node
docker ps --filter "label=kubernetes.io/config.mirror"

# Inspect a static Pod container
docker inspect <container-id>
```

```bash
# Identify the mirror Pod for a static Pod
kubectl get pods --all-namespaces -o wide --field-selector spec.nodeName=<node-name> -l kubernetes.io/config.mirror
```

## Additional Static Pod Commands

```bash
# View static Pods via kubectl
kubectl get pods --all-namespaces -o wide --field-selector spec.nodeName=<node-name>
```

```bash
# Create a static Pod by placing a manifest on the node
cat <<EOF | sudo tee /etc/kubernetes/manifests/my-static-pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-static-pod
spec:
  containers:
  - name: my-container
    image: my-image
EOF
```

```bash
# Delete a static Pod by removing its manifest
sudo rm /etc/kubernetes/manifests/my-static-pod.yaml
## Static Pod Steps

1. Create a static Pod manifest file on the node's filesystem, typically in `/etc/kubernetes/manifests`.
2. The kubelet detects the manifest and creates the static Pod on the node.
3. The kubelet also creates a mirror Pod in the Kubernetes API server for visibility.
4. To delete the static Pod, remove its manifest file; the kubelet deletes the mirror Pod.

## Static Pod vs DaemonSet

- A DaemonSet is a Kubernetes controller that ensures a Pod runs on all (or some) nodes.
- A static Pod is managed directly by the kubelet on a specific node and is not controlled by the API server.
- Static Pods are often used for critical system components; DaemonSets are used for node-level workload distribution.
```

# Priority Classes

- Priority Classes allow you to assign a priority level to Pods, influencing the order in which they are scheduled and evicted.
- Higher priority Pods are scheduled before lower priority ones and are less likely to be evicted during resource contention.

- Higher value means higher priority. The default priority is `0`. System-critical Pods often have a priority of `1000000` or more. Lower values indicate lower priority, and negative values can be used for best-effort workloads.Range: -1000000 to 1000000.

## Scenarios for Using Priority Classes
- Ensuring critical system components are scheduled before user workloads.
- Prioritizing important applications during resource contention.

## What if higher priority Pods cannot be scheduled?
- If a higher priority Pod cannot be scheduled due to resource constraints, the scheduler may preempt lower priority Pods to free up resources. Preempted Pods are evicted and may be rescheduled later when resources become available.

- When `preemptionPolicy` is set to `PreemptLowerPriority`, the scheduler will attempt to preempt lower priority Pods to make room for the higher priority Pod. If `preemptionPolicy` is set to `Never`, the scheduler will not preempt any Pods, and the higher priority Pod will remain in a `Pending` state until resources become available.

- Priority class object creation
```yaml
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: high-priority
value: 1000000
globalDefault: false # Optional, if true, this PriorityClass is the default for Pods that do not specify a priority class.
preemptionPolicy: PreemptLowerPriority # Optional, default is PreemptLowerPriority. Set to Never to disable preemption for this priority class.
description: "This priority class is for high-priority Pods."
```
- Assigning a priority class to a Pod
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  priorityClassName: high-priority
  containers: 
  - name: my-container
    image: my-image
``` 

## Commands to manage Priority Classes
```bash
# Create a PriorityClass
kubectl apply -f priority-class.yaml

# List PriorityClasses
kubectl get priorityclasses

# Describe a specific PriorityClass
kubectl describe priorityclass high-priority

# Delete a PriorityClass
kubectl delete priorityclass high-priority

# View Pods with their priority classes
kubectl get pods -o custom-columns=NAME:.metadata.name,PRIORITY:.spec.priorityClassName
``` 

# Multiple Schedulers

- Kubernetes allows you to run multiple schedulers in a cluster, each responsible for scheduling different sets of Pods based on specific criteria.

- Role of a Scheduler: A scheduler is responsible for assigning Pods to nodes based on resource availability and scheduling policies. The default scheduler is `kube-scheduler`, but you can deploy custom schedulers for specialized scheduling needs.

- Use Cases for Multiple Schedulers:
  - Specialized scheduling for specific workloads (e.g., GPU workloads, high-priority tasks).
  - Custom scheduling algorithms that differ from the default scheduler.
  - Isolation of scheduling responsibilities for different teams or applications.

## How to Deploy Multiple Schedulers:
1. Create a custom scheduler deployment with a unique name and label.
2. Configure the custom scheduler to watch for Pods with a specific `schedulerName` in their spec.
3. Create Pods that specify the custom scheduler in their `schedulerName` field.

- Example of a custom scheduler deployment:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: custom-scheduler
spec:
  replicas: 1
  selector:
    matchLabels:
      app: custom-scheduler
  command:
    - kube-scheduler
    - address= 127.0.0.1
    - --kubeconfig=/etc/kubernetes/scheduler.conf
    - config=/etc/kubernetes/scheduler-config.yaml
    image: k8s.gcr.io/kube-scheduler:v1.24.0
    name: custom-scheduler
   ...
```

- Example myscheduler-config.yaml:
```yaml
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration
profiles:
- schedulerName: custom-scheduler
leaderElection:
  leaderElect: true
```

- `leaderElection` is important for high availability. It ensures that if the active scheduler fails, another instance can take over without scheduling conflicts. If the value set to `true`, the scheduler will participate in leader election, allowing for high availability. If set to `false`, the scheduler will not participate in leader election, and if it fails, there will be no failover mechanism in place.

- `Note`: Another way to create was from the kube-scheduler binary, but the above method is more common in production environments.


- Usage of custom scheduler in a Pod:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  schedulerName: custom-scheduler
  containers:
  - name: my-container
    image: my-image
```

## Commands to manage multiple schedulers:
```bash
# List all schedulers in the cluster
kubectl get pods -n kube-system -l component=kube-scheduler

# Describe a specific scheduler
kubectl describe pod <scheduler-pod-name> -n kube-system

# View Pods scheduled by a specific scheduler
kubectl get pods -o wide --field-selector spec.schedulerName=custom-scheduler
```
# Scheduler Profiles

- Scheduler profiles allow you to define multiple scheduling policies within a single scheduler instance. Each profile can have its own set of plugins and rules for scheduling Pods.

- Consider the the pod to be scheduled in the node, undergoes a series of steps:

1. **Filtering**: The scheduler filters out nodes that do not meet the Pod's requirements (e.g., resource requests, node selectors).
  Plugins involved: `NodeResourcesFit`, `NodeSelector`, `TaintToleration`, etc.

2. **Scoring**: The scheduler scores the remaining nodes based on various criteria (e.g., resource availability, affinity rules).
  Plugins involved: `NodeResourcesLeastAllocated`, `NodeAffinity`, `PodAffinity`, etc

3. **Binding**: The scheduler binds the Pod to the selected node.
  Plugin involved: `DefaultBinder`  

- Use Cases for Scheduler Profiles:
  - Different scheduling policies for different types of workloads (e.g., high-priority vs. best-effort).
  - Testing new scheduling algorithms without affecting the default scheduler.
  - Custom scheduling for specific teams or applications.

## Example of a scheduler configuration with multiple profiles:
```yaml
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration
profiles:
- schedulerName: default-scheduler
  plugins:
    filter:
      enabled:
      - name: NodeResourcesFit
    score:
      enabled:
      - name: NodeResourcesLeastAllocated
- schedulerName: custom-scheduler
  plugins:  
    filter:
      enabled:
      - name: NodeSelector
    score:
      enabled:
      - name: NodeAffinity
```
