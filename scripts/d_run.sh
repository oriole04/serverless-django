#docker run --env PORT=8888 -it -p 8888:8888 serverless-django   #works using 0.0.0.0:$PORT in entrypoint.sh
#also works using -p 8888:8888

# docker run --env PORT=5000 -it -p 5000:5000  serverless-django
docker run --env PORT=8888 -it -p 5000:8888  serverless-django
# docker run --env PORT=5000 -it -p 80:5000 serverless-python; works on 127.0.0.1:5000
#docker run --env PORT=8888 -it -p 8080:8888 serverless-django   #works using 0.0.0.0:$PORT in entrypoint.sh

