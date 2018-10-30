import cTurtle
import turtle
import math
def createCityPopDic():
    file=open('pop3.txt','r')
    r=file.read()
    file.close()
    lines=r.split('\n')
    D={}
    for line in lines:
        wordLines=line.split()
        if len(wordLines)==3:
            x=wordLines[1]
            y=int(wordLines[2])
            D[x]=y
        if len(wordLines)==4:#Adds cities with two words in name(new york)
            L=[wordLines[1],wordLines[2]]
            x=' '.join(L)
            y=int(wordLines[3])
            D[x]=y
    return D
def createCityLatLonDict():
    file=open('latLon3.txt','r')
    r=file.read()
    file.close()
    lines=r.split('\n')
    D={}
    for i in range(len(lines)-1):
        words=lines[i].split()
        lat=words[0]
        lon=words[1]
        city=' '.join(words[2:])
        D[city]=(float(lat),-float(lon))
    return D
def createStateColorDict():
    file=open('stateAdj.txt','r')
    r=file.read()
    lines=r.split('\n')
    D={}
    for i in range(0,len(lines)-2,2):
        d=lines[i]
        x=d[0:2]
        y=int(lines[i+1])
        D[x.lower()]=y
    return D
def drawLower48Map():
    cityPopDict=createCityPopDic()
    cityLatLonDict=createCityLatLonDict()
    stateColorDict=createStateColorDict()
    colorList=['blue','green','pink','red']
    lat=[]
    long=[]
    for i in cityLatLonDict:
        long.append(cityLatLonDict[i][1])
        lat.append(cityLatLonDict[i][0])
    minLat=min(lat)
    minLong=min(long)
    maxLat=max(lat)
    maxLong=max(long)
    matthew = turtle.Turtle()
    s = turtle.getscreen()
    s.setworldcoordinates(minLong,minLat,maxLong,maxLat)
    matthew.ht()
    fileT=open('output.txt','w')
    fileT.write('{:<30}'.format('cityname')+'{:<15}'.format('latitude')+'{:<15}'.format('longitude')+'{:<15}'.format('population')+'\n')
    for x in cityLatLonDict:
        matthew.up()
        matthew.setposition(cityLatLonDict[x][1],cityLatLonDict[x][0])
        matthew.down()
        dotSize=4
        state=x[-2]+x[-1]
        color=colorList[stateColorDict[state]]
        if x in cityPopDict:
            population=cityPopDict[x]
            dotSize = 4 + math.ceil(math.sqrt(population/50000))
            fileT.write('{:<30}'.format(x)+'{:<15}'.format(cityLatLonDict[x][0])+'{:<15}'.format(cityLatLonDict[x][1])+'{:<15}'.format(population)+'\n')
        else:
            fileT.write('{:<30}'.format(x)+'{:<15}'.format(cityLatLonDict[x][0])+'{:<15}'.format(cityLatLonDict[x][1])+'\n')
        matthew.dot(dotSize,color)
drawLower48Map()         
        
        
    
    
    

