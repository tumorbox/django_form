from django.shortcuts import render

# Create your views here.
def loop(request):
    nums = []
    for data in range(10):
        nums.append(data)
    context = {
        'nums': nums
    }
    return render(request, 'loop.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    # request parameter는 요청 정보가 담겨있다.
    # request.GET == 딕셔너리와 유사하다.
    # request.GET != dict()
    # data = request.GET['message']
    data = request.GET.get('message')
    context ={ 
        'data': data
    }
    return render(request, 'catch.html', context)
