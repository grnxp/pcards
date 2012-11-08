# my_apps/image/templatetags/image_tags.py
import os.path

from django import template
from django.conf import settings

FMT = 'JPEG'
EXT = 'jpg'
QUAL = 75

THUMBNAIL_SIZE = '260x180'
IMAGE_SIZE = '300x300'

register = template.Library()

thumbnails_dir = os.path.join(settings.MEDIA_ROOT, 'pictures', 'thumbnails')

if not os.path.exists(thumbnails_dir):
	os.makedirs(thumbnails_dir)


def resized_path(card_id, path, method):
	if method == 'crop':
		size = THUMBNAIL_SIZE
	elif method == 'scale':
		size = IMAGE_SIZE
	
	dir, name = os.path.split(path)
	image_name, ext = name.rsplit('.', 1)
	
	thumbnails_dir = os.path.join(dir, 'thumbnails')
	
	final_path = os.path.join(thumbnails_dir, '%s_%s_%s.%s' % (card_id, method, size, EXT)).replace('\\', '/')

	print 'final path ' + final_path

	return final_path


def scale(card_item, method='scale'):
    """ 
    Template filter used to scale an image
    that will fit inside the defined area.

    Returns the url of the resized image.

    {% load image_tags %}
    {{ profile.picture|scale }}
    """
    
    imagefield = card_item.image

    # imagefield can be a dict with "path" and "url" keys
    if imagefield.__class__.__name__ == 'dict':
        imagefield = type('imageobj', (object,), imagefield)

    image_path = resized_path(card_item.id, imagefield.path, method)

    if not os.path.exists(image_path):
        try:
            import Image
        except ImportError:
            try:
                from PIL import Image
            except ImportError:
                raise ImportError('Cannot import the Python Image Library.')

        image = Image.open(imagefield.path)

        # normalize image mode
        if image.mode != 'RGB':
            image = image.convert('RGB')

        # use PIL methods to edit images
        if method == 'scale':
            width, height = [int(i) for i in IMAGE_SIZE.split('x')]
            image.thumbnail((width, height), Image.ANTIALIAS)
            image.save(image_path, FMT, quality=QUAL)

        elif method == 'crop':
            try:
                import ImageOps
            except ImportError:
                from PIL import ImageOps

            width, height = [int(i) for i in THUMBNAIL_SIZE.split('x')]
            ImageOps.fit(image, (width, height), Image.ANTIALIAS
                        ).save(image_path, FMT, quality=QUAL)

	
	print resized_path(card_item.id, imagefield.url, method)
	
    return resized_path(card_item.id, imagefield.url, method)

#def crop(imagefield):
def crop(card_item):
    """
    Template filter used to crop an image
    to make it fill the defined area.

    {% load image_tags %}
    {{ profile.picture|crop }}

    """
    return scale(card_item, 'crop')


register.filter('scale', scale)
register.filter('crop', crop)
