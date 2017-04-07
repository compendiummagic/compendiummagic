from django import forms

DATE_INPUT_FORMATS = (
    '%d.%m.%Y', '%d.%m.%Y', '%d.%m.%y',  # '25.10.2006', '25.10.2006', '25.10.06'
    '%d-%m-%Y', '%d/%m/%Y', '%d/%m/%y',  # '25-10-2006', '25/10/2006', '25/10/06'
    '%d %b %Y',  # '25 Oct 2006',
    '%d %B %Y',  # '25 October 2006',
    '%d %b',
    '%d %B',
)

CHOICES = [
    ("1-5", "1-5"), ("5-10", "5-10"), ("10-20", "10-20"), ("20-50", "20-50"), ("50-100", "50-100"), ("100+", "100+"),
]


class ReviewForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='')

class ContactForm(forms.Form):

    phone = forms.CharField(max_length=50, label='Mobile Number')
    date = forms.DateField(label='Event Date', input_formats=DATE_INPUT_FORMATS)
    time = forms.TimeField(label='Event Time')
    venue = forms.CharField(max_length=200, label='Event Venue')
    guests = forms.ChoiceField(choices=CHOICES, label='Number of Guests')
    extra_info = forms.CharField(widget=forms.Textarea, label='Extra Information', required=False)
    hear = forms.CharField(max_length=100, label='How did you hear of us?', required=False)

class ShippingForm(forms.Form):
    first_name = forms.CharField(max_length=50, label='First Name')
    last_name = forms.CharField(max_length=50, label='Last Name')
    house_number = forms.CharField(max_length=200, label='House Number')
    street_name = forms.CharField(max_length=200, label='Street Name')
    postcode = forms.CharField(max_length=200, label='Post Code')
    county = forms.CharField(max_length=200, label='County')
    country = forms.CharField(max_length=200, label='Country')
