Each dataset file is a Python dictionary which can be loaded using pickle.
An example of the data structure is 
	{	
		'dataset_name': "Wikitoxic", 
		'class_names': ["Not abusive", "Abusive"], 
    	'text_train': ["Document 1a", "Document 2a", "Document 3a", ...], 
    	'y_train': [1, 0, 1, ...], 
    	'gender_train': ['M', 'F', 'N', ...], 
        'text_validate': ["Document 1b", "Document 2b", "Document 3b", ...],
        'y_validate': [0, 0, 1, ...], 
        'gender_validate': ['N', 'F', 'N', ...], 
        'text_test': ["Document 1c", "Document 2c", "Document 3c", ...], 
        'y_test': [1, 1, 1, ...], 
        'gender_test': ['F', 'M', 'M', ...],
    }
Please not that some fields may not be applicable to some datasets.