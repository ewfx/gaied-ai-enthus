import csv
import global_variables as gv

class RequestTypesConfig():
    def __init__(self, requesttypesconfigfile=gv.PROJECT_ROOT/"code/src/requesttypesconfig.csv"):
        with open(requesttypesconfigfile, "r") as file:
            reader = csv.reader(file)
            rows = [row for row in reader]
            rows = rows[1:]
        self.request_types = [()]*len(rows)
        for row in rows:
            self.request_types[int(row[2])] = (row[0], row[1])
