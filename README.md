Data Centric Development: Irish Energy Assets Database
============================
This is the Milestone Project for the Data Centric Development module for the Code Institutes Diploma in Software Development. 
The project shows my understanding and capabilities in developing a data centric web applications using Python, Flask and Bootstrap to interact with MongoDB.

The project was also used to explore the uses of the software skills learned through this course, to intereact 
applwith the energy industry, in which I have a number of years of proffessional experience.

For the development of this app I moved away from using the online Cloud9 IDE to using Visual Studios on my local Windows machine.

The app comprises with a MongoDB database of all the Connected and Contracted energy assets on the Irish National Electrical rid. 
This included all assets on the transmission network operated by both the Irish Transmission System Operator (TSO), Eirgrid, and also the Distribution System Operator (DSO), ESB Networks.
The data for the database was scraped from publically availalbe pdfs from the respectful system operators websites, converted to csv using Tabula.py, organised initially using Excel, 
converted to json using an online tool, combined and added to te MongoDB database. Care was taken to gather upto date accourite data for the different assets. 
The data from the different operators was not standardised and so there was much digging required to accuire common data across all the assets.

The app can be used to explore all the assets on the Irish grid. New assets can be added to the database and current assets can be edited and deleted. 
A series of graphs are used to visualise the data to give some insights into the national electrical system.

UX
----
The application was developed with two end uses in mind:

* To be used by grid operators, traders and end users to keep track of all the assets available similar to that developed by the Energy Web Foundation (https://energyweb.org/  ). 
  Much of the Front-End design concepts were taken from images of their indevelopment online platform. 
  The Energy Web Foundation also uses json style data, which was more or a reason to use MongoDB as the database.

* To be used to visualise the Irish national grid in graphs to gain a greater insight into the countries energy pool.

__User Stories__

User stories were developed to guide game play and desired functions.

* As a site visitor I should provided with an About App summary before accessing any data.
* As a site visitor I should be able to see all energy assets in the DB including their attributes. Each attribute column should be filterable. And maybe have a search box.
* As a site visitor I should be able to see data visualisation summaries of the different asset types contribution to the energy mix.
* As a site visitor I should be able to see each asset in more detail..
* As a site visitor I should be able to sign in as ADMINISTRATOR or as a user. The user will a company that owns and energy asset.
* As admin should have full CRUD access access to all the assets.
* As non-admin logged in user I should be able to create a new asset and have update and delete access to all of my owned assets.


Features
-----------------

__Existing Features__

* The home page shows all energy assets, with collapsible details secion
* From the home page you can access the create new asset page, and include a new asset in the system
* From the home page you can access the edit asset page for each of the assets, from which you can update or delete the asset from the database
* The trend page displays two pie charts: the distribution of power capicity for each of the companies in the TSO non-wind catagory. 
  And a pie chart of the energy distribution of all connected assets across the counties of ireland.
 
__Future Features__
* Sign in feature. Admin ill have full access to database. A company will only be able to edit their owned assets.
* Use psyio app to show running trend of the irish generation data. This will either require a seperate collection of pull the data direct from the app.
* Funtion to set db back to original data
* Require summary as to why asset has been edited
* Get admin to confirm edit or entry
* Seperate page for user assets
* Filter and search funtions for database on home page
* Show more graphs. i.e compare TSO and DSO capacities and distributions, the percentage of new contracts under each heading ect.



Technologies Used
-----------------------
* __VisualStudios2017__ was used for developing the app.
* __VirtualEnvirnment__ was used to wrap the project.
* __Tabula.py__ was used to extract data from PDF to CVS
* __matplotlip__ was used to generate pie charts
* __geopy__ was used to get the address of the substations
* __FluidUI__ (https://www.fluidui.com) was used to develop wireframes for the initial UI design mockups.
* __Python3__ (https://docs.python.org/3/) was used to develop all back-end code.
* __HTML5__ (https://www.w3.org/TR/html5/) was used to develop front-end templates.
* __CSS__ (https://www.w3.org/Style/CSS/) was used for styling of front-end templates.
* __Flask__ (http://flask.pocoo.org/) microframework was used throughout the project in interacting between the back-end code and front-end templates, rendering templates and acquiring data.
* __json__ (http://www.json.org/) was used to store and access game play data.
* __Bootstrap 3.3.7__ (https://stackpath.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css) was used for more effective CSS layout styling. 
    - __Boostrap Grid__ system was used for content arrangement and responsive behavour when moving between different screen sizes
    - __Boostrap Navbar__ was used for the main navigation. Collapsible menu was utilised for lower screen resolutions.
    - __Bootstrap Forms Controls__ were used for the user actions.
* __Font-Awesome 5.3.1__ (https://use.fontawesome.com/releases/v5.3.1/css/all.css) was for the icons in the header, footer and quiz template.
* __Unittest__ (https://docs.python.org/3/library/unittest.html) unit testing framework was used for the testing of none template rendering functions.

Testing
-----------------------

__Code Validation__

* __Python__ was validated using http://pep8online.com/. Both run.py and test_quiz.py are pep8 compliant.
* __HTML__ was validated using https://validator.w3.org/. Due to the python code embedded in the HTML templates there were a number of errors.
* __CSS__ was validated using https://jigsaw.w3.org/css-validator/validator. No  errors were found.
* __Spelling and Grammar__ was validated using Google Docs.


