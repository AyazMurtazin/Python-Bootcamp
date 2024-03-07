# PREPARATION

## run

```
pip install -r requirements.txt
```

# TASK 00

## run:
```
python3 fight.py
```

# TASK 01

## run server:
```
uvicorn server:app --reload --port 8888
```

## run client:
```
python3 crawl.py https://example.com/ https://example.com/index/
```

# TASK 02

## run redis:
```
redis-server
```

## run server:
```
uvicorn server_cached:app --reload --port 8888
```

## run client:
```
python3 crawl.py https://example.com/ https://example.com/index/
```

## if you want to check cache:

```
python3 get_ceche.py
```

# EXIT

to stop redis-server run:

```
/etc/init.d/redis-server stop
```