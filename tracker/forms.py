from django import forms
from .models import CarModel
class CarForm(forms.ModelForm):
    link = forms.URLField(required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter car search link here','aria-describedby': 'sizing-addon3'}))
    #url = forms.URLField(label='Your website', required=False)
    #list_choices = ['Texas','Alabama']
    OPTIONS = [("Alaska", "Alaska"),
                 ( "Alabama","Alabama"),
                  ("Arkansas","Arkansas"),
                  ("Arizona", "Arizona"),
                  ("California","California"),
                  ("Colorado","Colorado"),
                  ("Connecticut","Connecticut"),
                  ("District of Columbia","District of Columbia"),
                  ("Delaware","Delaware"),
                  ("Florida","Florida"),
                  ("Georgia","Georgia"),
                  ("Hawaii","Hawaii"),
                  ("Guam","Guam"),
                  ("Iowa","Iowa"),
                  ("Idaho","Idaho"),
                  ("Illinois","Illinois"),
                  ("Indiana","Indiana"),
                  ("Kansas","Kansas"),
                  ("Kentucky","Kentucky"),
                  ("Louisiana","Louisiana"),
                  ("Massachusetts","Massachusetts"),
                  ("Maryland","Maryland"),
                  ("Maine","Maine"),
                  ("Michigan","Michigan"),
                  ("Minnesota","Minnesota"),
                  ("Missouri","Missouri"),
                  ("Mississippi","Mississippi"),
                  ("Montana","Montana"),
                  ("North Carolina","North Carolina"),
                  ("North Dakota","North Dakota"),
                  ("Nebraska","Nebraska"),
                  ("New Hampshire","New Hampshire"),
                  ("New Jersey","New Jersey"),
                  ("New Mexico","New Mexico"),
                  ("Nevada","Nevada"),
                  ("New York","New York"),
                  ("Ohio","Ohio"),
                  ("Oklahoma","Oklahoma"),
                  ("Oregon","Oregon"),
                  ("Pennsylvania","Pennsylvania"),
                  ("Puerto Rico","Puerto Rico"),
                  ("Rhode Island","Rhode Island"),
                  ("South Carolina","South Carolina"),
                  ("South Dakota","South Dakota"),
                  ("Tennessee","Tennessee"),
                  ("Texas","Texas"),
                  ("Utah","Utah"),
                  ("Virginia","Virginia"),
                  ("Virgin Islands","Virgin Islands"),
                  ("Vermont","Vermont"),
                  ("Washington","Washington"),
                  ("Wisconsin","Wisconsin"),
                  ("West Virginia","West Virginia"),
                  ("Wyoming","Wyoming"),]
    states = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             choices=OPTIONS)
    class Meta:
        model = CarModel
        fields = ("link","states")