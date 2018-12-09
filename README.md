Data Centric Development: Irish Energy Assets Database
=========================================================
This is the Milestone Project for the Data Centric Development module for the Code Institutes Diploma in Software Development.
The project displays clear understanding and capabilities in developing a data centric web application using the Flask Python framework to interact with a Mongo database.
The application was enhanced with JavaScript data visualizations and Bootstrap CSS styling.

Time was spent developing this project to best utilize data centric skills when applied to my key area of professional experience, the Energy Industry.

Irish-Energy-Assets application gives exploratory and CRUD access to a Mongo database comprising of all connected and contracted generation assets on the Irish national electrical grid.
It includes assets on the transmission network, operated by Eirgrid, and distribution network, operated by ESB Networks.

Technologies Used
-----------------------
* __VisualStudios2017__ (https://visualstudio.microsoft.com/downloads/) IDE was used in the development of the project.
* __VirtualEnvironment__ (https://docs.python.org/3/library/venv.html) was used to wrap the project.
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
    - __Bootstrap Grid__ system was used for content arrangement and responsive behavior when moving between different screen sizes
    - __Bootstrap Navbar__ was used for the main navigation. Collapsible menu was utilized for lower screen resolutions.
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
The application was developed as a tool to be managed by a system operator. 
The public could visit the site to get information on the generator assets around them, asset developers could see where there is saturation in the grid,
 asset owners could update any changes they have made to let the system operator keep track. As this is a technical application, the ‘programmer-esk’ dark background and color scheme was used.
The application was designed presuming it would be primarily accessed using a desktop computer but mobile capabilities would be valuable.

__User Stories__

User stories were developed to plan out the features for the application.

* As a site visitor I should be given an introduction and a guide to what the application is.
* As a site visitor I should be able to see all energy assets in the DB including their attributes.
* As a site visitor I should be able filter the results and search for keywords.
* As a site visitor I should be able to see graphical visualizations of the data for greater comprehension.
* As a site visitor I should be able to sign in as admin or as a user. The user will be a company that owns and energy asset.
* As admin I should have full CRUD access to all the assets.
* As non-admin logged in user I should be able to create a new asset and have update and delete access to all of my owned assets.
* As admin I should be able to backup up the current data to a json file stored in a local directory.
* As admin I should be able to fallback to previous backup database.

Features and Process
-----------------

__Existing Features__


* __Data Collection__ of asset details publicly available in PDF format from ESB and Eirgrid websites.
* __Data Formatting__ using Tabula.py to convert .pdf files to .csv format, which were then converted to .json using www.csvjson.com/csv2json.
* __MongoDB Creation__ by developing script to bulk import the .json data files.
* __Scrollable Data Display__ in index.html 'Assets List' section in tabular format, showing primary asset details (Name, Type and MEC). The table is scrollable rather than paginated as it would be more user friendly.
* __Accordion Collapse__ style dropdown shows further asset details when clicking on the primary line item. Additional details included details on the assets
connected network, when the asset was first added to the database and when it was last updated.
* __Geocoding__ was performed using GeoPy.py to assign full addresses to each Node by searching for 'Node Name' + 'Ireland'.
* __Data Filter__ scripts were written taking in filter parameters set in 'Refine Filter' side-nav. Next to each filter option the number of documents to that will be returned and sum of their MEC is displayed.
    - __Apply Filter Button__  reloads the page with filtered data based on filter parameters and selected sort arrangement.
    - __Reset Filter Button__ clears the parameters set in the filter side-nav since the last page load. Does not change the data currently displayed.
    - __Clear Filter Button__  reloads the page with no filters applied.
    - __Keyword Search__ loops through all document attributes and returns, subset where the keyword is found in values. This is not case sensitive.
    - __Tick Box Selectors__ for Status, SystemOperator, Types, Node and County attributes set list of value arguments for returning the subset. If no box from a section is ticked, then no filter for that attribute is imposed. 
    If a box is ticked in a section than only the values ticked will be displayed.
    - __Range Filter__ for MEC sets the range of MEC values to return.
* __Data Sorter__ sorts data alphabetically (A-Z) by asset 'Name' by default. This can be changed by selecting one of the 6 options from the 'Sort by' dropdown in the 'Refine Filter' section.
    - Name (A - Z)
    - Name (Z - A)
    - Type (A - Z)
    - Type (Z - A)
    - MEC (Low - High)
    - MEC (High - Low)
* __Interactive Charts__ display the database data. Three charts show the MEC distribution across Types, Counties and Status. Hovering the mouse over a segment displays the segments key, its percentage of the overall MEC and the value of its MEC.
* __About Site__ page gives information on the purpose of the site, how to use the site, how the electrical grid is organized, where the data came from and a glossary of terms and abbreviations used.
* __User Login__ for logging in as 'admin' or a company that owns one of the assets. Accessed by entering the login page from login button on top right of the page. Logging as a company gives you edit and delete database access to their assets. Login in as 'admin' gives full CRUD access to the database.
* __User Validation__ if user enters a name that is not on the list of company names, they are receive an erro message and asked to enter a valid company name.
* __Updating Document__ can be performed once logged in, by clicking 'Update Asset' link, located in the 'Data Details' section in the dropdown for that asset. This is only visible when you have access to the document. This opens edit_asset.html to edit the asset.
* __Deleting Document__ can be performed from the edit_asset.html page by clicking 'Delete Asset' button.
* __Creating Document__ to add to the database can only be performed by the admin. To add a document the admin must enter the 'Admin' page by clicking the menu option, only visible when logged in as 'admin'. Here the 'admin' can enter the new asset details.
Note: for the type section there is an option to select 'Other' and then enter the type under sub-type to allow for new technologies to be added to the system.
* __Database Backup__ can be performed from the 'Admin' page by clicking the 'Backup' button. This writes the MongoDB collection, less the object _ID, to a .json file in the websites directory. The backups are timestamped.
* __Database Fallback__ to a backup .json can be performed by selecting one of the backups in the directory and clicking 'Fallback' button. Before the collection is cleared, a backup is automatically created to avoid loss of data.
* __Responsive Design__ collapses and rearranges sections based on importance as the screen changes sizes. Dropdown indicators change to indicate what state the relevant collapse is in.
* __Data Analysis__ in the about page explains some of the insights that can be taken from the data.
* __Glossary__ of technical terms and abbreviations included in the about page.

__Future Development__

* __Change Log__ Record any changes made to the collection in a change log recording the change, timestamp, and who made the change.
* __Continued Filter Refining__ Currently the filter parameters set act out on the whole of the collections documents, past filters should be transferred on for further filter refining. This will most likely require AJAX or passing the filter parameters as a URL Query String.
* __Collapse Icon__ Currently the collapse in or out icons only change once active, they do not reflect the initial state on page load, and in the filter side-nav all icons are not independent. This will be solved with greater understanding of the DOM to be covered in the JavaScript module.
* __Filter Asset List using crossfilter.js__ Filters across the d3 charts should be reflected in the assets list shown. To be used instead of refine filter side-nav. ".top(Infinity)" will probably be used to make this work.                                            
* __Admin Confirmation__ Any non-admin changes to the collection should require confirmation from the admin before being applied to the database.

Testing
-----------------------

__Code Validation__

* __Python__ was validated using http://pep8online.com/. Both run.py and test_app.py are pep8 compliant.
* __HTML__ was validated using https://validator.w3.org/. Due to the python code embedded in the HTML templates there were a number of errors.
* __CSS__ was validated using https://jigsaw.w3.org/css-validator/. No errors were found.
* __Spelling and Grammar__ was validated using Google Docs.

__Unittest Automated Testing__

Throughout the development of this project a 'Test After' approach was taken. After deciding what was needed, the function was written, manually tested 
while developing. Once a basic function was built, an automated test was written in test_app.py using unittest testing framework for each of the possible conditions.
As functions became more complex and interacted with other functions, these automated tests insured that the functions all maintained their required functionality. 
8 functions were tested in this manner. 

The testing code can be found: https://github.com/dcasey720/irish_energy_assets/blob/master/test_app.py

__Visual Testing__

The dev tool within Firefox Development Edition was used to test that the pages were displaying correctly (alignment, spacing, position etc.) across different screen widths.


|                                                       | Galaxy S5 | Pixel 2 | Pixel 2XL | iPhone 5/SE |	iPhone 6/7/8 | iPhone 6/7/8 + | iPhone X | iPad  | iPad Pro   | Responsive 1366 x 768 | Responsive 1680 x 1050 |  
| ----------------------------------------------------- | --------- | ------- | --------- | ----------- | -------------- | -------------- | -------- | ------| ---------- | --------------------- | ---------------------- |
| index.html (collapsed and un-collapsed sections)      | OK        | OK      | OK        | OK          | OK             | OK             | OK       | OK    | OK         | OK                    | OK                     |                 
| about.html (collapsed and un-collapsed sections)      | OK        | OK      | OK        | OK          | OK             | OK             | OK       | OK    | OK         | OK                    | OK                     | 
| login.html                                            | OK        | OK      | OK        | OK          | OK             | OK             | OK       | OK    | OK         | OK                    | OK                     | 
| edit_asset.html (collapsed and un-collapsed sections) | OK        | OK      | OK        | OK          | OK             | OK             | OK       | OK    | OK         | OK                    | OK                     | 
| admin.html (collapsed and un-collapsed sections)      | OK        | OK      | OK        | OK          | OK             | OK             | OK       | OK    | OK         | OK                    | OK                     | 


__Manual Testing__

The following test were performed manually.

|    Feature            |   Test Action                                                                             |   Expected Result                                |  Chrome (Desktop) |  Firefox (Desktop)  | Chrome (Mobile) |
| --------------------- | ------------------------------------------------------------------------------------------| ------------------------------------------------ | ----------------- | ------------------- | --------------- |
| __Data Sorter__       | Select 'Sort by' option -> 'Apply Filter' -> repeat for all 'Sort by' options.            | Data is sorted appropriately                      | OK                | OK                  | OK              |
| __Keyword Search__    | 'Clear Filter' -> enter 'an cnoc' into 'Search' box -> 'Apply Filter'                     | Returns asset 'An Cnoc'                          | OK                | OK                  | OK              |
| __Tick Box Filter__   | 'Clear Filter' -> select 'Connected' under Status and 'Wind' under Type -> 'Apply Filter' | Returns list of all connected wind assets        | OK                | OK                  | OK              |
| __MEC Range Filter__  | 'Clear Filter' -> enter range 'from' 250 'to' 350 -> 'Apply Filter'                       | Returns 7 assets with 250 < MEC < 350            | OK                | OK                  | OK              |    
| __Company Login__     | Click 'Login' -> enter 'esb' -> click 'Login'                                             | Returns index.html 'Welcome ESB' top right       | OK                | OK                  | OK              |                                                                          
| __Only Access Your Assets__ | Expand 'AMETS'                                                                      | 'Update Details' button hidden                   | OK                | OK                  | OK              |
| __Access Your Assets__ | Select 'ESB' in Company Filter -> 'Apply Filter' -> Expand  'Aghada 1'                   | 'Update Details' button visible                  | OK                | OK                  | OK              |
| __Update Asset__      | Expand  'Aghada 1' -> 'Update Details' -> change Ireland to IRE -> 'Save Changes'         | Details in index now show IRE                    | OK                | OK                  | OK              |    
| __Log Out__           | Click 'Log Out'                                                                           | Reloads index.html, logged out                   | OK                | OK                  | OK              |    
| __Unknown Login__     | Click 'Login' -> enter 'abc' -> click 'Login'                                             | Error 'That is not a valid username.' displayed  | OK                | OK                  | OK              |    
| __Admin Login__       | Enter 'admin', click 'Login'                                                              | Returns index.html, 'Admin' menu tab visible     | OK                | OK                  | OK              |    
| __New Asset__         | Click 'Admin' -> enter Asset Name = 'abc', Max Export Capacity = 10  -> 'Add Asset' | Returns admin.html, 'Abc' included in index.html | OK                | OK                  | OK              |    
| __Backup Database__   | Enter 'Admin' -> click 'Backup'                                                           | New .json file in local directory                | OK                | OK                  | OK              |    
| __Delete Asset__      | Enter index.html -> expand asset 'Abc' -> click 'Update Asset' -> click 'Delete Asset'    | Returns index.html, 'Abc' no longer included     | OK                | OK                  | OK              |    
| __Database Fallback__ | Enter 'Admin' -> select most recent .json file -> click 'Fallback'                        | Returns admin.html, asset 'Abc' can be seen again in index.html, new .json file in local directory. | OK                | OK                  | OK              |   
| __Remains Logged In__ | Click 'About Site' -> Click 'Assets'                                                      | Return about.html with 'Welcome ESB' -> Returns index.html 'Welcome ESB' top right | OK                | OK                  | OK              | 

__Known Bugs__

* Can log in as any name if entering url directly i.e. http://irish-energy-assets.herokuapp.com/somename/ will return index.html logged in as 'somename'. This is outside of normal operation of the site. Deeper understanding of String Querries should resolve this.
* Dropdown icons do not represent initial state of collapsed div. Dropdown icons are not independent of each other in Refine Filter side-nav.
* Stacked Bar Chart 'MEC (MW) by Status' shading is off when isolating data.
* Charts do not align to the centre of the the divs.
* Navbar collapse in, renders slightly below header border before jumping to it desired position.
* Can not refine filter, this will probably require passing the filters as String Querries.
* Application is slow at loading data, this is probably due to the number of loops and querries to the MongoDB. 


Development
------------------------
Visual Studios 2017 was used in the development of this project. I moved away from using the online Cloud9 IDE as I was having issues with Python versions,
when working with pip installed packages. By moving my development onto my local machine, I have more control over the installed packages and can explore their folder
structures more easily. Sublime text editor as played with for a while but found Visual Studios much more featured and informative when developing.

This did require considerable more learning to manage my development on a Windows machine rather than on a Linux.
A number of packages needed to be downloaded, alternative windows commands needed to be used and System Variables set.
Although time consuming, I felt this was time well spent and has given me a greater understanding on the Windows 10 system.

Virtual Environment was used as a wrapper to keep the project requirements separate from the rest of the machine. As there was a lot of experimenting with this project,
a number of different projects were created, copied, deleted and edited. Utilizing the virtual environment made this an easy exercise and has left my final project much cleaner
than what would have been.

The data for the database was scraped from publicly available PDFs from the respectful system operators websites, converted to csv using Tabula.py, organized initially using Excel,
converted to json using an online tool, combined and added to the MongoDB database. Care was taken to gather up to date accurate data for the different assets.
The data from the different operators was not standardized and so there was much digging required to acquire common data across all the assets.

As the data came from a number of different sources, mostly in PDF, and in different layouts there was considerable manipulation required to combine and format the data in a
usable format. GeoPy was used to get the address of the node based off the Node name, so that a per county association could be established. 
I have kept the code and data not used by the running application but used in the development process in a separate folder, Dev Folder. 
Certain elements such as deleting of assets from the database require additional expanding of sections so that a user is less likely to activate the function by accident.
The login and database editing functions were purposely not obvious to the user, with the principle that a user that should be editing the database should have working knowledge of the application.

Mock ups can be found at https://github.com/dcasey720/irish_energy_assets/tree/master/dev_assets/mockups

Most of this project was completed before looking at the Interactive Frontend Modules. JavaScript was only looked into briefly to get the interactive charts working.

Deployment
------------------------

__Hosting__

The application is hosted on Heroku and can be accessed at:

https://irish-energy-assets.herokuapp.com/

A Procfile is required by Heroku to know what language to launch the application as. 
In Heroku the config variables were set:

IP: 0.0.0.0  
Port: 5000

__Requirements__

The requirements for running the app can be found at:
https://github.com/dcasey720/irish_energy_assets/blob/master/requirements.txt

__Deployed vs Development__

For the applied app, the 'dev_assets' has been removed. It has been left in the Github repository for proof of development work. It can be found at:
https://github.com/dcasey720/irish_energy_assets/tree/master/dev_assets

For the running app.py code the following differences exist between development and deployed.

|       Code       | Deployed | Development |
| ---------------- | -------- | ----------- | 
| app.run(debug= ) |  False   |   True      |       

Running App
------------------------

https://irish-energy-assets.herokuapp.com/

