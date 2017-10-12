from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from .models import Product, Comment
from django.template.context import RequestContext


def index(request):
    products = Product.objects.all()
    context={'products' : products}
    return render(request, 'shopping/index.html', context)

def show(request, resource_id):
    product = Product.objects.get(id=resource_id)
    comments= product.comment_set.all()
    context={'product' : product, 'comments' : comments}
    return render(request, 'shopping/show.html', context)


def comment(request):
	product = Product.objects.get(id=request.POST['product'])
	Comment.objects.create(user=request.user, product=product, content=request.POST['comment'])

	return HttpResponseRedirect('/product/%s' % product.id)