docker build -t serverless-django -f Dockerfile .

docker tag serverless-django gcr.io/quick-composite-291621/serverless-django:v0

docker push gcr.io/quick-composite-291621/serverless-django:v0