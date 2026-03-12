# Latvenergo_ML_task


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