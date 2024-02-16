from pymongo import MongoClient
from flask import Flask 

cluster=MongoClient("mongodb+srv://ssathvika404:c161234@mean.md1rt4w.mongodb.net/")
database=cluster['fullstack']
student_collection=database['student']
collection2=database['mba']

app=Flask(__name__)

@app.route('/data')
def sample():


    student_collection.insert_one({"name":"sai B","number":8184,"mobile":0,"add":[
        {"place":"guntur","pincode":522549,"mobile":[77777,99999] },
        {"place":"hyd","pincode":500084,"mobile":[11111]}
        ]})
    return "hello data inserted"








    
     


if __name__=="__main__":
    app.run(debug=True)