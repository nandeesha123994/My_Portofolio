from django.shortcuts import render, Http404

# --- Static Blog Data ---
POSTS = [
    {
        'slug': 'django-authentication-basics',
        'title': 'Mastering Django Authentication',
        'date': 'Dec 22, 2024',
        'read_time': '5 min read',
        'tags': ['Django', 'Security', 'Auth'],
        'description': 'A deep dive into how Django handles user login, signup, and password hashing securely out of the box.',
        'content': '''
            <h3>Why Authentication Matters</h3>
            <p>Authentication is the backbone of most web applications. It allows us to verify who a user is. Django provides a robust built-in User model and auth system that handles the heavy lifting.</p>
            
            <h3>The User Model</h3>
            <p>Django's <code>auth.User</code> model comes with fields like username, email, password, first_name, and last_name. It also handles password hashing automatically using PBKDF2 by default, making it secure against common attacks.</p>

            <h3>Login and Logout</h3>
            <p>Using <code>django.contrib.auth</code>, implementing login is as simple as:</p>
            <pre><code>from django.contrib.auth import authenticate, login
user = authenticate(username=u, password=p)
if user is not None:
    login(request, user)</code></pre>
            
            <h3>Key Takeaway</h3>
            <p>Never roll your own crypto! Always use Django's built-in authentication system unless you have a very specific reason not to.</p>
        '''
    },
    {
        'slug': 'sql-optimization-tips',
        'title': 'Writing Efficient SQL Queries',
        'date': 'Dec 24, 2024',
        'read_time': '4 min read',
        'tags': ['SQL', 'Database', 'Performance'],
        'description': 'Learn how to speed up your backend by writing smarter SQL queries and understanding indexing.',
        'content': '''
            <h3>The N+1 Problem</h3>
            <p>One of the most common performance killers in Django/ORM is the N+1 problem. This happens when you loop through objects and access a related object in each iteration, causing a new query every time.</p>
            <p><strong>Fix:</strong> Use <code>select_related</code> (for ForeignKey) or <code>prefetch_related</code> (for ManyToMany) to fetch data in a single query.</p>

            <h3>Indexing</h3>
            <p>Indexes are like the index at the back of a book. Without them, the database has to scan every row (full table scan) to find what you want. Adding an index to frequently searched columns (like email or username) drastically improves read speed.</p>
            
            <h3>Select Only What You Need</h3>
            <p>Instead of <code>Model.objects.all()</code>, use <code>.values('id', 'name')</code> or <code>.only('name')</code> if you don't need every field. This reduces the data transfer load.</p>
        '''
    },
    {
        'slug': 'rest-api-basics',
        'title': 'Understanding REST APIs',
        'date': 'Dec 25, 2024',
        'read_time': '6 min read',
        'tags': ['API', 'REST', 'JSON'],
        'description': 'What makes an API "RESTful"? Exploring the principles of statelessness and standard HTTP methods.',
        'content': '''
            <h3>What is REST?</h3>
            <p>REST (Representational State Transfer) is an architectural style for designing networked applications. It relies on a stateless, client-server, cacheable communications protocol -- virtually always the HTTP protocol.</p>

            <h3>HTTP Methods</h3>
            <ul>
                <li><strong>GET</strong>: Retrieve data (safe, idempotent).</li>
                <li><strong>POST</strong>: Create new data.</li>
                <li><strong>PUT</strong>: Update existing data (full).</li>
                <li><strong>PATCH</strong>: Update existing data (partial).</li>
                <li><strong>DELETE</strong>: Remove data.</li>
            </ul>

            <h3>Status Codes</h3>
            <p>Communicating the result is crucial. 200 means OK, 201 means Created, 400 is Bad Request, 401 is Unauthorized, and 500 is Server Error. Using these correctly makes your API professional.</p>
        '''
    }
]

def post_list(request):
    return render(request, 'learning_logs/post_list.html', {'posts': POSTS})

def post_detail(request, slug):
    post = next((item for item in POSTS if item['slug'] == slug), None)
    if post is None:
        raise Http404("Post not found")
    return render(request, 'learning_logs/post_detail.html', {'post': post})
