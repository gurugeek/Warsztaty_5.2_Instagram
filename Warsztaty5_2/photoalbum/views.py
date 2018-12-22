from django.shortcuts import render

from django.views import View


class MainView(View):
    def get(self, request):
        return render(request, "photoalbum/content_page.html", locals())
