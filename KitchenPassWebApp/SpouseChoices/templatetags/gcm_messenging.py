'''
Created on Jul 11, 2014

@author: toantran
'''
from django import template
from gcm.models import get_device_model

register = template.Library()

@register.filter
def send_phone(Device, args):
    phone = get_device_model().objects.get(name="device1")
    phone.send_message(args, collapse_key='something')