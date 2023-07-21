
# Create your views here.
from rest_framework import generics
from .models import Qualification
from .serializers import QualificationSerializer

class QualificationListCreateView(generics.ListCreateAPIView):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer

class QualificationRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer

class QualificationListByUserView(generics.ListAPIView):
    serializer_class = QualificationSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Qualification.objects.filter(user_id=user_id)
