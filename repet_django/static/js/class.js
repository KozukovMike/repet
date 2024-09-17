'use strict';
document.addEventListener('DOMContentLoaded', function() {
    const topicLinks = document.querySelectorAll('.topic-link');
    const taskLinks = document.querySelectorAll('.task-link');

    topicLinks.forEach(function(topicLink) {
        topicLink.addEventListener('click', function(event) {
            event.preventDefault();
            const topicId = topicLink.getAttribute('data-topic');
            const taskList = document.getElementById(`task-list-${topicId}`);
            const taskLinks = document.getElementById(`task-name-${topicId}`);
            if (taskList) {
                taskList.classList.toggle('show');
            }
        });
    });

    taskLinks.forEach(function(taskLink) {
        taskLink.addEventListener('click', function(event) {
            event.preventDefault();
            const taskId = taskLink.getAttribute('data-task');
            const taskText = document.getElementById(`task-text-${taskId}`);
            taskText.classList.toggle('show');
        });
    });
});