from django import forms
from main.models import Task


class CreateTaskForm(forms.ModelForm):
    name = forms.CharField(
        label='Название',
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 bg-transparent',
            'placeholder': "Название",
        })
    )
    description = forms.CharField(
        label='Заметка',
        widget=forms.Textarea(attrs={
            'class': 'form-control bg-transparent h-100 p-3',
            'placeholder': "Заметка",
        })
    )
    end_task_date = forms.DateTimeField(
        label="Дедлайн",
        input_formats=[
            "%Y-%m-%dT%H:%M:%S",
            "%Y-%m-%dT%H:%M:%S.%f",
            "%Y-%m-%dT%H:%M",
        ],
        widget=forms.DateTimeInput(
            attrs={
                'class': "form-control bg-transparent",
                'type': 'datetime-local',
                'placeholder': "Дедлайн",
            },
            format="%Y-%m-%dT%H:%M",
        )
    )

    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'end_task_date',
        ]
