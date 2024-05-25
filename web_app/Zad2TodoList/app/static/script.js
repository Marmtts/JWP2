document.addEventListener('DOMContentLoaded', () => {
    const taskForm = document.getElementById('taskForm');
    const taskName = document.getElementById('taskName');
    const taskList = document.getElementById('taskList');

    taskForm.addEventListener('submit', (event) => {
        event.preventDefault();
        const name = taskName.value;
        if (name) {
            fetch('/add_task', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ name: name }),
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                location.reload();
            });
        }
    });

    taskList.addEventListener('click', (event) => {
        if (event.target.classList.contains('delete')) {
            const id = event.target.parentElement.getAttribute('data-id');
            fetch('/delete_task', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ id: id }),
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                location.reload();
            });
        } else if (event.target.classList.contains('edit')) {
            const id = event.target.parentElement.getAttribute('data-id');
            const newName = prompt("Enter new task name:");
            if (newName) {
                fetch('/edit_task', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ id: id, name: newName }),
                })
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                    location.reload();
                });
            }
        }
    });
});
