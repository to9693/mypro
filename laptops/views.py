from django.shortcuts import render
from .models import Program, Graphic, Laptop
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    programs = Program.objects.all()

    context = {
        'programs': programs,
    }

    return render(request, 'laptops/index.html', context)
    

def detail(request, program_pk):
    # 1. Program ID를 주소로 부터 가져옴 + Program에서 pk에 해당하는 program 가져옴
    program = Program.objects.get(pk=program_pk)

    # 2. program을 돌릴 수 있는 그래픽 다 가져옴
    graphics = program.graphics.all()

    # 3. graphic이 장착된 laptop 가져오기 (for)
    laptops = []
    for graphic in graphics:
        for laptop in graphic.laptops.order_by('price'):
            laptops.append(laptop)

    context = {
        'graphics': graphics,
        'laptops': laptops,
    }

    return render(request, 'laptops/detail.html', context)