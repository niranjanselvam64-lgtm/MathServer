# Ex.04 Design a Website for Server Side Processing
## Date:12/12/2025

## AIM:
To create a web page to calculate vehicle mileage and fuel efficiency using server-side scripts.

## FORMULA:
M = D / F
<br> M --> Mileage (in km/l)
<br> D --> Distance Travelled (in km)
<br> F --> Fuel Consumed (in l)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM:
```
math.html
<html>
    <head>
        <title>
            efficiency
        </title>
        <style>
            body
            {
               background-color: rgb(210, 210, 27);
            }
            .box
            {
               width: 600px;
               height: 300px;
               background-color: red;
               border:dotted 3px black;
               padding: 10px;
               margin-left: 275px;
               margin-top: 200px;
               position:fixed;
               top: 100px;
               left: 275px; 
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h2 align="center"> EFFICIENCY OF A VEHICLE</h2>
            <h3 align="center">Niranjan S (25004141) </h3>
            <h2 align="center">MILEAGE CALCULATION</h2>
            <form method="post" align="center">
                {% csrf_token %}
                <label>Distance:</label>
                <input type="text" name="distance" value="{{ distance }}">
                <br>
                <br>
                <label>Fuel Consumed:</label>
                <input type="text" name="efficiency" value="{{ efficiency}}">
                <br>
                <br>
                <input type="submit" value="calculate">
                <br>
                <label>Mileage:</label>
                <input type="text" name="mileage" value="{{ mileage }}">
            </form>
        </div>
    </body>
</html>

views.py
from django.shortcuts import render
def mileage(request):
    distance = int(request.POST.get('distance', '0'))
    efficiency = int(request.POST.get('efficiency', '1'))
    mileage = distance/efficiency if request.method == 'POST' else 0
    print("distance=",distance)
    print("efficiency=",efficiency)
    print("mileage=",mileage)
    return render(request, 'mathserverapp/math.html', {'distance': distance, 'efficiency': efficiency, 'mileage': mileage})

    urls.py
    rom django.contrib import admin
from django.urls import path
from mathserverapp import views
urlpatterns = [path('',views.mileage,name='vehicle')]

```

## OUTPUT - SERVER SIDE:
![alt text](<Screenshot (41).png>)

## OUTPUT - WEBPAGE:
![alt text](<Screenshot (40)-1.png>)

## RESULT:
The a web page to calculate vehicle mileage and fuel efficiency using server-side scripts is created successfully.
