# AnthropometricsToday

In the 1880s students in Cambridge had their head measured to
test for correlations between head size and degree class
(https://goo.gl/Tbfoww). To celebrate the 200th anniversary of
the Cambridge Philosophical Society, a major public exhibition
will reconstruct this experience. You will use computer vision to
measure visitors' profiles, matching against archive records of
thousands of ex-students to identify a (possibly famous)
historical twin, and then render a simulation of a new
"handwritten" record card that can be accessed online to
compare your future grades to theirs.

## Front End
To run the web dev server, make sure to install an up to date version of
<a href="https://nodejs.org/en/">Node.JS</a> and <a href="https://www.npmjs.com/">npm</a>
and run npm install from \front-end\anthropometrics-today to install package dependencies.
You can then run npm start to start the web server which can be accessed at localhost:3000.

The home page for this site is the page to take a camera image. You can access reports by
navigating to /reports/{user}/{twin} where {user} and {twin} are the user and twin info
to pass to the report page. All other URLs will send you to a 404 page.

## Database
In order to run the database correctly, you need to do the following:
1. Install <a href="https://www.postgresql.org/download/">PostgreSQL</a>. (make sure that pgAdmin is included in your release)
2. During the installation, the program will ask you to create a password for the superuser 'postgres', either remember it or just write it down if you like. (￣３￣)a
3. Open pgAdmin, and create a database named "group project" in your localhost database server, set its owner to **postgres** (or whatever user you like if you are an expert of PostgreSQL).
4. Right click the "group project" database , and click Restore to restore the database from the **"fake database with fakedata.tar"** file provided underneath the dummy database directory (also underneath backend/venv/) , or you can create a table using the sql query table_generated.sql in the same directory and import your own collected data according to the schema if you wish.
5. (Only do this if you want to set it up for local test, otherwise go to step 6) Delete the password requirement to access this database, by editing the **"pg_hba.conf"** under the data directory of your installed PostgreSQL directory. You need to replace every 'md5' with 'trust' in this file. In the 5th line starting with 'conn=' in **"DataBaseScript.py"** in the /backend/venv/restAPI/ directory, you should empty the password field, and then setup the user to match the owner that you set in step 3. Then go to 7.
6. (Do this if you want to run this server publicly) Modify the 5th line starting with 'conn=' in **"DataBaseScript.py"** in the /backend/venv/restAPI/ directory, to match the owner user that you assigned in step 3 and the password that you created in step 2. Then go to 7.
7. Enjoy  (´・ω・)ﾉ

## REST API
To run the API:
1. Install Python 3
2. Install Python packages using pip:
	- flask
	- flask_jsonpify
	- datetime
	- functools
	- ast
	- numpy
	- face_recognition
	- skimage
	- psycopg2
	- heapq
3. Navigate to `AnthropometricsToday/backend/venv/restAPI`
4. run `Python3 RESTAPI.py` to start the server
