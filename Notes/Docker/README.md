# Docker Notes

## Topics covered

- [1. Docker Overview](1.docker-overview.md)
- [2. Docker Basic Commands](2.docker-basic-commands.md)
- [3. Docker Engine](3.docker-engine.md)
- [4. Docker Images](4.docker-images.md)
- [5. Docker Run](5.docker-run.md)
- [6. Docker Network](6.docker-network.md)
- [7. Docker Registry](7.docker-registry.md)
- [8. Docker Compose](8.docker-compose.md)
- [9. Container Orchestration](9.container-orchestration.md)

## Already covered in these notes

- Docker fundamentals, containers vs virtual machines, images, repositories, and DevOps use cases are covered in [Docker Overview](1.docker-overview.md).
- Basic image, container, port, attach/detach, `exec`, pull, stop, remove, and cleanup commands are covered in [Docker Basic Commands](2.docker-basic-commands.md).
- Docker Engine architecture, CLI, REST API, daemon, namespaces, cgroups, layers, copy-on-write, and volumes are covered in [Docker Engine](3.docker-engine.md).
- Docker image creation, Dockerfile basics, image layers, environment variables, `ENTRYPOINT`, `CMD`, and Docker Hub push flow are covered in [Docker Images](4.docker-images.md).
- `docker run`, tags, interactive mode, port mapping, volume mapping, inspect, logs, attach, and Jenkins container setup are covered in [Docker Run](5.docker-run.md).
- Network types, custom bridge networks, inspect, DNS/service discovery, and connect/disconnect commands are covered in [Docker Network](6.docker-network.md).
- Local registry, push/pull workflow, private registry basics, and Docker Hub are covered in [Docker Registry](7.docker-registry.md).
- Compose overview, basic `docker-compose.yml`, common commands, and local multi-container use cases are covered in [Docker Compose](8.docker-compose.md).
- Kubernetes vs Docker Swarm, orchestration concepts, and when to use orchestration are covered in [Container Orchestration](9.container-orchestration.md).
- Runnable practice examples are available in [Docker Compose sample](../../src/docker/1.docker-compose/README.md) and [Docker image sample](../../src/docker/2.docker-image/README.md).

## Official and free learning resources

Use these resources after your local notes. They are official documentation or official project learning pages and are free to read.

| Learning topic | Start from your notes | Official free resources |
| --- | --- | --- |
| Docker fundamentals refresh | [Docker Overview](1.docker-overview.md), [Docker Basic Commands](2.docker-basic-commands.md) | [Docker Get Started](https://docs.docker.com/get-started/), [Docker guides](https://docs.docker.com/guides/) |
| Dockerfile best practices | [Docker Images](4.docker-images.md), [Docker image sample](../../src/docker/2.docker-image/README.md) | [Dockerfile best practices](https://docs.docker.com/build/building/best-practices/), [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/) |
| Image optimization and BuildKit | [Docker Images](4.docker-images.md) | [BuildKit](https://docs.docker.com/build/buildkit/), [Multi-platform builds](https://docs.docker.com/build/building/multi-platform/), [Build cache optimization](https://docs.docker.com/build/cache/optimize/) |
| Docker Compose intermediate usage | [Docker Compose](8.docker-compose.md), [Docker Compose sample](../../src/docker/1.docker-compose/README.md) | [Docker Compose docs](https://docs.docker.com/compose/), [Compose file reference](https://docs.docker.com/reference/compose-file/), [Control startup order](https://docs.docker.com/compose/how-tos/startup-order/) |
| Container networking | [Docker Network](6.docker-network.md) | [Docker networking overview](https://docs.docker.com/engine/network/), [Network drivers](https://docs.docker.com/engine/network/drivers/), [Port publishing and mapping](https://docs.docker.com/engine/network/port-publishing/) |
| Storage and persistence | [Docker Engine](3.docker-engine.md), [Docker Run](5.docker-run.md) | [Docker volumes](https://docs.docker.com/engine/storage/volumes/), [Bind mounts](https://docs.docker.com/engine/storage/bind-mounts/), [Storage drivers](https://docs.docker.com/engine/storage/drivers/) |
| Container security basics | [Docker Engine](3.docker-engine.md), [Docker Images](4.docker-images.md) | [Rootless mode](https://docs.docker.com/engine/security/rootless/), [Docker Scout](https://docs.docker.com/scout/), [Docker security](https://docs.docker.com/engine/security/) |
| Registries and release workflow | [Docker Registry](7.docker-registry.md), [Docker Images](4.docker-images.md) | [Docker Hub docs](https://docs.docker.com/docker-hub/), [Docker image tag reference](https://docs.docker.com/reference/cli/docker/image/tag/), [Docker build GitHub Actions](https://docs.docker.com/build/ci/github-actions/) |
| Observability and debugging | [Docker Run](5.docker-run.md), [Docker Basic Commands](2.docker-basic-commands.md) | [docker logs reference](https://docs.docker.com/reference/cli/docker/container/logs/), [docker inspect reference](https://docs.docker.com/reference/cli/docker/inspect/), [Runtime metrics](https://docs.docker.com/engine/containers/runmetrics/) |
| CI/CD with Docker | [Docker Images](4.docker-images.md), [Docker Registry](7.docker-registry.md) | [Docker build GitHub Actions](https://docs.docker.com/build/ci/github-actions/), [Test before push](https://docs.docker.com/build/ci/github-actions/test-before-push/), [Tags and labels](https://docs.docker.com/build/ci/github-actions/manage-tags-labels/) |
| Docker to Kubernetes preparation | [Container Orchestration](9.container-orchestration.md) | [Kubernetes Pods](https://kubernetes.io/docs/concepts/workloads/pods/), [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/), [Services](https://kubernetes.io/docs/concepts/services-networking/service/), [ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/), [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/) |

## Topics to learn next - Intermediate level

### 1. Dockerfile best practices
- Write production-ready Dockerfiles using small base images.
- Use multi-stage builds to reduce final image size.
- Understand layer caching and how instruction order affects build speed.
- Run containers as a non-root user.
- Use `.dockerignore` to avoid copying unnecessary files into images.

### 2. Image optimization and build tooling
- Compare Alpine, slim, distroless, and full base images.
- Scan image size and remove unused build dependencies.
- Use Docker BuildKit for faster and cleaner builds.
- Learn `docker buildx` for multi-platform images like `linux/amd64` and `linux/arm64`.
- Tag images properly using semantic versions and Git commit hashes.

### 3. Docker Compose beyond basics
- Use multiple Compose files for dev, test, and production-like environments.
- Work with environment variables and `.env` files.
- Add health checks and dependency startup conditions.
- Use named volumes for persistent data.
- Create isolated networks for frontend, backend, database, and monitoring services.

### 4. Container networking
- Understand bridge, host, none, overlay, and macvlan networks.
- Learn container DNS and service discovery.
- Expose ports safely and understand port mapping.
- Debug connectivity using `docker exec`, `curl`, `ping`, `ss`, and logs.
- Know when to use internal-only networks.

### 5. Storage and persistence
- Understand bind mounts vs named volumes.
- Use volumes for databases and application uploads.
- Back up and restore Docker volumes.
- Manage permissions between host users and container users.
- Avoid storing state inside containers.

### 6. Security fundamentals
- Run containers with least privilege.
- Avoid running processes as root.
- Use read-only filesystems where possible.
- Manage secrets without hardcoding them into images.
- Scan images using tools like Docker Scout or Trivy.
- Understand image signing and trusted registries at a high level.

### 7. Registries and release workflow
- Push and pull images from Docker Hub or a private registry.
- Use image tags properly: `latest`, version tags, and commit-based tags.
- Create a basic release workflow from source code to image registry.
- Clean up unused local images, containers, networks, and volumes safely.

### 8. Observability and debugging
- Read container logs using `docker logs`.
- Inspect containers using `docker inspect`.
- Monitor resource usage with `docker stats`.
- Add health checks for web apps, APIs, databases, and queues.
- Debug failed containers using exit codes and temporary shell access.

### 9. CI/CD with Docker
- Build Docker images inside a CI pipeline.
- Run unit tests inside containers.
- Push images to a registry after successful tests.
- Use Docker Compose for integration tests.
- Learn the difference between building images locally and in CI.

### 10. Docker to Kubernetes preparation
- Map Docker concepts to Kubernetes concepts.
- Container -> Pod
- Compose service -> Deployment or StatefulSet
- Compose network -> Kubernetes Service and DNS
- Volume -> PersistentVolume and PersistentVolumeClaim
- Environment variables and secrets -> ConfigMap and Secret

## Suggested Docker project ideas

### Project 1: Containerize a simple web application
- Build a small Node.js, Python, Java, or Go web app.
- Write a Dockerfile using best practices.
- Add `.dockerignore`, non-root user, and health check.
- Run the app with environment variables.
- Goal: become confident with image building and running containers.

### Project 2: Full-stack app with Docker Compose
- Create a frontend, backend API, and PostgreSQL or MySQL database.
- Run all services using Docker Compose.
- Add named volumes for database persistence.
- Add separate networks for public and private services.
- Goal: understand real-world multi-container application setup.

### Project 3: Local development environment
- Build a reusable local dev setup for an app.
- Add hot reload using bind mounts.
- Add a database, cache like Redis, and admin tool like Adminer or pgAdmin.
- Use `.env` files for local configuration.
- Goal: learn how teams use Docker for daily development.

### Project 4: CI pipeline for Docker image release
- Create a GitHub Actions or Jenkins pipeline.
- Run tests first.
- Build the Docker image only if tests pass.
- Tag the image with version and commit SHA.
- Push the image to Docker Hub or a private registry.
- Goal: connect Docker with DevOps automation.

### Project 5: Secure and optimized production image
- Start with a working but large Docker image.
- Convert it to a multi-stage build.
- Run the application as a non-root user.
- Scan the image for vulnerabilities.
- Compare before and after image size.
- Goal: practice production-grade image hardening.

### Project 6: Monitoring stack using Docker Compose
- Run Prometheus and Grafana with Docker Compose.
- Add a sample app that exposes metrics.
- Create a Grafana dashboard for CPU, memory, and request count.
- Add health checks for each service.
- Goal: understand observability for containerized systems.

### Project 7: Reverse proxy and HTTPS-style local setup
- Run multiple apps behind Nginx or Traefik.
- Route traffic by hostname or path.
- Add local certificates or simulate HTTPS locally.
- Keep backend services private inside Docker networks.
- Goal: learn service routing and production-like networking.

### Project 8: Docker Compose integration testing lab
- Create an API with a test database.
- Use Compose to start dependencies before tests.
- Run tests inside a temporary test container.
- Clean up containers and volumes after the test run.
- Goal: learn how Docker improves repeatable testing.

## Intermediate Docker learning checklist

- [ ] I can write a clean Dockerfile without copying unnecessary files.
- [ ] I can reduce image size using multi-stage builds.
- [ ] I can run a multi-service app with Docker Compose.
- [ ] I can debug logs, networking, volumes, and failed containers.
- [ ] I can persist and back up database data using volumes.
- [ ] I can build and push images to a registry.
- [ ] I can add health checks and environment-specific Compose files.
- [ ] I can scan images and avoid common security mistakes.
- [ ] I can build Docker images in a CI/CD pipeline.
- [ ] I can explain how Docker concepts map to Kubernetes basics.

## How to use these notes

- Each file contains examples and commands; follow those in an isolated environment (VM, Docker Desktop, or a dedicated machine).
- For runnable examples, see the `src/docker/1.docker-compose` and `src/docker/2.docker-image` folders.
- If you'd like, I can add CI examples, Dockerfile best-practices, or convert these into a single guide.
