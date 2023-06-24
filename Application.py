from flask import Flask
app = Flask(__name__)

def readData(filename):
    JsonData=[]
    sortedData={}
    with open(filename,'r') as f:
        JsonData=f.readlines()
    for item in range(0,len(JsonData)):
        sortedData["university no: "+str(item)]=JsonData[item]
    return sortedData

@app.route('/')
def index():
    info=readData("varsityData")
    return info


if __name__ == '__main__':
   app.run()
