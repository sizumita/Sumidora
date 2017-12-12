# from django import template
# from pytz import timezone
# from dateutil import parser
# register = template.Library()
#
#
# @register.filter(name='cut')
# def cut(arg):
#     return parser.parse(arg).astimezone(timezone('Asia/Tokyo'))
#
# register.filter('cut', cut)