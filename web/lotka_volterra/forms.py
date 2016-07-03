from django import forms
from lotka_volterra.models import LVDiffEqSolution
from django.utils.translation import ugettext as _


class SubmitCalculationForm(forms.ModelForm):
    init_condition_x = forms.FloatField(help_text=_('Начальное условие x'))
    init_condition_y = forms.FloatField(help_text=_('Начальное условие y'))
    init_param_a = forms.FloatField(help_text=_('Коэф a'))
    init_param_b = forms.FloatField(help_text=_('Коэф b'))
    init_param_c = forms.FloatField(help_text=_('Коэф c'))
    init_param_d = forms.FloatField(help_text=_('Коэф d'))

    class Meta:
        model = LVDiffEqSolution
        fields = ('init_condition_x', 'init_condition_y',
                  'init_param_a', 'init_param_b',
                  'init_param_c', 'init_param_d')

