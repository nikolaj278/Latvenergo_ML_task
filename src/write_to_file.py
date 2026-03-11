import pandas as pd

def write_results(file_path, name_prefix, candidates):
    """
    Record results into 3 files of WER, CER and WIL for both cases: with and without punctiation. One text file and two csv for results with punctuatoin adn without punctuation.
    
    Args:
        file_npath (str): the path to teh folder of  file for recording results 
        name_prefix (str): prefix to use for 3 generated files (1 txt, 2 csv)
        candidates (dictionary of Candiate objects):  auto generated transcriptions 
    """

    # record results into txt file
    with open(file_path + name_prefix + ".txt", "w", encoding="utf-8") as file:
        for name, cand in candidates.items():
            ss = name + "\n" \
            + "Novērtējot teksa ar punktuāciju rādītājus: \nWER={}, CER={}, WIL={}\n\n" \
                .format(round(cand.wer, 4), round(cand.cer, 4), round(cand.wil, 4)) \
            + "Novērtējot teksta bez punktuācijas rādītājus: \nWER={}, CER={}, WIL={}\n\n\n" \
                .format(round(cand.wer_2, 4), round(cand.cer_2, 4), round(cand.wil_2, 4)) 
            file.write(ss)
    
    # record results for the case with punctuation    
    df_1 = {}
    for name, cand in candidates.items():
        df_1[name]= [round(cand.wer, 4), round(cand.cer, 4), round(cand.wil, 4)]
        
    pd.DataFrame(df_1, index=["WER", "CER", "WIL"])\
        .to_csv(file_path + name_prefix + "_with_punct" + ".csv")

    # record results for the case without punctuation  
    df_2 = {}
    for name, cand in candidates.items():
        df_2[name]= [round(cand.wer_2, 4), round(cand.cer_2, 4), round(cand.wil_2, 4)]
        
    pd.DataFrame(df_2, index=["WER", "CER", "WIL"])\
        .to_csv(file_path + name_prefix + "_without_punct" + ".csv")
    