from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from api.models import Employer
from api.serializers import EmployerSerializer

@api_view
def get_single_employer(request, employer_code):
    employer = get_object_or_404(Employer, employer_code=employer_code)
    serializer = EmployerSerializer(employer)
    return Response(serializer.data)