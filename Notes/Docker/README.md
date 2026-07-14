# Docker Notes

## Topics covered

- [1. Docker Overview](1.docker-overview.md)
- [2. Docker Basic Commands](2.docker-basic-commands.md)
- [3. Docker Engine](3.docker-engine.md)
- [4. Docker Images](4.docker-images.md)
- [5. Docker Run](5.docker-run.md)
- [6. Docker Network & Volumes](6.docker-network&volumes.md)
- [7. Docker Registry](7.docker-registry.md)
- [8. Docker Compose](8.docker-compose.md)
- [9. Container Orchestration](9.container-orchestration.md)
- [10. Docker Health Checks and Troubleshooting](10.docker-healthchecks-and-troubleshooting.md)
- [11. Docker Security Basics](11.docker-security-basics.md)
- [12. Docker Image Optimization](12.docker-image-optimization.md)
- [13. Docker Registry Workflow](13.docker-registry-workflow.md)
- [14. Docker Compose for Development and Production](14.docker-compose-dev-prod.md)
- [15. Docker Swarm, CI/CD, and Image Scanning](15.docker-swarm-and-ci-cd.md)

## Already covered in these notes

- Docker fundamentals, containers vs virtual machines, images, repositories, and DevOps use cases are covered in [Docker Overview](1.docker-overview.md).
- Basic image, container, port, attach/detach, `exec`, pull, stop, remove, and cleanup commands are covered in [Docker Basic Commands](2.docker-basic-commands.md).
- Docker Engine architecture, CLI, REST API, daemon, namespaces, cgroups, layers, copy-on-write, and volumes are covered in [Docker Engine](3.docker-engine.md).
- Docker image creation, Dockerfile basics, image layers, environment variables, `ENTRYPOINT`, `CMD`, and Docker Hub push flow are covered in [Docker Images](4.docker-images.md).
- `docker run`, tags, interactive mode, port mapping, volume mapping, inspect, logs, attach, and Jenkins container setup are covered in [Docker Run](5.docker-run.md).
- Network types, custom bridge networks, inspect, DNS/service discovery, and connect/disconnect commands are covered in [Docker Network & Volumes](6.docker-network&volumes.md).
- Local registry, push/pull workflow, private registry basics, and Docker Hub are covered in [Docker Registry](7.docker-registry.md).
- Compose overview, basic `docker-compose.yml`, common commands, and local multi-container use cases are covered in [Docker Compose](8.docker-compose.md).
- Kubernetes vs Docker Swarm, orchestration concepts, and when to use orchestration are covered in [Container Orchestration](9.container-orchestration.md).
- Runnable practice examples are available in [Docker Compose sample](../../src/docker/1.docker-compose/README.md) and [Docker image sample](../../src/docker/2.docker-image/README.md).

## Intermediate concepts to learn next
These topics are now part of the planned practice path for the Docker exercises:

- Health checks and troubleshooting with `docker compose ps`, `docker logs`, and `docker inspect` are covered in [Docker Health Checks and Troubleshooting](10.docker-healthchecks-and-troubleshooting.md).
- Container security basics such as running as a non-root user and using a read-only filesystem are covered in [Docker Security Basics](11.docker-security-basics.md).
- Image optimization with multi-stage builds and smaller base images are covered in [Docker Image Optimization](12.docker-image-optimization.md).
- Registry workflow including tagging, pushing, and pulling images are covered in [Docker Registry Workflow](13.docker-registry-workflow.md).
- Development versus production Compose patterns using override files and environment files are covered in [Docker Compose for Development and Production](14.docker-compose-dev-prod.md).
- Docker Swarm basics, `docker stack`, CI/CD pipelines using Docker images, and image scanning with vulnerability checks are covered in [Docker Swarm, CI/CD, and Image Scanning](15.docker-swarm-and-ci-cd.md).

## Practice roadmap for intermediate Docker
To continue beyond the current notes, use the practice roadmap in [src/docker/README.md](../../src/docker/README.md). It is designed for learners who want to move from beginner Docker knowledge to an intermediate level by practicing Compose, image optimization, volumes, networking, troubleshooting, and registry workflows.

## Practice README format
Use the same task-first structure for practice notes:

- [ ] Title of the task

```text
I will add this here once I practise it.
```

This format is used in practice folders such as [src/docker/4.networking/README.md](../../src/docker/4.networking/README.md).

## Official and free learning resources

Use these resources after your local notes. They are official documentation or official project learning pages and are free to read.

| Learning topic | Start from your notes | Official free resources |
| --- | --- | --- |
| Docker fundamentals refresh | [Docker Overview](1.docker-overview.md), [Docker Basic Commands](2.docker-basic-commands.md) | [Docker Get Started](https://docs.docker.com/get-started/), [Docker guides](https://docs.docker.com/guides/) |
| Dockerfile best practices | [Docker Images](4.docker-images.md), [Docker image sample](../../src/docker/2.docker-image/README.md) | [Dockerfile best practices](https://docs.docker.com/build/building/best-practices/), [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/) |
| Image optimization and BuildKit | [Docker Images](4.docker-images.md) | [BuildKit](https://docs.docker.com/build/buildkit/), [Multi-platform builds](https://docs.docker.com/build/building/multi-platform/), [Build cache optimization](https://docs.docker.com/build/cache/optimize/) |
| Docker Compose intermediate usage | [Docker Compose](8.docker-compose.md), [Docker Compose sample](../../src/docker/1.docker-compose/README.md) | [Docker Compose docs](https://docs.docker.com/compose/), [Compose file reference](https://docs.docker.com/reference/compose-file/), [Control startup order](https://docs.docker.com/compose/how-tos/startup-order/) |
| Container networking | [Docker Network & Volumes](6.docker-network&volumes.md) | [Docker networking overview](https://docs.docker.com/engine/network/), [Network drivers](https://docs.docker.com/engine/network/drivers/), [Port publishing and mapping](https://docs.docker.com/engine/network/port-publishing/) |
| Storage and persistence | [Docker Engine](3.docker-engine.md), [Docker Run](5.docker-run.md) | [Docker volumes](https://docs.docker.com/engine/storage/volumes/), [Bind mounts](https://docs.docker.com/engine/storage/bind-mounts/), [Storage drivers](https://docs.docker.com/engine/storage/drivers/) |
| Container security basics | [Docker Engine](3.docker-engine.md), [Docker Images](4.docker-images.md) | [Rootless mode](https://docs.docker.com/engine/security/rootless/), [Docker Scout](https://docs.docker.com/scout/), [Docker security](https://docs.docker.com/engine/security/) |
| Registries and release workflow | [Docker Registry](7.docker-registry.md), [Docker Images](4.docker-images.md) | [Docker Hub docs](https://docs.docker.com/docker-hub/), [Docker image tag reference](https://docs.docker.com/reference/cli/docker/image/tag/), [Docker build GitHub Actions](https://docs.docker.com/build/ci/github-actions/) |
| Observability and debugging | [Docker Run](5.docker-run.md), [Docker Basic Commands](2.docker-basic-commands.md) | [docker logs reference](https://docs.docker.com/reference/cli/docker/container/logs/), [docker inspect reference](https://docs.docker.com/reference/cli/docker/inspect/), [Runtime metrics](https://docs.docker.com/engine/containers/runmetrics/) |
| CI/CD with Docker | [Docker Images](4.docker-images.md), [Docker Registry](7.docker-registry.md) | [Docker build GitHub Actions](https://docs.docker.com/build/ci/github-actions/), [Test before push](https://docs.docker.com/build/ci/github-actions/test-before-push/), [Tags and labels](https://docs.docker.com/build/ci/github-actions/manage-tags-labels/) |
| Docker to Kubernetes preparation | [Container Orchestration](9.container-orchestration.md) | [Kubernetes Pods](https://kubernetes.io/docs/concepts/workloads/pods/), [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/), [Services](https://kubernetes.io/docs/concepts/services-networking/service/), [ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/), [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/) |

