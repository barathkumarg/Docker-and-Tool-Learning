# Docker Registry

## 1. Overview
- Where is the imgae pull from? Docker registry is a service that stores and distributes Docker images. It allows you to share your images with others and pull images created by the community. The most popular public registry is Docker Hub, but you can also set up private registries for your organization.

- `image: <library>/<image_name>:<tag>`: This is the format for specifying an image in a Dockerfile or when running a container. The library is the namespace (e.g., `library` for official images), the image name is the name of the image (e.g., `nginx`), and the tag specifies the version (e.g., `latest`).

## 2. Docker Hub
- Docker Hub (docker.io - default registry) is the default public registry for Docker images. It hosts a vast collection of images, including official images maintained by Docker and community-contributed images. You can search for images on Docker Hub and pull them to your local machine using the `docker pull` command.

- Other registries include:
  - Amazon Elastic Container Registry (ECR)
  - Google Container Registry (GCR)
  - Azure Container Registry (ACR)
  - GitHub Container Registry (GHCR)


## Private Registries
- You can set up your own private registry to store and manage your Docker images. This is useful for organizations that want to keep their images private or have specific requirements for image storage and distribution.

### Steps

 - Login the private registry
```
docker login private-registry.io`
```

- Run the application
```
docker run -d -p 8080:80 private-registry.io/myapp:latest
``` 

## Deploy a private registry using Docker
- You can deploy a private registry using the official `registry` image from Docker Hub. This allows you to have your own registry for storing and distributing images within your organization.

### Steps   
1. Run the registry container:
```docker run -d -p 5000:5000 --name registry registry:2
```
This command runs the registry container in detached mode, mapping port 5000 on the host to port 5000 in the container.     

2. Tag your image to push to the registry:
```docker tag myapp:latest localhost:5000/myapp:latest
```
This command tags your local image (`myapp:latest`) with the registry's address (`localhost:5000`) and the image name (`myapp:latest`).

3. Push the image to the registry:
```docker push localhost:5000/myapp:latest
```
This command pushes your tagged image to the private registry running on your local machine.

4. Pull the image from the registry:
```docker pull localhost:5000/myapp:latest
```
This command pulls the image from your private registry to your local machine, allowing you to run it or share it with others in your organization.

5. Run the application from the registry:
```docker run -d -p 8080:80 localhost:5000/myapp:latest
```
This command runs the application from your private registry, mapping port 8080 on the host to port 80 in the container, allowing you to access the application from your browser at `http://localhost:8080`.