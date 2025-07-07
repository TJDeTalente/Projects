const input = document.getElementById("input");
const priority = document.getElementById("priority");
const listsContainer = document.getElementById("lists-container");


function logTask() {
    console.log("Task function ran")
    const task = input.value
    if (task.trim() === "") {
        return;
    }
    const taskPriority = priority.value
    console.log(taskPriority)
    const taskItem = document.createElement("li");
    const taskText = document.createElement("span");
    taskText.classList.add("task-text")

    const checkbox = document.createElement("input");
    checkbox.classList.add("form-check-input")
    checkbox.type = "checkbox";

    taskText.textContent = task;
    taskItem.appendChild(checkbox)
    taskItem.appendChild(taskText);
    const taskList = document.getElementById("task-list-" + taskPriority)
    taskList.appendChild(taskItem);
    input.value = "";
}


listsContainer.addEventListener("click", function(e) {
    if (e.target.tagName === "INPUT" && e.target.type === "checkbox") {
        const listItem = e.target.parentNode;
        const taskList = listItem.parentNode;
        taskList.removeChild(listItem);
    }
});
