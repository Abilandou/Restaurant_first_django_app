from django.utils.text import slugify
import random
import string
'''
random_string_generator is located here:
http://joincfe.com/blog/random-string-generator-in-python/
'''

# from restaurants.utils import random_string_generator
DONT_USE = ['create']
def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
    """
    This is for a django project and it assumes your instance
    has a model with a slug field and a title character (char) field
    :param instance:
    :param new_slug:
    :return:
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    if slug in DONT_USE:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)

    klass = instance.__class__
    qs_exists = klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                slug=slug,
                randstr=random_string_generator(size=4)
            )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
