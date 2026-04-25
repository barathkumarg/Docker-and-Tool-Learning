# Container orchestration

- Why orchestration? When you have multiple containers running across different hosts, managing them manually can become complex and error-prone. Container orchestration tools help automate the deployment, scaling, and management of containerized applications, ensuring that they run smoothly and efficiently.

- Popular container orchestration tools include Kubernetes, Docker Swarm, and Apache Mesos. These tools provide features such as load balancing, service discovery, and automated rollouts and rollbacks.

## Service Creation and Scaling

```
docker service create --replicas 3 --name my_service nginx:latest
``` 
This command creates a new service named `my_service` with 3 replicas using the `nginx:latest` image. The orchestration tool will automatically manage the deployment and scaling of the service across the cluster, ensuring that there are always 3 instances of the Nginx container running.

## Solutions
- Kubernetes: An open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications. It provides features such as self-healing, load balancing, and rolling updates.

- Docker Swarm: A native clustering and orchestration tool for Docker. It allows you to create and manage a cluster of Docker nodes, providing features such as service discovery, load balancing, and scaling.

- Apache Mesos: A distributed systems kernel that abstracts CPU, memory, storage, and other resources away from machines, enabling fault-tolerant and elastic distributed systems to be easily built and run effectively. It can be used for container orchestration with frameworks like Marathon.

## Docker swarm
- Docker Swarm is a native clustering and orchestration tool for Docker. It allows you to create and manage a cluster of Docker nodes, providing features such as service discovery, load balancing, and scaling.

### Steps to create a swarm
- Setup the Swarm cluster by initializing the swarm on a manager node and joining worker nodes to the swarm. The manager node is responsible for managing the swarm and orchestrating the services, while worker nodes run the tasks assigned by the manager.

1. Initialize the swarm on the manager node:
```docker swarm init
```
This command initializes a new swarm and makes the current node the manager.

2. Join worker nodes to the swarm:
```docker swarm join --token <worker_token> <manager_ip>:2377
```
This command is run on each worker node, where `<worker_token>` is the token provided by the manager node during initialization, and `<manager_ip>` is the IP address of the manager node.

### Docker Service
- A Docker service is a higher-level abstraction that defines how containers should be deployed and managed in a swarm. It allows you to specify the desired state of your application, including the number of replicas, the image to use, and any necessary configurations. The swarm manager will ensure that the desired state is maintained, automatically scaling the service up or down as needed and replacing any failed containers.

3. Create a service in the swarm:
```docker service create --replicas 3 --name my_service nginx:latest
```
This command creates a new service named `my_service` with 3 replicas using the `nginx:latest` image. The swarm manager will automatically manage the deployment and scaling of the service across the cluster, ensuring that there are always 3 instances of the Nginx container running.


## Kubernetes
- Kubernetes is an open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications. It provides features such as self-healing, load balancing, and rolling updates.

### Steps to create a Kubernetes cluster
1. Set up a Kubernetes cluster using tools like Minikube (for local development) or kubeadm (for production environments). The cluster consists of a control plane (master node) that manages the cluster and worker nodes that run the containerized applications.

2. Deploy applications to the cluster using Kubernetes manifests (YAML files) that define the desired state of your application, including the number of replicas, the image to use, and any necessary configurations.  

3. Use Kubernetes features such as Deployments, Services, and Ingress to manage the lifecycle of your applications, handle load balancing, and expose your applications to the outside world.

4. Monitor and manage your cluster using tools like kubectl, which provides a command-line interface for interacting with the Kubernetes API server, allowing you to view the status of your applications, scale them up or down, and perform rolling updates.

### Useful commands 

- To create a deployment:
```kubectl create deployment my-deployment --image=nginx:latest
```
This command creates a new deployment named `my-deployment` using the `nginx:latest` image. Kubernetes will manage the deployment and ensure that the desired number of replicas are running.

- To scale a deployment:
```kubectl scale deployment my-deployment --replicas=5
```
This command scales the `my-deployment` deployment to 5 replicas, allowing Kubernetes to automatically create or remove pods as needed to maintain the desired state.

- To expose a deployment as a service:
```kubectl expose deployment my-deployment --type=LoadBalancer --port=80
```
This command exposes the `my-deployment` deployment as a service of type LoadBalancer, allowing external traffic to access the application running in the deployment on port 80. Kubernetes will automatically create a load balancer and route traffic to the appropriate pods.

### Nodes and Pods
- In Kubernetes, a node is a worker machine that runs containerized applications. A pod is the smallest deployable unit in Kubernetes, which can contain one or more containers. Pods are scheduled to run on nodes, and Kubernetes manages the lifecycle of pods, ensuring that they are running and healthy.
- To view the nodes in your cluster:
```kubectl get nodes
```
This command lists all the nodes in your Kubernetes cluster, showing their status and other relevant information.
- To view the pods in your cluster:
```kubectl get pods
```
This command lists all the pods in your Kubernetes cluster, showing their status and other relevant information.

### Master and Worker Nodes
- In Kubernetes, the master node is responsible for managing the cluster and orchestrating the deployment of applications. It runs the Kubernetes API server, scheduler, and controller manager. Worker nodes are responsible for running the containerized applications and are managed by the master node. The master node schedules pods to run on worker nodes and monitors their health, ensuring that the desired state of the applications is maintained.

### Components of Kubernetes
- Kubernetes consists of several components, including the API server, scheduler, controller manager, etcd, kubelet, and kube-proxy. The API server is the central component that exposes the Kubernetes API and serves as the entry point for all interactions with the cluster.

- The scheduler is responsible for scheduling pods to run on worker nodes based on resource availability and other constraints. The controller manager is responsible for managing the lifecycle of pods and ensuring that the desired state of the applications is maintained. etcd is a distributed key-value store that Kubernetes uses to store cluster state and configuration data.

- kubelet is an agent that runs on each worker node and is responsible for managing the pods running on that node. 

- kube-proxy is responsible for managing network communication between pods and services in the cluster, ensuring that traffic is properly routed to the appropriate pods. 

- etcd is a distributed key-value store that Kubernetes uses to store cluster state and configuration data. It is a critical component of the Kubernetes control plane, providing a reliable and consistent storage mechanism for cluster information.

- Controller manager is responsible for managing the lifecycle of pods and ensuring that the desired state of the applications is maintained. It monitors the state of the cluster and takes action to ensure that the desired state is achieved, such as creating new pods or deleting existing ones as needed.

- kubectl is a command-line tool for interacting with the Kubernetes API server, allowing you to manage your cluster and applications. It provides a wide range of commands for creating, updating, and deleting resources in your cluster, as well as for viewing the status of your applications and cluster components.