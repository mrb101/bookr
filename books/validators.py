from django.core.exceptions import ValidationError
import magic


class MimeTypeValidator(object):

    message = ('Files of type "%(invalid_type)s" are not allowed.')
    code = 'invalid_type'

    def __init__(self, mimetypes, message=None, code=None):
        self.mimetypes = mimetypes
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        try:
            mime = magic.from_buffer(value.read(1024), mime=True)
            if not mime in self.mimetypes:
                raise ValidationError(self.message, code=self.code, params={
                    'invalid_type': mime
                })
        except AttributeError as e:
            raise ValidationError(self.message, code=self.code, params={
                'invalid_type': mime})
