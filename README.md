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


UX
----
The application was developed with two end uses in mind:

decidedd to have index show the assets and provide the info seperatly.

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


Features and Process
-----------------

__Existing Features__


* __Data Collection__ of asset details publically available in PDF format from ESB and Eirgrid websites.
* __Data Formating__ using Tabula.py to convert .pdf files to .csv format, which were then converted to .json using www.csvjson.com/csv2json.
* __MongoDB Creation__ by developing script to bulk import the .json data files.
* __Scrollible Data Display__ in index.html 'Assets List' section in tabular format, showing primary asset details (Name, Type and MEC). The table is scrollable rather than paignated as it would be more user friendly.
* __Accordian Collapse__ style dropdown shows further asset details when clicking on the primary line item. Additional details included details on the assets
connected network, when the asset was first added to the database and when it was last updated.
* __Geocoding__ was performed using GeoPy.py to assign full addresses to each Node by searching for 'Node Name' + 'Ireland'.
* __Data Filter__ scripts were writen taking in filter parameters set in 'Refine Filter' side-nav. 
    - __Apply Filter__ button reloads the page with filtered data based on filter parameters and selected sort arrangment.
    - __Reset Filter__ button clears the parameters set in the filter nav since the last page load. Does not change the data currently displayed.
    - __Clear Filter__ button reloads the page with no filters applied.
    - __Keyword Search__ loops through all document attributes and returns, subset where the keyword is found in values. This is not case sensitive.
    - __Tick Box Selectors__ for Status, SystemOperator, Types, Node and County attributes set list of value argumenets for returning the subset. If no box from a section is ticked then no filter for that attribute is imposed. 
    If a box is ticked in a section than only the values ticked will be displayed.
    - __Range Filter__ for MEC sets the range of MEC values to return.
* __Data Sorter__ sorts data alphabetically (A-Z) by asset 'Name' by default. This can be changed by selecting one of the 6 options from the 'Srot by' dropdown in the 'Refine Filter' section.
    - Name (A - Z)
    - Name (Z - A)
    - Type (A - Z)
    - Type (Z - A)
    - MEC (Low - High)
    - MEC (High - Low)
* 







* DC interactive charts are displayed above the Assets list. An insightful example of the use of the interactive chart is by clicking on the connected bar on the MEC by Status chart, and Wind on the MEC by Type,
you will see from the MEC by County chart that half the connected wind is built on the most exposed corners of the Irish coast Kerry, Cork and Donegal, and if you then include contracted you will see that Mayo will have the most development in the coming years.
* 'About Site' page, accessed from the main nav gives information on the purpose of the site, how to use the site, how the electrical grid is organised, where the data came from and a glossary of terms and abbreviations used.

__Company Log In__

* User can log in by entering the login page by clicking on 'Login on the top right of the view'.
* 'Log In' instructs the user that they can log in as a company name on record or as 'admin'.
* If an invalid company name is entered an error message is displayed for the user to enter a valid name.
* If signed in as a company name on record (i.e. ESB) the home page is displayed filtered to display all assets owned by you.
* A welcomes message to the logged in user is displayed and the user is given the option to log out in the top right of the screen.
* As a user you can edit and delete your asset details from the database by clicking the 'Update Asset' link, located in the 'Data Details' section in the dropdown for that asset.
* The 'Update Asset' link opens the 'edit asset' page where the user can update the details or delete the asset entirely from the database.

__Admin Log In__

* If logged in as 'admin', you have edit and delete access to all assets, by the same means as detailed above for Company Login.
* An additional 'Admin' menu item is shown giving access to the 'admin' page.
* Here 'admin' can add a new asset to the database by entering in the details under the 'New Asset' section and clicking the 'Add Asset' button.
* Some of the attribute fields are required for the asset to be entered and some require to be chosen from a list of options.
* Note: for the type section there is an option to select 'Other' and then enter the type under sub-type to allow for new technologies to be added to the system.
* Under the 'Backup Control' section the admin can right the Mongo database (losing the object ID) to a .json file stored in the local website directory by clicking the 'Backup' button.
The backup is time stamped.
* The admin can also replace the Mongo database with one of the previous .json backups. The file to be used is selected from a dropdown and executed by clicking 'Overwrite' button.
* As the this function deletes all assets from the database before writing backup data to it, a backup of the current database is automatically created when executing the overwrite.



 
__Future Features + To Do__
* Include change log to each doc
* Update Voltage_kV _ further 45 to include
* Include Node capacity data
* Include glossary
* Either get d3 data direct from mongo or write to json on every change
                                                                                !* User stays signed in when moving around
                                                                                !* Filter on enter and pass filter onto next load
                                                                                !* Collapse script, run on first load
                                                                                !* Collapse icons, make correct on first load
* Include analysis section in about
* combine assets, filtered assets and check_username into one render event
                                                                                !* reload d3 charts on screen resize for correct formatting

not pushed
* For reading addresses, make it a loop, as some geopy addresses are >6 lines
* Use crossfilter.js to filter table results using .top(Infinity)
* Get admin to confirm edit or entry




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




