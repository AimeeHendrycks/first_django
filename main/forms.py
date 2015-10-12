from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, Layout, Div
from crispy_forms.bootstrap import FormActions
from main.models import City, State, StateCapital


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)
    #args are variables, key-word arguments are variables and a value
    #val, val2='something'
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/contact_view/'
        
        self.helper.layout = Layout(
            Div('name', 'email', 'phone', css_class="col-md-6"),
            Div('message', css_class="col-md-6")
            )

        self.helper.layout.append(
            FormActions(
                Submit('submit', 'Submit', css_class='btn-primary', style='background:#6C0D18; margin-left:15px')
                )
            )
#model form
class CityNewForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CityNewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/city_new/'
        self.helper.layout.append(
            FormActions(
                Submit('save_changes', 'Save Changes', css_class='btn-primary', style='background:#163559'),
                )
            )

class CityEditForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CityEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/city_edit/%s/' % self.instance.pk
        self.helper.layout.append(
            FormActions(
                Submit('save_changes', 'Save Changes', css_class='btn-primary', style='background:#163559'),
                )
            )

class StateNewForm(forms.ModelForm):
    class Meta:
        model = State
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StateNewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/state_new/'
        self.helper.layout.append(
            FormActions(
                Submit('save_changes', 'Save Changes', css_class='btn-primary', style='background:#163559'),
                )
            )

class StateEditForm(forms.ModelForm):
    class Meta:
        model = State
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StateEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/state_edit/%s/' % self.instance.pk
        self.helper.layout.append(
            FormActions(
                Submit('save_changes', 'Save Changes', css_class='btn-primary', style='background:#163559'),
                )
            )

class StateCapitalEditForm(forms.ModelForm):
    class Meta:
        model = StateCapital
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StateCapitalEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/state_capital_edit/%s/' % self.instance.pk
        self.helper.layout.append(
            FormActions(
                Submit('save_changes', 'Save Changes', css_class='btn-primary', style='background:#163559'),
                )
            )

class StateCapitalNewForm(forms.ModelForm):
    class Meta:
        model = StateCapital
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StateCapitalNewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/state_capital_new/'
        self.helper.layout.append(
            FormActions(
                Submit('save_changes', 'Save Changes', css_class='btn-primary', style='background:#163559'),
                )
            )
class CityRemoveForm(forms.ModelForm):
    class Meta:
        model = City
        fields = []

    def __init__(self, *args, **kwargs):
        super(CityRemoveForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/city_remove/%s/' % self.instance.pk
        self.helper.layout.append(
            FormActions(
                Submit('remove_city', 'Remove City', css_class='btn-primary', style='margin-left:40%; background:#163559'),
                )
            )

class StateRemoveForm(forms.ModelForm):
    class Meta:
        model = State
        fields = []

    def __init__(self, *args, **kwargs):
        super(StateRemoveForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/state_remove/%s/' % self.instance.pk
        self.helper.layout.append(
            FormActions(
                Submit('remove_state', 'Remove State', css_class='btn-primary', style='margin-left:39%; background:#163559'),
                )
            )
class StateCapitalRemoveForm(forms.ModelForm):
    class Meta:
        model = StateCapital
        fields = []

    def __init__(self, *args, **kwargs):
        super(StateCapitalRemoveForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/state_capital_remove/%s/' % self.instance.pk
        self.helper.layout.append(
            FormActions(
                Submit('remove_state_capital', 'Remove State Capital', css_class='btn-primary', style='margin-left:33%; background:#163559'),
                )
            )
