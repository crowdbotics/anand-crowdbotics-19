from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    packages = [
	{'name':'aa_airtable', 'url': 'http://pypi.python.org/pypi/aa_airtable/0.2'},
	{'name':'199Fix', 'url': 'http://pypi.python.org/pypi/199Fix/1.1.2'},
	{'name':'15five-django-ajax-selects', 'url': 'http://pypi.python.org/pypi/15five-django-ajax-selects/1.5.2.155'},
    ]
    context = {
        'title': 'anand-crowdbotics-19',
        'packages': packages
    }
    return render(request, 'home/index.html', context)
