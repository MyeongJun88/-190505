from django.shortcuts import render
#1. 회원가입 페이지 - 자기소개(아이디, 비밀번호, 이름, 나이, 학년, 학교, 자기소개, 백앤드, 프론트 앤드 선택), 완료 버튼(비어있는 부분이 있으면 오류창?)/ 회원가입 버튼 클릭시 - introduce.html
# Create your views here.
def login(request):
    if request.method == "POST":
        title = request.POST.get('title')
        writer = request.POST.get('writer')
        ddate = request.POST.get('ddate')
        deadline = request.POST.get('deadline')
        content = request.POST.get('content')
        lion = Lion(title=title, content=content)
        lion.save()
        return redirect('main')
    return render(request, 'lion/login.html')
    
    
def writing(request):
    if request.method == "POST":
        title = request.POST.get('title')
        writer = request.POST.get('writer')
        ddate = request.POST.get('ddate')
        major = request.POST.get('majomajor')
        description = request.POST.get('description')
        created_at = request.POST.get('created_at')
        player = Players(title=title, age=age, description=description, created_at=created_at)
        player.save()
        return redirect('list')
        
    return render(request, 'players/create0.html')