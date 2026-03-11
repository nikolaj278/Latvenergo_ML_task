from dataclasses import dataclass


@dataclass
class Candidate:
    """
    Represents a candidate transcription and its evaluation metrics.

    Attributes:
        text (str): The transcribed text for this candidate.
        wer (float | None): Word Error Rate for the first evaluation. None if not computed.
        cer (float | None): Character Error Rate for the first evaluation. None if not computed.
        wil (float | None): Word Information Lost for the first evaluation. None if not computed.
        wer_2 (float | None): Word Error Rate for evaluation when punctuation is removed. None if not computed.
        cer_2 (float | None): Character Error Rate for evaluation when punctuation is removed. None if not computed.
        wil_2 (float | None): Word Information Lost for evaluation when punctuation is removed. None if not computed.
    """
    text: str
    wer: float | None
    cer: float | None
    wil: float | None
    wer_2: float | None
    cer_2: float | None
    wil_2: float | None