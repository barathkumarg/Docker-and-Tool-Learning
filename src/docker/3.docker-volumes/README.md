# Docker Volumes Practice

## Status
- [ ] Not started

## Tasks
### 1. Create a named volume
- [ ] I will add this here once I practise it.

```text
I will add this here once I practise it.
```

### 2. Mount the volume in two containers
- [ ] I will add this here once I practise it.

```text
I will add this here once I practise it.
```

### 3. Verify persistence
- [ ] I will add this here once I practise it.

```text
I will add this here once I practise it.
```

### 4. Practice bind mounts
- [ ] I will add this here once I practise it.

```text
I will add this here once I practise it.
```


---

## Step-by-Step: Share a Volume Between 2 Containers

### Step 1 — Create the named volume
```sh
docker volume create volume_ubuntu
```
This creates a Docker-managed volume stored at `/var/lib/docker/volumes/volume_ubuntu/_data` on the host.

---

### Step 2 — Run Container 1 and write a file to the volume
```sh
docker run -it -v volume_ubuntu:/folder1 ubuntu:latest
```

Inside the container:
```sh
# Volume is mounted at /folder1
ls
# bin  boot  dev  etc  folder1  home ...

cd folder1

# Write a file into the shared volume
echo "Hello from container 1" > container1.txt

exit
```

> **What happened:** The file `container1.txt` was written into the volume, not into the container's own filesystem. When the container exits, the file stays alive inside the volume.

---

### Step 3 — Run Container 2 and access the same volume
```sh
docker run -it -v volume_ubuntu:/folder2 ubuntu:latest
```

> Note: The volume `volume_ubuntu` is the same, but you can mount it at any path inside the container — here it's `/folder2`.

Inside the container:
```sh
cd folder2

# File written by Container 1 is already here
ls
# container1.txt

# Container 2 adds its own file
echo "Hello from container 2" > container2.txt

ls
# container1.txt  container2.txt
```

> **What happened:** Container 2 can see `container1.txt` even though it was written by a completely different container. Both containers share the same underlying storage via the volume.

---

## How It Works Internally

```
 ┌─────────────────┐        ┌─────────────────┐
 │   Container 1   │        │   Container 2   │
 │  /folder1       │        │  /folder2       │
 └────────┬────────┘        └────────┬────────┘
          │                          │
          └──────────┬───────────────┘
                     │
          ┌──────────▼───────────┐
          │   Docker Volume      │
          │   volume_ubuntu      │
          │                      │
          │  container1.txt ✅   │
          │  container2.txt ✅   │
          └──────────────────────┘
```

- The volume lives **outside both containers**.
- Both containers mount the **same volume**, just at different internal paths.
- Files written by one container are **immediately visible** to the other.
- Even after both containers exit, the data **persists** in the volume.

---

## Useful Volume Commands

```sh
# List all volumes
docker volume ls

# Inspect volume details (see the host mountpoint)
docker volume inspect volume_ubuntu

# Remove a specific volume
docker volume rm volume_ubuntu

# Remove all unused volumes
docker volume prune
```

### Inspect output explained
```json
[
  {
    "Name": "volume_ubuntu",
    "Driver": "local",
    "Mountpoint": "/var/lib/docker/volumes/volume_ubuntu/_data",
    "Scope": "local"
  }
]
```
The `Mountpoint` is where Docker actually stores the files on the host machine.

# Docker Bind mount 

### Docker image file - mysql with data persistent
```dockerfile
FROM mysql:8.0
ENV MYSQL_USER=mysql-user
ENV MYSQL_PASSWORD=mysql-password
ENV MYSQL_ROOT_PASSWORD=mysql-root-password

VOLUME /var/lib/mysql
EXPOSE 3306
```

### Docker build command
```bash
docker build -t mysql-image .
```

### Docker run command with bind mount to persist data on host machine
```sh 
docker run -d --name mysql-container -v $(pwd)/mysql-data:/var/lib/mysql -p 3306:3307 mysql-image
```