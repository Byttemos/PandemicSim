import json
import nodeSystem as ns

#create dictionary to "carry" data
def writeToJson(path, fileName, data):
    filePathName = './' + path + '/' + fileName + '.json'
    with open(filePathName, "w"):
        json.dump(data, fp)

path = (r'.\\')
fileName = "jsonDump"
data = {ns.updatePosition()}

writeToJson(path, fileName, data)
