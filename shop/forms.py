from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, ProductOption


class CustomMMCF(forms.ModelMultipleChoiceField):
    """
    Custom form class that overrides the ‘label_from_instance’ method
    ref: http://tiny.cc/adg2vz
    """
    def label_from_instance(self, product_select):
        return '%s' % product_select.product_options


class ProductForm(forms.ModelForm):
    """
    Ability to add, update and delete products
    """

    class Meta:
        # defines model and fields to include
        model = Product
        fields = '__all__'
    
    name = forms.CharField(label="", widget=forms.TextInput(
        attrs={'placeholder': 'Name'}))

    description = forms.CharField(label="", widget=forms.Textarea(
        attrs={'placeholder': 'A brief Description of the product'}))
    
    price = forms.DecimalField(label="", widget=forms.NumberInput(
        attrs={'placeholder': 'Product price in Euro (€)'}))

    is_course = forms.BooleanField(
        label="This is a Course product",
        required=False)

    is_apparel = forms.BooleanField(
        label="This is Apparel",
        required=False)

    product_select = forms.ModelMultipleChoiceField(
        label="",
        queryset=ProductOption.objects.all(),
        widget=forms.CheckboxSelectMultiple
        )

    course_info = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={'placeholder': 'Course information'}
        ),
        required=False)
    
    course_age = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Minimum age for course attendance'}
        ),
        required=False)

    image = forms.ImageField(
        label='Image',
        required=True,
        widget=CustomClearableFileInput
        )
     
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-genetate
        labels and set autofocus on first field
        """

        # override the init method
        # to make changes to fields
        super().__init__(*args, **kwargs)

        # get categories to show in their friendly name
        categories = Category.objects.all()
        # list comprehension for loop to get friendly names
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]      
        # use category friendly name instead of id
        self.fields['category'].choices = friendly_names

        # cursor will start in name field
        self.fields['name'].widget.attrs['autofocus'] = True
        
        # iterate through fields with css for consistency
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'