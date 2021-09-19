from django.shortcuts import render
from django.views import View


class BasicView(View):
    def get(self, request):
        return render(request, 'basic_view.html')

    def post(self,request):
        pass

# może zrobić w JS wybieranie kategorii i autora, a później jeden wspólny submit?
