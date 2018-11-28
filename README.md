Data Centric Development: Irish Energy Assets Database
============================
This is the Milestone Project for the Data Centric Development module for the Code Institutes Diploma in Software Development. 
The project displays clear understanding and capabilities in developing a data centric web applications using the Flask Python framework to interact with a Mongo database. 
The application was enhanced with JavaScript data visualisations and Bootstrap CSS styling.

Time was spent developing this project to best utilise data centric skills when applied to my key area of professional experience, the Energy Industry.

Irish-Energy-Assets application gives exploratory and CRUD access to a Mongo database comprising of all connected and contracted generation assets on the Irish national electrical grid.
It includes assets on the transmission network, operated by Eirgrid, and distribution network, operated by ESB Networks.

The data for the database was scraped from publically available PDFs from the respectful system operators websites, converted to csv using Tabula.py, organised initially using Excel, 
converted to json using an online tool, combined and added to the MongoDB database. Care was taken to gather up to date accurate data for the different assets. 
The data from the different operators was not standardised and so there was much digging required to acquire common data across all the assets.



UX
----
The application was developed with two end uses in mind:

* To be used by grid operators, traders and end users to keep track of all the assets available similar to that developed by the Energy Web Foundation (https://energyweb.org/  ). 
  Much of the Front-End design concepts were taken from images of their in development online platform. 
  The Energy Web Foundation also uses json style data, which was more or a reason to use MongoDB as the database.

* To be used to visualise the Irish national grid in graphs to gain a greater insight into the countries energy pool.

__User Stories__

User stories were developed to guide game play and desired functions.

* As a site visitor I should be given an introduction and a guide to what the application is.
* As a site visitor I should be able to see all energy assets in the DB including their attributes. 
* As a site visitor I should be able filter the results and search for keywords.
* As a site visitor I should be able to see graphical visualisations of the data for greater comprehension.
* As a site visitor I should be able to sign in as admin or as a user. The user will be a company that owns and energy asset.
* As admin I should have full CRUD access access to all the assets.
* As non-admin logged in user I should be able to create a new asset and have update and delete access to all of my owned assets.
* As admin I should be able to backup up the current data to a json file stored in a local directory.
* As admin I should be able to overwrite the current database with the data from the json backup.


Features
-----------------

__Existing Features__

* Home page gives user an introduction and instructions as to how to use the application.
* All assets can be explored on a tabular format, with additional attributes hidden in accordian style collapse.
* A filter side bar allows the user the to easily filter or search the database for keywords.
* Can sign in as a company or as an administrator
* As signed in administrator you have full CRUD access to all assets.
* As signed in company you have CRUD access to all your company's assets.
* D3 interactive charts are displayed on the trend page.
* As ADMIN have button backup database to json

 
__Future Features + To Do__
* As ADMIN have dropdown to rewrite database with json backup, select file from dropdown
* Include change log to each doc
!5* Update Voltage_kV
* Include Node capacity data
* Incude glossary
* Either get d3 data direct from mongo or write to json on every change
!4* Types, limit dropdown
* User stays signed in when moving around 
* Filter on enter and pass filter onto next load
* Get admin to confirm edit or entry
* Use crossfilter.js to filter table results using .top(Infinity)
!3* Style sizing of charts
* Add title
* Collpase script, run on first load
* Collapse icons, make correct on first load
* Include analysis section in about
* For reading addresses, make it a loop, as some geopy addresses are >6 lines
* Clear filter btn
* combine assets, filtered assets and check_username into one render event



Technologies Used
-----------------------
* __VisualStudios2017__ (https://visualstudio.microsoft.com/downloads/) IDE was used in the development of the project.
* __VirtualEnvirnment__ (https://docs.python.org/3/library/venv.html) was used to wrap the project.
* __Git__ (https://git-scm.com/) was used for version control.
* __GitHub__ (https://github.com/) was used to share the repository.
* __Heroku__ (https://dashboard.heroku.com/) was used to host the application.
* __MonogDB__ (https://www.mongodb.com/) database was used to store data.
* __mLab__ (https://mlab.com/) was used to host and explore the Mongo database.
* __Python3.6__ (https://docs.python.org/3/) was used to develop all back-end code.
* __Flask__ (http://flask.pocoo.org/) microframework was used throughout the project in interacting between the back-end code and front-end templates.
* __HTML5__ (https://www.w3.org/TR/html5/) was used to develop front-end templates.
* __CSS__ (https://www.w3.org/Style/CSS/) was used for styling of front-end templates.
* __Bootstrap 3.3.7__ (https://stackpath.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css) was used for more effective CSS layout styling. 
    - __Boostrap Grid__ system was used for content arrangement and responsive behaviour when moving between different screen sizes
    - __Boostrap Navbar__ was used for the main navigation. Collapsible menu was utilised for lower screen resolutions.
    - __Bootstrap Forms Controls__ were used for the user actions.
* __Font-Awesome 5.3.1__ (https://use.fontawesome.com/releases/v5.3.1/css/all.css) was for the icons in the header, footer and quiz template.
* __JavaScript__ was used for interactive frontend development.
* __D3.js__ (https://d3js.org/) was used to develop graphical visualizations of the data.
* __DC.js__ (https://dc-js.github.io/dc.js/) was to give interactive attributes to D3 charts.
* __Tabula.py__ (https://github.com/tabulapdf/tabula) was used to extract PDF data to CVS
* __GeoPy__ (https://geopy.readthedocs.io/en/stable/) was used to get the address of the substations
* __FluidUI__ (https://www.fluidui.com) was used to develop wireframes for the initial UI design mockups.
* __Unittest__ (https://docs.python.org/3/library/unittest.html) unit testing framework was used for the testing of none template rendering functions.
* __json__ (http://www.json.org/) was used to store and access non-database data.
* __CSVJSON__ (https://www.csvjson.com/csv2json) was used to convert CSV formatted data to json.
* __Firefox Developer Edition__ (https://www.mozilla.org/en-US/firefox/developer/) was used for debugging of the running app.


Testing
-----------------------

__Code Validation__

* __Python__ was validated using http://pep8online.com/. Both run.py and test_quiz.py are pep8 compliant.
* __HTML__ was validated using https://validator.w3.org/. Due to the python code embedded in the HTML templates there were a number of errors.
* __CSS__ was validated using https://jigsaw.w3.org/css-validator/validator. No  errors were found.
* __Spelling and Grammar__ was validated using Google Docs.


Development
------------------------
Visual Studios 2017 was used in the development of this project. I moved away from using the online Cloud9 IDE as I was having issues with Python versions,
when working with pip installed packages. By moving my development onto my local machine I have more control over the installed packages and can explore their folder
structures more easily. Sublime text editor as played with for a while but found Visual Studios much more featured and informative when developing.

This did require considerable more learning to manage my development on a Windows machine rather than on a Linux. 
A number of packages needed to be downloaded, alternative windows commands needed to be used and System Variables set.
Although time consuming, I felt this was time well spent and has given me a greater understanding on the Windows 10 system.

Virtual Environment was used as a wrapper to keep the project requirements separate from the rest of the machine. As there was a lot of experimenting with this project,
a number of different projects were created, copied, deleted and edited. Utilising the virtual environment made this an easy exercise and has left my final project much cleaner 
than what would have been.

As the data came from a number of different sources, mostly in PDF, and in different layouts there was considerable manipulation required to combine and format the data in a 
usable format. I have kept the code and data not used by the running application, but used in the development process in a separate folder, Dev Folder. 


Deployment
------------------------


