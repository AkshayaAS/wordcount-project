#new views for this website
from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter
import operator

#def home(request):
#    return HttpResponse("Hello")

def home_page(request):
    return render(request,'home.html',{'users':"to all of YOU :)"})
    
def count(request):
    texts=request.GET["fulltext"] # here fulltext is the NAME of textarea in home.html and variable texts holds all those values here using GET
    #now pass the value texts and the count_of_words into the count.html page using dictionary (key-value pairs) as below
    
    count_of_words = texts.split()
    print(texts,len(count_of_words))
    
    count_of_each = Counter(count_of_words)
    
    return render(request,'count.html',{"fulltext":texts,"count":len(count_of_words),"each_count":sorted(count_of_each.items(),key=operator.itemgetter(1,0),reverse=True)})
    
def aboutus(request):
    return render(request,'aboutus.html') #page to describe ABOUT
