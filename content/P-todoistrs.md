---
path: /projects/todoist-rs.html
---
# todoist-rs 🦀

i use [Todoist](https://todoist.com) as my todo task manager. i like its label system, the mobile app, and most of all its [Quick Add feature](https://todoist.com/help/articles/use-task-quick-add-in-todoist-va4Lhpzz). however, there is no linux client that isn't just a web app. i use linux on my laptop that comes with me everywhere, and so i decided to create a TUI rust-based client for todoist using its Sync API.

currently it can:

- create a task using quick add
  - this means no description can be set right now
- display a list of all currently uncompleted tasks
- can display the title, priority, description, and due date of a currently uncompleted task
- can mark any currently uncompleted task as complete

i don't know how it interacts with different projects or collaborators, and have no plans to find out because i don't use these features.

i have plans to implement:

- better error handling
- maybe if i can work out non-blocking api requests so it doesn't feel as slow

you can find the [client here on my github](https://github.com/blltrx/todoist-rs), and install using 'cargo install --git'.

