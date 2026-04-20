
# Docker Basic Commands

## Table of Contents
1. [Images](#images)
2. [Containers](#containers)
3. [Executing Commands in Containers](#executing-commands-in-containers)
4. [Ports and Modes](#ports-and-modes)
5. [Image vs Container](#image-vs-container)


---

## 1. Images

### List Images
```
docker images
```
Lists all Docker images available locally.

### Pull an Image
```
docker pull <image_name>
```
Downloads an image from Docker Hub (e.g., `docker pull nginx`).

### Remove an Image
```
docker rmi <image_id|image_name>
```
Removes a Docker image. Ensure no containers are using the image.

---

## 2. Containers

### Run a Container
```
docker run -d -p 80:80 nginx
```
Runs an Nginx container in detached mode, mapping port 80 of the container to port 80 on the host.

### List Running Containers
```
docker ps
```
Shows all currently running containers.

### List All Containers (including stopped)
```
docker ps -a
```
Shows all containers, including stopped ones.

### Stop a Running Container
```
docker stop <container_id>
```
Stops a running container. Find `<container_id>` using `docker ps`.

### Remove a Container
```
docker rm <container_id>
```
Removes a stopped container from your system.

### To remove all the containers
```docker rm $(docker ps -a -q)
```
Removes all containers from your system. Use with caution, as this will delete all containers, including those that are running.

---

## 3. Executing Commands in Containers

### Execute a Command in a Running Container
```
docker exec -it <container_id> bash
```
Starts an interactive bash shell inside the running container. The `-it` flags enable interactive mode and allocate a pseudo-TTY.

---

### Execute the command without opening a shell
```
docker exec <container_id> <command>
```
Executes a specific command inside the running container without opening an interactive shell (e.g., `docker exec <container_id> ls /app`).

## 4. Ports and Modes

### Run in Detached Mode
```
docker run -d <image_name>
```
Runs the container in the background (detached).

### Run in Attached Mode
```
docker run <image_name>
```
Runs the container in the foreground (attached). Press `Ctrl+C` to stop.

### Port Mapping
```
docker run -p <host_port>:<container_port> <image_name>
```
Maps a port from the host to the container (e.g., `-p 8080:80`).

---

## 5. Image vs Container

- **Image:** A read-only template with instructions for creating a container. Includes application code, runtime, libraries, and dependencies.
- **Container:** A runnable instance of an image. Lightweight, standalone, and executable. Can be started, stopped, moved, and deleted. Runs the application process.

---

## List running containers
```
docker ps
```
This command lists all the currently running containers on your system.

Stop the Running container
```
docker stop <container_id>
```
This command stops a running container. Replace `<container_id>` with the actual ID of the container you want to stop, which you can find using `docker ps`.

## Remove a container
```
docker rm <container_id>
```
This command removes a container from your system. You must stop the container before you can remove it

## List images
```
docker images
```
This command lists all the Docker images that are currently available on your system.

## Remove images
```
docker rmi <image_id/name>
```
This command removes a Docker image from your system. Replace `<image_id/name>` with the actual ID or name of the image you want to remove, ensure that no containers are using the image before you can remove it.

## Docker pull
```
docker pull nginx
```
This command pulls the latest Nginx image from Docker Hub to your local machine, making it available for you to run containers based on that image.



## Note: Image and Container difference
- An image is a read-only template that contains the instructions for creating a container. It includes the application code, runtime, libraries, and dependencies.

- A container is a runnable instance of an image. It is a lightweight, standalone, and executable package that includes everything needed to run the application. Containers can be started, stopped, moved, and deleted. Container can be terminated once the process running inside it is completed or stopped.

## Docker ps
```
docker ps
```
This command lists all the currently running containers on your system. It provides information such as container ID, image name, command, creation time, status, ports, and names of the running containers.

## Docker exec
```
docker exec -it <container_id> bash
```
This command allows you to execute a command inside a running container. The `-it` flags enable interactive mode and allocate a pseudo-TTY, allowing you to interact with the container's shell. Replace `<container_id>` with the actual ID of the container you want to access. This command will open a bash shell inside the specified container, allowing you to run commands and interact with.

## Run - attach and detach 
- `docker run -d` runs the container in detached mode (in the background).

- `docker run` without `-d` runs the container in attached 
mode (foreground), allowing you to see the output and interact with it directly. You can stop the container by pressing `

## Docker run sample program 
 - We will pull the debian updated image will name it, run and bash into the bash shell of the container.
 - Stop the container
 - Remove the container and image
```
docker pull debian:latest
docker run -it --name my-debian debian:latest bash
# run it a detach mode
docker run -d --name my-debian debian:latest tail -f /dev/null

docker stop my-debian
docker rm my-debian
docker rmi debian:latest 
```
    


