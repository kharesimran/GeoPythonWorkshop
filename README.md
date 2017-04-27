# GeoPython-Workshop
For the GeoPython Workshop, Easy Programming QGIS with Python for Expression Functions. 

## What can we accomplish with Custom Python Expression Functions in QGIS?
  Expression functions in QGIS give us the power to perform tasks like the following in a customized way suited to our specific needs.  
  * Feature selection
  * Field calculation
  * Feature labeling
  * Displaying map tips
  
## Getting started

1. Download and install QGIS 2.14/2.18 ([Link to the download page](http://www.qgis.org/en/site/forusers/download.html)).
2. Get some sample data:
    * The [Populated Places (Simple)](http://www.naturalearthdata.com/downloads/50m-cultural-vectors/50m-populated-places/) dataset containing various city and town points from Natural Earth.
    * The [Uster]() geopackage from Openstreetmap.   
3. Start up QGIS 2.18 and we're ready!

**Note:** This repository contains some incomplete code snippets which we will complete together during the workshop. You can either save them to `.qgis2/python/expressions` or do a quick copy-paste as we go along. 

## Things to Note About Custom Python Expression Functions in QGIS

* Import the modules `qgis.core` and `qgis.gui`. *(Find out why and which functions are using them)*
* Expression functions are called iteratively for each feature on the layer.
* Expression funcions must be preceded by the `@qgsfunction` decorator.
* The function must receive `feature` and `parent` as its last two parameters.
* The feature's attributes can be accessed as `feature['attribute_name]`. 

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
    ```Layer -> Add Layer -> Add Vector Layer -> Browse to the directory and select populated_places_simple file```
    
 2. View the attribute table as `Layer -> Open Attribute Table` or by clicking on the `Attribute Table` button in the Attribute bar.
 
 3. Open the `Select by Expression dialog box` either by clicking on the Select by Expression button on the Attributes toolbar or by
    ```View -> Select -> Select by Expression```
    
 4. In the `Function Editor` tab create a new file and write your first custom python expression function as:
 
    ```python
    @qgsfunction(args='auto', group='Populated places')
    def select_populated_capitals(input_pop, feature, parent):
      is_capital = feature['featurecla'] == 'Admin-0 capital'
      is_populated = int(feature['pop_max']) > int(input_pop)
      return is_capital and is_populated
    ```
    
  5. Click on `Load`.
  
  6. In the `Expression Engine` tab, call your function as `select_populated_capitals(input_pop)`.
  
  7. Done! Now you can view the selected features on the layer and in the attribute table.   

**Task 1.2: Selecting Features based on the value of their calculated [UTM Zone](http://www.dmap.co.uk/utmworld.htm)**.
  
  1. Please find the scaffolding code in the function `select_by_utm_zone()` in `Code-snippets-for-workshop/pp-select-features.py`
  2. Calculate the centroid using the built in `geometry()` function *(or method)* provided in `qgis.core` *(check)*.
  3. Calculate the centroid using the built in `geometry()` function *(or method)* provided in `qgis.core` *(check)*.
  4. Return the calculated UTM zone.
  5. Select the features lying within a given UTM zone by calling the function as:
     ```select_by_utm_zone() = '45N'```  

## Task 2. Feature Labeling and Displaying Map Tips with Expression Functions 

  - **Dataset used:** Populated Places
  - **Objective:** Write expression functions to label features based their attribute values, or values computed using their attributes.
  - **Functions:** get_population_variation() and get_utm_zone()  
  
**Task 2.1: Labeling all the points as 'City_Name: Population_Variation'.**  
 
 1. Open the `Layer Properties Dialog Box` by double clicking the layer in the Layers Panel or:  
    ```Right click on the layer in the Layers Panel -> Properties```
    
 2. Enable the labels by navigating to Layers and selecting `Show labels for this layer`.
 
 3. Complete and load the code for `get_population_variation()`.
    
 4. Back in the Expression tab, call the `get_population_variation()` function.
    
 5. Click `OK` to apply the changes and close the dialog box.
  
 6. Done! The map will now display the labeled features.
 
 7. Select `No labels` in the Layer Labeling Settings to disable the labels.

**Task 2.2: Displaying Map Tips as 'City_Name, UTM_Zone: Population_Variation' when the mouse hovers over a feature**.
  
  1. Open Layer Properties and select `Display`.
  2. Select the `HTML` radio button and click on `Insert expression`.  
