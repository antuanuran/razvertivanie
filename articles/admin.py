from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeForm(BaseInlineFormSet):
    def clean(self):
        temp = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                temp += 1

        if temp != 1:
            raise ValidationError('Главный тег должен быть один!')
        return super(ScopeForm, self).clean()


class TagInline(admin.TabularInline):
    model = Scope
    formset = ScopeForm


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    list_display = ['title', 'image', 'id']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']

