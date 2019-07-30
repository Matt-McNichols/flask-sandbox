from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import os
from seqTest import zNzSequence

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    res = getResults()
    return render_template('home.html',results=res)

@app.route('/<name>/<run>')
def output(name,run):
    #print 'name: %s'%name
    res = getResults()
    ns=[]
    #for EquipName,cFiles in res:
    #    if EquipName == name
    print 'NAME: {0}'.format(name)
    print 'RUN: {0}'.format(run)
    if name == 'sequences':
        print 'START SEQUENCE'
        zNz=zNzSequence()
        if True: 
            n=0
            zNzOut = zNz.run(n,n+10)
            print zNzOut
            ns = zNzOut['PzPrimes']
        # create plot object from array 
        #nsPlotObj=makePlotObj(ns)
    return render_template('/results/{0}/{1}.html'.format(name,run),results=res,plotObj=ns,plotLen=len(ns))

def getResults():
    res = []
    walkDir='./templates/results'
    # get output directory names
    for cDir, sDirs, cFiles in os.walk(walkDir):
        #print 'cDir:%s,   sdirs:%s,  cFiles:%s'%(cDir, sDirs, cFiles)
        cFilesHtml = []
        if len(cFiles) > 0: 
            EquipName = cDir[len('./templates/results/'):]
            for tmpF in cFiles:
                if tmpF[-5:]=='.html':
                    cFilesHtml.append(tmpF)
            res.append((EquipName,cFilesHtml))
            #print '( EquipName:%s  cFiles:%s )'%(EquipName,cFiles)
    return res

def t():
   return 'yess'

def makePlotObj(arrIn):
    arrOut=[]
    for val in arrIn:
        arrOut.append({'y':val})
    return arrOut    
