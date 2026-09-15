from pathlib import Path
from IPython.display import display, HTML

html_code = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Accessible enterprise dashboard using Semantic HTML5 and WCAG 2.1 principles">
<title>Enterprise Accessible Dashboard</title>

<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body {
    font-family: Arial, Helvetica, sans-serif;
    background: #f4f6f8;
    color: #17202a;
    line-height: 1.6;
}
.skip-link {
    position: absolute;
    top: -50px;
    left: 10px;
    background: #111827;
    color: white;
    padding: 10px 16px;
    text-decoration: none;
    z-index: 9999;
    border-radius: 4px;
}
.skip-link:focus { top: 10px; }
:focus {
    outline: 3px solid #005fcc;
    outline-offset: 3px;
}
.sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0,0,0,0);
    white-space: nowrap;
    border: 0;
}
.site-header {
    background: #17202a;
    color: white;
    min-height: 70px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 15px 25px;
}
.brand { font-size: 24px; font-weight: bold; }
.user-area { display: flex; align-items: center; gap: 15px; }
.user-avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: white;
    color: #17202a;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
}
.dashboard-layout {
    display: grid;
    grid-template-columns: 240px 1fr;
    min-height: calc(100vh - 70px);
}
.sidebar {
    background: white;
    border-right: 1px solid #d9dee3;
    padding: 20px;
}
.sidebar h2 { font-size: 18px; margin-bottom: 20px; }
.nav-list { list-style: none; }
.nav-list li { margin-bottom: 8px; }
.nav-list a {
    display: block;
    text-decoration: none;
    color: #17202a;
    padding: 12px;
    border-radius: 6px;
}
.nav-list a:hover, .nav-list a.active { background: #e9eef5; }
main {
    padding: 30px;
    max-width: 1600px;
    width: 100%;
}
.page-heading { margin-bottom: 25px; }
.page-heading h1 { font-size: 30px; margin-bottom: 5px; }
.page-heading p { color: #4b5563; }
.search-section {
    background: white;
    padding: 20px;
    border-radius: 8px;
    border: 1px solid #d9dee3;
    margin-bottom: 25px;
}
.search-section label {
    display: block;
    font-weight: bold;
    margin-bottom: 8px;
}
.search-row { display: flex; gap: 10px; }
.search-row input {
    flex: 1;
    padding: 12px;
    border: 1px solid #8a939b;
    border-radius: 5px;
    font-size: 16px;
}
button {
    padding: 12px 20px;
    border: none;
    border-radius: 5px;
    background: #17202a;
    color: white;
    font-size: 15px;
    cursor: pointer;
}
button:hover { background: #2c3e50; }
.metrics-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
    margin-bottom: 30px;
}
.metric-card {
    background: white;
    padding: 22px;
    border: 1px solid #d9dee3;
    border-radius: 8px;
}
.metric-card h2 { font-size: 16px; color: #4b5563; margin-bottom: 10px; }
.metric-value { font-size: 32px; font-weight: bold; }
.metric-change { margin-top: 8px; color: #1f6f43; font-size: 14px; }
.content-grid {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 25px;
}
.panel {
    background: white;
    border: 1px solid #d9dee3;
    border-radius: 8px;
    padding: 22px;
    margin-bottom: 25px;
}
.panel h2 { margin-bottom: 18px; font-size: 21px; }
.table-wrapper { overflow-x: auto; }
table { width: 100%; border-collapse: collapse; }
caption { text-align: left; padding-bottom: 10px; font-weight: bold; }
th, td {
    text-align: left;
    padding: 13px;
    border-bottom: 1px solid #d9dee3;
}
th { background: #eef1f4; }
.status {
    display: inline-block;
    padding: 5px 10px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: bold;
}
.status-active { background: #dff3e6; color: #155c35; }
.status-pending { background: #fff0c2; color: #674d00; }
.status-completed { background: #e0e7ff; color: #283593; }
.activity-list { list-style: none; }
.activity-list li {
    padding: 15px 0;
    border-bottom: 1px solid #e1e5e8;
}
.activity-list li:last-child { border-bottom: none; }
.activity-time {
    display: block;
    font-size: 13px;
    color: #68727c;
}
.progress-item { margin-bottom: 18px; }
.progress-header {
    display: flex;
    justify-content: space-between;
    margin-bottom: 7px;
}
progress { width: 100%; height: 18px; }
footer {
    background: #17202a;
    color: white;
    padding: 20px;
    text-align: center;
}
@media (max-width: 1100px) {
    .metrics-grid { grid-template-columns: repeat(2, 1fr); }
    .content-grid { grid-template-columns: 1fr; }
}
@media (max-width: 700px) {
    .dashboard-layout { grid-template-columns: 1fr; }
    .sidebar {
        border-right: none;
        border-bottom: 1px solid #d9dee3;
    }
    main { padding: 20px; }
    .metrics-grid { grid-template-columns: 1fr; }
    .search-row { flex-direction: column; }
    .site-header {
        flex-direction: column;
        gap: 10px;
        align-items: flex-start;
    }
}
@media (prefers-reduced-motion: reduce) {
    html { scroll-behavior: auto; }
    * {
        animation-duration: 0.01ms !important;
        transition-duration: 0.01ms !important;
    }
}
</style>
</head>

<body>

<a class="skip-link" href="#main-content">Skip to main content</a>

<header class="site-header">
    <div class="brand">Enterprise Dashboard</div>
    <div class="user-area">
        <span>Welcome, Admin</span>
        <div class="user-avatar" aria-hidden="true">A</div>
    </div>
</header>

<div class="dashboard-layout">

<aside class="sidebar">
    <nav aria-label="Primary navigation">
        <h2>Dashboard Menu</h2>
        <ul class="nav-list">
            <li><a href="#overview" class="active" aria-current="page">Overview</a></li>
            <li><a href="#analytics">Analytics</a></li>
            <li><a href="#reports">Reports</a></li>
            <li><a href="#users">Users</a></li>
            <li><a href="#settings">Settings</a></li>
        </ul>
    </nav>
</aside>

<main id="main-content">

<section class="page-heading" id="overview" aria-labelledby="dashboard-title">
    <h1 id="dashboard-title">Dashboard Overview</h1>
    <p>Monitor enterprise activities, performance, users, and system progress.</p>
</section>

<section class="search-section" aria-labelledby="search-heading">
    <h2 id="search-heading" class="sr-only">Search Dashboard</h2>

    <form id="searchForm">
        <label for="dashboardSearch">Search dashboard</label>

        <div class="search-row">
            <input type="search"
                   id="dashboardSearch"
                   name="dashboardSearch"
                   placeholder="Search..."
                   aria-describedby="search-help">

            <button type="submit">Search</button>
        </div>

        <small id="search-help">
            Enter a keyword to search dashboard information.
        </small>
    </form>

    <p id="searchResult" role="status" aria-live="polite" class="sr-only"></p>
</section>

<section aria-labelledby="metrics-heading">
    <h2 id="metrics-heading" class="sr-only">Performance Metrics</h2>

    <div class="metrics-grid">

        <article class="metric-card">
            <h2>Total Users</h2>
            <p class="metric-value">1,248</p>
            <p class="metric-change">12% increase this month</p>
        </article>

        <article class="metric-card">
            <h2>Active Projects</h2>
            <p class="metric-value">86</p>
            <p class="metric-change">8 new projects</p>
        </article>

        <article class="metric-card">
            <h2>Completed Tasks</h2>
            <p class="metric-value">3,420</p>
            <p class="metric-change">18% increase this week</p>
        </article>

        <article class="metric-card">
            <h2>System Uptime</h2>
            <p class="metric-value">99.9%</p>
            <p class="metric-change">System operating normally</p>
        </article>

    </div>
</section>

<div class="content-grid">

<div>

<section class="panel" id="analytics" aria-labelledby="analytics-heading">
    <h2 id="analytics-heading">Recent Projects</h2>

    <div class="table-wrapper">
        <table>
            <caption>Current enterprise project status</caption>

            <thead>
                <tr>
                    <th scope="col">Project</th>
                    <th scope="col">Owner</th>
                    <th scope="col">Progress</th>
                    <th scope="col">Status</th>
                </tr>
            </thead>

            <tbody>
                <tr>
                    <th scope="row">Digital Transformation</th>
                    <td>Alex Johnson</td>
                    <td>85%</td>
                    <td><span class="status status-active">Active</span></td>
                </tr>

                <tr>
                    <th scope="row">Mobile Application</th>
                    <td>Sarah Williams</td>
                    <td>65%</td>
                    <td><span class="status status-pending">Pending</span></td>
                </tr>

                <tr>
                    <th scope="row">Data Migration</th>
                    <td>David Brown</td>
                    <td>100%</td>
                    <td><span class="status status-completed">Completed</span></td>
                </tr>
            </tbody>
        </table>
    </div>
</section>

<section class="panel" id="reports" aria-labelledby="progress-heading">
    <h2 id="progress-heading">Department Progress</h2>

    <div class="progress-item">
        <div class="progress-header">
            <span id="sales-label">Sales</span>
            <span>75%</span>
        </div>
        <progress value="75" max="100" aria-labelledby="sales-label">75%</progress>
    </div>

    <div class="progress-item">
        <div class="progress-header">
            <span id="development-label">Development</span>
            <span>90%</span>
        </div>
        <progress value="90" max="100" aria-labelledby="development-label">90%</progress>
    </div>

    <div class="progress-item">
        <div class="progress-header">
            <span id="marketing-label">Marketing</span>
            <span>60%</span>
        </div>
        <progress value="60" max="100" aria-labelledby="marketing-label">60%</progress>
    </div>
</section>

</div>

<div>

<section class="panel" id="users" aria-labelledby="activity-heading">
    <h2 id="activity-heading">Recent Activity</h2>

    <ul class="activity-list">
        <li>
            <strong>New user registered</strong>
            <span class="activity-time">10 minutes ago</span>
        </li>
        <li>
            <strong>Project status updated</strong>
            <span class="activity-time">30 minutes ago</span>
        </li>
        <li>
            <strong>Monthly report generated</strong>
            <span class="activity-time">1 hour ago</span>
        </li>
        <li>
            <strong>System backup completed</strong>
            <span class="activity-time">2 hours ago</span>
        </li>
    </ul>
</section>

<section class="panel" id="settings" aria-labelledby="quick-heading">
    <h2 id="quick-heading">Quick Actions</h2>

    <button type="button"
            onclick="showMessage('Report generation started.')">
        Generate Report
    </button>

    <br><br>

    <button type="button"
            onclick="showMessage('User management opened.')">
        Manage Users
    </button>

    <p id="actionMessage" role="status" aria-live="polite" style="margin-top:15px;"></p>
</section>

</div>
</div>

</main>
</div>

<footer>
    <p>&copy; 2026 Enterprise Dashboard. Built with semantic HTML5 and accessible components.</p>
</footer>

<script>
document.getElementById("searchForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const searchValue = document.getElementById("dashboardSearch").value.trim();
    const result = document.getElementById("searchResult");

    if (searchValue === "") {
        result.textContent = "Please enter a search keyword.";
    } else {
        result.textContent = "Searching for " + searchValue + ".";
    }

    result.classList.remove("sr-only");
});

function showMessage(message) {
    document.getElementById("actionMessage").textContent = message;
}
</script>

</body>
</html>
"""

file_path = Path("/content/semantic_accessible_dashboard.html")
file_path.write_text(html_code, encoding="utf-8")

print("Project created successfully!")
print("HTML file:", file_path)

display(HTML(html_code))

from google.colab import files
files.download(str(file_path))
