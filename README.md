Data Centric Development: Irish Energy Assets Database
=========================================================
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
* __Data Filter__ scripts were writen taking in filter parameters set in 'Refine Filter' side-nav. NExt to each filter option the number of documents to that will be returned and sum of their MEC is displayed.
    - __Apply Filter Button__  reloads the page with filtered data based on filter parameters and selected sort arrangment.
    - __Reset Filter Button__ clears the parameters set in the filter nav since the last page load. Does not change the data currently displayed.
    - __Clear Filter Button__  reloads the page with no filters applied.
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
* __Interactive Charts__ display the database data. Three charts show the MEC distribution across Types, Counties and Status. An insightful example of the use of the interactive chart is by clicking on the connected bar on the MEC by Status chart, and Wind on the MEC by Type,
you will see from the MEC by County chart that half the connected wind is built on the most exposed corners of the Irish coast Kerry, Cork and Donegal, and if you then include contracted you will see that Mayo will have the most development in the coming years.
* __About Site__ page gives information on the purpose of the site, how to use the site, how the electrical grid is organised, where the data came from and a glossary of terms and abbreviations used.
* __User Login__ for logging in as 'admin' or a company that owns one of the assetss. Accessed by entering the login page from login button on top right of the page. Loging as a company gives you edit and delete database access to their assets. Loggin in as 'admin' gives full CRUD access to the database.
* __User Validation__ if user enters a name that is not on the list of company names, they are receive an erro message and asked to enter a valid company name.
* __Updating Document__ can be performed once logged in, by clicking 'Update Asset' link, located in the 'Data Details' section in the dropdown for that asset. This is only visible when you have access to the document. This opens edit_asset.html to edit the asset.
* __Deleting Document__ can be performed from the edit_asset.html page by clicking 'Delete Asset' button.
* __Creating Documnet__ to add to the database can only be performed by the admin. To add a document the admin must enter the 'Admin' page by clicking the menu option, only visible when logged in as 'admin'. Here the 'admin' can enter the new asset details.
Note: for the type section there is an option to select 'Other' and then enter the type under sub-type to allow for new technologies to be added to the system.
* __Database Backup__ can be performed from the 'Admin' page by clicking the 'Backup' button. This writes the MongoDB collection, less the object _ID, to a .json file in the websites directory. The backups are timestamped.
* __Database Fallback__ to a backup .json can be performed by selecting one of the backups in the directory and clicking 'Fallback' button. Before the collection is cleared, a backup is automatically created to avoid loss of data.
* __Responsive Design__ collapses and rearranges sections based on importance as the screen changes sizes. Dropdown indicators change to indicate what state the relevent collapse is in.


__Future Development__


* __Change Log__ recording if, when and by who a document was updated.
* __Node Capacity__ to indicate which nodes are reaching their maximium connected MEC limit.
* __Glossary__ of abbrevieations and terminaology
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
* __CSS__ was validated using https://jigsaw.w3.org/css-validator/validator. No errors were found.
* __Spelling and Grammar__ was validated using Google Docs.

__Unittest Automated Testing__

Throughout the development of this project a 'Test After' approach was taken. After deciding what was needed, the function was written, manually tested 
while developing. Once a basic function was built, an automated test was written in test_app.py using unittest testing framework for each of the possible conditions.
As functions became more complex and interacted with other functions, these automated tests insured that the functions all maintained their required functionality. 8 functions were tested in this manor.

__Visual Testing__

The dev tool within Firefox Development Edition was used to test that the pages were displaying correctly (alignment, spacing, position etc) across different screen widths.


|                                                       | Galaxy S5 | Pixel 2 | Pixel 2XL | iPhone 5/SE |	iPhone 6/7/8 | iPhone 6/7/8 + | iPhone X | iPad  | iPad Pro   | Responsive 1366 x 768 | Responsive 1680 x 1050 |  
| ----------------------------------------------------- | --------- | ------- | --------- | ----------- | -------------- | -------------- | -------- | ------| ---------- | --------------------- | ---------------------- |
| index.html (collapsed and un-collpased sections)      | OK        | OK      | OK        | OK          | OK             | OK             | OK       | OK    | OK         | OK                    | OK                     |                 
| about.html (collapsed and un-collpased sections)      | OK        | OK      | OK        | OK          | OK             | OK             | OK       | OK    | OK         | OK                    | OK                     | 
| login.html                                            | OK        | OK      | OK        | OK          | OK             | OK             | OK       | OK    | OK         | OK                    | OK                     | 
| edit_asset.html (collapsed and un-collpased sections) | OK        | OK      | OK        | OK          | OK             | OK             | OK       | OK    | OK         | OK                    | OK                     | 
| admin.html (collapsed and un-collpased sections)      | OK        | OK      | OK        | OK          | OK             | OK             | OK       | OK    | OK         | OK                    | OK                     | 


__Manual Testing__

The following test were performed manually.

|    Feature        |   Test Action                                                                         |   Expected Result                                |  Chrome (Desktop) |  Firefox (Desktop)  | Chrome (Mobile) |
| ----------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------ | ----------------- | ------------------- | --------------- |
| Data Sorter       | Select 'Sort by' option, 'Apply Filter', Repeat for all 'Sort by' options.            | Data is sorted appropritely                      | OK                | OK                  | OK              |
| Keyword Search    | 'Clear Filter', enter 'an cnoc' into 'Search' box, 'Apply Filter'                     | Returns asset 'An Cnoc'                          | OK                | OK                  | OK              |
| Tick Box Filter   | 'Clear Filter', select 'Connected' under Status and 'Wind' under Type, 'Apply Filter' | Returns list of all connected wind assets        | OK                | OK                  | OK              |
| MEC Range Filter  | 'Clear Filter', enter range 'from' 250 'to' 350, 'Apply Filter'                       | Returns assets with 250 < MEC < 350              | OK                | OK                  | OK              |    
| MEC Range Filter  | 'Clear Filter', enter range 'from' 250 'to' 350, 'Apply Filter'                       | Returns assets with 250 < MEC < 350              | OK                | OK                  | OK              |    
| Company Login     | Click 'Login', enter 'esb', click 'Login'                                             | Returns index.html filtered for ESB owned assets, 'Welcome ESB' top right, 'Update Details' visible in assets dropdown | OK                | OK                  | OK              | 
| Update Asset      | Expand  'Aghada 1', 'Update Details', change Ireland to IRE, 'Save Changes'           | Details in index now show IRE                    | OK                | OK                  | OK              |    
| Log Out           | Click 'Log Out'                                                                       | Reloads index.html, logged out                   | OK                | OK                  | OK              |    
| Unknown Login     | Click 'Login', enter 'abc', click 'Login'                                             | Error 'That is not a valid username.' displayed  | OK                | OK                  | OK              |    
| Admin Login       | Enter 'admin', click 'Login'                                                          | Returns index.html, 'Admin' menu tab visible     | OK                | OK                  | OK              |    
| New Asset         | Click 'Admin', enter asset name 'abc' details, 'Add Asset'                            | Returns admin.html, asset 'abc' included in index.html | OK                | OK                  | OK              |    
| Backup Database   | Enter 'Admin', click 'Backup'                                                         | New .json file in local directory                | OK                | OK                  | OK              |    
| Delete Asset      | Enter index.html, expand asset 'abc', click 'Update Asset', click 'Delete Asset'      | Returns index.html, 'abc' no longer included     | OK                | OK                  | OK              |    
| Database Fallback | Enter 'Admin', select most recent .json file, click 'Fallback'                        | Returns admin.html, asset 'abc' can be seen again in index.html, new .json file in local directory. Returns index.html, 'abc' no longer included     | OK                | OK                  | OK              |   



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




