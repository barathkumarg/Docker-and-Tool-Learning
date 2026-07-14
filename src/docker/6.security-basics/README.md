# Security Basics

## Goal
Practice basic Docker security concepts by running a container in a safer way and reducing its attack surface.

This task is intended for an intermediate-level practice exercise.

## Task Overview

### Main Task
Create a simple containerized app and apply common security practices such as non-root execution, read-only filesystems, and minimal image contents.

## Subtasks

### 1. Create a simple containerized application
- [ ] Create a small app or use a basic image for practice
- [ ] Make sure the app runs successfully before applying security changes
- [ ] Keep the setup minimal and easy to debug

### 2. Run the container as a non-root user
- [ ] Add a non-root user in the Dockerfile
- [ ] Switch to that user with `USER`
- [ ] Run the container and confirm it does not run as root

### 3. Use a read-only filesystem
- [ ] Start the container with a read-only root filesystem
- [ ] Avoid writing to the container filesystem unless required
- [ ] Test whether the app still runs as expected

### 4. Drop unnecessary Linux capabilities
- [ ] Run the container with reduced capabilities
- [ ] Use options such as `--cap-drop ALL` where appropriate
- [ ] Understand the difference between a normal container and a hardened one

### 5. Minimize image contents
- [ ] Remove unnecessary packages and files from the image
- [ ] Use a smaller base image when possible
- [ ] Keep only what the app really needs

### 6. Inspect the running container
- [ ] Use `docker inspect` to review security-related settings
- [ ] Check the user, capabilities, and filesystem options
- [ ] Compare the container before and after hardening

### 7. Document the security improvements
- [ ] Note what changed in the Dockerfile or run command
- [ ] Record why each change improves security
- [ ] Summarize the trade-offs of each hardening step

## Working Expected

When completed successfully, you should be able to:
- run a container as a non-root user
- start the container with a read-only filesystem
- reduce unnecessary privileges and image size
- understand how simple security hardening improves container safety

## Notes

- Security in Docker is about reducing privileges and minimizing the attack surface.
- Some applications need writable directories, so read-only mode should be used carefully.
- Start with small security improvements before applying more advanced changes.
