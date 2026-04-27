# Kubernetes Core Concepts

## Cluster Architecture

Kubernetes follows a control plane + worker node model.

### Control Plane Components

- `kube-apiserver`: Entry point for all cluster operations.
- `etcd`: Distributed key-value store for cluster state and metadata.
- `kube-scheduler`: Assigns Pods to worker nodes.
- `kube-controller-manager`: Runs controllers (for node health, replicas, endpoints, etc.).

### Worker Node Components

- `kubelet`: Node agent that talks to the API server and manages Pods on the node.
- `kube-proxy`: Handles Service networking and Pod traffic routing rules.
- `containerd` (or another CRI runtime): Runs containers.

## Quick Analogy (Dock and Cargo Ships)

Use this only as a memory aid:

- Control plane: Dock operations center (plans, schedules, monitors).
- Worker nodes: Cargo ships carrying workloads (Pods/containers).
- `etcd`: Cargo manifest database.
- `kube-scheduler`: Decides which ship carries which cargo.
- Node controller: Monitors ship health and reports status.
- `kube-apiserver`: Communication and control channel.
- `kubelet`: Captain on each ship executing instructions.
- `kube-proxy`: Network routing between ships and services.

## Docker vs Containerd

- Docker is a full container platform.
- Kubernetes is a container orchestration system.
- Kubernetes now talks to runtimes through the **Container Runtime Interface (CRI)**.

### Why CRI Matters

Earlier Kubernetes relied on Docker integration. With CRI, Kubernetes supports multiple runtimes such as:

- `containerd`
- `CRI-O`
- (historically) `rkt`

### OCI Standards

Container runtimes and images follow **Open Container Initiative (OCI)** specs:

- OCI Runtime Specification
- OCI Image Specification

### Dockershim (Historical)

- `dockershim` was the bridge between Kubernetes and Docker.
- It has been deprecated/removed in modern Kubernetes releases.
- Preferred runtimes are CRI-native options like `containerd` and `CRI-O`.

## Runtime CLI Tools

### `ctr` (low-level containerd CLI)

```bash
ctr images pull docker.io/library/nginx:latest
ctr images list
```

### `nerdctl` (Docker-like UX for containerd)

```bash
nerdctl pull docker.io/library/nginx:latest
nerdctl images
```

### `crictl` (Kubernetes runtime debugging)

```bash
crictl pods
crictl ps
crictl images
```

## etcd

`etcd` is a distributed, reliable key-value store used by Kubernetes to persist:

- Cluster configuration
- Object metadata
- Desired and current state

It is critical for consistency, leader election, and recovery behavior in the control plane.

### Basic Installation (Example)

```bash
curl -LO https://github.com/etcd-io/etcd/releases/download/v3.6.10/etcd-v3.6.10-linux-amd64.tar.gz
tar xzvf etcd-v3.6.10-linux-amd64.tar.gz
cd etcd-v3.6.10-linux-amd64
./etcd
```

### Basic `etcdctl` Commands

```bash
etcdctl put key1 value1
etcdctl get key1
etcdctl --help
```

Note: Most modern setups use API v3 (`ETCDCTL_API=3`).

## etcd in Kubernetes Deployments

- **Manual/self-managed control plane**: `etcd` is installed and managed as a service (or externally).
- **kubeadm-based setup**: `etcd` usually runs as a static Pod on control plane nodes (unless external etcd is configured).
