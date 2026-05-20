# OG-GDAC-demo

A federated ERDDAP of Ocean Gliders data. How hard can it be?

For instructions to setup this ERDDAP, see `setup.md`

For example notebooks on getting data from this ERDDAP, see the `notebooks` directory.

### Success criteria

- [x] Simple ERDDAP setup with docker
- [x] Federate OG data from one server
- [x] Federate OG data from multiple servers 
- [ ] Check that OG datasets are compliant with IOOS compliance checker
- [ ] Consistently distinguish between nrt and delayed mode datasets
- [x] Make datasets searchable
- [ ] Execute queries across all datasets
- [ ] Instructions to convert this from proof-of-concept docker to a persistent server

# Credits

`compose.yaml` based on the example from the IOOS[ERDDAP gold standard repo](https://github.com/ioos/erddap-gold-standard)