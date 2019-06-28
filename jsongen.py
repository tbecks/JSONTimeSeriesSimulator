## This is a Simulator for IoT Data
import json
import pandas as pd

df = pd.DataFrame()

print(df)

for x in range(1, 3):



#for x in range(10):
    #df = df.append({'key1': i, 'key2': i*2, 'key3': i**3}, ignore_index=True)

    df=df.append (
            {
                "topic":
                    {"namespace":"spBv1.0",
                    "groupId":"901",
                    "edgeNodeId":"901-100-101",
                    "deviceId":"UNIT1"},
                "payload":
                    {  "timestamp":1535473997109,
                    "metrics":
                        [{  "eventid":x,
                            "name":"DateTime",
                            "timestamp":1535473996109,
                            "dataType":"DateTime",
                            "value":1535473995000}],
                    "seq":121}
            } 
                       
            ,ignore_index=True)


out = df.to_json(orient='records') #[1:-1].replace('},{', '} {')

# print(out,"\n") 

with open('C:\Working\Data Sources\JSONSimulator\data.json', 'w',newline='\n') as outfile:
    outfile.write(out)
   
