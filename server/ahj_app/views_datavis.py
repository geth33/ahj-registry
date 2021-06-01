from django.db import connection
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .authentication import WebpageTokenAuth
from .models import Polygon
from .serializers import DataVisAHJPolygonInfoSerializer, PolygonSerializer
from .utils import dictfetchall


@api_view(['GET'])
@authentication_classes([WebpageTokenAuth])
@permission_classes([IsAuthenticated])
def data_map(request):
    statepolygonid = request.query_params.get('StatePK', None)
    polygon_columns = 'Name, Polygon.PolygonID, InternalPLatitude, InternalPLongitude, Name'
    ahj_columns = 'AHJPK, AHJName'
    serializer_context = {}
    if statepolygonid is not None:
        with connection.cursor() as cursor:
            cursor.execute('SELECT ' + \
                           polygon_columns + ', ' + ahj_columns + ', ' + \
                           'IF(BuildingCode IS NULL,0,1) as numBuildingCodes,' + \
                           'IF(ElectricCode IS NULL,0,1) as numElectricCodes,' + \
                           'IF(FireCode IS NULL,0,1) as numFireCodes,' + \
                           'IF(ResidentialCode IS NULL,0,1) as numResidentialCodes,' + \
                           'IF(WindCode IS NULL,0,1) as numWindCodes' + \
                           ' FROM Polygon JOIN (' \
                           'SELECT PolygonID FROM CountyPolygon WHERE StatePolygonID=' + \
                           '%(statepolygonid)s' + \
                           ' UNION SELECT PolygonID FROM CityPolygon WHERE StatePolygonID=' + \
                           '%(statepolygonid)s' + \
                           ' UNION SELECT PolygonID FROM CountySubdivisionPolygon WHERE StatePolygonID=' + \
                           '%(statepolygonid)s' + \
                           ') as polygons_of_state ON Polygon.PolygonID=polygons_of_state.PolygonID LEFT JOIN AHJ ON Polygon.PolygonID=AHJ.PolygonID;', params={
                'statepolygonid': statepolygonid
            })
            results = dictfetchall(cursor)
    else:
        with connection.cursor() as cursor:
            cursor.execute('SELECT ' + polygon_columns + \
                           ' FROM StatePolygon JOIN Polygon ON Polygon.PolygonID=StatePolygon.PolygonID;')
            results = dictfetchall(cursor)
        serializer_context['is_state'] = True
    return Response(DataVisAHJPolygonInfoSerializer(results, context=serializer_context, many=True).data)


@api_view(['GET'])
@authentication_classes([WebpageTokenAuth])
@permission_classes([IsAuthenticated])
def data_map_get_polygon(request):
    return Response(PolygonSerializer(Polygon.objects.get(PolygonID=request.query_params.get('PolygonID', None))).data)
