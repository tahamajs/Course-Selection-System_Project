def has_faculty_permission(user_model, request, view):
    try:
        user_obj = user_model.objects.filter(user=request.user).first()
        is_same_faculty = view.queryset.filter(
            id=view.kwargs['pk']).filter(faculty=user_obj.faculty).exists()
        return user_obj and is_same_faculty
    except:
        return False
