# Basic-spell-checker
 
This repository contains minimum edit distance algorithm to find spell-checked versions of words.

`utils.py` contains all necessary functions and besides you only need numpy. 

Let's start with the functions of `utils.py`:

## Functions

### process_data

Processing the given file and returns all words that lowered. Finding words are provided by `\w+` regular expression.
This matches words with lowercase, uppercase, digit and underscore characters.

### get_counter 

Gives counter dictionary of all word. 

### get_probs 

A probability of word is equal to how many times that word appeared divided by sum of total words.

### edit_one_letter

This function gives you to one edit version of every word.
That can be happend with 4 interaction: Deletion, switching, replacing, insertion.

1) split

splitting word through every character gives us left and right split. For example:

**word**: play

**splits**: [('', 'play'), ('p', 'lay'), ('pl', 'ay'), ('pla', 'y'), ('play', '')]

2) delete

Deletion happens by removing every first element from the right split.

**deletes**: ['lay', 'pay', 'ply', 'pla']

3) switch

switching happens by we swap first and second character of right split .

**switches**: ['lpay', 'paly', 'plya']

4) replaces


**replaces**: ['aan', 'ban', 'caa', 'cab', 'cac', 'cad', 'cae', 'caf', 'cag', 'cah', 'cai', 'caj', 'cak', 'cal', 'cam', 'cao', 'cap', 'caq', 'car', 'cas', 'cat', 'cau', 'cav', 'caw', 'cax', 'cay', 'caz', 'cbn', 'ccn', 'cdn', 'cen', 'cfn', 'cgn', 'chn', 'cin', 'cjn', 'ckn', 'cln', 'cmn', 'cnn', 'con', 'cpn', 'cqn', 'crn', 'csn', 'ctn', 'cun', 'cvn', 'cwn', 'cxn', 'cyn', 'czn', 'dan', 'ean', 'fan', 'gan', 'han', 'ian', 'jan', 'kan', 'lan', 'man', 'nan', 'oan', 'pan', 'qan', 'ran', 'san', 'tan', 'uan', 'van', 'wan', 'xan', 'yan', 'zan'] 


