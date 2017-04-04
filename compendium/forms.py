from django import forms

class ReviewForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='')

class ContactForm(forms.Form):

    CHOICES = [
        (1, "1-5"), (2, "5-10"), (3, "10-20"), (4, "20-50"), (5, "50-100"), (6, "100+"),
    ]

    phone = forms.CharField(max_length=50, label='Mobile Number')
    date = forms.DateField(label='Event Date')
    time = forms.TimeField(label='Event Time')
    venue = forms.CharField(max_length=200, label='Event Venue')
    guests = forms.ChoiceField(choices=CHOICES, label='Number of Guests')
    extra_info = forms.CharField(widget=forms.Textarea, label='Extra Information', required=False)
    hear = forms.CharField(max_length=100, label='How did you hear of us?', required=False)
