"""Transcribe speech from a video stored on GCS."""
from google.cloud import videointelligence
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'service_account_key'  # just paste the path for json file downloaded from gcp project

from google.cloud import videointelligence
client = videointelligence.VideoIntelligenceServiceClient()

video_path = 'googlecloudfileuri'  # paste the path uri of file uploaded on google cloud's bucket

video_client = videointelligence.VideoIntelligenceServiceClient()
features = [videointelligence.Feature.SPEECH_TRANSCRIPTION]

config = videointelligence.SpeechTranscriptionConfig(
    language_code="en-US", enable_automatic_punctuation=True
)
video_context = videointelligence.VideoContext(speech_transcription_config=config)

operation = video_client.annotate_video(
    request={
        "features": features,
        "input_uri": video_path,
        "video_context": video_context,
    }
)

print("\nProcessing video for speech transcription.")

result = operation.result(timeout=600)

# There is only one annotation_result since only
# one video is processed.
annotation_results = result.annotation_results[0]
for speech_transcription in annotation_results.speech_transcriptions:

    # The number of alternatives for each transcription is limited by
    # SpeechTranscriptionConfig.max_alternatives.
    # Each alternative is a different possible transcription
    # and has its own confidence score.
    for alternative in speech_transcription.alternatives:
        print("Alternative level information:")

        print("Transcript: {}".format(alternative.transcript))
        print("Confidence: {}\n".format(alternative.confidence))

        # print("Word level information:")
        # for word_info in alternative.words:
        #     word = word_info.word
        #     start_time = word_info.start_time
        #     end_time = word_info.end_time
        #     print(
        #         "\t{}s - {}s: {}".format(
        #             start_time.seconds + start_time.microseconds * 1e-6,
        #             end_time.seconds + end_time.microseconds * 1e-6,
        #             word,
        #         )
        #     )

# python speech_transcription.py
