from django.shortcuts import render, redirect, get_object_or_404
from .models import Lion


def login(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        identity = Identity(username=username, password=password)
        identity.save()
    return render(request, 'lion/accounts/login.html')
    
def main(request):
    lion = Lion.objects.all()
    return render(request, 'main.html', {'lion' : lion})
    
 #글 작성 페이지   
def writing(request):
    if request.method == "POST":
        title = request.POST.get('title')
        writer = request.POST.get('writer')
        #ddate = request.POST.get('ddate')
       # major = request.POST.get('major')
        description = request.POST.get('description')
        deadline = request.POST.get('deadline')
       # people = request.POST.get('people')
        #created_at = request.POST.get('created_at')
        image = request.FILES['image']
        location = request.POST.get('location')
        lion = Lion(title=title, description=description, location=location, image=image, deadline=deadline, writer=writer)
        lion.save()
        return redirect('main')
    return render(request, 'lion/writing.html')
    
   #상세내용 페이지 
def detail(request, post_id):
    lion =  get_object_or_404(Lion, pk=post_id)
    default_view_count = lion.view_count
    lion.view_count = default_view_count + 1
    lion.save()
    return render(request, 'lion/detail.html', {'lion': lion})
    
#회원정보 수정 페이지     
def edituser(request, id):
    if request.method == "POST":
        title = request.POST.get('title')
        writer = request.POST.get('writer')
        ddate = request.POST.get('ddate')
        major = request.POST.get('major')
        description = request.POST.get('description')
        people = request.POST.get('people')
        created_at = request.POST.get('created_at')
        lion = Lion(title=title, writer=writer, ddate=ddate, major=major, description=description, people=people, created_at=created_at)
        return redirect('login', lion.pk)
      
#글수정기능
def edit(request, id):
    lion =  get_object_or_404(Lion, pk=id)
    return render(request, 'lion/edit.html', {'lion' : lion})
    
# 글삭제 기능
def delete(request, id):
    if request.method == "POST":
        lion = Lion.objects.get(pk=id)
        lion.delete()
        return redirect('main')
        
        
def update(request, id):
    if request.method == "POST":
        lion = Lion.objects.get(pk=id)
        title = request.POST.get('title')
        description = request.POST.get('description')
        writer = request.POST.get('writer')
        location = request.POST.get('location')
        deadline = request.POST.get('deadline')
        image = request.FILES['image']
        lion.title = title
        lion.description = description
        lion.location = location
        lion.writer = writer
        lion.image = image
        lion.deadline = deadline
        lion.save()
        return redirect('main')
        
