

# Docker Engine

## 1. Overview

Docker Engine is the core software that enables containerization on a host system. It lets you run applications in isolated environments called containers. Think of containers as lightweight, portable boxes that package your app and everything it needs to run.

**Beginner Example:**

If you want to run a simple web server in a container, you can use:

```
docker run -d -p 8080:80 nginx
```

This command downloads the Nginx web server image (if not already present), runs it in the background (`-d`), and maps port 8080 on your computer to port 80 in the container.


## 2. Components

### 2.1 Docker CLI
- The Docker CLI is a command-line tool for managing containers, images, networks, and volumes.

**Beginner Example:**

To list all running containers:
```
docker ps
```
To stop a container:
```
docker stop <container_id>
```

### 2.2 REST API
- The Docker REST API provides HTTP endpoints for programmatic interaction and automation. Most beginners use the CLI, but tools and scripts can use the API to control Docker.

**Beginner Note:**
You usually don't need to use the REST API directly unless you're building automation tools.

### 2.3 Docker Daemon
- The Docker Daemon is a background process that manages containers, images, networks, and volumes. It listens for Docker API requests and manages the lifecycle of containers and images.

**Beginner Note:**
You don't interact with the daemon directly. The CLI and API talk to the daemon for you.


## 3. Containerization Concepts

### 3.1 Namespaces
- Types: Network, IPC, Mount, PID, Unix Timesharing
- **PID Namespace:** Each container has its own PID namespace, isolating processes for security and resource management. PIDs are unique per container, preventing conflicts.

**Beginner Explanation:**
Namespaces are like invisible walls that keep containers separate from each other and from your computer. For example, a process running in one container can't see or affect processes in another container.

### 3.2 cgroups
- Control groups (cgroups) are a Linux kernel feature for allocating and managing system resources (CPU, memory, disk I/O). Docker uses cgroups to limit container resource usage.

**Beginner Example:**
To limit a container to 256MB of memory:
```
docker run -m 256m nginx
```
This ensures the container can't use more than 256MB of RAM.


## 4. Storage in Docker

### 4.1 File System
- Default storage location: `/var/lib/docker` (contains aufs, containers, images, etc.)

**Beginner Note:**
You usually don't need to access this folder directly. Docker manages it for you.

### 4.2 Layered Architecture
- Docker images and containers are built in layers. Each layer represents changes to the file system. Layers enable efficient storage, sharing, and updates, as multiple images and containers can share underlying layers.

**Beginner Explanation:**
If you update your app and create a new image, Docker only saves the changes as a new layer. This saves space and makes sharing faster.

### 4.3 Copy-on-Write (COW)
- Copy-on-write (COW) optimizes storage and performance. New images or containers share base layers; changes create new layers containing only the differences, reducing duplication.

**Beginner Example:**
If you run a container and create a new file inside it, only that file is stored in a new layer. The rest of the files are shared from the image.

### 4.4 Volumes
- Volumes persist data outside the container’s file system, allowing data to survive container removal. Volumes are managed via the Docker CLI or API, stored at `/var/lib/docker/volumes`, and can be shared between containers.

**Beginner Example:**
To run a MySQL database and keep its data even if the container is deleted:
```
docker run -v mysql-data:/var/lib/mysql mysql
```
Or using the new syntax:
```
docker run --mount source=mysql-data,target=/var/lib/mysql mysql
```
Now, your database data is safe in the `mysql-data` volume, even if you remove the container.

**Beginner Note:**
Volumes are the best way to store important data with Docker. Avoid saving important files only inside the container.

Storage drivers (e.g., `aufs`, `overlay2`, `btrfs`, `zfs`, `devicemapper`) manage the underlying file system. Each has pros and cons, affecting performance and functionality. As a beginner, you can use the default driver Docker selects for your system.