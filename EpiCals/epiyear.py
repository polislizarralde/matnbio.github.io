#!/usr/bin/env python
# -*- coding: utf-8 -*-

import calendar
import datetime
from datetime import timedelta
import sys

aday = timedelta(days=1)

calendar.setfirstweekday(calendar.SUNDAY)
#calendar.prcal(2016)
#calendar.prcal(2001)

def epiyear(year):
    """
    Epiyear calcula las semanas epidemiologicas, retornando una lista de hasta
    54 semanas (semana 0 incluiria dias que no hacen parte de la primera semana
    epidemiologica pero si del primer día, semana 53 en caso de que haya para
    un total de 54 posibles elementos.)
    la primera semana epidemiológica termina, por definición, el primer sábado
    de Enero que incluya en los días inmediatamente precendentes cuatro o más
    días del mes de Enero. Para que la primera semana inicie incluyendo el 1ero
    de enero, este debe caer o lunes o martes.
    http://www.col.ops-oms.org/sivigila/anioepidemiologicodef.asp
    """

    weeks=[]
    theday = datetime.date(year,1,1)
    #  Domingo 6, Lunes 0, Martes 1, Miercoles 2, Jueves 3, Viernes 4, Sabado 5

    weeks.append([])

    #print(theday.weekday)
    if(theday.weekday<=1):thisweek=1
    else: thisweek = 0

    while(theday<=datetime.date(year,12,31)):#datetime.date(year,1,10).days):
        #print(theday,theday.weekday())

        if(theday.weekday()>5):
            thisweek+=1
            weeks.append([])
        weeks[thisweek].append(theday.day)
        theday += aday
    return weeks

def printWeeks(file,weeks):
    x = [i.rjust(4) for i in ("DLMWJVS")]
    days = ""
    for w in x: days+=w
    file.write(days+"\n")

    for i in range(0,len(weeks)):
        w = ""
        for j in weeks[i]:
            w += repr(j).rjust(4)
        file.write((w + " <- Semana: {} \n").format(i))

def printWeeksCSV(file, weeks):
    with file as sys.stdout:
        print ', '.join("DLMWJVS")
        print '\n'.join([', '.join(map(str, week)) for week in weeks])

for z in range(2002,2017):
    a = open(str(z)+".txt",'w')
    printWeeks(a,epiyear(z))

for z in range(2002,2017):
    a = open(str(z)+".csv",'w')
    printWeeksCSV(a,epiyear(z))# -> [[1,2],[3,4,5,6,7,8,9]...[25,26,27,28,29,30,31]]

#epiyear(2016)
#print epiyear(2001)# -> [[31,1,2,3,4,5,6],...,]
