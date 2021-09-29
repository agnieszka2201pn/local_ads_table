import datetime


def my_cp(request):
    context = {
        'now': datetime.datetime.now(),
        'version': '1.0'
    }
    return context