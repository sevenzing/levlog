Lev blog 
===

1. Env

```
export $(grep -v '^#' .env | xargs)
```


2. DB

```
docker-compose up -d
docker exec -it levlog_db_1 psql postgresql://levlog:levlog@localhost:5432/levlog
```
