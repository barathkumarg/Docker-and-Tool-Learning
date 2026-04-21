
# Docker Images

## What is a Docker Image?
Docker images are lightweight, standalone, and executable software packages that include everything needed to run an application: code, runtime, libraries, environment variables, and configuration files. They provide a consistent and reproducible environment for applications, making it easier to develop, test, and deploy across different platforms.

---

## Why Use Docker Images?
- Consistent environment across platforms
- Simplifies application deployment
- Isolates dependencies and configurations
- Enables easy versioning and rollback

---

## Creating Your Own Docker Image

You can create your own Docker image by writing a `Dockerfile`, which is a text file that contains instructions on how to build the image. The `Dockerfile` specifies the base image, the application code, dependencies, and any necessary configuration. Once you have a `Dockerfile`, you can build the image using the `docker build` command.

### Example Scenario
Suppose you want to run a Flask application. Instead of installing OS packages, dependencies, and the application code on your host machine, you can create a Docker image that contains all these components. This allows you to run the application in a containerized environment without worrying about compatibility issues or conflicts with other applications on the host.

### Example `Dockerfile` for a Flask Application
```Dockerfile
FROM ubuntu

RUN apt-get update \
    && apt-get install -y python3 python3-pip

RUN pip3 install flask flask-mysql

COPY . /opt/source-code

ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run
```

- `CAPS` indicate Dockerfile instructions, `lowercase` are arguments, and `#` is used for comments.

---

## Building a Docker Image
To build a Docker image from a `Dockerfile`, use:

```sh
docker build -t <image_name>:<tag> <path_to_dockerfile>
# -t: Tag the image with a name and optional tag (e.g., myapp:latest)
# <path_to_dockerfile>: The directory containing the Dockerfile (use . for the current directory)
```

---

## Viewing Image Layers
To verify and view each layer of the image and the commands used to create those layers, use:

```sh
docker history <image_name>
# Displays the history of an image, showing each layer and the command used to create it.
```