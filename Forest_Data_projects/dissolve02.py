import geopandas as gpd

# Read the shapefile
data = gpd.read_file('/Users/kawuli/Desktop/Forest_Data/Forest_Data/樹種界区_PairwiseDissolveAll.shp')

# Create a column for polygon area
data['Shape_Area'] = data.geometry.Shape_Area

# Find polygons smaller than 600m²
small_polygons = data[data['Shape_Area'] < 600]


# Function to find the largest neighboring polygon
def find_largest_neighbour(geometry):
    # Get all neighbors
    neighbors = data[~data.geometry.touches(geometry)]

    # Filter by area and sort by largest area
    neighbors = neighbors[neighbors['Shape_Area'] >= 600].sort_values(by='Shape_Area', ascending=False)

    # Return the largest neighbor's geometry if any
    if not neighbors.empty:
        return neighbors.iloc[0].geometry
    else:
        return None


# Dissolve small polygons into their largest neighboring polygons
for index, row in small_polygons.iterrows():
    largest_neighbor = find_largest_neighbour(row.geometry)
    if largest_neighbor is not None:
        data.loc[index, 'geometry'] = largest_neighbor
        data = data.drop(index)

# Save the modified shapefile
data.to_file('output_shapefile.shp')
