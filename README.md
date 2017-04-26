# GeoPython-Workshop
For the GeoPython Workshop, Easy Programming QGIS with Python for Expression Functions. 

## What can we accomplish with Custom Python Expression Functions in QGIS?
  Expression functions in QGIS give us the power to perform tasks like the following in a customized way suited to our specific needs.  
  * Feature selection
  * Field calculation
  * Feature labeling
  * Displaying map tips
  
## Getting started

1. Download and install QGIS 2.14/2.18. [Link to the download page](http://www.qgis.org/en/site/forusers/download.html)
1. Get some sample data:
    * The [Populated Places (Simple)](http://www.naturalearthdata.com/downloads/50m-cultural-vectors/50m-populated-places/) dataset from Natural Earth. This is a vector containing various city and town points in the world. 
    * The [Uster]() geopackage from Openstreetmap.
1. Start up QGIS 2.18 and we're ready!

## Task 1. Custom Select Features 
  
  - **Dataset used:** Populated Places
  - **Objective:** Write expression functions to select features based their attribute values, or values computed using their attributes. 

** Task 1.1: Select all capital cities with a population greater than a user defined number
 1. Load the vector layer.  
    ``` Layer -> Add Layer -> Add Vector Layer -> Browse to the directory and select populated_places_simple file```
 2. View the attribute table as `Layer -> Open Attribute Table´ or by clicking on the `Attribute Table` button in the Attribute bar.  
 3. Open the `Select by Expression dialog box` either by clicking on the Select by Expression button on the Attributes toolbar or by
    ``` View -> Select -> Select by Expression```
 4. In the `Function Editor` tab create a new file and write your first custom python expression function as:
    ```python
    @qgsfunction(args='auto', group='Populated places')
    def select_populated_capitals(input_pop, feature, parent):
        is_capital = feature['featurecla'] == 'Admin-0 capital'
        is_populated = int(feature['pop_max']) > int(input_pop)
        return is_capital and is_populated
        ```
  4. In the `Expression Engine` tab, call your function as `select_populated_capitals(input_pop)`  
  5. Done! View the selected features on the layer and in the attribute table.  
