rf_api_key = 'pmYGAawja0bc61QUy0rH'
project_id = 'hts-uki6g'
model_name = 'hts-uki6g/1'

from PIL import Image
Image.MAX_IMAGE_PIXELS = None
import roboflow

rf = roboflow.Roboflow(api_key=rf_api_key)

project = rf.workspace().project(project_id)
model = project.version(1).model

print (model)
# # predict on a local image
prediction = model.predict('..//images/data/images/Akins HS.png', confidence=.19)

print (prediction.json())
# from inference import get_model
# import supervision as sv
# import cv2

# # define the image url to use for inference
# import os

# image_file = "..//images/data/images/Akins HS.png"
# image = cv2.imread(image_file)

# # load a pre-trained yolov8n model
# model = get_model(model_id=model_name)

# # run inference on our chosen image, image can be a url, a numpy array, a PIL image, etc.
# print ('inferinng')
# results = model.infer(image)[0]
# print (results)
# load the results into the supervision Detections api
# detections = sv.Detections.from_inference(results)

# # create supervision annotators
# bounding_box_annotator = sv.BoxAnnotator()
# label_annotator = sv.LabelAnnotator()

# # annotate the image with our inference results
# annotated_image = bounding_box_annotator.annotate(
#     scene=image, detections=detections)
# annotated_image = label_annotator.annotate(
#     scene=annotated_image, detections=detections)

# # display the image
# sv.plot_image(annotated_image)