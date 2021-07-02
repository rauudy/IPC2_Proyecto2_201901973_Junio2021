import xml
from django.shortcuts import render, redirect
import requests as req
import re
from xml import dom
from xml.dom import minidom
from typing import ItemsView
from xml.dom import minidom
import xml.etree.ElementTree as ET

# Create your views here.
archivos =[]
clientes=[]

def index(request):
    xml_data = req.get('http://localhost:5000/tareas')
    xml_str = xml_data.text
    context ={
        'dato': xml_str,
        'csv': archivos,
    }
    return render(request, 'index.html', context)

  

def reportes(request):
    if request.method == 'GET':
        fecha = request.GET.get('fecha', None)
        #corregir_fecha = re.sub('-', '/', fecha)
        contador_fecha = req.get('http://localhost:5000/por_fecha', {
            'fecha': fecha
        }).text

        
        context ={'fecha': contador_fecha}
    return render(request, 'reportes.html', context)

def recibir_xml(request):
    global archivos,clientes
    
    if request.method == 'POST':
        csv_index= request.FILES.getlist('docs')
        print()
        for i in csv_index:
            archivos.append(i.file.getvalue().decode('latin-1'))

        #print(type(archivos))
        clientes=archivos[0].split('\n')
        print(type(clientes))
        print(clientes)
        print('line-------')

        for line in clientes:
            print(line)


        

        #for a in archivos:
        #    print(a)
        
        #print()
        #print(archivos[0])

    
    #csv_inf = csv_index.read() 
    #prueba = csv_inf.decode('latin-1')
    #for a in csv_inf:
        #   csv.append(a.decode('latin-1'))

    #if request.method == 'POST':
     #   xml_file = request.FILES['docs']
      #  xml_data = xml_file.read() #convertirlo en string , data es el que mandaremos a flask

       # print('****************************')
       # print(str(xml_data))

        #procesar el csv

    #req.post('http://localhost:5000/tareas', xml_data)

    return redirect('index')