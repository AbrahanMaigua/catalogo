from django import forms

class add_car(forms.Form):
    #   <input placeholder="1" type="number" class="cantidad" >
    catidad = forms.IntegerField(
        max_value=100,
        required=True, 
        #help_text='1',
        label='',
        widget=forms.NumberInput(attrs={'class':'cantidad',
                                        'placeholder':'1'}))
    
    