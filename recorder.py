import sounddevice as sd
import soundfile as sf

SAMPLE_RATE = 16000

def record_audio(filename="temp_audio.wav"):
    print("\nPress ENTER to START recording...")
    input()

    print("🎤 Recording... Press ENTER to STOP.")

    recording = []

    def callback(indata, frames, time, status):
        recording.append(indata.copy())

    with sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=1,
        callback=callback,
        dtype="float32"
    ):
        input()

    audio = __import__("numpy").concatenate(recording, axis=0)

    sf.write(filename, audio, SAMPLE_RATE)

    print("✅ Recording saved:", filename)