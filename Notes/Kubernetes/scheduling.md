
## Table of Contents

- <a href="#topics">Topics</a>
- <a href="#manual-scheduling">Manual Scheduling</a>
  - <a href="#what-is-manual-scheduling">What is Manual Scheduling?</a>
  - <a href="#use-cases">Use Cases</a>
  - <a href="#how-to-manually-schedule-a-pod">How to Manually Schedule a Pod</a>
  - <a href="#considerations">Considerations</a>
  - <a href="#commands">Commands</a>
  - <a href="#notes">Notes</a>
- <a href="#labels-and-selectors">Labels and Selectors</a>
  - <a href="#what-are-labels-and-selectors">What are Labels and Selectors?</a>
  - <a href="#use-cases-1">Use Cases</a>
  - <a href="#examples">Examples</a>
  - <a href="#replicaset-example">ReplicaSet Example</a>
- <a href="#annotations">Annotations</a>
  - <a href="#what-are-annotations">What are Annotations?</a>
  - <a href="#use-cases-2">Use Cases</a>
  - <a href="#example-1">Example</a>
- <a href="#taints-and-tolerations">Taints and Tolerations</a>
  - <a href="#what-are-taints-and-tolerations">What are Taints and Tolerations?</a>
  - <a href="#use-cases-3">Use Cases</a>
  - <a href="#taint-and-toleration-components">Taint and Toleration Components</a>
  - <a href="#commands-1">Commands</a>
  - <a href="#pod-toleration-example">Pod Toleration Example</a>
  - <a href="#notes-1">Notes</a>
- <a href="#node-selectors-node-affinity-and-anti-affinity">Node Selectors, Node Affinity, and Anti-Affinity</a>
  - <a href="#what-are-node-selectors-node-affinity-and-anti-affinity">What are Node Selectors, Node Affinity, and Anti-Affinity?</a>
  - <a href="#use-cases-4">Use Cases</a>
  - <a href="#node-selector-example">Node Selector Example</a>
  - <a href="#node-affinity-example">Node Affinity Example</a>
  - <a href="#node-affinity-operators">Node Affinity Operators</a>
  - <a href="#behavior">Behavior</a>
  - <a href="#anti-affinity-example">Anti-Affinity Example</a>
- <a href="#node-affinity-and-taint-tolerations">Node Affinity and Taint-Tolerations</a>
- <a href="#resource-requirements">Resource Requirements</a>
  - <a href="#what-are-resource-requests-and-limits">What are Resource Requests and Limits?</a>
  - <a href="#use-cases-5">Use Cases</a>
  - <a href="#example-2">Example</a>
  - <a href="#constraints-cpu-and-memory">Constraints: CPU and Memory</a>
  - <a href="#behavior-of-resource-requests-and-limits">Behavior of Resource Requests and Limits</a>
  - <a href="#notes-2">Notes</a>
  - <a href="#limitrange">LimitRange</a>
    - <a href="#example-limitrange">Example LimitRange</a>
    - <a href="#apply-to-a-namespace">Apply to a Namespace</a>
  - <a href="#resource-quota">Resource Quota</a>
    - <a href="#example-resourcequota">Example ResourceQuota</a>
- <a href="#daemonsets">DaemonSets</a>
  - <a href="#example-daemonset">Example DaemonSet</a>
  - <a href="#daemonset-notes">DaemonSet Notes</a>
  - <a href="#commands-2">Commands</a>
- <a href="#static-pods">Static Pods</a>
  - <a href="#control-plane-note">Control Plane Note</a>
  - <a href="#kubelet-configuration">Kubelet Configuration</a>
  - <a href="#mirror-pods">Mirror Pods</a>
  - <a href="#static-pod-behavior">Static Pod Behavior</a>
  - <a href="#commands-3">Commands</a>
  - <a href="#additional-static-pod-commands">Additional Static Pod Commands</a>
  - <a href="#static-pod-steps">Static Pod Steps</a>
  - <a href="#static-pod-vs-daemonset">Static Pod vs DaemonSet</a>
- <a href="#priority-classes">Priority Classes</a>
  - <a href="#scenarios-for-using-priority-classes">Scenarios for Using Priority Classes</a>
  - <a href="#what-if-higher-priority-pods-cannot-be-scheduled">What if higher priority Pods cannot be scheduled?</a>
  - <a href="#commands-to-manage-priority-classes">Commands to manage Priority Classes</a>
- <a href="#multiple-schedulers">Multiple Schedulers</a>
  - <a href="#scheduler-deployment-styles">Scheduler deployment styles</a>
    - <a href="#scheduler-as-a-pod-in-cluster">Scheduler as a Pod (in-cluster)</a>
    - <a href="#scheduler-as-a-service-or-binary-out-of-cluster">Scheduler as a service or binary (out-of-cluster)</a>
  - <a href="#how-the-creation-process-differs">How the creation process differs</a>
  - <a href="#how-to-deploy-a-custom-scheduler-pod-based">How to deploy a custom scheduler (Pod-based)</a>
  - <a href="#how-to-run-a-scheduler-as-a-servicebinary">How to run a scheduler as a service/binary</a>
  - <a href="#commands-to-manage-multiple-schedulers">Commands to manage multiple schedulers</a>
- <a href="#scheduler-profiles">Scheduler Profiles</a>
  - <a href="#example-of-a-scheduler-configuration-with-multiple-profiles">Example of a scheduler configuration with multiple profiles</a>
- <a href="#securing-kubernetes">Securing Kubernetes</a>
  - <a href="#authentication-and-authorization">Authentication and Authorization</a>
  - <a href="#admission-controls">Admission Controls</a>
    - <a href="#types-of-admission-controllers">Types of Admission Controllers</a>
    - <a href="#common-built-in-admission-controllers">Common built-in Admission Controllers</a>
    - <a href="#example-limitranger-policy">Example: LimitRanger policy</a>
    - <a href="#example-resourcequota-policy">Example: ResourceQuota policy</a>
    - <a href="#example-validating-admission-with-podsecurity">Example: Validating admission with PodSecurity</a>
    - <a href="#configuring-admission-controllers">Configuring Admission Controllers</a>
    - <a href="#pod-level-effect">Pod-level effect</a>
    - <a href="#notes-3">Notes</a>
  - <a href="#difference-between-mutating-and-validating-admission-controllers">Difference between Mutating and Validating Admission Controllers</a>
  - <a href="#external-admission-controls--mutatingadmissionwebhook--validatingadmissionwebhook">External Admission Controls — MutatingAdmissionWebhook & ValidatingAdmissionWebhook</a>
    - <a href="#minimal-example-webhook-server-python--flask">Minimal example: webhook server (Python + Flask)</a>
    - <a href="#certificates-self-signed-quickstart">Certificates (self-signed quickstart)</a>
    - <a href="#deployment-and-service-simplified">Deployment and Service (simplified)</a>
    - <a href="#webhook-configuration-mutating-and-validating">Webhook configuration (Mutating and Validating)</a>
    - <a href="#apply-sequence">Apply sequence</a>
    - <a href="#testing">Testing</a>
    - <a href="#notes-and-best-practices">Notes and best practices</a>

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

- Kubernetes allows multiple schedulers in one cluster. Each scheduler watches for Pods that request its specific `schedulerName` and tries to assign those Pods to nodes.

- Role of a Scheduler: A scheduler assigns Pods to nodes based on resources, policies, and Pod requirements. The default scheduler is `kube-scheduler`, but custom schedulers can handle special workloads or custom placement rules.

- Use Cases for Multiple Schedulers:
  - Specialized scheduling for GPU, high-priority, or latency-sensitive workloads.
  - Different scheduling logic for separate teams or applications.
  - Testing alternative scheduling algorithms without changing the default scheduler.

## Scheduler deployment styles

### Scheduler as a Pod (in-cluster)

- The scheduler itself runs as a Kubernetes object, such as a `Deployment` or `DaemonSet`.
- This is the common way to deploy custom schedulers in modern clusters.
- The scheduler Pod is created by the API server and managed like other workloads.
- Advantages:
  - Easy to update, monitor, and scale.
  - Uses the same Kubernetes control plane for lifecycle management.
  - Works well with custom scheduler images and RBAC service accounts.

### Scheduler as a service or binary (out-of-cluster)

- The scheduler runs as a standalone process or system service on a control-plane node.
- It is started directly from a command line, systemd unit, or static Pod manifest on the node.
- This is often how the default `kube-scheduler` runs in kubeadm-managed clusters.
- Advantages:
  - Simpler in small or highly controlled clusters.
  - Can run outside the main cluster API lifecycle.
- Considerations:
  - Requires direct access to API server credentials via a kubeconfig file.
  - Still needs leader election to avoid multiple active schedulers using the same `schedulerName`.

## How the creation process differs

- Pod-based scheduler:
  1. Write a Deployment/Pod manifest for the scheduler.
  2. Submit it to the API server with `kubectl apply`.
  3. Kubernetes schedules and runs the scheduler Pod on a node.

- Service/binary-based scheduler:
  1. Install or place the `kube-scheduler` binary on a control-plane node.
  2. Configure it with a kubeconfig and scheduler config file.
  3. Start it as a process or via a node-level service.

## How to deploy a custom scheduler (Pod-based)

1. Create a custom scheduler Deployment with a unique name and label.
2. Configure the scheduler with a config file that defines `schedulerName`.
3. Create Pods that specify the custom scheduler in their `spec.schedulerName` field.

- Example custom scheduler Deployment:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: custom-scheduler
  namespace: kube-system
spec:
  replicas: 1
  selector:
    matchLabels:
      app: custom-scheduler
  template:
    metadata:
      labels:
        app: custom-scheduler
    spec:
      serviceAccountName: custom-scheduler
      containers:
      - name: kube-scheduler
        image: k8s.gcr.io/kube-scheduler:v1.24.0
        command:
        - kube-scheduler
        - --config=/etc/kubernetes/scheduler-config.yaml
        - --kubeconfig=/etc/kubernetes/scheduler.conf
        - --leader-elect=true
        volumeMounts:
        - name: config
          mountPath: /etc/kubernetes
      volumes:
      - name: config
        configMap:
          name: custom-scheduler-config
```

- Example custom scheduler configuration:
```yaml
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration
profiles:
- schedulerName: custom-scheduler
leaderElection:
  leaderElect: true
```

- Example Pod using a custom scheduler:
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

## How to run a scheduler as a service/binary

- Instead of creating a Deployment, the scheduler runs as a node-local process.
- The command and config are managed outside the API server lifecycle.

- Example command:
```bash
kube-scheduler \
  --kubeconfig=/etc/kubernetes/scheduler.conf \
  --config=/etc/kubernetes/scheduler-config.yaml \
  --leader-elect=true
```

- In kubeadm setups, the default `kube-scheduler` is often run as a static Pod manifest in `/etc/kubernetes/manifests/kube-scheduler.yaml`.
- In older setups, it may also run as a systemd or init service.

## Commands to manage multiple schedulers
```bash
# List scheduler Pods in the cluster
kubectl get pods -n kube-system -l component=kube-scheduler

# Describe a specific scheduler Pod
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

# Securing Kubernetes 
## Authentication and Authorization
- Kubectl -> API Server -> Authentication -> Authorization -> Scheduler -> Kubelet

- The API server authenticates requests from users and service accounts, then authorizes them based on RBAC policies. The scheduler and kubelet enforce these policies when scheduling and running Pods.

- Things can be achieed in the Authentication and Authorization process:
  - Authentication: Verify the identity of the user or service account making the request.
  - Authorization: Determine if the authenticated user has permission to perform the requested action on the specified resource.

  - Can create/Delete/list a Pod with specified labels, annotations, or taints based on RBAC policies.

  - Can create a custom scheduler with specific permissions to schedule Pods with certain labels or annotations.

  e.g:
  ```yaml
  apiVersion: rbac.authorization.k8s.io/v1
  kind: Role
  metadata:
    namespace: my-namespace
    name: pod-manager
  rules:
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["create", "delete", "get", "list", "watch"]
  - apiGroups: [""]
    resources: ["pods/exec"]
    verbs: ["create", "get"]
  ```
  - The above Role allows users to create, delete, and list Pods in the `my-namespace` namespace, as well as execute commands in Pods.

  - Config to be applied in the pod manifest to use the Role:
  ```yaml
  apiVersion: v1
  kind: Pod
  metadata: 
    name: my-pod
    namespace: my-namespace
  spec:
    serviceAccountName: pod-manager
    containers:
    - name: my-container
      image: my-image
  ```

  - The above Pod manifest specifies the `serviceAccountName` as `pod-manager`, which is associated with the Role that allows managing Pods in the `my-namespace` namespace.

- Things cannot be achieved in the Authentication and Authorization process:
  - Cannot specify the image to be pulled for global registry access without proper permissions.
  - Cannot schedule Pods on specific nodes without the necessary RBAC permissions.
  - Cannot modify the scheduler's configuration or add new scheduling policies without appropriate access rights.
  - Pods cannot be scheduled on nodes with specific taints or labels unless the user has the required permissions to create or modify those taints and labels.
  - Donot permit root access to containers without proper authorization, as it may lead to security vulnerabilities.


## Admission Controls

- Admission Controllers are a set of plugins that run after Authentication and Authorization, but before the request is saved in etcd.
- They inspect, modify, or reject API requests for Kubernetes objects such as Pods, Deployments, Services, and PersistentVolumeClaims.
- This makes them a powerful place to enforce cluster policy, provide defaults, and improve security.

- Request flow in Kubernetes:
  - kubectl -> API Server -> Authentication -> Authorization -> Admission Controllers -> Scheduler -> Kubelet

### Types of Admission Controllers

- Mutating Admission Controllers
  - These can change the incoming object before it is stored.
  - Example: add default labels, set image pull policy, inject sidecar containers.

- Validating Admission Controllers
  - These only accept or reject the request.
  - Example: prevent Pods from running as root, deny unsupported API fields, enforce size limits.

### Common built-in Admission Controllers

- `NamespaceLifecycle`
  - Prevents operations in terminating namespaces and ensures namespace rules are followed.

- `LimitRanger`
  - Enforces default resource requests/limits when a Pod or Container does not specify them.

- `ResourceQuota`
  - Limits how many resources (CPU, memory, Pods, Services, PersistentVolumeClaims) a namespace can use.

- `DefaultStorageClass`
  - Automatically fills in a default storage class for PersistentVolumeClaims that do not specify one.

- `ServiceAccount`
  - Automatically creates a ServiceAccount for new Pods and mounts service account tokens.

- `PodSecurity`
  - Enforces Pod security policies such as restricted capabilities, root user restrictions, and host path usage.

### Example: LimitRanger policy

A `LimitRange` object is a simple example of admission control rules for a namespace.

```yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: example-limitrange
  namespace: demo
spec:
  limits:
  - type: Container
    max:
      cpu: "500m"
      memory: "512Mi"
    min:
      cpu: "100m"
      memory: "128Mi"
    default:
      cpu: "200m"
      memory: "256Mi"
    defaultRequest:
      cpu: "150m"
      memory: "192Mi"
```

- When a Pod is created in the `demo` namespace, the admission controller enforces these limits.
- If a container does not specify CPU/memory requests or limits, default values are applied.
- If the container requests more than the maximum, the Pod is rejected.

### Example: ResourceQuota policy

A `ResourceQuota` object limits the total resources a namespace can consume.

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: demo-quota
  namespace: demo
spec:
  hard:
    pods: "10"
    requests.cpu: "2"
    requests.memory: "2Gi"
    persistentvolumeclaims: "5"
```

- This policy prevents the namespace from creating more than 10 Pods or requesting more than 2 CPU cores and 2Gi of memory.
- If the quota is exceeded, new object creation is rejected.

### Example: Validating admission with PodSecurity

`PodSecurity` is a built-in policy that validates Pod security settings.

```yaml
apiVersion: policy/v1
kind: PodSecurityPolicy
metadata:
  name: restricted
spec:
  privileged: false
  allowPrivilegeEscalation: false
  volumes:
  - configMap
  - secret
  - emptyDir
  runAsUser:
    rule: MustRunAsNonRoot
```

- This example prevents privileged containers and requires Pods to run as a non-root user.
- If a Pod violates the policy, the admission controller rejects the creation.

### Configuring Admission Controllers

- Admission controllers are set on the API server, not inside normal application Pod manifests.
- In a systemd-managed cluster, update the kube-apiserver `.service` file and add flags like:

```bash
--enable-admission-plugins=NamespaceLifecycle,LimitRanger,ServiceAccount
```

- In kubeadm or static-pod setups, edit the `/etc/kubernetes/manifests/kube-apiserver.yaml` file and change the `kube-scheduler` container command args.

- Example snippet from a static pod manifest:

```yaml
spec:
  containers:
  - name: kube-apiserver
    command:
    - kube-apiserver
    - --enable-admission-plugins=NamespaceLifecycle,LimitRanger,ServiceAccount
```

### Pod-level effect

- Admission controllers may mutate or reject Pods during creation.
- A simple Pod manifest can be accepted with defaults or rejected if it violates policy.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: demo-pod
  namespace: demo
spec:
  containers:
  - name: app
    image: nginx:latest
```

- If `LimitRanger` is enabled, the Pod may get default CPU/memory requests added.
- If a Pod violates a security policy, the request is rejected before the Pod is created.


### Notes

- Admission Controllers help enforce cluster rules automatically and consistently.
- They are especially useful for ensuring resource limits, security policies, and namespace behavior.
- Many important controllers are enabled by default, so you often only need to add custom webhooks or extra policy plugins when required.
- For custom policies, Kubernetes supports `MutatingAdmissionWebhook` and `ValidatingAdmissionWebhook` to connect external services.
## Difference between Mutating and Validating Admission Controllers

- **Mutating Admission Controllers:**
  - Can modify incoming API objects before they are persisted.
  - Typically used to inject defaults, add labels/annotations, or insert sidecars (e.g., Istio/Linkerd sidecar injection).
  - Run in the admission pipeline during the "mutating" phase; multiple mutating webhooks may be called in sequence.
  - A mutation returns a JSONPatch in the AdmissionReview response; the API server applies the patch and continues processing.

- **Validating Admission Controllers:**
  - Cannot change objects; they only accept or reject requests.
  - Used to enforce policies, security rules, or organizational constraints (e.g., deny privileged containers, enforce image registries).
  - Run after mutating admission controllers; validators see the object after any mutations have been applied.
  - A validation webhook returns allowed=true/false and may include a message explaining rejections.

- **Key differences & behavior:**
  - Mutating controllers may change objects; validating controllers only allow/deny.
  - Order: Mutating webhooks run first (possibly multiple), then validating webhooks run on the final, mutated object.
  - Failure handling: webhook failures can be configured with `failurePolicy` (`Fail` or `Ignore`). `Fail` will block the request if the webhook cannot be reached.
  - Use mutating webhooks for defaulting/enrichment and validating webhooks for policy enforcement and safety checks.

## External Admission Controls — MutatingAdmissionWebhook & ValidatingAdmissionWebhook

External admission webhooks let you implement admission logic outside the API server. Common usage is to run an HTTPS service (inside the cluster) that the API server calls during object creation/update.

High-level steps to host and run a webhook as a Kubernetes Service:

1. Implement a webhook server with HTTPS endpoints that accept `AdmissionReview` requests and return `AdmissionReview` responses.
2. Generate or obtain TLS certificates for the webhook server and a CA certificate for the API server to trust.
3. Deploy the webhook server in the cluster (Deployment + Service) and store the server cert/key in a TLS Secret.
4. Create `MutatingWebhookConfiguration` and/or `ValidatingWebhookConfiguration` resources that point to the Service and include the CA bundle.
5. Test by creating objects that should be mutated or validated.

### Minimal example: webhook server (Python + Flask)

Below is a simple example that implements both a mutating and validating endpoint. The mutating endpoint adds an annotation; the validating endpoint rejects Pods that set `containers[0].securityContext.runAsNonRoot=false`.

app.py:

```python
from flask import Flask, request, jsonify
import json, base64

app = Flask(__name__)

def admission_response(uid, allowed=True, patch=None, message=None):
    resp = {
        "apiVersion": "admission.k8s.io/v1",
        "kind": "AdmissionReview",
        "response": {
            "uid": uid,
            "allowed": allowed
        }
    }
    if message:
        resp['response']['status'] = {"message": message}
    if patch is not None:
        # patch must be base64-encoded JSONPatch
        resp['response']['patchType'] = 'JSONPatch'
        resp['response']['patch'] = base64.b64encode(json.dumps(patch).encode()).decode()
    return resp

@app.route('/mutate', methods=['POST'])
def mutate():
    req = request.get_json()
    uid = req['request']['uid']
    obj = req['request']['object']
    # Ensure annotations map exists
    patch = []
    if 'metadata' not in obj:
        patch.append({"op": "add", "path": "/metadata", "value": {}})
    if 'annotations' not in obj.get('metadata', {}):
        patch.append({"op": "add", "path": "/metadata/annotations", "value": {"mutated-by": "example-webhook"}})
    else:
        patch.append({"op": "add", "path": "/metadata/annotations/mutated-by", "value": "example-webhook"})
    return jsonify(admission_response(uid, allowed=True, patch=patch))

@app.route('/validate', methods=['POST'])
def validate():
    req = request.get_json()
    uid = req['request']['uid']
    obj = req['request']['object']
    # Very simple check: reject Pod if first container explicitly allows running as root
    containers = obj.get('spec', {}).get('containers', [])
    for c in containers:
        sc = c.get('securityContext', {})
        if sc.get('runAsNonRoot') is False:
            return jsonify(admission_response(uid, allowed=False, message='Containers must not set runAsNonRoot: false'))
    return jsonify(admission_response(uid, allowed=True))

if __name__ == '__main__':
    # In production, run behind a WSGI server and use TLS at the pod level.
    app.run(host='0.0.0.0', port=8443)
```

### Certificates (self-signed quickstart)

Run locally to create a CA and a server cert (adjust CN to match the service DNS name):

```bash
openssl genrsa -out ca.key 2048
openssl req -x509 -new -nodes -key ca.key -subj "/CN=example-ca" -days 365 -out ca.crt

openssl genrsa -out server.key 2048
openssl req -new -key server.key -subj "/CN=webhook-service.default.svc" -out server.csr
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 365 -sha256
```

Create a TLS secret in the namespace where the webhook will run (example uses `default`):

```bash
kubectl create secret tls webhook-server-cert --cert=server.crt --key=server.key -n default
```

### Deployment and Service (simplified)

deployment.yaml:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: example-webhook
  namespace: default
spec:
  replicas: 1
  selector:
    matchLabels:
      app: example-webhook
  template:
    metadata:
      labels:
        app: example-webhook
    spec:
      containers:
      - name: webhook
        image: python:3.9-slim
        command: ["python", "/app/app.py"]
        ports:
        - containerPort: 8443
        volumeMounts:
        - name: webhook-certs
          mountPath: /etc/webhook/certs
          readOnly: true
      volumes:
      - name: webhook-certs
        secret:
          secretName: webhook-server-cert

---
apiVersion: v1
kind: Service
metadata:
  name: webhook-service
  namespace: default
spec:
  ports:
  - port: 443
    targetPort: 8443
  selector:
    app: example-webhook
```

Mount the certificate files from `/etc/webhook/certs` and configure your server to use them.

### Webhook configuration (Mutating and Validating)

You must include the CA bundle so the API server can verify the webhook server's certificate. Example commands to prepare the CA bundle:

```bash
CA_BUNDLE=$(base64 -w0 < ca.crt)
```

mutating-webhook.yaml (snippet):

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: MutatingWebhookConfiguration
metadata:
  name: example-mutating-webhook
webhooks:
  - name: example.mydomain.io
    clientConfig:
      service:
        name: webhook-service
        namespace: default
        path: "/mutate"
      caBundle: <CA_BUNDLE_REPLACE>
    rules:
      - apiGroups: [""]
        apiVersions: ["v1"]
        operations: ["CREATE","UPDATE"]
        resources: ["pods"]
    admissionReviewVersions: ["v1"]
    sideEffects: None
    failurePolicy: Fail
```

validating-webhook.yaml (snippet):

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
metadata:
  name: example-validating-webhook
webhooks:
  - name: validate.example.mydomain.io
    clientConfig:
      service:
        name: webhook-service
        namespace: default
        path: "/validate"
      caBundle: <CA_BUNDLE_REPLACE>
    rules:
      - apiGroups: [""]
        apiVersions: ["v1"]
        operations: ["CREATE","UPDATE"]
        resources: ["pods"]
    admissionReviewVersions: ["v1"]
    sideEffects: None
    failurePolicy: Fail
```

Replace `<CA_BUNDLE_REPLACE>` with the value of `$CA_BUNDLE` (or paste the PEM directly encoded in base64).

### Apply sequence

1. Create the TLS secret in the webhook namespace (see `kubectl create secret tls` above).
2. Deploy the webhook server (`kubectl apply -f deployment.yaml`).
3. Compute the CA bundle and create the webhook configurations (`kubectl apply -f mutating-webhook.yaml` and `validating-webhook.yaml`).

### Testing

Test mutation:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-to-be-mutated
spec:
  containers:
  - name: nginx
    image: nginx:alpine
```

Create it: `kubectl apply -f test-pod.yaml` and then `kubectl get pod pod-to-be-mutated -o yaml` — you should see the `mutated-by: example-webhook` annotation added by the mutating webhook.

Test validation (example that should be rejected):

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-to-be-rejected
spec:
  containers:
  - name: busy
    image: busybox
    securityContext:
      runAsNonRoot: false
    command: ["sleep","3600"]
```

If the validating webhook is active, the create request will be rejected with the message configured in the webhook server.

### Notes and best practices

- Use `failurePolicy: Fail` for strict enforcement or `Ignore` when you prefer availability over policy enforcement.
- Keep webhook handlers efficient and highly available; slow webhooks increase API server latency.
- Prefer deploying webhooks in the control plane or with high availability and proper RBAC service accounts.
- For production use, automate certificate management using cert-manager to provision and rotate certificates.

----
Updated the sections for admission controller differences and provided a runnable webhook example and deployment steps.

