### to build images from docker-compose.yml for the first time.
docker-compose up --build

### to build only single image using docker-compose
docker-compose build <image_name>
### to run images after built
docker-compose up

### to stop all containers
docker-compose down


### to open shell inside container
docker exec -it <container_id> sh

### to execute command directly in conainer
docker exec <container_id/name> <command>

### to list all container
docker ps -a

### to delete all containers
docker system prune -a

### to delete individual containers
docker container rm <container_name_or_id>