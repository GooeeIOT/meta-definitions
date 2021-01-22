# meta-definitions

Metrics used in the Gooee Cloud. The meta definitions here are intended to be
used as a single source of truth across Gooee repositories.


# How to add a new meta

1. Update the appropriate file under the meta_definitions folder. 
2. Adjust the package version in the setup.py file and add the tag with the new version number.
   For example: `git tag 1.0.0`.
2. Open a PR against master. Once it is merged, make sure the new Release is added in 
   Github under the `Releases` section with the new `version` as `tag` and add some description of 
   the updates.
3. Then you will need to trigger the deployment of the repositories
   using this package (adjust package version in the respective `requirements.txt` file of
   each repository to point ot the latest version).
     - anx-api
     - anx-datalake-fhose-transform
     - anx-snowflake-sqlalchemy 
     - cloud-api (pending update)
     - cloud-mqtt (pending update)
     
     Sample installation requirement for version 0.0.1: 
     ```
     git+ssh://git@github.com/GooeeIOT/meta-definitions@0.0.1
     ```
    
