from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def reverse(request):
    user_text = request.GET['usertext']
    count_of_words = len(user_text.split())
    reversed_text = user_text[::-1]
    return render(request, 'reverse.html', {'usertext': user_text, 'reversedtext': reversed_text,
                                            'words': count_of_words})
