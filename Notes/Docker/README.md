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

### Learning Roadmap

This roadmap is organized in **4 phases** with increasing complexity. Complete each phase sequentially to build a solid intermediate foundation.

---

## Phase 1: Production-Ready Images (Weeks 1-2)

### 1.1 Dockerfile Best Practices
**Goal**: Write production-ready, optimized Dockerfiles

**Topics**:
- Write Dockerfiles using small base images (Alpine, slim, distroless)
- Understand layer caching and instruction ordering for build speed
- Use multi-stage builds to reduce final image size
- Run containers as non-root user for security
- Use `.dockerignore` to exclude unnecessary files
- Order instructions to maximize cache hit rate

**Practice**:
- [Refactor existing Dockerfile to use multi-stage builds](../../src/docker/2.docker-image/README.md)
- Create a Dockerfile with non-root user and compare image sizes

**Resources**:
- [Dockerfile best practices](https://docs.docker.com/build/building/best-practices/)
- [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/)
- [Use the BUILDKIT](https://docs.docker.com/build/buildkit/)

---

### 1.2 Image Optimization and BuildKit
**Goal**: Build faster, smaller, more efficient images

**Topics**:
- Compare base images: Alpine vs Slim vs Distroless vs Full
- Scan and analyze image size layers
- Remove unused build dependencies and clean up caches
- Use Docker BuildKit for faster builds and advanced features
- Use `docker buildx` for multi-platform builds (`linux/amd64`, `linux/arm64`)
- Implement semantic versioning and tag strategy

**Practice**:
- Build same app with Alpine and distroless, compare sizes
- Set up BuildKit and test build speed improvements
- Create multi-platform build for both amd64 and arm64

**Resources**:
- [BuildKit documentation](https://docs.docker.com/build/buildkit/)
- [Multi-platform builds](https://docs.docker.com/build/building/multi-platform/)
- [Build cache optimization](https://docs.docker.com/build/cache/optimize/)
- [Image tagging best practices](https://docs.docker.com/reference/cli/docker/image/tag/)

---

## Phase 2: Advanced Composition & Networking (Weeks 3-4)

### 2.1 Docker Compose Beyond Basics
**Goal**: Manage complex multi-container applications

**Topics**:
- Use multiple Compose files for different environments (dev, test, prod)
- Work with environment variables and `.env` files
- Implement health checks (`healthcheck` directive)
- Control startup order with `depends_on` and wait conditions
- Use named volumes vs bind mounts strategically
- Create isolated networks for service segmentation
- Override services for different deployment scenarios

**Practice**:
- Create dev, test, and prod Compose files for a 3-tier app
- Implement health checks for web and database services
- Set up `.env` file with environment-specific variables
- Use volume backups and restoration

**Resources**:
- [Compose file reference](https://docs.docker.com/reference/compose-file/)
- [Compose documentation](https://docs.docker.com/compose/)
- [Control startup and shutdown order](https://docs.docker.com/compose/how-tos/startup-order/)
- [Networking in Compose](https://docs.docker.com/compose/networking/)

---

### 2.2 Container Networking Deep Dive
**Goal**: Master network types and service communication

**Topics**:
- Understand network drivers: bridge, host, none, overlay, macvlan
- Container DNS and service discovery (hostname resolution)
- Port mapping and exposure strategies
- Debug connectivity issues using `docker exec`, `curl`, `ping`, `ss`, `nslookup`
- Understand when to use isolated networks
- Network policies and access control basics

**Practice**:
- Create custom bridge network and test service discovery
- Debug connectivity between containers
- Map and expose ports safely
- Use host network mode and understand trade-offs

**Resources**:
- [Docker networking overview](https://docs.docker.com/engine/network/)
- [Network drivers](https://docs.docker.com/engine/network/drivers/)
- [Port publishing and mapping](https://docs.docker.com/engine/network/port-publishing/)
- [Service discovery and DNS](https://docs.docker.com/engine/network/drivers/bridge/#embedded-dns-server)

---

## Phase 3: Data Persistence & Security (Weeks 5-6)

### 3.1 Storage and Persistence
**Goal**: Manage data safely across container lifecycle

**Topics**:
- Understand volumes vs bind mounts vs tmpfs mounts
- Use named volumes for databases and stateful apps
- Bind mounts for development workflows
- Back up and restore Docker volumes
- Manage file permissions between host and container users
- Avoid storing state in containers (stateless design)
- Volume driver plugins and advanced storage options

**Practice**:
- Create named volume for PostgreSQL database
- Back up and restore volume data
- Set up bind mount for live code reload in development
- Test permission issues and solutions

**Resources**:
- [Docker volumes guide](https://docs.docker.com/engine/storage/volumes/)
- [Bind mounts](https://docs.docker.com/engine/storage/bind-mounts/)
- [Storage drivers](https://docs.docker.com/engine/storage/drivers/)
- [Volume backup and restore](https://docs.docker.com/engine/storage/volumes/#backup-restore-or-migrate-data-volumes)

---

### 3.2 Container Security Fundamentals
**Goal**: Implement security best practices in containerized applications

**Topics**:
- Run containers with least privilege (minimal permissions)
- Run processes as non-root user (avoid UID 0)
- Use read-only filesystems (`--read-only` flag)
- Manage secrets securely without hardcoding in images
- Scan images for vulnerabilities (Docker Scout, Trivy, Snyk)
- Understand image signing and trusted registries
- Resource limits to prevent DoS (`--memory`, `--cpus`)
- User namespace mapping

**Practice**:
- Create container with non-root user and verify
- Scan an image for vulnerabilities
- Use Docker secrets for sensitive data
- Set resource limits on containers
- Run container with read-only filesystem

**Resources**:
- [Docker security guide](https://docs.docker.com/engine/security/)
- [Rootless mode](https://docs.docker.com/engine/security/rootless/)
- [Docker Scout](https://docs.docker.com/scout/)
- [Running containers with resource constraints](https://docs.docker.com/config/containers/resource_constraints/)
- [Managing sensitive data with secrets](https://docs.docker.com/engine/swarm/secrets/)

---

## Phase 4: Release & Operations (Weeks 7-8)

### 4.1 Registries and Release Workflow
**Goal**: Establish CI/CD and release processes

**Topics**:
- Push/pull images from Docker Hub and private registries
- Image tagging strategy: `latest`, semantic versioning, commit hashes
- Automated release workflow from source to registry
- Create private registries (Docker Registry, Harbor)
- Clean up unused images, containers, and networks safely
- Mirror images and manage registry access

**Practice**:
- Tag and push image to Docker Hub
- Create release workflow with Git tags and Docker tags
- Set up local private registry
- Implement cleanup scripts for unused resources

**Resources**:
- [Docker Hub documentation](https://docs.docker.com/docker-hub/)
- [Docker image tag reference](https://docs.docker.com/reference/cli/docker/image/tag/)
- [Docker Registry deployment](https://docs.docker.com/registry/deploying/)
- [Docker build GitHub Actions](https://docs.docker.com/build/ci/github-actions/)

---

### 4.2 Observability and Debugging
**Goal**: Monitor, log, and debug containerized applications

**Topics**:
- Read and analyze container logs (`docker logs` with filtering)
- Inspect container state (`docker inspect` for detailed info)
- Monitor resource usage and performance (`docker stats`)
- Collect metrics (CPU, memory, I/O, network)
- Centralized logging with ELK stack or alternatives
- Distributed tracing basics
- Debug containerized applications using debugging tools

**Practice**:
- Analyze logs from failing container
- Use `docker inspect` to troubleshoot configuration
- Monitor resource usage under load
- Set up centralized logging

**Resources**:
- [docker logs reference](https://docs.docker.com/reference/cli/docker/container/logs/)
- [docker inspect reference](https://docs.docker.com/reference/cli/docker/inspect/)
- [Runtime metrics](https://docs.docker.com/engine/containers/runmetrics/)
- [View logs for a service](https://docs.docker.com/compose/how-tos/view-compose-logs/)

---

### 4.3 CI/CD with Docker
**Goal**: Automate image building and testing

**Topics**:
- Set up automated image builds on code push
- Test containers before pushing to registry
- Tag images automatically based on Git metadata
- Scan images in CI pipeline
- Implement multi-environment deployments
- Create reusable CI/CD workflows

**Practice**:
- Create GitHub Actions workflow to build and push image
- Add image scanning to CI/CD pipeline
- Implement semantic versioning in automated builds

**Resources**:
- [Docker build GitHub Actions](https://docs.docker.com/build/ci/github-actions/)
- [Test before push workflow](https://docs.docker.com/build/ci/github-actions/test-before-push/)
- [Manage tags and labels](https://docs.docker.com/build/ci/github-actions/manage-tags-labels/)

---

## Progression Checklist

- [ ] **Phase 1**: Can write multi-stage Dockerfiles, optimize images, use BuildKit
- [ ] **Phase 2**: Manage complex Compose files, debug network issues
- [ ] **Phase 3**: Secure containers, manage persistence, scan vulnerabilities
- [ ] **Phase 4**: Automate releases, centralize logging, monitor applications

**Next Step After Intermediate**: [Docker Swarm](../../Notes/Docker/README.md) or **Kubernetes** preparation with container orchestration concepts.
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



## How to use these notes

- Each file contains examples and commands; follow those in an isolated environment (VM, Docker Desktop, or a dedicated machine).
- For runnable examples, see the `src/docker/1.docker-compose` and `src/docker/2.docker-image` folders.
- If you'd like, I can add CI examples, Dockerfile best-practices, or convert these into a single guide.
