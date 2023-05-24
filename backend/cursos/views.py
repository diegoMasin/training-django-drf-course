from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course, Rating
from .serializers import CourseSerializer, RatingSerializer


class CourseAPIView(APIView):
    """
    Course API View
    """

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)

        return Response(serializer.data)


class RatingAPIView(APIView):
    """
    Rating API View
    """

    def get(self, request):
        ratings = Rating.objects.all()
        serializer = RatingSerializer(ratings, many=True)

        return Response(serializer.data)
