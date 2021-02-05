from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import requests
from random import randint
# from .forms import ContactForm

# Create your views here.
# def index(request): return render(request, 'form.html', {})

""" 
def indexView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            your_email = form.cleaned_data['your_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, your_email, ['preciousolusola16@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')

    return render(request, "form.html", {'form': form})

 """

def GetQUote():
    try:
        quote = requests.get("https://type.fit/api/quotes")
        lenght = len(quote.json())
        get_random = randint(1,lenght)

        response_quote = quote.json()[get_random]
        response_quote['type'] = 'success'
        return response_quote
    except:
        return {'text':"There is no WIFI in the forest, But you will find a better connection. Please subscribe", 'author':"App Author", "type": "danger"}


def indexView(request):
    global quote
    if request.method == 'POST':
        # form = ContactForm()
        name = request.POST['name']
        subject = request.POST['subject']
        
        email = request.POST['email']
        body = request.POST['content']

        

        try:
            send_mail(subject, body, email, [
                      'precious.olusola@geeksvillage.com'])
        except BadHeaderError:
                return HttpResponse('Invalid header found.')
        return redirect('success')

    else:
        
        quote = GetQUote()
        #print(quote)
        return render(request, "form.html", {'quote':quote})



def successView(request):
    #return HttpResponse('Success! Thank you for your message.')
    return render(request, "success.html", {'quote': quote})
