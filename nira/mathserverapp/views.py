from django.shortcuts import render
def mileage(request):
    distance = int(request.POST.get('distance', '0'))
    efficiency = int(request.POST.get('efficiency', '1'))
    mileage = distance/efficiency if request.method == 'POST' else 0
    print("distance=",distance)
    print("efficiency=",efficiency)
    print("mileage=",mileage)
    return render(request, 'mathserverapp/math.html', {'distance': distance, 'efficiency': efficiency, 'mileage': mileage})

