import json
import os

from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def index(request):
    """Return API info
    """
    manifest_file_loc = os.path.join(
        settings.BASE_DIR,
        'config',
        'manifest.json'
    )

    with open(manifest_file_loc) as f:
        manifest = json.load(f)

    return Response({
        'name': manifest['name'],
        'version': manifest['version']
    })
