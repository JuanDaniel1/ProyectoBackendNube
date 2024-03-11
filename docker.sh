docker build -t backend .
docker run -t -d -p 7070:7070 --name backendocker backend
docker ps -a
