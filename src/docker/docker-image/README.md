# To build a docker image of flask app and push to the docker hub

## 1. Writing a Dockerfile
create a `Dockerfile` with the following content:

```Dockerfile
FROM ubuntu
RUN apt-get update \
    && apt-get install -y python3 python3-pip
RUN pip3 install --no-cache-dir flask flask-mysql --break-system-packages
COPY . /opt/source-code
ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run --host=0.0.0
```

## 2. Building the Docker Image
Run the following command in the terminal to build the Docker image:    

```sh
docker build -t myflaskapp:latest .
# -t: Tag the image with a name and optional tag (e.g., myflaskapp:latest)
# .: The directory containing the Dockerfile (use . for the current directory)
```
## 3. Running the Docker Container
After building the image, you can run a container from it using:
```sh
docker run -d -p 5000:5000 myflaskapp:latest
# -d: Run the container in detached mode
# -p: Map a port on the host to a port in the container (e.g., 5000:5000)
```

## 4. Push  the docker image to Docker Hub
To share your Docker image with others, you can push it to a Docker registry like Docker Hub:
Default organization: `dockerhub_username` (you need to create an account on Docker Hub and log in using `docker login`)

```sh
docker tag myflaskapp:latest dockerhub_username/myflaskapp:latest
docker push dockerhub_username/myflaskapp:latest
```