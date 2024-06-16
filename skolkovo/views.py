from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render

from skolkovo.forms import CompanyForm, ProductForm
from skolkovo.models import Company, Product


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def grants(request):
    return render(request, 'grants.html', {})


def services(request):
    return render(request, 'services.html', {})


def navigator(request):
    companies = Company.objects.all()
    return render(request, 'navigator.html', {'companies': companies})


# Показываем список компаний и продуктов пользователя, он должен быть залогинен
@login_required
def my_companies(request):
    companies = Company.objects.filter(owner=request.user)
    context = {'company_form': CompanyForm(),
               'product_form': ProductForm(),
               'companies': companies
               }
    return render(request, 'my_companies.html', context)


# Обработка формы создания новой компании, автоматически проверяем, что пользователь залогинен
@login_required
def create_company(request):
    # Проверяем корректность вида запроса
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        # Средствами Django валидируем данные формы
        if form.is_valid():
            company = Company(owner=request.user, # Владелец компании по умолчанию залогиненный пользователь
                              name=form.cleaned_data['name'],
                              creation_date=form.cleaned_data['creation_date'],
                              inn=form.cleaned_data['inn'],
                              )
            company.save()
    # Обновляем пользователю страницу
    return HttpResponseRedirect('/navigator/my_companies/')


# Обработка формы создания нового продукта
@login_required
def create_product(request, company_id=0):
    if request.method == 'POST':
        try:
            company = Company.objects.get(id=company_id)
            # Проверяем, что продукт создается пользователем для своей, а не чужой компании
            if company.owner != request.user:
                return HttpResponseRedirect('/navigator/my_companies/')
        except ObjectDoesNotExist:
            return HttpResponseRedirect('/navigator/my_companies/')
        form = ProductForm(request.POST)
        if form.is_valid():
            product = Product(company=company,
                              name=form.cleaned_data['name'],
                              description=form.cleaned_data['description'],
                              price=form.cleaned_data['price'],
                              )
            product.save()
    return HttpResponseRedirect('/navigator/my_companies/')


@login_required
def delete_company(request, company_id=0):
    try:
        company = Company.objects.get(id=company_id)
        # Проверяем, что пользователь пытается удалить свою компанию
        if company.owner != request.user:
            return HttpResponseRedirect('/navigator/my_companies/')
        company.delete()
        return HttpResponseRedirect('/navigator/my_companies/')
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/navigator/my_companies/')


@login_required
def delete_product(request, product_id=0):
    try:
        product = Product.objects.get(id=product_id)
        # Проверяем, что пользователь пытается удалить продукт своей компании
        if product.company.owner != request.user:
            return HttpResponseRedirect('/navigator/my_companies/')
        product.delete()
        return HttpResponseRedirect('/navigator/my_companies/')
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/navigator/my_companies/')


# Выходим из аккаунта
def quick_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
