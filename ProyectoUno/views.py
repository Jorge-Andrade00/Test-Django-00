from django.http import HttpResponse
import datetime

def test(request):
    return HttpResponse("<h1>Hola xd<h1>")
def getFecha(request):
    fecha =datetime.datetime.now()
    html = """
    <h1>fecha y hora actual</h1>
    <br>
    %s
    """%fecha
    return HttpResponse(html)