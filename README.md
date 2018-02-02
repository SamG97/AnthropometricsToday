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
