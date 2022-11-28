# COMP3900 Recipe Manager
This is a web application that allows users to add and edit recipes. 

## Running in a VM 

Before doing these steps I'd recommend adjusting the screen resolution of the VM. To do this click on the Lubuntu logo, then type `Monitor Settings`.
Change the Resuloution to whatver your monitor can handle and click apply. Note you may need to reboot your vm for the effects to take place. 

1. Download the zip file from github for the repository. Save it in the default folder (Downloads). DO NOT UNZIP OR SAVE ELSEWHERE

2. Open a QTerminal and run `unzip ~/Downloads/capstone-project-comp3900-w18a-shehulk-main.zip -d ~/cs3900/`

3. Next run `cd ~/cs3900/capstone-project-comp3900-w18a-shehulk-main/ && bash setup.sh` in QTerminal.

4. When prompted for password enter the VM password, for other prompts press y. This will take a few minutes. 

5. Once the required packages are downloaded close and reopen QTerminal.

6. Now you may run `dostart` to start up the application. Wait for the backend to start.

7. Next run `pypop` to populate the database with test data. 

8. Lastly run `festart` to start the frontend. Note: This will launch the application and open up the frontend in firefox. 

9. To close the application go to the Qterminal instance running and press ctrl c. then run `festop` in Qterminal 

Note, there are much more detailed instructions (with images) in the Project Report. 

## Instructions on Running Application Locally
Note, this section is NOT required but is an easier way to develop.

### Running the Database and Flask in Docker
  
1. Install Docker Desktop from https://www.docker.com/get-started/ and follow the installation instructions.

2. Create up a .env file as below, with values for PG_USER, PG_USER_PASSWORD, PG_ADMIN_EMAIL and PG_ADMIN_PASSWORD:
```
export DB_HOST=db
export PG_USER=
export PG_USER_PASSWORD=
export PG_ADMIN_EMAIL=
export PG_ADMIN_PASSWORD=
export FLASK_SECRET=

FLASK_APP=project/__init__.py
FLASK_ENV=development

```

3. Then run `docker-compose build --up` to build the images and start up the containers. If you don't want to see the logs, run with the `-d` flag. 
   
4. You should see the below (among other logs) if it has created the tables and added the test data properly successfully. 
```
CREATE EXTENSION
CREATE TABLE
CREATE TABLE
CREATE TABLE

INSERT 0 1
INSERT 0 3
```

If you don't see the above logs and instead you see the below, complete Step 6 before going back to step 4. 
```
Database is already initalised, skipping initalisation. 
```

5. (OPTIONAL) You can view this database through opening http://localhost:5050/browser/ and logging in with the email and password credentials you set in the docker-compose.yml file.

6. Run `pytest` in another terminal.
   
7. If you ever need to close the container/volumes, run `docker compose down -v`.

8. (OPTIONAL) You can access the Flask through http://localhost:5000/ 

### Running the FE Locally

1. Open another terminal and move into the frontend directory: `cd frontend`.
   
2. Run `npm run start` to run FE. If there are any package errors, you may need to run `npm i` first. 





