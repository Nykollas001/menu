from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Grade, TierList, TierItem, UserActivity, DiaryEntry, PasswordStorage
import random

@login_required
def index(request):
    # Obtém estatísticas para o dashboard
    grades_count = Grade.objects.filter(user=request.user).count()
    tierlists_count = TierList.objects.filter(user=request.user).count()
    diary_count = DiaryEntry.objects.filter(user=request.user).count()
    passwords_count = PasswordStorage.objects.filter(user=request.user).count()
    
    # Obtém as últimas notas
    latest_grades = Grade.objects.filter(user=request.user).order_by('-date')[:5]
    
    context = {
        'grades_count': grades_count,
        'tierlists_count': tierlists_count,
        'diary_count': diary_count,
        'passwords_count': passwords_count,
        'latest_grades': latest_grades,
        'user': request.user
    }
    return render(request, 'expenses/index.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('expenses:index')
    else:
        form = UserCreationForm()
    return render(request, 'expenses/register.html', {'form': form})

# Views para Notas (Grades)
@login_required
def grade_list(request):
    grades = Grade.objects.filter(user=request.user).order_by('-date')
    return render(request, 'expenses/grade_list.html', {'grades': grades})

@login_required
def grade_create(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        value = request.POST.get('value')
        date = request.POST.get('date')
        notes = request.POST.get('notes')
        
        if subject and value and date:
            try:
                value = float(value)
                if 0 <= value <= 10:
                    Grade.objects.create(
                        user=request.user,
                        subject=subject,
                        value=value,
                        date=date,
                        notes=notes
                    )
                    messages.success(request, 'Nota adicionada com sucesso!')
                    return redirect('expenses:grade_list')
                else:
                    messages.error(request, 'A nota deve estar entre 0 e 10.')
            except ValueError:
                messages.error(request, 'Nota inválida!')
        else:
            messages.error(request, 'Por favor, preencha todos os campos obrigatórios.')
    
    return render(request, 'expenses/grade_form.html')

@login_required
def grade_edit(request, pk):
    grade = get_object_or_404(Grade, pk=pk, user=request.user)
    
    if request.method == 'POST':
        subject = request.POST.get('subject')
        value = request.POST.get('value')
        date = request.POST.get('date')
        notes = request.POST.get('notes')
        
        if subject and value and date:
            try:
                value = float(value)
                if 0 <= value <= 10:
                    grade.subject = subject
                    grade.value = value
                    grade.date = date
                    grade.notes = notes
                    grade.save()
                    messages.success(request, 'Nota atualizada com sucesso!')
                    return redirect('expenses:grade_list')
                else:
                    messages.error(request, 'A nota deve estar entre 0 e 10.')
            except ValueError:
                messages.error(request, 'Nota inválida!')
        else:
            messages.error(request, 'Por favor, preencha todos os campos obrigatórios.')
    
    return render(request, 'expenses/grade_form.html', {'grade': grade})

@login_required
def grade_delete(request, pk):
    grade = get_object_or_404(Grade, pk=pk, user=request.user)
    grade.delete()
    messages.success(request, 'Nota excluída com sucesso!')
    return redirect('expenses:grade_list')

# Views para Tier Lists
@login_required
def tierlist_list(request):
    tierlists = TierList.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'expenses/tierlist_list.html', {'tierlists': tierlists})

@login_required
def tierlist_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            TierList.objects.create(user=request.user, name=name)
            messages.success(request, 'Tier List criada com sucesso!')
            return redirect('expenses:tierlist_list')
        messages.error(request, 'Por favor, informe um nome para a Tier List.')
    return render(request, 'expenses/tierlist_form.html')

@login_required
def tierlist_detail(request, pk):
    tierlist = get_object_or_404(TierList, pk=pk, user=request.user)
    items = tierlist.items.all()
    return render(request, 'expenses/tierlist_detail.html', {
        'tierlist': tierlist,
        'items': items
    })

@login_required
def tierlist_edit(request, pk):
    tierlist = get_object_or_404(TierList, pk=pk, user=request.user)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            tierlist.name = name
            tierlist.save()
            messages.success(request, 'Tier List atualizada com sucesso!')
            return redirect('expenses:tierlist_list')
        messages.error(request, 'Por favor, informe um nome para a Tier List.')
    
    return render(request, 'expenses/tierlist_form.html', {'tierlist': tierlist})

@login_required
def tierlist_delete(request, pk):
    tierlist = get_object_or_404(TierList, pk=pk, user=request.user)
    tierlist.delete()
    messages.success(request, 'Tier List excluída com sucesso!')
    return redirect('expenses:tierlist_list')

# Views para Tier Items
@login_required
def tieritem_create(request, tierlist_id):
    tierlist = get_object_or_404(TierList, pk=tierlist_id, user=request.user)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        tier = request.POST.get('tier')
        if name and tier:
            TierItem.objects.create(
                tierlist=tierlist,
                name=name,
                tier=tier
            )
            messages.success(request, 'Item adicionado com sucesso!')
            return redirect('expenses:tierlist_detail', pk=tierlist.pk)
        messages.error(request, 'Por favor, preencha todos os campos.')
    
    return render(request, 'expenses/tieritem_form.html', {'tierlist': tierlist})

@login_required
def tieritem_edit(request, pk):
    item = get_object_or_404(TierItem, pk=pk, tierlist__user=request.user)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        tier = request.POST.get('tier')
        if name and tier:
            item.name = name
            item.tier = tier
            item.save()
            messages.success(request, 'Item atualizado com sucesso!')
            return redirect('expenses:tierlist_detail', pk=item.tierlist.pk)
        messages.error(request, 'Por favor, preencha todos os campos.')
    
    return render(request, 'expenses/tieritem_form.html', {'item': item})

@login_required
def tieritem_delete(request, pk):
    item = get_object_or_404(TierItem, pk=pk, tierlist__user=request.user)
    tierlist_id = item.tierlist.pk
    item.delete()
    messages.success(request, 'Item excluído com sucesso!')
    return redirect('expenses:tierlist_detail', pk=tierlist_id)

# Views para Diário
@login_required
def diary_list(request):
    entries = DiaryEntry.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'expenses/diary_list.html', {'entries': entries})

@login_required
def diary_create(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            DiaryEntry.objects.create(user=request.user, content=content)
            messages.success(request, 'Anotação adicionada com sucesso!')
            return redirect('expenses:diary_list')
        else:
            messages.error(request, 'Por favor, escreva algo antes de salvar.')
    return render(request, 'expenses/diary_form.html')

@login_required
def diary_delete(request, pk):
    entry = get_object_or_404(DiaryEntry, pk=pk, user=request.user)
    entry.delete()
    messages.success(request, 'Anotação excluída com sucesso!')
    return redirect('expenses:diary_list')

# Views para Senhas
@login_required
def password_list(request):
    passwords = PasswordStorage.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'expenses/password_list.html', {'passwords': passwords})

@login_required
def password_create(request):
    if request.method == 'POST':
        service = request.POST.get('service')
        password = request.POST.get('password')
        if service and password:
            PasswordStorage.objects.create(
                user=request.user,
                service_name=service,
                password=password
            )
            messages.success(request, 'Senha armazenada com sucesso!')
            return redirect('expenses:password_list')
        messages.error(request, 'Por favor, preencha todos os campos.')
    return render(request, 'expenses/password_form.html')

# View para Cartas
@login_required
def draw_card(request):
    cards = {
        1: {
            'title': 'Aspecto Masculino - Lição Atual',
            'message': 'Esta carta revela sua atual lição no aspecto Yang (masculino). '
                      'Foque em ação, iniciativa e expressão externa. '
                      'É um momento para liderar e manifestar suas ideias no mundo.',
            'icon': 'mars'
        },
        2: {
            'title': 'Aspecto Feminino - Lição Atual',
            'message': 'Esta carta mostra sua lição presente no aspecto Yin (feminino). '
                      'Dê atenção à sua intuição, sentimentos e vida interior. '
                      'É hora de nutrir, acolher e compreender.',
            'icon': 'venus'
        },
        3: {
            'title': 'Desafio do Aspecto Masculino',
            'message': 'Aqui está seu atual desafio no aspecto Yang (masculino). '
                      'Observe onde você pode estar sendo muito agressivo ou passivo. '
                      'Encontre o equilíbrio na sua força e determinação.',
            'icon': 'fist-raised'
        },
        4: {
            'title': 'Desafio do Aspecto Feminino',
            'message': 'Este é seu desafio presente no aspecto Yin (feminino). '
                      'Reflita sobre suas emoções e conexões. '
                      'Busque harmonia entre sentir e agir.',
            'icon': 'heart'
        },
        5: {
            'title': 'Assistência dos Ancestrais',
            'message': 'Uma mensagem de sabedoria dos seus ancestrais. '
                      'Eles oferecem apoio e orientação no seu caminho. '
                      'Confie na sabedoria que flui através das gerações.',
            'icon': 'tree'
        }
    }
    
    card_number = random.randint(1, 5)
    card = cards[card_number]
    
    return render(request, 'expenses/card.html', {
        'card_number': card_number,
        'card_title': card['title'],
        'card_message': card['message'],
        'card_icon': card['icon']
    })

# View para Atividade dos Usuários
def is_superuser(user):
    return user.is_superuser

@user_passes_test(is_superuser)
def user_activity(request):
    activities = UserActivity.objects.select_related('user').all()
    return render(request, 'expenses/admin/user_activity.html', {'activities': activities})
