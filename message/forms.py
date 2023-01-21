from django import forms



class MessageForm(forms.Form):
    receptor=forms.CharField(label="Receptor")
    mensaje=forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))