# GeoPython-Workshop
For the GeoPython Workshop, Easy Programming QGIS with Python for Expression Functions. 

## Custom Python Expression Functions in QGIS
  Expression functions in QGIS give us the power to automate tasks, perform calculations on the available data, and custom select and label features using Python. During this workshop we will discuss how we can write expression functions to customize the  tasks to meet our specific needs.   
  * Feature selection
  * Field calculation
  * Feature labeling
  * Displaying map tips
  
## Getting started

1. Download and install QGIS 2.18 ([Link to the download page](http://www.qgis.org/en/site/forusers/download.html)).
2. Get some sample data:
    * The [Populated Places (Simple)](http://www.naturalearthdata.com/downloads/50m-cultural-vectors/50m-populated-places/) dataset containing various city and town points from Natural Earth.
    * The [Uster]() geopackage containing several vector layers from Openstreetmap.   
3. Start up QGIS 2.18 and we're ready!

**Notes:**
  * This repository contains some expression functions that we will use during the workshop. You can either save them to `%userprofile%/.qgis2/python/expressions` or do a quick copy-paste as we go along.

  * For QGIS 2.14 users, please see the section **Notes for QGIS 2.14** below. 


## Things to Note About Custom Python Expression Functions in QGIS

* The modules `qgis.core` and `qgis.gui`.
* Expression functions are called iteratively for each feature on the layer.
* Expression funcions must be preceded by the `@qgsfunction` decorator.
* The function must receive `feature` and `parent` as its last two parameters.
* The feature's attributes can be accessed as `feature['attribute_name']`.
* The feature attributes that we intend to use within the function must be supplied as arguments to the function. This is a new addition to QGIS 2.18 in contrast to QGIS 2.14. The latest release of QGIS only fetches the data we explicitly specify as required, with the view of achieving better performance.      

**Syntax:**

  ```python
      from qgis.core import *
      from qgis.gui import *
      
      @qgsfunction(args='auto', group='Custom')
      def function_name(input_value, feature, parent):
          # Statements to be executed 
          return return_value
  ```

## Task 1. Feature Selection with Expression Functions 
  
  - **Dataset used:** Populated Places
  - **Objective:** Write expression functions to select features based their attribute values, or values computed using their attributes.
  - **Functions:** select_populated_capitals() and select_by_utm_zone() 

**Task 1.1: Selecting all capital cities with a population greater than a user defined number.**  
 
 1. Load the vector layer.  
    `Layer -> Add Layer -> Add Vector Layer -> Browse to the directory and select populated_places_simple file`
    
 2. View the attribute table as `Layer -> Open Attribute Table` or by clicking on the `Attribute Table` button in the Attribute bar.
 
 3. Open the `Select by Expression dialog box` either by clicking on the Select by Expression button on the Attributes toolbar or by
    `View -> Select -> Select by Expression`
    
 4. In the `Function Editor` tab create a new file and write your first custom python expression function as:
 
    ```python
    @qgsfunction(args=0, group='Populated places')
    def select_country_capitals(field1, feature, parent):
      is_capital = feature['featurecla'] == 'Admin-0 capital'
      return is_capital
    ```
    
  5. Click on `Load`.
  
  6. In the `Expression Engine` tab, call your function as `select_populated_capitals("featurecla")`.
  
  7. Done! Now you can view the selected features on the layer and in the attribute table.   

**Task 1.2: Selecting Features based on the value of their calculated [UTM Zone](http://www.dmap.co.uk/utmworld.htm)**.
  
  1. Please find the code in the function `calculate_utm_zone()` in `calculate-utm-zone.py`
  2. Calculate the centroid using the built in `geometry()` method.
  3. Calculate the latitude and l using the built in `geometry()` function *(or method)* provided in `qgis.core` *(check)*.
  4. Return the calculated UTM zone.
  5. Select the features lying within a given UTM zone by calling the function as:
     ```python
        select_by_utm_zone() = '45N'
     ```  

## Task 2. Feature Labeling and Displaying Map Tips with Expression Functions 

  - **Dataset used:** Populated Places
  - **Objective:** Write expression functions to label features based their attribute values, or values computed using their attributes.
  - **Functions:** get_population_variation() and get_utm_zone()  
  
**Task 2.1: Labeling all the points as 'City_Name: Population_Variation'.**  
 
 1. Open the `Layer Properties Dialog Box` by double clicking the layer in the Layers Panel or:  
    `Right click on the layer in the Layers Panel -> Properties`
    
 2. Enable the labels by navigating to Layers and selecting `Show labels for this layer`.
 
 3. Complete and load the code for `get_population_variation()`.
    
 4. Back in the Expression tab, call the `get_population_variation()` function.
    
 5. Click `OK` to apply the changes and close the dialog box.
  
 6. Done! The map will now display the labeled features.
 
 7. Select `No labels` in the Layer Labeling Settings to disable the labels.

**Task 2.2: Displaying Map Tips as 'City_Name: Population_Variation, UTM_Zone' when the mouse hovers over a feature**.
  
  1. Open Layer Properties and select `Display`.
  2. Select the `HTML` radio button and click on `Insert expression`.
  3. In the Insert Expression Dialog box, call the `get_population_variation()` function.
  4. Similarly, call the `get_utm_zone()` function.
  5. Enable Map Tips through the Attributes toolbar or *View -> Map Tips*
  6. Now you will see a map tip on hovering the mouse over the feature. 


## Task 3. Field Calculation with Expression Functions 

  - **Dataset used:** Populated Places
  - **Objective:** Write an expression function for reverse geocoding, i.e. get the address of each feature given its coordinates and store this address in the Attribute table.
  - **Functions:** get_address()  
  
**Task 3.1: Creating a new layer with a subset of all the features.**  
 
 1. Select a subset of features from the layer with a simple selection expression. For example, select all capital cities with a population rank of 14.
     ```python
        select_populated_capitals('10000000')
     ```
 
 2. Create a new layer containing only these selected points. Right click on the layer in the Layers planel and select `Save As`.
 3. Keeping all fields as default, just browse to the directory where you want to save the file and give it a name.
 4. Under `Encoding`, check the `Save only selected features` checkbox.
 5. On clicking `OK` your new layer will be automatically added to the current project.
 6. On the Layers Panel, uncheck the populated places layer to view only the new layer.  

**Task 3.2: Write an expression function to calculate a new 'address' field using Nominatim's reverse geocoding API.**

 1. Nominatim is the search engine used in Openstreetmap data. We will be using Nominatim's [reverse geocoding API](http://wiki.openstreetmap.org/wiki/Nominatim#Reverse_Geocoding) to get the address of a point given its latitude and longitude.
 2. We will select a subset of features to get the address of. Let's select all points with a population rank of 14. To do this, call the 
 3. 
 




# Notes for QGIS 2.14

When writing custom expression functions in QGIS 2.14, a few differences must be noted.

  In QGIS 2.18, we need to pass as arguments, any layer attributes that we intend to use in our expression function. However, this is not a requirement in QGIS 2.14. So the function `select_populated_capitals()` in QGIS 2.14 would look like the following. 

    ```python
    @qgsfunction(args='auto', group='Populated places')
    def select_populated_capitals(input_pop, feature, parent):
      is_capital = feature['featurecla'] == 'Admin-0 capital'
      is_populated = int(feature['pop_max']) > int(input_pop)
      return is_capital and is_populated
    ```
    
 We can call the function from the expression engine as: 
   
   ```python
    select_populated_capitals(input_pop, feature, parent):
   ```
