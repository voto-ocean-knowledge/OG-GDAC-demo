### Pre-requisites

1. A linux machine with docker compose installed
2. A few GB disk space
3. 2 GB of RAM

### Get the GDAC ERDDAP running

```bash
docker compose up
```

Now navigate in your browser to http://localhost:8080/erddap/index.html

You should see a basic ERDDAP server with a couple of datasets
### ERDDAP settings

All of the config parameters are in `erddap/conf/config.sh`. Alternatively, these can be overridden using `erddap/contet/setup.xml` which is currently empty.

### Add datasets from other ERDDAP servers

1. Edit `src/add_federated_datasets.py` to include the sources you want (currently pulling from VOTO and BODC)
2. Run `src/add_federated_datasets.py`
3. Restart the ERDDAP server
