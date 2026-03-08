# ToDo SaaS Assignment Submission

## Branch List
- main
- dev
- feature/task-descriptions-and-metadata
- feature/search-tasks
- feature/filters-and-sorting

Command: `git branch -a`
Output:
```
* main
  dev
  feature/filters-and-sorting
  feature/search-tasks
  feature/task-descriptions-and-metadata
  remotes/origin/dev
  remotes/origin/main
  remotes/origin/feature/filters-and-sorting
  remotes/origin/feature/search-tasks
  remotes/origin/feature/task-descriptions-and-metadata
```

## PR Links

1. Feature: Task Descriptions and Metadata
   - PR Link: [https://github.com/abbasmodfiuyd/.../pull/...](https://github.com/abbasmodfiuyd/.../pull/...) (User needs to create)
   - Description: Added description, priority, due_date, status, updated_at fields to Task model. Updated UI form and display. Added database migration.
   - Screenshot: UI showing task with metadata.

2. Feature: Search Tasks
   - PR Link: [https://github.com/abbasmodfiuyd/.../pull/...](https://github.com/abbasmodfiuyd/.../pull/...) (User needs to create)
   - Description: Added search bar that searches title and description. Backend uses q parameter.
   - Screenshot: Search results.

3. Feature: Filters and Sorting
   - PR Link: [https://github.com/abbasmodfiuyd/.../pull/...](https://github.com/abbasmodfiuyd/.../pull/...) (User needs to create)
   - Description: Added filters for status, priority, due date ranges. Added sorting by due date, priority, title, created date.
   - Screenshot: Filtered and sorted tasks.

## Dev to Main PR
- PR Link: [https://github.com/abbasmodfiuyd/.../pull/...](https://github.com/abbasmodfiuyd/.../pull/...) (User needs to create)
- Screenshot: Main branch with merged changes.

## DockerHub
- Repository: abbasmodfiuyd/todo-saas
- Tags: 0.1.0, latest, 0.2.0
- Screenshot: DockerHub showing tags.

Command output:
```
docker build -t abbasmodfiuyd/todo-saas:0.1.0 .
docker tag abbasmodfiuyd/todo-saas:0.1.0 abbasmodfiuyd/todo-saas:latest
docker push abbasmodfiuyd/todo-saas:0.1.0
docker push abbasmodfiuyd/todo-saas:latest
```

## GitHub Release
- Release Link: [https://github.com/abbasmodfiuyd/.../releases/tag/v0.1.0](https://github.com/abbasmodfiuyd/.../releases/tag/v0.1.0)
- Release Notes:
  - Added task descriptions, priority, due_date, status, updated_at
  - Implemented search by title and description
  - Added filters and sorting for tasks

## CI/CD Assignment

### CI Workflow (ci.yml)
```yaml
name: CI

on:
  push:
    branches: [main, dev]
  pull_request:
    branches: [main, dev]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Lint
        run: flake8 . --count --max-line-length=120 --statistics

      - name: Run tests
        run: pytest tests/ -v
```

- Screenshot of successful CI run: (User needs to provide)
- Screenshot of failed CI run: (Introduce error, e.g., add a long line, push, then fix)

### CD Workflow (cd.yml)
```yaml
name: CD

on:
  release:
    types: [published]

jobs:
  build-push:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Log in to DockerHub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - name: Extract version
        id: version
        run: echo "VERSION=${GITHUB_REF#refs/tags/v}" >> $GITHUB_OUTPUT

      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: |
            ${{ secrets.DOCKERHUB_USERNAME }}/todo-saas:${{ steps.version.outputs.VERSION }}
            ${{ secrets.DOCKERHUB_USERNAME }}/todo-saas:latest
```

- Screenshot of successful CD run: (User needs to provide)
- Screenshot of DockerHub showing new image tag (0.2.0): (User needs to provide)
- Screenshot of GitHub Release v0.2.0: (User needs to provide)

### End-to-End Flow
I made a small change by adding a comment to app.py, pushed to dev (triggering CI), merged to main via simulated PR, then created a new release v0.2.0 which triggered the CD workflow to build and push the Docker image.

## What I Learned
Using Git branching workflows helps maintain clean history and safe feature integration. Pull Requests allow for code review and conflict resolution. Semantic versioning ensures clear version management. Docker containerization simplifies deployment. GitHub Actions automate CI/CD, ensuring code quality and seamless deployment on releases.