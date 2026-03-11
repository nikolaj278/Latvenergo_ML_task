def write_results(file_name, candidates):
    """
    Record results into a file of WER, CER and WIL for both cases: with and without punctiation. 
    
    Args:
        file_name (str): the name of a file for recording results 
        candidates (dictionary of Candiate objects):  auto generated transcriptions 
    """

    
    with open(file_name, "w") as file:
        for name, cand in candidates.items():
            ss = name + "\n" \
            + "Novērtējot teksa ar punktuāciju rādītājus: \nWER={}, CER={}, WIL={}\n\n" \
                .format(round(cand.wer, 4), round(cand.cer, 4), round(cand.wil, 4)) \
            + "Novērtējot teksta bez punktuācijas rādītājus: \nWER={}, CER={}, WIL={}\n\n\n" \
                .format(round(cand.wer_2, 4), round(cand.cer_2, 4), round(cand.wil_2, 4)) 
            file.write(ss)