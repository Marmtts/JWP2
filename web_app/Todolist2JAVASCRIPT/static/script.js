document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.edit-button').forEach(button => {
        button.addEventListener('click', (e) => {
            const li = e.target.closest('li');
            const span = li.querySelector('span');
            const taskId = li.dataset.id;
            const newTask = prompt('Edit task:', span.textContent);
            if (newTask) {
                const formData = new FormData();
                formData.append('task', newTask);

                fetch(`/edit/${taskId}`, {
                    method: 'POST',
                    body: formData
                }).then(() => {
                    span.textContent = newTask;
                });
            }
        });
    });
});
