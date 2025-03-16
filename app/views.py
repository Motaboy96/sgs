from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import metrics


@login_required(login_url='login')
def home(request):
    product_metrics = metrics.get_product_metrics()

    context = {
        'product_metrics': product_metrics,
    }
    
    return render(request, 'home.html', context)



    