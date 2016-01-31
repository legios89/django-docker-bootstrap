# coding: utf-8
# Core and 3th party packages
import datetime


def media_directory_path(instance, filename):
    now = datetime.datetime.now()
    year = now.strftime('%Y')
    # file will be uploaded to MEDIA_ROOT/<year>/<time><filename>
    return '{0}/{1}{2}'.format(year, now.strftime('%s'), filename)
