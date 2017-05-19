# GeoPython-Workshop
For the GeoPython Workshop, Easy Programming QGIS with Python for Expression Functions. 

## Custom Python Expression Functions in QGIS
  Expression functions give us the power to automate tasks, perform calculations on the available data, and custom select and label features in QGIS. During this workshop we will use expression functions to customize tasks like the following and discover how this opens up various new possibilities of what can be achieved using this open source GIS application.
  * Feature selection
  * Feature labeling
  * Field calculation
  
## Getting started

1. Download and install QGIS 2.18 ([Link to the download page](http://www.qgis.org/en/site/forusers/download.html)).
2. Get some sample data:
    * The [Populated Places (Simple)](http://www.naturalearthdata.com/downloads/50m-cultural-vectors/50m-populated-places/) dataset containing various city and town points from Natural Earth.
    * The [Uster](https://drive.google.com/file/d/0B6XgCRKKPmwzMWRTcFR6SzJNZkU/view?usp=sharing) geopackage containing several vector layers of Openstreetmap data downloaded from [OSMaxx](https://osmaxx.hsr.ch/).   
3. Start up QGIS 2.18 and we're ready!

**Notes:**
  * This repository contains some expression functions that we will use during the workshop. You can save them to `%userprofile%/.qgis2/python/expressions`.
  * For QGIS 2.14 users, please see the section **Notes for QGIS 2.14** below. 


## Things to Note About Custom Python Expression Functions in QGIS

* Custom expression funcions must be preceded by the *@qgsfunction* decorator.
* The function must receive *feature* and *parent* as its last two parameters.
* The feature attributes that we intend to use within the function must be specified as 'referenced_columns' in the @qgsfunction decorator.

**Syntax:**

  ```python
      @qgsfunction(args='auto', group='Custom', referenced_columns=['column_name'])
      def function_name(input_value, feature, parent):
          # Statements to be executed 
          return return_value
  ```

## Task 1. Feature Selection with Expression Functions 
  
  - **Dataset used:** Populated Places
  - **Objective:** Write expression functions to select features based on values computed using their attributes.
  - **Functions:** is_populous_capital() and get_utm_zone() 
  
### Task 1.1. Selecting all capital cities with a population greater than a user defined number.

  1. Load the vector layer. *Layer -> Add Layer -> Add Vector Layer -> Browse to the directory and select populated_places_simple file*.
  2. View the attribute table as *Layer -> Open Attribute Table* or by clicking on the *Attribute Table* button in the Attribute bar.
  3. Open the *Select by Expression dialog box* either by clicking on the *Select by Expression* button on the Attributes toolbar or by
    *View -> Select -> Select by Expression*.
  4. In the Function Editor tab create a new file and write a custom python expression function as:
   
   
  ```python
  @qgsfunction(args='auto', group='Custom', referenced_columns=['featurecla', 'pop_max'])
  def is_populous_capital(input_pop, feature, parent):
    is_capital = feature['featurecla'] == 'Admin-0 capital'
    is_populous = feature['pop_max'] > input_pop
    return is_capital and is_populous
  ```
    
  5. Click on *Load*.
  6. In the Expression Engine tab, call your function as `is_populous_capital(500000)`.
  7. Done! Now you can view the selected features on the layer and in the attribute table.

### Task 1.2. Selecting Features based on the value of their calculated [UTM Zone](http://www.dmap.co.uk/utmworld.htm).
  
  1. Please find the code in *get_utm_zone.py*.
  2. Note how we can get the feature's geometry, latitude and longitude using the built-in methods provided by the QGIS Python API. ([Link](http://geoapis.sourcepole.com/qgispyapi/) to the documentation).
  3. Select the features lying within a given UTM zone by calling the function as `get_utm_zone() = '45N'`.  

## Task 2. Feature Labeling and Displaying Map Tips with Expression Functions 

  - **Dataset used:** Populated Places
  - **Objective:** Write expression functions to label features based on values computed using their attributes.
  - **Functions:** get_population_rank() and get_utm_zone()  
  
### Task 2.1. Labeling all the points as 'City_Name: Population_Rank'.  
 
 1. Open the *Layer Properties Dialog Box* by double clicking the layer in the Layers Panel or *Right click on the layer in the Layers Panel -> Properties*.
 2. Enable the labels by navigating to Layers and selecting *Show labels for this layer*.
 3. Load and call the function `get_population_rank()` in the Expression tab.
 4. Click *OK* to apply the changes and close the dialog box.
 5. Done! The map will now display the labeled features.
 6. Select *No labels* in the Layer Labeling Settings to disable the labels.

### Task 2.2. Displaying Map Tips as 'City_Name, UTM_Zone: Population_Rank'.
  
  1. Open Layer Properties and select *Display*.
  2. Select the *HTML* radio button and click on *Insert expression*.
  3. In the Insert Expression Dialog box, call the `get_utm_zone()` function.
  4. Similarly, call the `get_population_rank()` function.
  5. Enable Map Tips through the Attributes toolbar or *View -> Map Tips*
  6. Now you will see a map tip on hovering the mouse over the feature. 

## Task 3. Field Calculation with Expression Functions 

  - **Dataset used:** Populated Places
  - **Objective:** Write an expression function for reverse geocoding, i.e. get the address of each feature given its coordinates and store this address as a  new column in the attribute table.
  - **Functions:** get_address()
  
### Task 3.1. Creating a new layer with a subset of all the features.

  1. We will select a subset of features to get the address of. We can do this with a simple selection expression. For example, select all capital cities with a population greater than 10 million.  
      ```python
       is_populous_capital(10000000)
      ```
  2. Create a new layer containing only these selected points. Right click on the layer in the Layers planel and select *Save As*.
  3. Keeping all fields as default, browse to the directory where you want to save the file and give it a name.
  4. Under *Encoding*, check the *Save only selected features* checkbox.
  5. On clicking *OK* your new layer will be automatically added to the current project.
  6. On the Layers Panel, uncheck the populated places layer to view only the new layer. 


### Task 3.2. Write an expression function to calculate a new 'address' field.

 1. Nominatim is the search engine used in Openstreetmap data. We will be using Nominatim's [reverse geocoding API](http://wiki.openstreetmap.org/wiki/Nominatim#Reverse_Geocoding) to get the address of a point given its latitude and longitude.
 2. Open the Field Calculator by clicking on the *Field Calculator* button in the attributes toolbar. 
 3. Note that in the function get_address(), we make an API request, passing the latitude and longitude, as well as some more data in accordance with the API's usage policy.
 4. In the Field Calculator, enter the *Output field name* as 'address'.
 5. Change the *Output Field Type* to 'Text (string)'.
 6. Enter a value for the *Output Field Length*, say '100'.
 7. Call the function get_address() from within the Expression engine.
 8. The function might take a while to execute, when done, open the Attribute Table.
 9. A new column named 'address' containing the address for each feature will have been added to the attribute table.
 

## Recap and Working with OSM Data

  - **Dataset used:** Uster
  - **Objective:** Recap of what we have learnt to select all the restaurants in Uster and label them with their addresses.
  - **Functions:** hstore_contains_key_value() and hstore_get_value()
  
### Filtering out all the restaurant points.

  1. Right click on the layer *uster_address_p* and click on *Filter*.
  2. In the *Query Builder* dialog box, under *Provider specific filter expression*, emter the expression as:
  ```python
     "tags" LIKE '%"amenity"=>"restaurant"%'
 ```
  3. Click on *OK*. Only the restaurants will now be visible on the map.

### Labeling the restaurants as 'Name, address'.

 1. Go to *Layer Properties -> Labels* or click on the *Layer labeling Options* in the Labels toolbar.
 2. Select *Show labels for this layer*.
 3. Click on the *Expression* button to open the *Expression dialog*.
 4. Write an expression using the hstore_get_value() function as:
  ```
     hstore_get_value('name')  || ', '  || hstore_get_value('addr:street') || ' '  || hstore_get_value('addr:housenumber')
  ```
  5. The label styles and colours can be changed in the *Layer Styling* panel.  

## Notes for QGIS 2.14

In QGIS 2.18, any feature attributes/columns that we use within the function must be specified as 'referenced_columns' in the @qgsfunction decorator. This is optional in QGIS 2.14. The latest release of QGIS only fetches the data we explicitly specify as required, in order to optimize the performance. So, for example, the function below when called as `is_populous_capital(100000)` would work perfectly in QGIS 2.14, but would fail to select any features in 2.18.

  ```python
    @qgsfunction(args='auto', group='Custom')
    def is_populous_capital(input_pop, feature, parent):
      is_capital = feature['featurecla'] == 'Admin-0 capital'
      is_populated = feature['pop_max'] > input_pop
      return is_capital and is_populated
  ```
  
## Bonus Material

**nullif('argument_1', argument_2')**

Returns a None/NULL value if argument_1 is equal to argument_2, otherwise it returns argument_1 (SQL alike).

```
For example, 

  ```python
    nullif('hello world','')
  ```
  
The expression function above will return 'hello world'. A good use case would be to use this function with the in-built coalesce in an expression like the following.

  ```python
    coalesce(nullif("name",''), nullif("name_en",''), 'unknown')
  ```

Where "name" and "name_en" are field names (note the double quotes). This would return the 'name' if it is not an empty string, 'name_en' if the 'name' is empty and 'unknown' if both the 'name' and 'name_en' are empty.


**jitter_geometry('max_offset_percent', 'segment_length_percent')**

This function creates a jittered geometry from a linestring or polygon geometry. Given the maximum offset and segment length as percentages, it first interpolates points on the linestring or polygon boundary at the segments. Then it displaces the point perpendicular to the linestring or polygon boundary by a random distance less than or equal to the maximum offset. Finally it joins all these displaced points and returns a jittered geometry.

To use this function:   

1. Go to Layer Properties -> Style -> Click on the green *Plus* button to *Add a Symbol layer*.
2. Set the *Symbol layer type* as *Geometry generator*.
3. Set the *Geometry Type* as *LineString/MultiLineString* for linestrings or *Polygon/Multipolygon* for polygons.
4. *Load* the *jitter_geometry.py* file in the Function Editor.
5. In the Expression Tab, call the function as:

  ```python
    jitter_geometry(5, 20)
  ```
Where '5' and '20' are the maximum_offset_percent and segment_length_percent respectively. These values can range between 1 and 99.

6. On clicking 'OK' the jittered geometries will be displayed on the layer.
