from django import forms

from leaflet.forms.widgets import LeafletWidget


class CountyForm(forms.ModelForm):

    class Meta:
        model = County
        fields = ('name', 'geom')
        widgets = {'geom': LeafletWidget(attrs=LEAFLET_WIDGET_ATTRS)}