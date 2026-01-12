import React from "react";
/**
 * TodoList component
 * Displays a list of predefined tasks using list rendering.
 * Tasks are stored in an array of objects and rendered using map().
 */
function TodoList() {
  /**
   * Array of todo tasks
   * Each task contains a unique id and task text
   */
  const tasks = [
    { id: 1, text: "Learn React basics" },
    { id: 2, text: "Practice useState" },
    { id: 3, text: "Understand list rendering" }
  ];

  return (
    <div>
      <h2>Todo List</h2>

      <ul>
        {/**
         * map() is used to iterate over the tasks array
         * and return a list item for each task
         */}
        {tasks.map((task) => (
          <li key={task.id}>
            {task.text}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TodoList;
