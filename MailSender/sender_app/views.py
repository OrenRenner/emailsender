from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage
from django.http import JsonResponse

def main(request):
    return render(request, "index.html")


def sender(request):
    emails = request.GET.get("emails", "")
    theme = request.GET.get("theme", "")
    body = request.GET.get("body", "")
    emails = emails.split("|")
    if "" in emails:
        emails.remove("")
    emails = list(set(emails))
    
    if True:
        try:
            email = EmailMessage(theme, body, to=emails)
            email.send()
        except BadHeaderError:
            return JsonResponse({"data": "1"}, status=400)
        return JsonResponse({"data": "0"}, status=200)
    else:
        return JsonResponse({"data": "1"}, status=400)