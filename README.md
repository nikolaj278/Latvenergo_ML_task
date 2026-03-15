# Latvenergo_ML_task


This project focuses on automatic speech recognition (ASR) quality estimation.
Given one reference transcription and three candidate transcriptions, the goal is to estimate the quality of each candidate. 
\
\
The following metrics were used: WER, CER, and WIL. These metrics were described and calculated using Python. Three additional files with highlighted errors were generated based on the WER results.
\
\
A manual (subjective) analysis of the candidates was also performed to see how the metric values relate to typical transcription problems. For example, certain metric combinations may indicate issues such as incorrect word forms.


## Insallation:
1. Copy the repo

2. Install required libraries:

```{terminal}
pip install -r requirements
```

## Run the code:
Run main.py file.
If you see "The code ran successfully.", the program has finished and all output files have been generated

## Output:
All code output files are located in the output/ folder:
- Files with errors marked by the WER metric for both cases: with punctuation and without punctuation
- Scores for both cases in a .txt file
- Scores for both cases in two separate .csv files

All manual analysis in Latvian is located in the info/ folder.


## Tech Stack / Built With
Languages:
- Python 3.10

Packages:
- re
- pandas
- jiwer