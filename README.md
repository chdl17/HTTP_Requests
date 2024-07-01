<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Fetch Project</title>
</head>
<body>
    <h1>Data Fetch Project</h1>
    <p>This project demonstrates how to fetch data from a URL using Python, process the JSON response, and handle potential errors gracefully. The project uses environment variables to store the URL and includes methods for making HTTP requests and processing the responses.</p>
    <h2>Getting Started</h2>
    <p>To get started with this project, follow the steps below:</p>
    <ol>
        <li>Clone the repository to your local machine.</li>
        <li>Ensure you have Python installed on your machine.</li>
        <li>Install the required libraries using pip:</li>
    </ol>
    <pre><code>pip install requests pandas python-dotenv</code></pre>
    <h2>Environment Variables</h2>
    <p>Create a <code>.env</code> file in the root directory of the project and add the following line:</p>
    <pre><code>URL=your_api_url_here</code></pre>
    <p>Replace <code>your_api_url_here</code> with the actual URL you want to fetch data from.</p>
    <h2>Usage</h2>
    <p>Here is an example of how to use the <code>DataFetch</code> class:</p>
    <pre><code>import requests
