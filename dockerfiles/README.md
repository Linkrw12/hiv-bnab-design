# Dockerfiles

The pipeline uses a combination of custom-made docker images and images from already 

# Custom dockerfile

For all custom docker images, run `docker build -t {package_name}:{version} .`


# Publicly available Dockerfiles

## Boltzgen 0.3.1
```
git clone https://github.com/HannesStark/boltzgen.git
cd boltzgen/
docker build -t boltzgen:0.3.1 --build-arg DOWNLOAD_WEIGHTS=true .
```