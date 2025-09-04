# #from django.shortcuts import render
# from .serializer import ProgrammerSerializer 
# from .models import programmer 
# # Create your views here.


# class Nacionalidad_ViewSet(viewsets.ModelViewSet):
#     # acá creamos una QUERY a nuestra tabla, trayendo todos los campos como un objeto. 
#     queryset = programmer.objects.all()
#     # Agregamos la clase ProgrammerSerializer que ya tiene el modelo serializado para mostrar 
#     serializer_class = Nacionalidad_Serializer

# class Autor_ViewSet(viewsets.ModelViewSet):
#     queryset = programmer.objects.all()
#     serializer_class = Autor_Serializer

# class Comuna_ViewSet(viewsets.ModelViewSet):
#     queryset = programmer.objects.all() 
#     serializer_class = Comuna_Serializer

# class Direccion_ViewSet(viewsets.ModelViewSet):
#     queryset = programmer.objects.all()
   
#     serializer_class = Direccion_Serializer