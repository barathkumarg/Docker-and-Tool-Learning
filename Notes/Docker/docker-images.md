
# Docker Images

## Overview

### What is a Docker Image?
Docker images are lightweight, standalone, and executable software packages that include everything needed to run an application: code, runtime, libraries, environment variables, and configuration files. They provide a consistent and reproducible environment for applications, making it easier to develop, test, and deploy across different platforms.

### Why Use Docker Images?
- Consistent environment across platforms
- Simplifies application deployment
- Isolates dependencies and configurations
- Enables easy versioning and rollback

## Creating Docker Images

### Writing a Dockerfile
You can create your own Docker image by writing a `Dockerfile`, which is a text file that contains instructions on how to build the image. The `Dockerfile` specifies the base image, the application code, dependencies, and any necessary configuration. Once you have a `Dockerfile`, you can build the image using the `docker build` command.

#### Example Scenario
Suppose you want to run a Flask application. Instead of installing OS packages, dependencies, and the application code on your host machine, you can create a Docker image that contains all these components. This allows you to run the application in a containerized environment without worrying about compatibility issues or conflicts with other applications on the host.

#### Example `Dockerfile` for a Flask Application
```Dockerfile
FROM ubuntu

RUN apt-get update \
    && apt-get install -y python3 python3-pip

RUN pip3 install flask flask-mysql

COPY . /opt/source-code

ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run
```

- `CAPS` indicate Dockerfile instructions, `lowercase` are arguments, and `#` is used for comments.

### Building a Docker Image
To build a Docker image from a `Dockerfile`, use:

```sh
docker build -t <image_name>:<tag> <path_to_dockerfile>
# -t: Tag the image with a name and optional tag (e.g., myapp:latest)
# <path_to_dockerfile>: The directory containing the Dockerfile (use . for the current directory)
```

## Managing Docker Images

### Viewing Image Layers
To verify and view each layer of the image and the commands used to create those layers, use:

```sh
docker history <image_name>
# Displays the history of an image, showing each layer and the command used to create it.
```

### Running Containers from Images
After building the image, you can run a container from it using:

```sh
docker run -d -p <host_port>:<container_port> <image_name>:<tag>
# -d: Run the container in detached mode
# -p: Map a port on the host to a port in the container (e.g., 5000:5000)
``` 

### Push the docker image to Docker Hub
To share your Docker image with others, you can push it to a Docker registry like Docker Hub:  

Default organization: `dockerhub_username` (you need to create an account on Docker Hub and log in using `docker login`)

```sh
docker tag <image_name>:<tag> <dockerhub_username>/<repository_name>:<tag>
docker push <dockerhub_username>/<repository_name>:<tag>
``` 


## Environment Variables

Sometimes you may need to set environment variables in the container. This can be done using the `-e` flag when running a container:

```sh
docker run -d -p 5000:5000 -e ENV_VAR_NAME=value <image_name>:<tag>
# -e: Set environment variables in the container (e.g., ENV_VAR_NAME=value)
```

### Inspect Container Environment Variables
To view the environment variables set in a running container, use:

```sh
docker inspect <container_id>
```

- View the "Env" section in the output to see all environment variables set in the container.

## ENTRYPOINT vs CMD

- `ENTRYPOINT` sets the main command to run when the container starts. It is always executed.
- `CMD` provides default arguments to the `ENTRYPOINT`, or if `ENTRYPOINT` is not set, it sets the default command.
- If both are present, `CMD` supplies arguments to `ENTRYPOINT`.

**Example:**
```Dockerfile
FROM ubuntu
RUN apt-get update \
    && apt-get install -y python3 python3-pip
RUN pip3 install flask flask-mysql
COPY . /opt/source-code
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
CMD ["--port=5000"]
```
In this example, the container will run `flask run --host=0.0.0.0 --port=5000` by default. If you want to override the port, you can do so when running the container:

```sh
docker run -d -p 5001:5000 <image_name>:<tag> --port=5001
# This will run: flask run --host=0.0.0.0 --port=5001
```

- When the entrypoint to be overridden, use `--entrypoint` flag:

```sh
docker run -d -p 5000:5000 --entrypoint "/bin/bash" <image_name>:<tag>
# This will override the ENTRYPOINT and start a bash shell instead of running the Flask application.
```