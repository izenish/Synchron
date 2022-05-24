1. run sh inside postgres container
```bash
    docker exec -it postgres sh
    /bin/bash
```

2. run psql shell
```
    psql -U <postgres_user> <postgres_db>
```
> eg. psql -U synchron postgres

# OR

### Combine 1 and 2
```
    docker exec -it posgres psql -U synchron postgres
```

3. 
## SQL commands

1. \l -> lists all databases
2. \dt -> lists all database tables
3. select version();
4. select current_date;
5. \q -> quit

#### Note: you can run sql queries like SELECT,UPDATE,CREATE etc..