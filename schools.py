import os
import numpy as np
import leafmap

def generate_tif_files(gdf, schools_folder):
    bbox_scaler = np.array([-0.00326218, -0.0018414 ,  0.00233782,  0.0020586 ])
    for i, school in gdf.iterrows():
        tif_filename = f'{school["School Name"]}.tif'
        center = school.geometry.centroid.coords[0]

        bbox = (np.array(bbox_scaler) + np.repeat(np.array(center).reshape(1,2), 2, axis=0).flatten()).tolist()
        leafmap.map_tiles_to_geotiff(
            output=os.path.join(schools_folder, tif_filename), bbox=bbox, resolution=.03, source="Satellite", overwrite=True
        )