# Final Docker Project Task

## Goal
Build a production-style Docker project that brings together the major concepts you have practiced so far.

This final task should combine:
- multi-container Compose setup
- networking between services
- health checks and troubleshooting
- security hardening
- image optimization
- registry workflow
- Docker Swarm basics or Compose production patterns
- CI/CD-style image build and push flow
- basic image scanning

## Main Task
Create a small but realistic application stack such as:
- a Python Flask or Node.js API
- a Redis cache
- a PostgreSQL or MySQL database
- optional Nginx reverse proxy

The project should be containerized, run with Docker Compose, and be structured in a way that could be extended to a production-like environment.

## Subtasks

### 1. Create the application structure
- [ ] Create a project folder for the final app
- [ ] Add application code for the web service
- [ ] Prepare a simple database and cache dependency

### 2. Create Dockerfiles for the services
- [ ] Write a Dockerfile for the web app
- [ ] Optimize the image using a multi-stage build if possible
- [ ] Use a smaller base image where appropriate

### 3. Create a Compose setup
- [ ] Create a `docker-compose.yml` file
- [ ] Define the web app, database, and cache services
- [ ] Use networks so the services can communicate by service name

### 4. Add development and production Compose patterns
- [ ] Create a base Compose file for shared settings
- [ ] Add an override file for local development
- [ ] Prepare a production-oriented configuration or environment-based setup

### 5. Add health checks and troubleshooting setup
- [ ] Add health checks to the main service
- [ ] Practice checking status with `docker compose ps`
- [ ] Use `docker logs` and `docker inspect` to troubleshoot issues

### 6. Apply basic security practices
- [ ] Run the app as a non-root user
- [ ] Use a read-only filesystem where appropriate
- [ ] Reduce unnecessary image contents

### 7. Build, tag, and push the image
- [ ] Build the image locally
- [ ] Tag it with a meaningful version
- [ ] Push it to a registry if you have access

### 8. Add CI/CD-style workflow concepts
- [ ] Document how the image would be built in CI
- [ ] Describe how tests and registry push would happen automatically
- [ ] Note the steps for deployment after image validation

### 9. Add image scanning and vulnerability checks
- [ ] Scan the built image for known vulnerabilities
- [ ] Review the results and note any follow-up actions
- [ ] Document how scanning fits into a secure release process

### 10. Explore Swarm or production deployment concepts
- [ ] Learn the basics of Docker Swarm and `docker stack`
- [ ] Compare Compose and Swarm for deployment usage
- [ ] Note how the project could be scaled or deployed further

## Working Expected

When completed successfully, you should be able to:
- run the app stack locally using Docker Compose
- see the services communicate with each other over a Docker network
- understand how health checks and troubleshooting work in practice
- explain how security, image optimization, and registry workflows improve delivery
- describe how the project could be promoted from development to a production-style environment

## Notes

This task is meant to be a capstone exercise. It should help you connect the beginner, intermediate, and advanced Docker concepts into one real-world workflow.
