# Compose for Development and Production

## Goal
Practice using Docker Compose in both development and production-style workflows by separating environment-specific settings and commands.

This task is intended for an intermediate-level practice exercise.

## Task Overview

### Main Task
Create a simple Compose-based application setup and learn how to use development overrides and production-oriented configuration.

## Subtasks

### 1. Create a base Compose file
- [ ] Create a simple `docker-compose.yml` file for the application
- [ ] Define the main services needed for the app
- [ ] Keep the configuration readable and beginner-friendly

### 2. Create a development override file
- [ ] Create a development override file such as `docker-compose.override.yml`
- [ ] Add development-specific settings such as ports, volumes, or environment variables
- [ ] Use the override file to make local development easier

### 3. Create a production-oriented compose setup
- [ ] Define a production-style configuration with environment-specific values
- [ ] Use settings suitable for deployment or closer to production behavior
- [ ] Keep the production setup separate from local development settings

### 4. Compare Compose commands for different environments
- [ ] Practice starting services with `docker compose up`
- [ ] Practice using override files for development
- [ ] Compare behavior between development and production-oriented configurations

### 5. Test the setup locally
- [ ] Run the services and confirm they start correctly
- [ ] Check that the application works as expected
- [ ] Observe how the development override changes behavior

### 6. Document the learning points
- [ ] Record the difference between development and production Compose usage
- [ ] Note the commands used to run each setup
- [ ] Summarize the purpose of override files and environment separation

## Working Expected

When completed successfully, you should be able to:
- create a basic Compose file for an application
- use an override file for development-specific changes
- understand how Compose can be adapted for production-style setups
- distinguish between local development and production-oriented Docker workflows

## Notes

- Compose is commonly used for local development first, then adapted for staging or production.
- Override files help keep the base configuration clean while adding local convenience settings.
- Production setups often use stricter settings, different environment variables, and fewer development features.
