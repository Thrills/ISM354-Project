from django.contrib import admin

from .models import Chairperson
admin.site.register(Chairperson)

from .models import CommitteeMember

class CommitteeMemberAdmin(admin.ModelAdmin):
    fieldsets = [                                                      # Creates fieldsets for the data about CM members
	('Personal Information', {'fields': ['cm_name', 'cm_surname', 'cm_institution', 'cm_email']}),
]

admin.site.register(CommitteeMember, CommitteeMemberAdmin)

from .models import Paper

class PaperAdmin(admin.ModelAdmin):
    fieldsets = [
	('Paper Details', {'fields': ['paper_code', 'paper_submissionDate', 'paper_submissionUpdate', 'paper_avgScore', 'paper_accepted']}) # Different data the Admin will be able to view
]

admin.site.register(Paper, PaperAdmin)

from .models import Reviewer

class ReviewerAdmin(admin.ModelAdmin):
    fieldsets = [
	('Personal Information', {'fields': ['reviewer_id', 'reviewer_name', 'reviewer_surname', 'reviewer_institution', 'reviewer_email']})
]

admin.site.register(Reviewer, ReviewerAdmin)

from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    fieldsets = [
	('Review Details', {'fields': ['review_reviewCode', 'review_score', 'review_paperCode']})
]

admin.site.register(Review, ReviewAdmin)

from .models import Author

class AuthorAdmin(admin.ModelAdmin):
    fieldsets = [
	('Personal Information',
     {'fields': ['author_id', 'author_name', 'author_surname', 'author_institution', 'author_email']})
]

admin.site.register(Author, AuthorAdmin)
