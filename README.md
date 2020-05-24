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
```buildoutcfg
docker-compose up
```
