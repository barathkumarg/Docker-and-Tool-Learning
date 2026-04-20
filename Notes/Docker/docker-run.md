
# Docker Run: Tags, STDIN, and Interactive Modes

## 1. Running Containers with Tags (Versions)

You can run containers with specific versions using image tags. For example, to run two different versions of Redis:

```sh
# Pull a specific version of Redis
docker pull redis:<tag>

# Run containers with different versions and names
docker run -d --name redis-6 redis:6
docker run -d --name redis-7 redis:7
```

Replace `<tag>` with the desired version (e.g., `6`, `7`, `latest`).

---

## 2. Running Containers with STDIN and Interactive Modes

You can run containers in different modes to control how input/output is handled:

### a. Normal Mode (No STDIN)
Runs the container and displays output, but does not accept user input.

```sh
docker run barathkumargn/sample-app
# Output:
# Hello, I am <name to be expected>
```

### b. Interactive Mode (`-i`)
Keeps STDIN open, allowing you to pass input to the container.

```sh
docker run -i barathkumargn/sample-app
# Output:
# Hello, I am barath
```

### c. Interactive Terminal Mode (`-it`)
Combines interactive mode with a pseudo-TTY, enabling prompts and full terminal interaction.

```sh
docker run -it barathkumargn/sample-app
# Output:
# Enter your name: barath
# Hello, I am barath
```


---

## 3. Port Mapping and Modes

Port mapping allows you to expose container ports to the host machine, making services accessible outside the container.

- Use the `-p <host_port>:<container_port>` option to map ports.
- Example: `-p 5000:80` maps port 80 in the container to port 5000 on the host.

```sh
docker run -d -p 5000:80 nginx
# Runs Nginx in detached mode, mapping host port 5000 to container port 80.
```

---

## 4. Volume Mapping (Persisting Data)

By default, data inside a container is lost when the container is removed. To persist data, use volume mapping:

- Use the `-v <host_path>:<container_path>` option to map a directory from the host to the container.
- Example: Persist MySQL data to the host.

```sh
docker run -d -p 3306:3306 -v /my/own/datadir:/var/lib/mysql mysql:latest
# Maps /my/own/datadir on the host to /var/lib/mysql in the container.
```

---

## 5. Inspecting Containers

To view detailed information about a container (such as port mappings, volumes, environment variables, etc.), use:

```sh
docker inspect <container_id>
# Outputs a JSON with all container details.
```

---

## 6. Viewing Container Logs

To see the logs (stdout/stderr) of a running or stopped container:

```sh
docker logs <container_id>
# Shows logs for the specified container.
```

---

## 7. Attaching to Running Containers
To interact with a running container's terminal:

```sh
docker attach <container_id>
# Attaches your terminal to the container's STDIN, STDOUT, and STDERR.
```

## 8. Installation of Jenkins using Docker
To install Jenkins using Docker, you can run the following command:

```sh
docker run -d -p 8080:8080 -p 50000:50000 --name jenkins jenkins/jenkins:lts
# Runs Jenkins in detached mode, mapping host port 8080 to container port 8080 and host port 50000 to container port 50000.
```

Usage of Ports in Jenkins
- Port 8080: This is the default port for Jenkins web interface. You can access Jenkins by navigating to `http://localhost:8080` in your web browser.

- Port 50000: This port is used for Jenkins agents (also known as Jenkins slaves) to communicate with the Jenkins master. If you have Jenkins agents that need to connect to the Jenkins master, they will use this port for communication.

At this pont no volume been mapped, results after stoping the jenkins container, re-triggerring again the jenkins container will result in loss of data, to avoid this we can use volume mapping to persist the data.

```sh
docker run -d -p 8080:8080 -p 50000:50000 --name jenkins -v /root/my-jenkins-data:/var/jenkins_home jenkins/jenkins:lts
# Runs Jenkins in detached mode, mapping host port 8080 to container port 8080 and host port 50000 to container port 50000, with a named volume 'jenkins_home' mapped to '/var/jenkins_home' in the container.
```

**Tips:**
- Use `-i` to keep STDIN open (for scripts or input redirection).
- Use `-it` for interactive prompts and shell access (e.g., bash, sh, or user input).



**Note:**
- Use `-i` for keeping STDIN open (for scripts or input redirection).
- Use `-it` for interactive prompts and shell access (e.g., bash, sh, or user input).

---

