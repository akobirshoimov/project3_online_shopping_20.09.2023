from django.shortcuts import render,get_object_or_404
from .models import OnlineShoppingModel
from .serializer import OnlineShoppingSer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class ListOnlineShoppingView(APIView):
    def get(self,request):
        if request.user == 'AnonymousUser':
            return Response({'you can not read these'})
        all = OnlineShoppingModel.objects.all()
        serializer = OnlineShoppingSer(all,many=True)
        return Response(serializer.data)
    
class UpdateOnlineShoppingView(APIView):
    def patch(self,request,*args,**kwargs):
        if request.user != 'AnonymousUser':
            if request.user.roles == 3:
                
                info = get_object_or_404(OnlineShoppingModel,id=kwargs['shopping_id'])
                serializer = OnlineShoppingSer(info,data=request.data,partial= True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
            return Response({'only director can update '})
        return Response({'only director can update '})
    
class CreateOnlineShoppingView(APIView):
    def post(self,request):
        if request.user != 'AnonymousUser':
            if request.user.roles == 3:
                serializer = OnlineShoppingModel(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
            return Response({'only manager can add '})
        return Response({'only manager can add '})
    
    