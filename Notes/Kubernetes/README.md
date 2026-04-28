# Kubernetes 

## Synopsis

This section covers Kubernetes core concepts including cluster architecture (control plane + worker nodes), container runtimes (containerd, CRI-O), storage (etcd), and the Kubernetes API. Learn about the reconciliation loop pattern, controllers for node health/replication/deployments, the scheduling mechanism for pod placement, and how worker node components (kubelet, kube-proxy) work together to manage container orchestration at scale.

## Core Concepts

### Architecture & Basics
- **Cluster Architecture**: Control plane + worker node model
- **Quick Analogy**: Dock and cargo ships memory aid
- **Docker vs Containerd**: Runtime differences and CRI
- **Runtime CLI Tools**: ctr, nerdctl, crictl

### Storage & State
- **etcd**: Distributed key-value store for cluster state
- **etcd in Kubernetes Deployments**: Manual vs kubeadm-based setups

### Control Plane Components
- **Kubernetes Architecture**: API Server overview
- **Kube API Server**: Entry point for all cluster operations
- **Kube Scheduler**: Pod assignment to nodes (Filter → Score → Bind)
- **Kube Controller Manager**: Reconciliation loops for desired state

### Worker Node Components
- **Kubelet**: Node agent managing containers
- **Kube-Proxy**: Service networking and routing (iptables/ipvs)

### Key Concepts
- **API Primitives**: Pods, Services, Deployments, ConfigMaps
- **Service and Other Network Primitives**: Services, Ingress, Network Policies