from redis import Redis


redis_cli = Redis()
redis_cli_prod = Redis(host="redis")
