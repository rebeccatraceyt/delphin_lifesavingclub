from django import forms
from .models import UserProfile


class ProfileForm(forms.ModelForm):
    """
    A user profile model for maintaining default
    delivery information and order history
    """

    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-genetate
        labels and set autofocus on first field
        """
        # call default init to set form up
        super().__init__(*args, **kwargs)

        # dictionary for form fields
        placeholders = {
            'default_full_name': 'Full Name',
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Eircode',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County',
        }

        # cursor will start in full name field
        self.fields['default_full_name'].widget.attrs['autofocus'] = True

        # iterate through form fields
        for field in self.fields:
            # remove 'country' placeholder
            if field != 'default_country':
                # Add * to placeholder, if required
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]

                # setting placeholder attributes to dictionary values
                self.fields[field].widget.attrs['placeholder'] = placeholder

            # add CSS class
            self.fields[field].widget.attrs['class'] = 'profile-style-input'

            # remove form field labels
            self.fields[field].label = False
