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
- Tags: 0.1.0, latest
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

## What I Learned
Using Git branching workflows helps maintain clean history and safe feature integration. Pull Requests allow for code review and conflict resolution. Semantic versioning ensures clear version management. Docker containerization simplifies deployment.