from django import forms


class GalleryFilterForm(forms.Form):
    max_price = forms.IntegerField(label="от", required=False)
    min_price = forms.IntegerField(label="до", required=False)
    ordering = forms.ChoiceField(label="Сортировка", required=False, choices=[
        ['p_name', 'по алфавиту'],
        ['p_price', 'дешевые сверху'],
        ['-p_price', 'дорогие сверху'],
    ])
