import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';

const Dashboard = () => {
  const navigate = useNavigate();
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  // Simulated authentication check
  useEffect(() => {
    // Replace with actual auth check (e.g., check token in localStorage or API)
    const token = localStorage.getItem('token'); // Example: check for a token
    if (!token) {
      navigate('/login');
    } else {
      setIsAuthenticated(true);
    }
  }, [navigate]);

  if (!isAuthenticated) {
    return null; // Render nothing while redirecting
  }

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <div className="max-w-7xl mx-auto">
        <h1 className="text-3xl font-bold text-center mb-8">Task Management Dashboard</h1>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {/* Admin Panel Section */}
          <div className="bg-white p-6 rounded-lg shadow-lg">
            <h2 className="text-xl font-semibold mb-4">Admin Panel</h2>
            <div className="space-y-4">
              <div>
                <h3 className="text-sm font-medium text-gray-700">User Management</h3>
                <p className="text-gray-600 text-sm">
                  Manage users with CRUD operations.
                </p>
                <button className="mt-2 text-blue-500 hover:underline">View Users</button>
              </div>
              <div>
                <h3 className="text-sm font-medium text-gray-700">Permissions</h3>
                <p className="text-gray-600 text-sm">
                  Assign and modify user roles and permissions.
                </p>
                <button className="mt-2 text-blue-500 hover:underline">Manage Permissions</button>
              </div>
              <div>
                <h3 className="text-sm font-medium text-gray-700">System Logs</h3>
                <p className="text-gray-600 text-sm">
                  View system activity and audit logs.
                </p>
                <button className="mt-2 text-blue-500 hover:underline">View Logs</button>
              </div>
            </div>
          </div>

          {/* Project Management Section */}
          <div className="bg-white p-6 rounded-lg shadow-lg">
            <h2 className="text-xl font-semibold mb-4">Project Management</h2>
            <div className="space-y-4">
              <div>
                <h3 className="text-sm font-medium text-gray-700">Task Status</h3>
                <p className="text-gray-600 text-sm">
                  Track task progress and completion status.
                </p>
                <button className="mt-2 text-blue-500 hover:underline">View Tasks</button>
              </div>
              <div>
                <h3 className="text-sm font-medium text-gray-700">Team Performance</h3>
                <p className="text-gray-600 text-sm">
                  Monitor team productivity and metrics.
                </p>
                <button className="mt-2 text-blue-500 hover:underline">View Metrics</button>
              </div>
              <div>
                <h3 className="text-sm font-medium text-gray-700">Burndown Charts</h3>
                <p className="text-gray-600 text-sm">
                  Visualize project progress with burndown charts.
                </p>
                <button className="mt-2 text-blue-500 hover:underline">View Charts</button>
              </div>
            </div>
          </div>

          {/* DevOps / Monitoring Section */}
          <div className="bg-white p-6 rounded-lg shadow-lg">
            <h2 className="text-xl font-semibold mb-4">DevOps / Monitoring</h2>
            <div className="space-y-4">
              <div>
                <h3 className="text-sm font-medium text-gray-700">Uptime</h3>
                <p className="text-gray-600 text-sm">
                  Monitor system uptime and availability.
                </p>
                <button className="mt-2 text-blue-500 hover:underline">View Uptime</button>
              </div>
              <div>
                <h3 className="text-sm font-medium text-gray-700">CPU/RAM Usage</h3>
                <p className="text-gray-600 text-sm">
                  Track server resource usage.
                </p>
                <button className="mt-2 text-blue-500 hover:underline">View Metrics</button>
              </div>
              <div>
                <h3 className="text-sm font-medium text-gray-700">Error Logs</h3>
                <p className="text-gray-600 text-sm">
                  Review application error logs.
                </p>
                <button className="mt-2 text-blue-500 hover:underline">View Logs</button>
              </div>
              <div>
                <h3 className="text-sm font-medium text-gray-700">Deployment Pipelines</h3>
                <p className="text-gray-600 text-sm">
                  Manage and monitor deployment workflows.
                </p>
                <button className="mt-2 text-blue-500 hover:underline">View Pipelines</button>
              </div>
            </div>
          </div>
        </div>
        <div className="mt-6 text-center">
          <Link
            to="/login"
            className="text-blue-500 hover:underline"
            onClick={() => localStorage.removeItem('authToken')} // Simulated logout
          >
            Logout
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;