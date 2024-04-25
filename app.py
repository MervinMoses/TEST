from flask import Flask,render_template
import pyodbc

import pandas as pd


app=Flask(__name__)


    #if you dont want to change the varible then type it in upper class
SERVER="DESKTOP-14J830G\SQLEXPRESS"
DATABASE="excerise"

    #create a connection string using windows authentication
connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE}; Trusted_Connection=yes;'

    #create a connection
conn = pyodbc.connect(connectionString)



select_query='select * from dbo.book'
df=pd.read_sql(select_query,conn)
print(df) # shows in the form of table  
dict_DF=df.to_dict(orient='records')



@app.route("/")
def home():
    return render_template('home.html')

@app.route("/getall")
def getall():
    return render_template('getALL.html',all_employess=dict_DF)





if __name__=='__main__':
    app.run(debug=True)