# user-service

## Set up
### Create virtual environment
```buildoutcfg
cd user-service
python3 -m venv .env
source .env/bin/activate
```
### Install dependencies
```buildoutcfg
pip install -r requirements.txt
```

## Run on localhost
```buildoutcfg
cd user_service
flask run
```
## Debug on localhost
```buildoutcfg
cd user_service
FLASK_ENV=development flask run
```

## Run in Docker
Note: requires Docker to be installed
```buildoutcfg
docker-compose up
```

## Swagger
To access Swagger go to
http://127.0.0.1:5000/api/spec.html#!/spec
