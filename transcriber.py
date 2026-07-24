from faster_whisper import WhisperModel

# Load the model once
model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

def transcribe(audio_path: str) -> str:
    segments, info = model.transcribe(
        audio_path,
        beam_size=5,
        language="en",
        vad_filter=True
    )

    text = ""

    for segment in segments:
        text += segment.text + " "

    return text.strip()