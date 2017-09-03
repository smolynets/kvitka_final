# -*- coding: utf-8 -*-
from .models import Flower
from django.utils.translation import ugettext as _


def basket_list(request):
	flowers=Flower.objects.all()
	list = []
	for p in flowers:
		p = request.COOKIES.get(p.lat_title)
		if p:
			c=Flower.objects.get(lat_title=p)
			if c:
				list.append(c)
	return list



def suma(request):
    flowers=Flower.objects.all()
    price_list = 0
    for p in flowers:
      p = request.COOKIES.get(p.lat_title)
      if p:
        c=Flower.objects.get(lat_title=p)
        if c:
          price_list = price_list + int(c.price)
    return price_list



def flow_count_name(request):
  count = len(basket_list(request))
  if count == 1:
     a='квітка'
  elif count > 1 and count<5:
     a='квітки'
  elif count > 4:
     a='квіток'
  elif count == 0:
  	return None
  else:
     return 0
  return a



def is_digit(string):
    if string.isdigit():
       return 1
    else:
        try:
            float(string)
            return None
        except ValueError:
            return None




def get_lang(request):
  if request.COOKIES.get('django_language') == 'en':
     pk = 'english'
     return pk
  elif request.COOKIES.get('django_language') == 'uk':
     pk = u'українська'
     return pk
  else:
     pk = u'українська'
     return pk