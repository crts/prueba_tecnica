from rest_framework.permissions import IsAuthenticated
from gastos.models import Gasto
from gastos.serializers import GastoSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
class GastoList(APIView):
    """Vista para la lista de gastos.

       Esta vista maneja las solicitudes GET y POST para la lista de gastos.
       """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Maneja las solicitudes GET para obtener la lista de gastos.
                Returns:
                    Response: Una respuesta con los datos serializados de los gastos.
                """
        try:
            gastos = Gasto.objects.all()
            serializer = GastoSerializer(gastos, many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response(status=500)
    def post(self, request):
        """Maneja las solicitudes POST para crear un nuevo gasto.

                Args:
                  request (Request):
                     "usuario": (str): nombre de usuario,
                     "categoria": (str) nombre de la categoria,
                     "monto": (float) monto del gasto

                Returns:
                    Response: Una respuesta con los datos serializados del nuevo gasto.
                """

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
    """Vista para los detalles de un gasto.

       Esta vista maneja las solicitudes GET, PUT y DELETE para un gasto específico.
       """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        """Maneja las solicitudes GET para obtener los detalles de un gasto.
               Returns:
                   Response: Una respuesta con los datos serializados del gasto.
               """
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
        """Maneja las solicitudes PUT para actualizar un gasto.

                Args:
                    request (Request):
                        "usuario": (str): nombre de usuario,
                         "categoria": (str) nombre de la categoria,
                         "monto": (float) monto del gasto
                    pk (int): La clave primaria del gasto.

                Returns:
                    Response: Una respuesta con los datos serializados del gasto actualizado.
                """
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
        """Maneja las solicitudes DELETE para eliminar un gasto.

               Args:
                   pk (int): La clave primaria del gasto.

               Returns:
                   Response: Una respuesta indicando que el gasto ha sido eliminado.
               """

        try:
            gasto = Gasto.objects.get(pk=pk)
            gasto.delete()
            return Response(status=204)
        except Gasto.DoesNotExist:
            return Response(status=404)
        except Exception as e:
            print(e)
            return Response(status=500)


