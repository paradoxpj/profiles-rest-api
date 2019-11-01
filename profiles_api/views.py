from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    '''Testing API Views'''

    def get(self, request, format=None):
        '''Returns a list of APIView'''
        an_apiview = [
            'Uses HTTP methods as functions',
            'Is similar to traditional Django views',
            'Gives you great control over logic',
            'Is mapped manualy to URls',
        ]

        return Response({'message': 'hello!', 'an_apiview': an_apiview })
