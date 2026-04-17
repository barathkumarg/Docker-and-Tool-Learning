# Basic commands

## Docker run 
```
docker run -d -p 80:80 nginx
```
This command runs an Nginx web server in a container and maps it to your machine's port `80`. The `-d` flag runs the container in detached mode (in the background), and `-p 80:80` maps port 80 of the container to port 80 on the host machine.

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


