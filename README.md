# AnthropometricsToday
## Project Brief

In the 1880s students in Cambridge had their head measured to test for
correlations between head size and degree class (https://goo.gl/Tbfoww).
To celebrate the 200th anniversary of the Cambridge Philosophical Society, a
major public exhibition will reconstruct this experience. You will use
computer vision to measure visitors' profiles, matching against archive records
of thousands of ex-students to identify a (possibly famous) historical twin,
and then render a simulation of a new "handwritten" record card that can be
accessed online to compare your future grades to theirs.

#Installation
Below follows a guide to install and configure the various servers necessary to
run the project. This guide assumes that you are using a Linux distribution but
other operating systems should be also work (although this is not guaranteed)
with obvious adjustments to the installation process for that specific OS.

## Front End
### Development Server
This is a guide for running a development server for testing and making
changes.
1. Install nodejs using the following commands:
   ```
   curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
   sudo apt-get install -y nodejs
   ```
2. Install `npm` using a standard package manager.
3. Navigate to `AnthropometricsToday/front-end/anthropometrics-today`
4. To configure the server, navigate further to `src/utility/config.js`
5. Update the fields `backEndBaseUrl` and `webBaseUrl` to the address of the
   REST API configured below and the address of the web server (which will be 
   `http://localhost:3000` for the development server) respectively
6. If you wish to change the suffixes for the REST API's different requests,
   this can be done by changing the suffix options in the same file
7. Return to `AnthropometricsToday/front-end/anthropometrics-today`
8. Run `npm start` which will start a local web server at `localhost:3000`


### Production Server
If you want to run the server in a production environment for other users to
access, you need to host it on a web server. This will show you how to
configure the server on Apache2.
1. Follow steps 1-7 if not done so already for setting up the development
   server (changing the addresses for the web server if necessary)
2. Install `apache2`
3. Run `npm run build` from `AnthropometricsToday/front-end/
   anthropometrics-today` which will create a new directory `build`
4. Copy the contents of the `build` folder (not the folder itself) to the root
   directory of the web server (which is `/var/www/html` by default)
5. Navigate to `AnthropometricsToday/front-end/webserver-config`
6. Copy the `.htaccess` file to the root directory of the web server
7. Replace the `000-default.conf` file in `/etc/apache2/sites-available` with
   the file in `AnthropometricsToday/front-end/webserver-config`
8. Run `sudo a2enmod rewrite && sudo service apache2 restart` to restart the
   web server with the updated configurations

## Database
In order to run the database correctly, you need to do the following:
1. Install <a href="https://www.postgresql.org/download/">PostgreSQL</a>.
   (make sure that pgAdmin is included in your release)
2. During the installation, the program will ask you to create a password for
   the superuser 'postgres', either remember it or just write it down if you
   like.
3. Open pgAdmin, and create a database named `group project` in your localhost
   database server, set its owner to **postgres** (or whatever user you like if
   you are an expert of PostgreSQL).
4. Right click the `group project` database , and click Restore to restore the
   database from the `fake database with fakedata.tar` file provided underneath
   the dummy database directory (also underneath `backend/
   
   
   
   
   
   
   
   
   
   
   
   
   `) , or you can
   create a table using the sql query table_generated.sql in the same directory
   and import your own collected data according to the schema if you wish.
5. Modify the 5th line starting with `conn=` in `DataBaseScript.py` in the
   `/backend/restAPI/` directory, to match the owner user that you assigned
   in step 3 and the password that you created in step 2.

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
3. Navigate to `AnthropometricsToday/backend/restAPI`
4. Run `Python3 RESTAPI.py` to start the server

## Troubleshooting
Everything should now be working fine but here are some possible issues you
may run into with some possible causes:

1. If when navigating to `<root>` (where `<root>` is the
   base address of your web server), no page loads, the web server is likely
   not running. Make sure you have run `npm start` if using a development
   server or that the apache2 process (or other host) is running if using a
   production server,
2. If you navigate to `<root>/report/1/Sam&&AMAMAM` and receive an Apache 404
   error, the URL rewriting that the configuration options included in
   `AnthropometricsToday/front-end/webserver-config` have not worked. Ensure
   that the root of the web server (`/var/www/html` by default) contains the
   `.htaccess` file. This may be hidden so use `ls -A` to show it if it exists.
   Additionally, check that the `000-default.conf` file in 
   `etc/apache2/sites-available` contains the `Directory /var/www/html` block
   in the file included on this repository,
3. If you navigate to the same address as in 2 and get an error page or find
   that there are missing attributes in the report page, something has gone
   wrong with the back end server. Check that the address used for the 
   `backEndBaseUrl` option in `AnthropometricsToday/front-end/
   anthropometrics-today/src/utility/config.js` is set to the correct value.
   If this is correct, check the API server logs which will likely indicate
   the problem that has occurred.
