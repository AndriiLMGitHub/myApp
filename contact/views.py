from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import django
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError

from django import forms

# Create your views here.
"""def contact(request):
	return render(request, 'contact/contact.html', {})"""


class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	sender = forms.EmailField()
	message = forms.CharField()
	copy = forms.BooleanField(required=False)
	name = forms.CharField(max_length=100)



# Функция формы обратной связи
def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST, request.FILES)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
		if form.is_valid():
			subject = form.cleaned_data['subject']
			sender = form.cleaned_data['sender']
			message = form.cleaned_data['message']
			copy = form.cleaned_data['copy']
			name = form.cleaned_data['name']

			recepients = ['andreydecua@gmail.com']

			global_message = "Імя: " + name + "\n" + "Повідомлення: " + message + "\n"

            # Если пользователь захотел получить копию себе, добавляем его в список получателей
			if copy:
				recepients.append(sender)
			try:
				send_mail(subject, global_message, 'andreydecua@gmail.com', recepients)
			except BadHeaderError: #Защита от уязвимости
				return HttpResponse('Invalid header found')
			# Переходим на другую страницу, если сообщение отправлено
			return render(request, 'contact/thanks.html', {})

		else:
			form = ContactForm()
	# Выводим форму в шаблон
	return render(request, 'contact/contact.html')



"""def thanks(reguest):
	thanks = 'thanks'
	return render(request, 'contact/thanks.html', {'thanks': thanks})"""
