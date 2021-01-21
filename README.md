# meta-definitions

Metrics used in the Gooee Cloud. The meta definitions here are intended to be
used as a single source of truth across Gooee repositories.


# How to add a new meta

1. Update the appropriate file under the meta_definitions folder. 
2. Open a PR against master. 
3. After merging you will need to trigger the re-deployment of the repositories
   using this package:
     - anx-api
     - anx-datalake-fhose-transform
     - anx-snowflake-sqlalchemy 
     - cloud-api (pending update)
     - cloud-mqtt (pending update)
