from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from itertools import chain
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import person

def list_person(request):
    l = 10
    personlist = person.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(personlist, l)
    try:
        personlist = paginator.page(page)
    except PageNotAnInteger:
        personlist = paginator.page(1)
    except EmptyPage:
        personlist = paginator.page(paginator.num_pages)
    return render(request, 'personlist.html', {'personlist': personlist })

def add(request):
    person_data = person.objects.all()
    if request.method == "POST":
        reg_no = request.POST.get('reg_no')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        grand_father = request.POST.get('grand-fathername')
        qualification = request.POST.get('qlu')
        sername = request.POST.get('sername')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        Frno = request.POST.get('Frno')
        email = request.POST.get('email')
        images =request.FILES.get('image')
        new_person = person(registerno=reg_no,father_registerno=Frno, first_name=first_name, last_name=last_name,
                            g_father=grand_father, sername=sername, address=address,
                            qualification=qualification,phone=phone, email=email, image=images)
        new_person.save()
        return redirect('home')
    return render(request, "add.html")

def edit(request, id):
    person_id = person.objects.get(id=id)
    if request.method == "POST":
        person_id.registerno = request.POST.get('reg_no')
        person_id.father_registerno = request.POST.get('Frno')
        person_id.first_name = request.POST.get('first_name')
        person_id.last_name = request.POST.get('last_name')
        person_id.sername = request.POST.get('sername')
        person_id.g_father = request.POST.get('grand-fathername')
        person_id.address = request.POST.get('address')
        person_id.qualification = request.POST.get('qlu')
        person_id.phone = request.POST.get('phone')
        person_id.email = request.POST.get('email')
        person_id.qualification = request.POST.get('qlu')
        person_id.save()
        return redirect('home')
    return render(request, 'edit.html', {'person': person_id})

def delete(request, id):
    person_id = person.objects.get(id=id)
    person_id.delete()
    return redirect('home')

def search(request):
    person_data = person.objects.all()
    q = request.POST.get('query')
    if q:
        nameResult = person.objects.filter(Q(first_name__contains=q))
        nregisternoResult = person.objects.filter(Q(registerno__contains=q))
        lastname = person.objects.filter(Q(last_name__contains=q))
        sername = person.objects.filter(Q(sername__contains=q))
        phoneResult = person.objects.filter(Q(phone__contains=q))
        mainresult = list(chain(phoneResult, nameResult, sername, lastname, nregisternoResult))

    data = {'q':q, 'personlist':mainresult}
    return render(request, 'personlist.html', data)


def deshboard(request):
    persons = person.objects.all()
    person_length = len(persons)
    return render(request, 'deshboard.html',{'person_length':person_length})

def imageEdit(request, id):
    image_id = person.objects.get(id=id)
    image_id.image =request.FILES.get('image')
    image_id.save()
    return render(request, 'edit.html', {'person': image_id})

