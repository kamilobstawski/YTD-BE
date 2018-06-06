from celery.result import AsyncResult
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .tasks import download

from downloader.serializers import DownloadSerializer


def percent(tem, total):
    perc = (float(tem) / float(total)) * float(100)
    return perc


@api_view(['GET', ])
def get_progress(request, task_id):
    result = AsyncResult(task_id)
    return Response({'state': str(result.state), 'details': result.info})


class DownloadView(APIView):
    serializer_class = DownloadSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            task_id = download.delay(serializer.validated_data['url'])
            return Response({'task_id': task_id.id}, status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'Something went wrong. Please try again'}, status=status.HTTP_400_BAD_REQUEST)
