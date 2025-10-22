<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Notes Organizer</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f8f9fa; padding: 30px; }
        h1 { color: #333; }
        form { margin-bottom: 20px; }
        input, textarea { width: 100%; padding: 8px; margin-top: 8px; border: 1px solid #ccc; border-radius: 6px; }
        button { margin-top: 10px; padding: 10px 15px; background-color: #007bff; color: white; border: none; border-radius: 6px; cursor: pointer; }
        button:hover { background-color: #0056b3; }
        .note { background: white; border-radius: 6px; padding: 10px; margin-bottom: 10px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
        .category { font-size: 0.9em; color: #888; }
    </style>
</head>
<body>
    <h1>Notes Organizer</h1>
    <form action="/add" method="post">
        <input type="text" name="title" placeholder="Note title" required>
        <textarea name="content" placeholder="Write your note..." rows="4" required></textarea>
        <input type="text" name="category" placeholder="Category (optional)">
        <button type="submit">Add Note</button>
    </form>

    <h2>Your Notes</h2>
    {% for note in notes %}
        <div class="note">
            <h3>{{ note.title }}</h3>
            <p>{{ note.content }}</p>
            {% if note.category %}
                <p class="category">Category: {{ note.category }}</p>
            {% endif %}
        </div>
    {% else %}
        <p>No notes yet!</p>
    {% endfor %}
</body>
</html>
