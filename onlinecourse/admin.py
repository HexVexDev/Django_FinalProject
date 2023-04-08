from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice

# <HINT> Register QuestionInline and ChoiceInline classes here

class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra= 4

class QuestionInLine(admin.StackedInline):
    model = Question

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['ctext']
    

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]
    list_display=['qtext']



class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 2


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)
