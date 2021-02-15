c:\dev\cloud_sql_proxy.exe -instances=quick-composite-291621:us-central1:ihm-chapel-db=tcp:6543 -credential_file=c:\dev\serverless-django\db\key.json

#postgres locally uses port tcp:5432
#C:\Users\cfe\cloud_sql_proxy -instances=serverless-cfe:us-west1:serverless-django-db-instance-01 -credential_file=C:\Users\cfe\Dev\serverless-django\db\key.json
#use this line, it works at the c:\dev dir:
#.\cloud_sql_proxy.exe -instances=quick-composite-291621:us-central1:serverless-django-ihm=tcp:6543 -credential_file=c:\dev\serverless-django\db\key.json
#psql -U myUser -h 127.0.0.1