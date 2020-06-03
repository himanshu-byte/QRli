#generate.py

import qrlib.utils as ql

def json(QRtype, name, body=None, frame=None, ball=None, bodycolor=None, bgcolor=None, ballcolor=None, framecolor=None, shadecolor=None, shadeonball=None, shadetype=None, logo=None, size=None):
    json_data={'QRtype':QRtype, 'body':body, 'frame':frame, 'ball':ball, 'bodycolor':bodycolor, 'bgcolor':bgcolor, 'ballcolor':ballcolor, 'framecolor':framecolor, 'shadecolor':shadecolor, 'shadeonball':shadeonball, 'shadetype':shadetype, 'logo':logo, 'size':size, 'image':image}
    js= ql._str2json(json_data)
    nametemp = (str(name)+'.json')
    json_file = open(nametemp, "w")
    json_file.write(str(js))
    json_file.close()


def html():
















def secureQR(qrdata, name, size, key):
    ql._checkdata(qrdata, 'string', 'DATA FOR QR')
    ql._checkdata(name, 'string', 'NAME FOR QR')
    ql._checkdata(size, 0, 'SIZE FOR QR')
    encdata=ql._encode(key, qrdata)
    data1=(f'''"type":"secure","data":"{encdata}"''')
    data2=("{"+str(data1)+"}")
    transparentQR(data2, name, img="", size=size)