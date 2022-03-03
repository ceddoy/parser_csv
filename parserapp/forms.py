from django import forms

from parserapp.models import CSV_file


class CSVFileForm(forms.ModelForm):
    class Meta:
        model = CSV_file
        fields = '__all__'

    def clean_file(self):
        csv_file = self.cleaned_data.get('file')
        if csv_file.name.endswith('.csv'):
            return csv_file
        else:
            raise forms.ValidationError("Только формат .csv")
