# Registry and Image Sharing

## Goal
Practice building, tagging, pushing, and pulling Docker images so they can be shared across machines or teams.

This task is intended for an intermediate-level practice exercise.

## Task Overview

### Main Task
Create a simple Docker image, push it to a registry, and pull it back to verify that it can be shared and reused.

## Subtasks

### 1. Create a simple application image
- [ ] Create a small app or use a basic example for practice
- [ ] Write a Dockerfile for the app
- [ ] Build the image locally

### 2. Tag the image properly
- [ ] Add a meaningful image tag
- [ ] Use a repository name and version tag
- [ ] Practice tagging with a personal or local registry name

### 3. Push the image to a registry
- [ ] Use Docker Hub or a local registry for practice
- [ ] Authenticate if required
- [ ] Push the image and verify that it is available remotely

### 4. Pull the image from the registry
- [ ] Remove the local image if needed
- [ ] Pull the image again from the registry
- [ ] Confirm that the image can be reused on another machine or environment

### 5. Run the pulled image
- [ ] Start a container from the pulled image
- [ ] Verify that the application works after pulling
- [ ] Confirm that the image behaves the same way as the original local build

### 6. Practice image versioning and reuse
- [ ] Tag the same image with multiple versions
- [ ] Compare the behavior of different tags
- [ ] Understand how tags help with rollout and rollback

### 7. Clean up and document results
- [ ] Remove temporary containers and images if needed
- [ ] Record the push and pull commands used
- [ ] Note the final results and learning points

## Working Expected

When completed successfully, you should be able to:
- build a Docker image locally
- tag it clearly
- push it to a registry
- pull it back and run it successfully
- understand how image sharing works in real-world Docker workflows

## Notes

- A registry is where Docker images are stored and shared.
- Docker Hub is the most common public registry, while private or local registries are common in teams.
- Image tags are important for versioning and deployment tracking.
