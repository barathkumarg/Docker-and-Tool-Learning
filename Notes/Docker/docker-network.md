# Docker Network

## 1. Overview
Docker Network allows containers to communicate with each other and with the outside world. It provides various network drivers to create different types of networks for your containers.

### Bridge Network
- The default network driver. It creates a private internal network on the host where containers can communicate with each other. Containers on the bridge network can access the outside world, but they are isolated from the host and other networks.

**Beginner Example:**
When you run a container without specifying a network, it is connected to the default bridge network. For example:
```docker run -d nginx
```
This container will be connected to the bridge network and can communicate with other containers on the same network.

- Associate the port  with host to the container port to access the application running inside the container from outside. For example:
```docker run -d -p 8080:80 nginx
```
This command maps port 8080 on the host to port 80 in the container, allowing you to access the Nginx web server from your browser at `http://localhost:8080`.

### Host Network
- The host network driver removes network isolation between the container and the host. Containers using the host network share the host's network stack and can access the host's network interfaces directly. This can improve performance but may lead to security risks since the container can access the host's network.  

**Beginner Example:**   
To run a container using the host network:
```docker run -d --network host nginx
```
This command runs the Nginx container using the host's network, allowing it to access the host's network interfaces directly.

### None Network
- The none network driver disables all networking for the container. Containers using this driver cannot communicate with other containers or the outside world. This can be useful for containers that do not require network access.

### User-defined Networks
- Docker allows you to create custom networks using the `docker network create` command. User-defined networks provide better isolation and control over container communication. You can specify the network driver (e.g., bridge, overlay) when creating a user-defined network.

**Beginner Example:**
To create a user-defined bridge network:
```docker network create 
          --driver bridge
          --subnet 182.18.0..0/16
          --gateway <ip range>
          my_bridge_network
        
```
To run a container and connect it to the user-defined network:
```docker run -d --network my_bridge_network nginx
```
This command runs the Nginx container and connects it to the `my_bridge_network`, allowing it to communicate with other containers on the same network.

- Run `docker inspect <container_id>` to see the network settings of a container, including its IP address and network mode.

#### Example 

- How to connect the mysql container to the nginx container using user-defined network:
```docker network create my_network
docker run -d --name mysql --network my_network mysql:latest
docker run -d --name nginx --network my_network nginx:latest
```

In the app to connect - user container name
```mysql.connect(mysql_container_ip, username, password)```