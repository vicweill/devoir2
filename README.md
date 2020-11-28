Si vous définissez un dockerfile, assurez vous que vous incluyez le dossier de test
Si vous créez une image, assurez vous que celui si est tagguée avec pour nom ...
Vous utiliserez le nom de Dockerfile.dev pour votre dockerfile
Le nom du tag de l'image sera appelé "manager:latest"


### bind mounts exclusions

First of all, docker volumes or bind mounts behave like linux mounts.

If the host volume/mount exists and contains files it will "override" whatever is in the container. If not the container files will be mirrored onto the host volume/mount and the container folder and the host will be in sync. In both cases editing the files on the host will ALWAYS be reflected inside the container.

https://blog.maqpie.com/2017/02/22/fully-automated-development-environment-with-docker-compose/

https://bbengfort.github.io/observations/2017/12/06/psycopg2-transactions.html