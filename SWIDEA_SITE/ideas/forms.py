from django import forms
from .models import Idea

class IdeaForm(forms.ModelForm):
  class Meta:
    model = Idea
    fields = ('__all__')
    # widgets = {
    #         'devtool': forms.Select(
    #             choices=[
    #                 ('none', '----------'),
    #                 ('django', 'django'),
    #                 ('react', 'react'),
    #                 ('vue', 'vue'),
    #                 ('spring', 'spring'),
    #                 ('node.js', 'node.js'),
    #             ]
    #         )
    #     }