docker build -t backend .
docker run -t -d -p 5040:5040 --name backendocker backend
docker ps -a
