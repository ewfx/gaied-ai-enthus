import csv
import pandas as pd
import emailhandler
import global_variables as gv

with open(gv.PROJECT_ROOT/"code/src/trainconfig.csv", "r") as file:
    reader = csv.reader(file)
    trainconfig = [row for row in reader]
    trainconfig = trainconfig[1:]

trainingpd = pd.DataFrame(trainconfig, columns=['filepath','label'])
trainingpd['text'] = trainingpd['filepath'].apply(emailhandler.extract_email_content)
trainingpd.pop('filepath')
trainingpd.to_csv(gv.PROJECT_ROOT/'data/training/trainingdata.csv',index=False)