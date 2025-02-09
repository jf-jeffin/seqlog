from pymongo import MongoClient
def connection(cc="localhost",port=27017,col=""):
    conn=MongoClient(cc,port)
    if col:
        SeqLog=conn.SeqLog
        return SeqLog.col
    else:
        return conn.SeqLog

def cconst (connection,name):
    return connection.create_collection(name)


def insertion(col,doc):
    return col.insert_one(doc)
