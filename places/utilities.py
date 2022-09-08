from os.path import splitext
from django.utils import timezone


def get_image_path(instance, filename):
    """ Get path of image """
    filepath = timezone.now().strftime('%Y/%m/%d/%H%M%S%f')
    file_ext = splitext(filename)[1].lower()
    return f'images/{ filepath }{ file_ext }'
