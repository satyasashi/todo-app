from django.contrib.admin import widgets
from django.conf import settings
from django import forms
from bootstrap_datepicker_plus import DateTimePickerInput
from django.core.exceptions import ValidationError
from .models import Task, SubTask
import datetime

PENDING=[('Pending','Pending')]
COMPLETED=[('Completed','Completed')]

STATUS = [('Pending','Pending'), ('Completed', 'Completed')]


class TodoForm(forms.ModelForm):
    sub_tasks = forms.CharField(label="Sub Tasks", required=False)
    due_date = forms.DateTimeField(label="Due-Date format yyyy-mm-dd hh:mm", widget=DateTimePickerInput(format='%Y-%m-%d %H:%M'))
    notify_before = forms.IntegerField(initial=1, label="Mention number of hours before 'Due-Date' time you want to get notified.")
    status = forms.ChoiceField(choices=STATUS, widget=forms.RadioSelect())

    def clean_sub_tasks(self):
        sub_tasks = self.cleaned_data['sub_tasks']
        print(sub_tasks)
        return sub_tasks

    def clean_notify_before(self):
        notify_before = self.cleaned_data['notify_before']
        if notify_before < 1:
            notify_before = 1
        return notify_before

    def save(self):
        result = Task.objects.create(
            title = self.cleaned_data['title'],
            description = self.cleaned_data['description'],
            due_date = self.cleaned_data['due_date'],
            notify_before = self.cleaned_data['notify_before'],
            status = self.cleaned_data['status']
            )    
        print("todo created")
        subtask = self.cleaned_data['sub_tasks']
        if len(subtask) > 0:
            if created:
                result2 = SubTask.objects.create(subtask_title=self.cleaned_data['sub_tasks'], task=result)
                print("subtask saved")
        return


    def update_save(self, pk):
        result = Task.objects.get(id=pk)
        result.title = self.cleaned_data['title']
        result.description = self.cleaned_data['description']
        result.due_date = self.cleaned_data['due_date']
        result.notify_before = self.cleaned_data['notify_before']
        result.status = self.cleaned_data['status']
        result.save()
        subtask = self.cleaned_data['sub_tasks']
        if len(subtask) > 0:
            if result:
                result2 = SubTask.objects.create(subtask_title=self.cleaned_data['sub_tasks'], task=result)
                print("subtask saved")
        return

    class Meta:
        model = Task
        fields = ['title', 'sub_tasks', 'description', 'due_date', 'notify_before', 'status']
        exclude = ['created_on', 'soft_del', 'soft_del_timestamp']

    # def __init__(self, *args, **kwargs):
    #     super(TodoForm, self).__init__(*args, **kwargs)
    #     self.fields['due_date'].widget = widgets.AdminDateWidget()
    #     self.fields['due_date'].widget.attrs.update({'id': 'datetimepicker'})


# class UpdateTodoForm(forms.ModelForm):
#     sub_tasks = forms.CharField(label="Sub Tasks", required=False)
#     due_date = forms.DateTimeField(label="Due-Date format yyyy-mm-dd hh:mm", widget=DateTimePickerInput(format='%Y-%m-%d %H:%M'))
#     notify_before = forms.IntegerField(label="Mention number of hours before 'Due-Date' time you want to get notified.")
#     status = forms.ChoiceField(choices=STATUS, widget=forms.RadioSelect())

#     def clean_sub_tasks(self):
#         sub_tasks = self.cleaned_data['sub_tasks']
#         print(sub_tasks)
#         return sub_tasks

#     def save(self):
#         result = Task.objects.get(title=self.cleaned_data['title'])
#         subtask = self.cleaned_data['sub_tasks']
#         if len(subtask) > 0:
#             if result:
#                 result2 = SubTask.objects.create(subtask_title=subtask, task=result)
#                 print("subtask saved")
#         return
    
#     class Meta:
#         model = Task
#         fields = ['title', 'sub_tasks', 'description', 'due_date', 'notify_before', 'status']
#         exclude = ['created_on', 'soft_del', 'soft_del_timestamp']


class ActionForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['status']