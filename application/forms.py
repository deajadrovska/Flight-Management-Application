from django import forms

from application.models import Flight


class FlightForm(forms.ModelForm):
    def __init__(self, *args ,**kwargs):
        super(FlightForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Flight
        fields = "__all__"
        exclude = ('user', )