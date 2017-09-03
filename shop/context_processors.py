from .util import basket_list
from .cart import Cart
from .util import get_lang

def buy_processor(request):
	return {'buy_status': basket_list(request)}



def cart(request):
    return {'cart': Cart(request)}



#select language
def lang_processor(request):
	return {'PK': get_lang(request)}
