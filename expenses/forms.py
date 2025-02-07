from django import forms
from .models import Grade, TierList, TierItem, DiaryEntry, PasswordStorage

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['subject', 'value', 'date', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

class TierListForm(forms.ModelForm):
    class Meta:
        model = TierList
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class TierItemForm(forms.ModelForm):
    class Meta:
        model = TierItem
        fields = ['name', 'tier', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class DiaryEntryForm(forms.ModelForm):
    class Meta:
        model = DiaryEntry
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }

class PasswordStorageForm(forms.ModelForm):
    class Meta:
        model = PasswordStorage
        fields = ['service_name', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
