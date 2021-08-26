import os

"""Detect text in a video stored on GCS."""
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'service_account_key'  # just paste the path for json file downloaded from gcp project

from google.cloud import videointelligence
client = videointelligence.VideoIntelligenceServiceClient()

video_path = 'googlecloudfileuri'  # paste the path uri of file uploaded on google cloud's bucket

video_client = videointelligence.VideoIntelligenceServiceClient()
features = [videointelligence.Feature.TEXT_DETECTION]



operation = video_client.annotate_video(
    request={"features": features, "input_uri": video_path}
)

print("\nProcessing video for text detection.")
result = operation.result(timeout=600)

# The first result is retrieved because a single video was processed.
annotation_result = result.annotation_results[0]

for text_annotation in annotation_result.text_annotations:
    print("\nText: {}".format(text_annotation.text))

    # Get the first text segment
    text_segment = text_annotation.segments[0]
    start_time = text_segment.segment.start_time_offset
    end_time = text_segment.segment.end_time_offset
    print(
        "start_time: {}, end_time: {}".format(
            start_time.seconds + start_time.microseconds * 1e-6,
            end_time.seconds + end_time.microseconds * 1e-6,
        )
    )

    print("Confidence: {}".format(text_segment.confidence))

    # # Show the result for the first frame in this segment.
    # frame = text_segment.frames[0]
    # time_offset = frame.time_offset
    # print(
    #     "Time offset for the first frame: {}".format(
    #         time_offset.seconds + time_offset.microseconds * 1e-6
    #     )
    # )
    # print("Rotated Bounding Box Vertices:")
    # for vertex in frame.rotated_bounding_box.vertices:
    #     print("\tVertex.x: {}, Vertex.y: {}".format(vertex.x, vertex.y))

# python text_detection.py
