from uuid import uuid4

def get_file_path(instance, filename):
    initial, ext = filename.split('.')
    filename = f'{initial}+{uuid4()}.{ext}'
    return filename