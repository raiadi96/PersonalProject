from amazon_transcribe.model import StartStreamTranscriptionEventStream
from typing import AsyncIterable, Dict
import time
import asyncio

async def apply_realtime_delay(
    stream: StartStreamTranscriptionEventStream,
    reader: AsyncIterable,
    bytes_per_sample: int,
    sample_rate: float,
    channel_nums: int,
) -> None:
    """Applies a delay when reading an audio file steam to simulate a real-time delay."""
    start_time = time.time()
    elapsed_audio_time = 0.0
    async for chunk in reader:
        await stream.input_stream.send_audio_event(audio_chunk=chunk)
        elapsed_audio_time += len(chunk) / (
            bytes_per_sample * sample_rate * channel_nums
        )
        # sleep to simulate real-time streaming
        wait_time = start_time + elapsed_audio_time - time.time()
        await asyncio.sleep(wait_time)