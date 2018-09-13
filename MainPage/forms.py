from django import forms
from MainPage.models import HomePageInfo


class HomePageForm(forms.ModelForm):
    intro_text = forms.CharField(max_length=150,
                                label="Item Description",
                                widget=forms.Textarea,
                                required=True)

    project_one = forms.CharField(label="Project #1",
                                  max_length=250,
                                  required=True)

    project_two = forms.CharField(label="Project #2",
                                  max_length=250,
                                  required=True)

    project_three = forms.CharField(label="Project #3",
                                    max_length=250,
                                    required=True)

    project_four = forms.CharField(label="Project #4",
                                   max_length=250,
                                   required=True)

    project_five = forms.CharField(label="Project #5",
                                   max_length=250,
                                   required=True)

    project_six = forms.CharField(label="Project #6",
                                  max_length=250,
                                  required=True)
    project_seven = forms.CharField(label="Project #7",
                                    max_length=250,
                                    required=True)



class HomePageModelForm(HomePageForm):
    class Meta:
        model = HomePageInfo
        fields = ['intro_text',
                 'project_one',
                 'project_two',
                 'project_three',
                 'project_four',
                 'project_five',
                 'project_six',
                 'project_seven'
                ]
