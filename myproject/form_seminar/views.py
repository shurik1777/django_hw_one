from django.shortcuts import render
from .forms import RandomForm
import random


def flip_coin(request, tryes: int):
    flips_list = [random.choice(["Орёл", "Решка"]) for _ in range(tryes)]
    context = {"title": "Flip coin", "content": flips_list}
    return render(request, "form_seminar/coin.html", context)


def roll_cube(request, tryes: int):
    cubes_list = [random.randint(1, 6) for _ in range(tryes)]
    context = {"title": "Cube game", "content": cubes_list}
    return render(request, "form_seminar/coin.html", context)


def random_number(request, tryes: int):
    cubes_list = [random.randint(1, 100) for _ in range(tryes)]
    context = {"title": "Random numbers", "content": cubes_list}
    return render(request, "form_seminar/coin.html", context)


def perform_action(request):
    if request.method == "POST":
        form = RandomForm(request.POST)
        if form.is_valid():
            result = form.cleaned_data['event_type']
            attempts = form.cleaned_data['attempts']
            if result == "coin":
                return flip_coin(request, attempts)
            elif result == "dice":
                return roll_cube(request, attempts)
            elif result == "number":
                return random_number(request, attempts)
    else:
        form = RandomForm()
    return render(request, "form_seminar/games_f.html", {"form": form})
