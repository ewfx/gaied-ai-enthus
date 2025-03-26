**Before watching demo, please note these details about the structure and purposes of different files in the project folder:**

1. **code/src/requesttypesconfig.csv** - input configuration file with definitions of request type, sub request type and the combinations's labels (0 through 15)
2. **data/test_emails** - contains all sample emails (in .eml format) I have generated using various online tools like ChatGPT
3. **code/src/trainconfig.csv** - the configuration file with each file from (data/test_emails/*.eml) labelled with corresponding labels (0 through 15).
4. **data/training/trainingdata.csv** - result of preprocessing.py's execution which contains extracted email's contents and their labels (as defined in trainconfig.csv). This is the input file to be loaded for training the model.
5. **preprocessing.py** - prepares the data for training and places in trainingdata.csv
6. **train_classification.py** - fine-tunes the 'distilbert/distilbert-base-uncased' model on the sample emails. This model is choosen so it can completely run on my local machine efficiently and can help with text classification.
7. **/data/evaluation/** - lists the .eml files that are used to evaluate model after training.
8. **evaluate_email.py** - evaluates the files after training and output the result.