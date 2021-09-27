from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from main_app.models import list_of_categories, User, Ad


class BasicView(View):
    def get(self, request):
        categories = list_of_categories
        authors = User.objects.all()
        ctx = {'categories': categories, 'authors':authors}
        return render(request, 'basic_view.html', ctx)

    def post(self,request):
        categories = request.POST.getlist('category')
        authors = request.POST.getlist('author')
        keywords = str(request.POST.get('keyword'))
        chosen_ads = []

        if categories or authors or keywords:

            if keywords:
                result = Ad.objects.filter(content__icontains=keywords)
                result2 = Ad.objects.filter(title__icontains=keywords)
                if result:
                    for item in result:
                        chosen_ads.append(item)
                elif result2:
                    for item in result2:
                        chosen_ads.append(item)
                else:
                    pass

            if categories:
                for i in range(0, len(categories)):
                    result = Ad.objects.get(category=int(categories[i]))
                    if result not in chosen_ads:
                        chosen_ads.append(result)

            if authors:
                for i in range(0, len(authors)):
                    result = Ad.objects.get(user=int(authors[i]))
                    if result not in chosen_ads:
                        chosen_ads.append(result)

        else:
            return HttpResponse('podaj kryteria wyszukiwania')

        if len(chosen_ads) > 0:
            ctx = {'chosen_ads': chosen_ads}
            return render(request, "filtered_ads.html", ctx)
        else:
            return HttpResponse('nie znaleziono ogłoszeń')

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
        new_ad = Ad.objects.create(title=title, content=content, active=active, category=category, user_id=user)
        return HttpResponse('Dodano ogłoszenie')


# dodać widoki: - wyświetlania wyszukanych ogłoszeń