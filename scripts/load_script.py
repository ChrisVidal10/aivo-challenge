import sqlite3
import time
import csv


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def Add_Record(db, data):
    #Insert record into table
    with sqlite3.connect(db) as conn:
        conn.row_factory = dict_factory
        conn.text_factory = str

        cursor = conn.cursor()

        query = "INSERT INTO country_index ({cols}) VALUES ({vals});".format(cols=",".join(data.keys()),
                                                                             vals=str([data[i] for i in data]).strip('[]'))
        cursor.execute(query)


def Load_Data(file_name):
    records = list()
    with open(file_name, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            records.append(list(row.values()))
    return records    


if __name__ == "__main__":
    t = time.time()

    db = 'db.sqlite'  # Database filename

    file_name = "data/BLI_28032019144925238.csv"

    data = Load_Data(file_name)  # Get data from CSV

    #For every record, format and insert to table
    for i in data:
        record = {
            "code": i[0],
            "code_desc": i[1],
            "indicator": i[2],
            "indicator_desc": i[3],
            "measure": i[4],
            "measure_desc": i[5],
            "inequality": i[6],
            "inequality_desc": i[7],
            "unit_code": i[8],
            "unit_code_desc": i[9],
            "powercode_code": i[10],
            "powercode_desc": i[11],
            "reference_period": i[12],
            "reference_period_desc": i[13],
            "value": float(i[14]),
            "flag_code": i[15],
            "flag_code_desc": i[16],
        }
    
        Add_Record(db, record)

    print("Time elapsed: " + str(time.time() - t) + " s.")
