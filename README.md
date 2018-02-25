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

## Back End
In order to run the database correctly, you need to do the following:
1. Install PostgreSQL. (make sure that pgAdmin is included in your release)
2. Open pgAdmin, and create a database named "group project" in your localhost database server.
3. Right click the group project database , and click Restore to restore the database from the .backup file provided underneath the dummy database directory.
4. Delete the password requirement to access this database, by editing the **pg_hba.conf** under the data directory of your installed PostgreSQL directory.
5. Enjoy  (´・ω・)ﾉ
