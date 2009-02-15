# file Valseq.py

valid_sequence_dict = { "P1": "complete protein", \
"F1": "protein fragment", "DL": "linear DNA", "DC": "circular DNA", \
"RL": "linear RNA", "RC":"circular RNA", "N3": "transfer RNA", \
"N1": "other"   }

def find_valid_key(e):
    for key,value in valid_sequence_dict.items():
        if value == e:
        	return key

