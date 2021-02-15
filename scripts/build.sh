# execute from c:/dev/serverless-django directory

gcloud builds submit --tag gcr.io/quick-composite-291621/serverless-django:v0 . --project quick-composite-291621

# --async makes it non-blocking to avoid Output: failed to load paths messages, but then you'll have to log on to see if it really pushed

