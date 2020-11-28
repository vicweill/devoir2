# Last session project.
## Duration: 3h

## In English (French below)

### Must Do !
- You can define your dockerfile wherever you want but you **MUST** copy **all the contents** of the directory **manager** in a **app** folder from the **root of the container**
- You **MUST** define the **docker-compose.yml** file where it is usually defined, that is, the **project root**.
- The Python code **MUST NOT** be modified, **NOR** moved under **NO** circumstances, **only 1 Dockerfile and 1 docker-compose file should be created**
- You will need, using the docker-compose file, to **tag** the image built from the dockerfile with the exact name: **manager:latest**.

Anything that does not respect the aforementioned conditions will result in an automatic score of 0 for this exam. This is CRUCIAL so that I can perform the tests on your project.

### Tips
* the **dockerfile filename and extension** is left free, however remember to adapt the docker-compose file if the name were to be different from the conventions (eg: Dockerfile.dev).
* Proceed step-by-step ! We do the dockerfile first, make sure it builds, then we can orchestrate everything with the docker-compose file.
* for the dockerfile: check if the project requires one or more **libraries**, from the **import** statements in the application logic.
* it is **strongly advised to take a recent version of python image** (> 3.5) and **not** lightweight versions (such as the slim tag therefore), the latest and 3.8.4 tags are operational.
* wait for it: https://github.com/vishnubob/wait-for-it
* **environment variables** must be defined in order to **connect to the Postgres server** (user to authenticate, user password, database)
* For the **port and the name of the host to connect to the database**, you can directly find it in the code in the very first functions! **You will have to cleverly use the automatic service discovery feature provided by the docker-compose file** (if you had forgotten already, here [it is](https://docs.docker.com/compose/networking/)...! Again, you **can't** change the **code nor structure** so to be convenient for you.
So look at both how the official Postgres Docker image defines these variable names, and how the code/application logic uses them.


## French

### Chose à respecter absolument !
- Vous pouvez définir votre dockerfile où vous le souhaitez mais vous **DEVEZ** copier l'ensemble du contenu du directory **manager** dans un dossier **app** depuis la **racine du conteneur**
- Vous **DEVEZ** définir le **docker-compose.yml** file là où on le définit usuellement: la **racine du projet**.
- Le code Python **NE** doit être modifié, **NI** déplacé en AUCUN cas, **seuls 1 Dockerfile et 1 docker-compose file comptent.**
- Vous devrez, en utilisant le docker-compose file, **tagguer** l'image built à partir du dockerfile avec pour nom exact: **manager:latest**.

Vous devez respecter toutes les conditions ci-dessus, tout non respect entraînera une note de 0. Ceci est crucial pour que je puisse effectuer les tests sur votre projet.

### Astuces

* le nom de fichier du dockerfile est laissé libre, pensez bien cependant à adapter le docker-compose file si le nom venait à être différent des conventions (ex: Dockerfile.dev).
* faites par étape ! on fait le dockerfile d'abord, on s'assure que ça build, puis on peut alors orchestrer l'ensemble avec le docker-compose file.
* pour le dockerfile: regardez bien si le projet nécessite une librairie, du côté des **import** statements donc.
* il est vivement **conseillé de prendre une version récente d'image python** (>3.5) et **pas** allégée (pas le tag slim donc), exemple: les tag latest et 3.8.4 sont opérationels.
* wait for it : https://github.com/vishnubob/wait-for-it
* des **variables d'environnement** devront être définies pour pouvoir **se connecter au serveur Postgres** (user à authentifier, mot de passe du user, database)
* quand au **port et le nom du host**, vous pouvez directement le trouver dans le code dans les toutes premières fonctions ! **Il faudra astucieusement utiliser la fonctionnalité d'automatic service discovery apportée par le docker-compose file** (si vous aviez oublié... https://docs.docker.com/compose/networking/) ! Encore une fois, vous ne pouvez **PAS** modifier le code ni la structure pour vous "arranger".
Pensez donc à regarder à la fois comment **l'image Docker officielle de Postgres** definit ces noms de variables, et  comment le code les utilise.

<!-- 
### bind mounts exclusions

First of all, docker volumes or bind mounts behave like linux mounts.

If the host volume/mount exists and contains files it will "override" whatever is in the container. If not the container files will be mirrored onto the host volume/mount and the container folder and the host will be in sync. In both cases editing the files on the host will ALWAYS be reflected inside the container.

https://blog.maqpie.com/2017/02/22/fully-automated-development-environment-with-docker-compose/

https://bbengfort.github.io/observations/2017/12/06/psycopg2-transactions.html


tests here are mostly dependent of each other, 
you need to connect to db before doing request
you need to have uploaded a csv to create a table before checking its existence
etc.

"""
runs tkinter/__main__.py, which has this line:

from . import test as main

In this context, . is tkinter, so importing . imports tkinter, which runs tkinter/__init__.py. test is a function defined within that file. So calling main() (next line) has the same effect as running python -m tkinter.__init__ at the command line.


# what's the difference between a server side cursor and client side cursor (apprently you can't use a server side cursor to create a table): https://stackoverflow.com/questions/51804513/psycopg2-syntax-error-at-or-near-update

# dirname gives the last trailing directory in the absolute path defined by __file__
# again dirname will give the 2nd last trailing directory
 -->