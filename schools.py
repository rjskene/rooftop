import os
import numpy as np
import leafmap
from PIL import Image
from tqdm.auto import tqdm

def generate_tif_files(gdf, schools_folder, resolution=.03):
    bbox_scaler = np.array([-0.00326218, -0.0018414 ,  0.00233782,  0.0020586 ])
    pbar = tqdm(gdf.iterrows(), total=len(gdf))
    for i, school in pbar:
        pbar.set_description(f'Processing {school["School Name"]}')

        tif_filename = f'{school["School Name"]}.tif'
        center = school.geometry.centroid.coords[0]
        bbox = (np.array(bbox_scaler) + np.repeat(np.array(center).reshape(1,2), 2, axis=0).flatten()).tolist()
        leafmap.map_tiles_to_geotiff(
            output=os.path.join(schools_folder, tif_filename), bbox=bbox, resolution=resolution, source="Satellite", overwrite=True
        )

def tif_to_png(file_path, tif_file):
    tiff_image = Image.open(os.path.join(file_path, tif_file))
    jpeg_image = tiff_image.convert('RGB')
    jpeg_image.save(os.path.join(file_path, tif_file.replace('.tif', '.png')))