from django.db import models
import mimetypes
from django.core.exceptions import ValidationError

def validate_audio_file_extension(file):
    if mimetypes.guess_type(file.path)[0] != 'audio/mpeg':
        raise ValidationError(f'This is {mimetypes.guess_type(file.path)} format file')


class Blog(models.Model):
    file = models.FileField(upload_to='documents/',
                            validators=[validate_audio_file_extension])
    