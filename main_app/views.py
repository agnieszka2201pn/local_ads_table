from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from main_app.models import list_of_categories, Ad


class BasicView(View):
    def get(self, request):
        categories = list_of_categories
        ctx = {'categories': categories}
        return render(request, 'main_app/basic_view.html', ctx)

    def post(self,request):
        category = request.POST.get('category')
        keyword = str(request.POST.get('keyword'))
        chosen_ads = []

        if category == '7':
            filtered_ads = Ad.objects.filter(content__icontains=keyword)
            for ad in filtered_ads:
                chosen_ads.append(ad)
        else:
            filtered_ads = Ad.objects.filter(category=category).filter(content__icontains=keyword)
            for ad in filtered_ads:
                chosen_ads.append(ad)

        if chosen_ads:
            ctx = {'chosen_ads': chosen_ads}
            return render(request, "main_app/chosen_ads.html", ctx)
        else:
            return HttpResponse('nie znaleziono ogłoszeń')


class NewAd(View):
    def get(self, request):
        categories = list_of_categories
        ctx = {'categories':categories}
        return render(request, 'main_app/new_ad.html', ctx)
    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        category = int(request.POST.get('category'))
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        new_ad = Ad.objects.create(title=title, content=content, category=category, contact=contact, password=password)
        return redirect('/all_ads/')


class AllAds(View):
    def get(self, request):
        chosen_ads = Ad.objects.all()
        ctx = {'chosen_ads':chosen_ads}
        return render(request, 'main_app/chosen_ads.html', ctx)

class RemoveAd(View):
    def get(self, request, ad_id):
        ad = Ad.objects.get(id = ad_id)
        return render(request, 'main_app/remove_ad.html', {'ad':ad})

    def post(self, request, ad_id):
        ad_to_remove = Ad.objects.get(id=ad_id)
        password = request.POST.get('password')
        if password == ad_to_remove.password:
            ad_to_remove.delete()
            return redirect('/basic_view/')
        else:
            return HttpResponse('podaj właściwe hasło')
