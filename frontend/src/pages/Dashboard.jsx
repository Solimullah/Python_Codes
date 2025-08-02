import React, { useState, useEffect, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';
import { DndProvider, useDrag, useDrop } from 'react-dnd';
import { HTML5Backend } from 'react-dnd-html5-backend';

const ItemTypes = {
  TASK: 'task',
};

// Single task card component with drag source
const TaskCard = ({ task, index, columnKey, moveTask }) => {
  const [{ isDragging }, drag] = useDrag({
    type: ItemTypes.TASK,
    item: { task, index, columnKey },
    collect: (monitor) => ({
      isDragging: monitor.isDragging(),
    }),
  });

  return (
    <div
      ref={drag}
      className={`bg-white p-4 rounded-lg shadow border-l-4 mb-3 cursor-move transition hover:scale-[1.02] hover:shadow-lg ${
        isDragging ? 'opacity-50' : ''
      }`}
      style={{
        borderColor:
          columnKey === 'todo'
            ? '#7f5af0'
            : columnKey === 'inProgress'
            ? '#00c2d4'
            : columnKey === 'review'
            ? '#f78db8'
            : '#00d59f',
      }}
    >
      <p className="font-medium">{task}</p>
      <p className="text-sm text-gray-500">Description</p>
    </div>
  );
};

// Column component with drop target and add task functionality
const TaskColumn = ({
  columnKey,
  title,
  color,
  tasks,
  addTask,
  moveTaskBetweenColumns,
}) => {
  const [showInput, setShowInput] = useState(false);
  const [newTaskInput, setNewTaskInput] = useState('');

  // Drop target for tasks
  const [, drop] = useDrop({
    accept: ItemTypes.TASK,
    drop: (item) => {
      if (item.columnKey !== columnKey) {
        moveTaskBetweenColumns(item.columnKey, columnKey, item.index);
      }
    },
  });

  const handleAddClick = () => setShowInput((v) => !v);

  const handleAddTask = () => {
    const trimmed = newTaskInput.trim();
    if (!trimmed) return;
    addTask(columnKey, trimmed);
    setNewTaskInput('');
    setShowInput(false);
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      handleAddTask();
    } else if (e.key === 'Escape') {
      setShowInput(false);
      setNewTaskInput('');
    }
  };

  return (
    <div ref={drop} className="bg-purple-50 rounded p-4 min-h-[300px] flex flex-col">
      <div className="flex justify-between items-center mb-2">
        <h2 className="text-lg font-semibold">{title}</h2>
        <button
          onClick={handleAddClick}
          title={`Add task to ${title}`}
          className="text-2xl font-bold px-2 rounded hover:bg-purple-300 transition select-none"
        >
          +
        </button>
      </div>

      {showInput && (
        <input
          type="text"
          autoFocus
          value={newTaskInput}
          onChange={(e) => setNewTaskInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="New task..."
          className="mb-3 px-3 py-2 border rounded"
        />
      )}

      <div className="flex-grow overflow-auto">
        {tasks.map((task, i) => (
          <TaskCard
            key={`${task}-${i}`}
            task={task}
            index={i}
            columnKey={columnKey}
            moveTask={moveTaskBetweenColumns}
          />
        ))}
      </div>
    </div>
  );
};

const Dashboard = () => {
  const navigate = useNavigate();
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  // State for tasks
  const [tasks, setTasks] = useState({
    todo: ['Task 1'],
    inProgress: ['Task A'],
    review: ['Task R1'],
    completed: ['Task C1'],
  });

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) {
      navigate('/login');
    } else {
      setIsAuthenticated(true);
    }
  }, [navigate]);

  const handleLogout = () => {
    localStorage.removeItem('token');
    navigate('/login');
  };

  const addTask = (column, taskText) => {
    setTasks((prev) => ({
      ...prev,
      [column]: [...prev[column], taskText],
    }));
  };

  // Move task from one column to another
  const moveTaskBetweenColumns = useCallback(
    (fromColumn, toColumn, taskIndex) => {
      setTasks((prev) => {
        const fromTasks = [...prev[fromColumn]];
        const [movedTask] = fromTasks.splice(taskIndex, 1);
        const toTasks = [...prev[toColumn], movedTask];
        return {
          ...prev,
          [fromColumn]: fromTasks,
          [toColumn]: toTasks,
        };
      });
    },
    []
  );

  if (!isAuthenticated) return null;

  return (
    <DndProvider backend={HTML5Backend}>
      <div className="min-h-screen bg-purple-50 p-6">
        <div className="max-w-7xl mx-auto">
          {/* Header */}
          <header className="flex items-center justify-between mb-8">
            <h1 className="text-3xl font-bold">Task Management</h1>
            <div className="flex items-center gap-4">
              <span className="text-2xl">👤</span>
              <button
                onClick={handleLogout}
                className="px-4 py-2 bg-red-500 text-white rounded hover:bg-red-600 transition"
              >
                Logout
              </button>
            </div>
          </header>

          {/* Overview */}
          <div className="bg-purple-100 rounded-xl p-6 flex flex-col md:flex-row gap-8 mb-10">
            {/* Donut Chart */}
            <div className="w-40 h-40 relative bg-[conic-gradient(#7f5af0_0%_25%,#00c2d4_25%_50%,#f78db8_50%_70%,#00d59f_70%_100%)] rounded-full">
              <div className="absolute top-1/4 left-1/4 w-1/2 h-1/2 bg-purple-50 rounded-full"></div>
            </div>

            {/* Legend */}
            <div className="flex flex-col justify-center gap-2">
              {[
                { label: 'To Do', color: '#7f5af0', count: tasks.todo.length },
                { label: 'In Progress', color: '#00c2d4', count: tasks.inProgress.length },
                { label: 'Review', color: '#f78db8', count: tasks.review.length },
                { label: 'Completed', color: '#00d59f', count: tasks.completed.length },
              ].map((item, idx) => (
                <div key={idx} className="flex items-center justify-between w-48">
                  <span className="flex items-center gap-2">
                    <span
                      className="w-4 h-4 rounded-full"
                      style={{ backgroundColor: item.color }}
                    ></span>
                    {item.label}
                  </span>
                  <span className="font-bold">{item.count}</span>
                </div>
              ))}
            </div>
          </div>

          {/* Task Columns */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {[
              { key: 'todo', title: 'To Do', color: 'purple' },
              { key: 'inProgress', title: 'In Progress', color: 'blue' },
              { key: 'review', title: 'Review', color: 'pink' },
              { key: 'completed', title: 'Completed', color: 'green' },
            ].map(({ key, title, color }) => (
              <TaskColumn
                key={key}
                columnKey={key}
                title={title}
                color={color}
                tasks={tasks[key]}
                addTask={addTask}
                moveTaskBetweenColumns={moveTaskBetweenColumns}
              />
            ))}
          </div>
        </div>
      </div>
    </DndProvider>
  );
};

export default Dashboard;
