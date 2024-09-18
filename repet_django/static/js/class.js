document.addEventListener('DOMContentLoaded', function() {
    const topicLinks = document.querySelectorAll('.topic-link');
    const taskLinks = document.querySelectorAll('.task-link');
    const testLinks = document.querySelectorAll('.test-link');
    const taskDescription = document.getElementById('task-description');
    const text = taskDescription.innerHTML;

    topicLinks.forEach(function(topicLink) {
        topicLink.addEventListener('click', function(event) {
            event.preventDefault();
            const topicId = topicLink.getAttribute('data-topic');
            const taskList = document.getElementById(`task-list-${topicId}`);
            if (taskList) {
                taskList.classList.toggle('show');
            }
        });
    });

    taskLinks.forEach(function(taskLink) {
        taskLink.addEventListener('click', function(event) {
            event.preventDefault();
            const taskId = taskLink.dataset.task;
            const taskText = document.getElementById('task-text-' + taskId);
            taskDescription.innerHTML = text + taskText.innerHTML;
        });
    });

    testLinks.forEach(function (testLink){
       testLink.addEventListener('click', function (event) {
           event.preventDefault();
           const testId = testLink.dataset.test;
           const testText = document.getElementById('test-form-' + testId);
           taskDescription.innerHTML = text + testText.innerHTML;
       });
    });

});
