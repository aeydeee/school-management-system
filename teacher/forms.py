from django import forms

from teacher.models import Teacher, Address
from datetime import datetime

# Get the current year
current_year = datetime.now().year


class TeacherForm(forms.ModelForm):
    # Teacher specific fields
    gender = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                               choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], required=True)
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=True
    )
    joining_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=True
    )
    teacher_image = forms.ImageField(widget=forms.ClearableFileInput(
        attrs={
            'class': 'form-control',
            'accept': 'image/*',
            'placeholder': 'Choose an image',
        }), required=False)

    def clean_joining_date(self):
        joining_date = self.cleaned_data['joining_date']
        if joining_date.year < 1900 or joining_date.year > current_year:
            raise forms.ValidationError("Please select a date between 1900 and the current year.")
        return joining_date

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        if date_of_birth.year < 1900 or date_of_birth.year > current_year:
            raise forms.ValidationError("Please select a date between 1900 and the current year.")
        return date_of_birth

    class Meta:
        model = Teacher
        exclude = [
            'address',
            'slug',
            'user'
        ]
        # Default widget: apply 'form-control' class to all fields
        widgets = {
            field.name: forms.TextInput(attrs={'class': 'form-control'})
            for field in model._meta.fields
            if field.name not in ['gender', 'date_of_birth', 'joining_date', 'teacher_image']
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': f'Enter {field.label}'
            })
