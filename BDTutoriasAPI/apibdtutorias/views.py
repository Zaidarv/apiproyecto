from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt 
from .models import Tutor
import json 

# Create your views here.

class TutorView(View):

    @method_decorator(csrf_exempt) 
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request, id=0):
        if(id>0):
            tutor=list(Tutor.objects.filter(id=id).values())
            if len(tutor)>0:
                tutores = tutor[0]
                datos={'message': "Success", 'tutor': tutores}
            else:
                datos={'message':"Tutor not found..."}
            return JsonResponse(datos)
        else:
            tutor=list(Tutor.objects.values())
            if len(tutor)>0:
                datos={'message':"Success",'tutor':tutor}
            else:
                datos={'message':"Tutores not found."}
            return JsonResponse(datos)

    def post(self,request):
        # print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Tutor.objects.create(rfc=jd['rfc'], periodo=jd['status_empleado'], carrera=jd['clave_area'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self,request,rfc):
        jd=json.loads(request.body)
        tutor=list(Tutor.objects.filter(rfc=rfc).values())
        if len(tutor)>0:
            tutor=Tutor.objects.get(rfc=rfc)
            tutor.rfc = jd['rfc']
            tutor.periodo = jd['periodo']
            tutor.carrera = jd['carrera'] 
            tutor.save()
            datos={'message':"Success"}
        else:
            datos={'message':"Tutor not found..."}
        return JsonResponse (datos)
      
    def delete(self,request,id):
        tutor=list(Tutor.objects.filter(id=id).values())
        if len(tutor)>0: 
            Tutor.objects.filter(id=id).delete()
            datos={'message':"Success"}
        else:
            datos={'message': "Tutor not found..."}
        return JsonResponse(datos)