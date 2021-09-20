from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from table_app.models import list_of_categories, User, Ad


class BasicView(View):
    def get(self, request):
        categories = list_of_categories
        authors = User.objects.all()
        ctx = {'categories':categories, 'authors':authors}
        return render(request, 'basic_view.html', ctx)

    def post(self,request):
        category = request.POST.get('category')
        author = request.POST.get('author')
        keyword = request.POST.getlist('keyword')
        if keyword and category and author:
            all_ads = Ad.objects.all()
            contents = []
            chosen_ads = []
            for ad in all_ads:
                if keyword in ad.content:
                    contents.append(ad.id)
            for i in range(0, len(contents)):
                chosen_ad=Ad.objects.get(category=category, user=author, id=contents[i])
                chosen_ads.append(chosen_ad)
        if category and author:
            chosen_ads = Ad.objects.get(category=category, user=author)
        elif author:
            chosen_ads = Ad.objects.get(user=author)
        elif category:
            chosen_ads = Ad.objects.get(category=category)

        return HttpResponse(chosen_ads)

# może zrobić w JS wybieranie kategorii i autora, a później jeden wspólny submit?

class AddUser(View):
    def get(self,request):
        return render(request, 'add_user.html')
    def post(self, request):
        name= request.POST.get('name')
        surname = request.POST.get('surname')
        phone_number = request.POST.get('phone')
        email=request.POST.get('email')

        if name and surname and email and phone_number:
            User.objects.create(name=name, surname=surname, phone_number=phone_number, email=email)
        elif name and surname and email:
            User.objects.create(name=name, surname=surname, email=email)
        else:
            return HttpResponse("Podaj właściwe dane")
        return HttpResponse('Zarejestrowano autora ogłoszeń')


class NewAd(View):
    def get(self, request):
        categories = list_of_categories
        authors = User.objects.all()
        ctx = {'categories':categories, 'authors':authors}
        return render(request, 'new_ad.html', ctx)
    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        active = request.POST.get('active') == 'on'
        category = int(request.POST.get('category'))
        user = int(request.POST.get('author'))
        new_ad = Ad.objects.create(title=title, content=content, active=active, user_id=user)
        new_ad.category.add(category)
        return HttpResponse('Dodano ogłoszenie')