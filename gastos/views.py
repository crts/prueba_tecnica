from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.decorators import authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from gastos.models import Gasto
from gastos.serializers import GastoSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
class GastoList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            gastos = Gasto.objects.all()
            serializer = GastoSerializer(gastos, many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response(status=500)
    def post(self, request):
        try:
            serializer = GastoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except Exception as e:
            print(e)
            return Response(status=500)
class GastoDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            gasto = Gasto.objects.get(pk=pk)
            serializer = GastoSerializer(gasto)
            return Response(serializer.data)
        except Gasto.DoesNotExist:
            return Response(status=404)
        except Exception as e:
            print(e)
            return Response(status=500)

    def put(self, request, pk):
        try:
            gasto = Gasto.objects.get(pk=pk)
            serializer = GastoSerializer(gasto, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Gasto.DoesNotExist:
            return Response(status=404)
        except Exception as e:
            print(e)
            return Response(status=500)

    def delete(self, request, pk):
        try:
            gasto = Gasto.objects.get(pk=pk)
            gasto.delete()
            return Response(status=204)
        except Gasto.DoesNotExist:
            return Response(status=404)
        except Exception as e:
            print(e)
            return Response(status=500)


