import re
import numpy as np
from collections import Counter 


def process_data(file_name):
    with open(file_name) as f:
        file_name_data = f.read()
    file_name_data=file_name_data.lower()
    words = re.findall('\w+',file_name_data)
    return words


def get_counter(words):
    return Counter(words)


def get_probs(counter):
    probs = {}
    total = sum(counter.values())
    for word in counter.keys():
        probs[word] = counter[word] / total
    return probs


def edit_one_letter(word, verbose=False, allow_switches=False):
    letters = 'abcdefghijklmnopqrstuvwxyz'

    splits = [(word[:i], word[i:]) for i in range(len(word)+1)]

    deletes = [L+R[1:] for L, R in splits if R]

    switches = [L + R[1] + R[0] + R[2:] for L,R in splits if len(R) >= 2]      

    replaces = []
    for L, R in splits:
        if not R:
            continue
        for char in letters:
            ending = R[1:] if len(R) > 1 else ''
            replaces.append(L + char + ending)

    inserts = [ L + l + R for L,R in splits for l in letters]

    if verbose: 
        print(f"Input word {word}, \nsplit list = {splits}")
        print(f"Delete:\n {deletes}")
        print(f"Switches:\n {switches}")
        print(f"Replaces:\n {replaces}")
        print(f"Inserts:\n {inserts}")
    res = set()
    res.update(deletes)
    res.update(inserts)
    res.update(replaces)
    if allow_switches:
        res.update(switches)
    return res 


def edit_two_letters(word, allow_switches = False):
    edit_two_set = set()
    edit_one = edit_one_letter(word,allow_switches=allow_switches)
    for w in edit_one:
        if w:
            edit_two = edit_one_letter(w,allow_switches=allow_switches)
            edit_two_set.update(edit_two)

    return edit_two_set


def min_edit_distance(source, target, ins_cost = 1, del_cost = 1, rep_cost = 2):
    m = len(source)
    n = len(target)

    D = np.zeros((m+1, n+1), dtype=int) 
    
    for row in range(1,m+1): 
        D[row,0] = D[row-1,0] + del_cost

    for col in range(1,n+1): 
        D[0,col] = D[0,col-1] + ins_cost
        
    for row in range(1,m+1): 
        for col in range(1,n+1):
            r_cost = rep_cost
            
            if source[row-1] == target[col-1]:
                r_cost = 0
                
            D[row,col] = min([D[row-1,col]+del_cost, D[row,col-1]+ins_cost, D[row-1,col-1]+r_cost])
          
    med = D[m,n]
    return D, med


def get_corrections(word, probs, vocab, verbose = False):
    suggestions = []
    n_best = []
    
    suggestions = list((word in vocab and word) or edit_one_letter(word).intersection(vocab) or edit_two_letters(word).intersection(vocab))
    print(suggestions)
    n_best = [[s,probs[s]] for s in list(suggestions)]
    
    if verbose: 
        print("suggestions = ", suggestions)

    return n_best