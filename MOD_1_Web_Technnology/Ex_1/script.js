// Select DOM elements
const taskInput = document.getElementById('new-task');
const addTaskButton = document.getElementById('add-task');
const taskListContainer = document.querySelector('.task-list');
const taskCount = document.getElementById('task-count');

// Load tasks from localStorage
let tasks = JSON.parse(localStorage.getItem('tasks')) || [];

// Function to update the task count
function updateTaskCount() {
    taskCount.textContent = `Pending tasks: ${tasks.filter(task => !task.completed).length}`;
}

// Function to render tasks
function renderTasks() {
    taskListContainer.innerHTML = ''; // Clear the current list
    tasks.forEach((task, index) => {
        const taskElement = document.createElement('li');
        taskElement.classList.add('list-group-item', 'd-flex', 'justify-content-between', 'align-items-center');
        if (task.completed) {
            taskElement.classList.add('completed');
        }

        taskElement.innerHTML = `
            <span class="task-text">${task.name}</span>
            <div>
                <button class="btn btn-sm btn-warning edit-task" onclick="editTask(${index})">Edit</button>
                <button class="btn btn-sm btn-danger delete-task" onclick="deleteTask(${index})">Delete</button>
                <button class="btn btn-sm btn-success complete-task" onclick="toggleComplete(${index})">${task.completed ? 'Undo' : 'Complete'}</button>
            </div>
        `;
        taskListContainer.appendChild(taskElement);
    });
    updateTaskCount();
}

// Function to add a new task
function addTask() {
    const taskName = taskInput.value.trim();
    if (taskName) {
        tasks.push({ name: taskName, completed: false });
        localStorage.setItem('tasks', JSON.stringify(tasks));
        taskInput.value = '';
        renderTasks();
    }
}

// Function to delete a task
function deleteTask(index) {
    tasks.splice(index, 1);
    localStorage.setItem('tasks', JSON.stringify(tasks));
    renderTasks();
}

// Function to mark a task as completed (or undo)
function toggleComplete(index) {
    tasks[index].completed = !tasks[index].completed;
    localStorage.setItem('tasks', JSON.stringify(tasks));
    renderTasks();
}

// Function to edit a task
function editTask(index) {
    const newName = prompt('Edit task name:', tasks[index].name);
    if (newName !== null) {
        tasks[index].name = newName;
        localStorage.setItem('tasks', JSON.stringify(tasks));
        renderTasks();
    }
}

// Event listeners
addTaskButton.addEventListener('click', addTask);

// Initial render of tasks
renderTasks();
