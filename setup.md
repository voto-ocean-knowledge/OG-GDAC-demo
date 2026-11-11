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

### Going public

**TODO: do a full worked example of setup with nginx, ssl etc.**

To make this server public, you need a server with an associated address and SSL certificate. Since ERDDAP 2.28, you may need to set `useHeadersForUrl` to `false` in `setup.xml` so that urls are rendered as you would expect them (explained in the [gold standard repo readme](https://github.com/ioos/erddap-gold-standard)). At least, I had to with my nginx setup ymmv.
