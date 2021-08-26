import io
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'service_account_key'  # just paste the path for json file downloaded from gcp project

from google.cloud import  videointelligence
client = videointelligence.VideoIntelligenceServiceClient()

video_path = 'googlecloudfileuri'  # paste the path of file uploaded on google cloud's bucket

features = [videointelligence.Feature.LABEL_DETECTION]

operation = client.annotate_video(video_path, features = features)

result = operation.result(timeout=300)

print(result)

# def detect_faces(local_file_path = gs_uri):
#     client = videointelligence.VideoIntelligenceServiceClient()

#     with io.open(local_file_path, 'rb') as f:
#         input_content = f.read()

#     config = videointelligence.FaceDetectionConfig(include_bounding_boxes = True, include_attributes = True)

#     context = videointelligence.VideoContext(face_detection_config = config)

#     operation = client.annotate_video(
#         request = {
#             "features": [videointelligence.Feature.FACE_DETECTION],
#             "input_content": input_content,
#             "video_context": context,
#         }
#     )

#     print("\nProcessing video for face detection")

#     result = operation.result(timeout=300)
#     print("finished processing. \n")

#     annotation_result = result.annotation_result[0]

#     for annotation in annotation_result.face_detection_annotations:
#         print("Face detected")
#         for track in annotation.tracks:
#             print("Segment: {}s to {}s".format(
#                 track.segment.start_time_offset.seconds +
#                 track.segment.start_time_offset.microseconds / 1e6,
#                 track.segment.end_time_offset.seconds +
#                 track.segment.end_time_offset.microseconds/1e6,
#                 )
#             )
#             # Each segment includes timestamped faces that include
#             # characteristics of the face detected.
#             # Grab the first timestamped face
#             timestamped_object = track.timestamped_objects[0]
#             box = timestamped_object.normalized_bounding_box
#             print("Bounding box:")
#             print("\tleft  : {}".format(box.left))
#             print("\ttop   : {}".format(box.top))
#             print("\tright : {}".format(box.right))
#             print("\tbottom: {}".format(box.bottom))

#             # Attributes include glasses, headwear, smiling, direction of gaze
#             print("Attributes:")
#             for attribute in timestamped_object.attributes:
#                 print(
#                     "\t{}:{} {}".format(
#                         attribute.name, attribute.value, attribute.confidence
#                     )
#                 )

# detect_faces()
