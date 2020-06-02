from django.contrib import admin
from .models import *

class CollegeAdmin(admin.ModelAdmin):
    list_display = ['a_id','name','password']
class HAdmin(admin.ModelAdmin):
    list_display = ['h_id','name','password']
class MAdmin(admin.ModelAdmin):
    list_display = ['m_id','name','password']
class LAdmin(admin.ModelAdmin):
    list_display = ['l_id','name','password']
class StudentAdmin(admin.ModelAdmin):
    list_display = ['roll_no','name','branch','year','password']
class HmaintenanceAdmin(admin.ModelAdmin):
    list_display = ['student','hostel_name','room_no','fan','tubelight','cupboard','bed','table','chair']
class FoodReviewAdmin(admin.ModelAdmin):
    list_display = ['student','rating','feedback','comment']

admin.site.register(Admin,CollegeAdmin)
admin.site.register(HostelAdmin,HAdmin)
admin.site.register(MessAdmin,MAdmin)
admin.site.register(LabAdmin,LAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(HostelMaintenance,HmaintenanceAdmin)
admin.site.register(FoodReview,FoodReviewAdmin)
