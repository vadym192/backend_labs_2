# Backend Labs 1

## Setup Environment

1. Clone Repository
```
git clone https://github.com/vadym192/backend_labs_1.git
cd backend_labs_1
```

2. Build a Docker Image
```
docker build -t <your image name> .
```

3. Run Docker Container
```
docker run -it --rm --network=host -e PORT=8000 lab1_image:latest
```

4. Check the result
```
http://127.0.0.1:8000/healthcheck
```

## If you want to use docker-compose just run these two commands
1. Build docker
```
docker-compose build
```
2. Run docker
```
docker-compose up
```
3. Check the result
```
http://127.0.0.1:8000/healthcheck
```
