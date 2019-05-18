from django.http import HttpResponse
from django.shortcuts import render

def contact(request):
      return render(request, 'contact.html')
def about(request):
      return render(request,'about.html')
def index2(request): 
      return render( request,'index2.html') 
def remove_punc(text):
      pun = '''{}[]:;<>?*()*&^%$#@_-"'||'''
      mtext = ''
      for i in text:
            if i not in pun: mtext = mtext + i
      return mtext            

def remove_space(text):
      return  text.replace(' ', '')            


def analyze2(request):
      dtext = request.POST.get('text', 'default')
      removepunc = request.POST.get('removepunc','off')
      removespace = request.POST.get('removespace','off')
      selected = ""
      if removepunc == 'on': 
            dtext = remove_punc(dtext)
            selected = selected + " Remove Punctuation"
      if removespace == 'on': 
            dtext = remove_space(dtext)
            selected = selected + " Remove Spaces"      
      param = {'purpose': selected , "Anayzed_Text": dtext}
      return render(request, 'analyze2.html', param)
