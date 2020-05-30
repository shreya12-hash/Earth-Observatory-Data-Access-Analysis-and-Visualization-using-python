##What is NAIP?

The National Agriculture Imagery Program (NAIP) acquires aerial imagery during the agricultural growing seasons in the continental U.S. A primary goal of the NAIP program is to make digital ortho photography available to governmental agencies and the public within a year of acquisition.
NAIP is a great source of high resolution imagery across the United States. NAIP imagery is often collected with just a red, green and Blue band. However, some flights include a near infrared band which is very useful for quantifying vegetation cover and health
One last step before we can search and download sentinel 2 images is to create a footprint from the nReservegeometry. Here I've used Shapely Python library since our data is in Shapefiles and read it already as Geopandas GeodataFrame. (Now one thing if we have Geojson data, Sentinelsat provides a handy way to convert our data into a proper format in the query).

###Open NAIP Data in Python
