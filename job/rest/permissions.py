from rest_framework.permissions import BasePermission



class IsRecruiter(BasePermission):
    def has_permission(self, request, view):
        print('request.user.is_authenticated' , request.user.is_authenticated)
        print("request.user.role == 'recruiter'",request.user.role == 'recruiter')
        return bool(request.user.is_authenticated and request.user.role == 'RECRUITER')


class IsCandidate(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.role == 'CANDIDATE')