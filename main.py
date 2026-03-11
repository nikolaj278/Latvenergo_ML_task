import pandas as pd
import jiwer

from src.data_classes import Candidate
from src.error_markup import write_error_markup_to_file
from src.preprocessing import basic_prep
from src.write_to_file import write_results

PATH = "./data/"
ref_file_name = "transkripts.txt"
candidate_names = ["auto-1", "auto-2", "auto-3"]

if __name__ == "__main__":
    
    candidates = {}

    # read transkripts.txt file
    with open(PATH + ref_file_name, "r", encoding="utf-8") as file:
            reference = file.read()

    #read candidate files and create Candidate objects
    for name in candidate_names:
        with open(PATH + name + ".txt", "r", encoding="utf-8") as file:
            text = file.read()
            candidates[name] = Candidate(
                                text=text, 
                                wer=None, cer=None, wil=None,
                                wer_2=None, cer_2=None, wil_2=None)
    
    for name, cand in candidates.items():
        # evaluation of quality when reference and candidates have punctuation
        cand.wer = jiwer.wer(basic_prep(reference), basic_prep(cand.text))
        cand.cer = jiwer.cer(basic_prep(reference), basic_prep(cand.text))
        cand.wil = jiwer.wil(basic_prep(reference), basic_prep(cand.text))
    
        # evaluation of quality when reference and candidates haven't any punctuation
        cand.wer_2 = jiwer.wer(basic_prep(reference, rem_punct=True),
                               basic_prep(cand.text, rem_punct=True))
        cand.cer_2 = jiwer.cer(basic_prep(reference, rem_punct=True),
                               basic_prep(cand.text, rem_punct=True))
        cand.wil_2 = jiwer.wil(basic_prep(reference, rem_punct=True),
                               basic_prep(cand.text, rem_punct=True))
        
    # write candidate evaluation results in the file
    write_results(file_path="output/", 
                  name_prefix="scores",
                  candidates=candidates)
        

    # write WER identified errors marked with colors into the files in output folder 
    for name, cand in candidates.items():
        # errors, taking punctuation into account
        write_error_markup_to_file(reference=basic_prep(reference), 
                                   candidate=basic_prep(cand.text),
                                   out_file_path="output/with_punctuation/out_" + name + ".html")
        
        # errors without taking punctuation into account
        write_error_markup_to_file(reference=basic_prep(reference, rem_punct=True), 
                                   candidate=basic_prep(cand.text, rem_punct=True),
                                   out_file_path="output/without_punctuation/out_" + name + ".html")
    print("The code ran successfully.")


    
    
    
    
    
    
    
        