from django.shortcuts import render, get_object_or_404
from .models import LearningMaterial

def learn_home(request, lesson_id):
    lesson = get_object_or_404(LearningMaterial, id=lesson_id)
    cpp_materials = LearningMaterial.objects.filter(module=lesson.module).order_by('sequence')
    
    # Get next lesson in sequence
    next_lesson = LearningMaterial.objects.filter(
        module=lesson.module,
        sequence__gt=lesson.sequence
    ).order_by('sequence').first()

    # Get previous lesson in sequence
    prev_lesson = LearningMaterial.objects.filter(
        module=lesson.module,
        sequence__lt=lesson.sequence
    ).order_by('-sequence').first()
    
    return render(request, 'variables_and_constants.html', {
        'lesson': lesson,
        'current_material': lesson,
        'cpp_materials': cpp_materials,
        'title': lesson.title,
        'next_lesson': next_lesson,
        'prev_lesson': prev_lesson
    })
    #return render(request, 'variables_and_constants.html', {'title':lesson.title,'lesson': lesson})

