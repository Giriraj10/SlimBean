from SlimBean.common.common_imports import *

data = {
    "movies":[
        {
            "id":0,
            "name":"Jaws",
            "year":1998
        },
        {
            "id":1,
            "name":"Shawshank Redemption",
            "year":2000
        }
    ]
}

def home(request):
    return HttpResponse("Home!")

def home_page(request):
    return render(request , 'oneview/oneview.html',data)

