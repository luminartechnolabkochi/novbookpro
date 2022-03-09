from django.shortcuts import render
from owner.forms import BookForm
from django.views.generic import View


class AddBook(View):
    def get(self,request):
        form=BookForm()
        return render(request,"add_book.html",{"form":form})
    def post(self,request):
        form=BookForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print(form.cleaned_data.get("book_name"))
            print(form.cleaned_data.get("author"))
            print(form.cleaned_data.get("price"))
            print(form.cleaned_data.get("copies"))

            return render(request,"add_book.html",{"msg":"book created"})
        else:
            return render(request, "add_book.html", {"form": form})





# Create your views here.

# add book
#list all book

# book detail

# edit book

#delete book