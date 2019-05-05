from django.shortcuts import render, get_object_or_404
from .models import Lion
#1. 회원가입 페이지 - 자기소개(아이디, 비밀번호, 이름, 나이, 학년, 학교, 자기소개, 백앤드, 프론트 앤드 선택), 완료 버튼(비어있는 부분이 있으면 오류창?)/ 회원가입 버튼 클릭시 - introduce.html
# Create your views here.
def login(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        identity = Identity(username=username, password=password)
        identity.save()
    return render(request, 'lion/login.html')
    
def main(request):
    lion = Lion.objects.all()
    return render(request, 'main.html', {'lion' : lion})
    
 #글 작성 페이지   
def writing(request):
    if request.method == "POST":
        title = request.POST.get('title')
        writer = request.POST.get('writer')
        ddate = request.POST.get('ddate')
        major = request.POST.get('major')
        description = request.POST.get('description')
        people = request.POST.get('people')
        created_at = request.POST.get('created_at')
        lion = Lion(title=title, writer=writer, ddate=ddate, major=major, description=description, people=people, created_at=created_at)
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
        lion.save()
        return redirect('login', lion.pk)
      
#수정기능
def edit(request, id):
    lion =  get_object_or_404(Lion, pk=id)
    return render(request, 'lion/edit.html', {'lion' : lion})
    
# 글삭제 기능
def delete(request, id):
    if request.method == "POST":
        lion = Lion.objects.get(pk=id)
        lion.delete()
        return redirect('main')