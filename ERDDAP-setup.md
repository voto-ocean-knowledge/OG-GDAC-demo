### Pre-requisites

1. A linux machine with docker compose installed
2. A few GB disk space
3. 2 GB of RAM

### Get the GDAC ERDDAP running

```bash
docker compose up
```

Now navigate in your browser to http://localhost:8080/erddap/index.html


### ERDDAP settings

All of the config is in `erddap/conf/config.sh`. Alternatively, these can be overriden using `erddap/contet/setup.xml` which is currently empty.