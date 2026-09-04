# Backend Developer Roadmap — 0 to Hired in 2 Years (AI-Augmented)

*A complete, self-paced study plan for going from basic Python familiarity to a first backend developer job, studying ~5 hours/day, 6 days/week, over 24 months.*

---

## Table of Contents

1. [Assumptions & Overview](#1-assumptions--overview)
2. [Weekly Schedule (Full 2 Years)](#2-weekly-schedule-full-2-years)
3. [Detailed Topic Breakdown](#3-detailed-topic-breakdown)
4. [Tasks, Challenges & AI Workflows](#4-tasks-challenges--ai-workflows)
5. [Milestone Projects](#5-milestone-projects)
6. [Core Topic Coverage Map](#6-core-topic-coverage-map)
7. [Job Preparation Plan](#7-job-preparation-plan)
8. [Progress Tracking](#8-progress-tracking)

---

## 1. Assumptions & Overview

### 1.1 Stated assumptions and adjustments

- **Study capacity:** 5 hours/day × 6 days/week = **30 hours/week**, for 24 months = **104 weeks ≈ 3,000+ hours**. This is realistic for someone with free time (student, career-break, or reducing other commitments) but it is *aggressive* — most working adults cannot sustain this. If you're studying alongside a full-time job, stretch this plan to 3–4 years by keeping the same content but halving weekly hours.
- **Adjustment made:** I built in **1 buffer/review week roughly every 8 weeks** (marked "Buffer Week" in the schedule) for catch-up, spaced repetition, and burnout prevention. Skipping buffer weeks is fine if you're ahead of schedule — use them for extra project polish instead.
- **1 rest day/week is mandatory.** Five hours a day, six days a week, for two years without a real day off is a reliable route to burnout and worse retention. Do not skip rest days to "get ahead" — cognitive consolidation happens during rest, not just during study.
- **"Basic Python familiarity"** is assumed to mean: you've seen variables, loops, if/else, and functions, but haven't built anything real, don't know OOP well, and have never touched a database, a web framework, git, or the command line seriously. The plan starts there.
- **Goal definition:** "hireable" means you can pass a first-round technical screen, build and defend a non-trivial REST API with a database, explain your design decisions, and demonstrate you can use AI tools *productively and critically* (not blindly) — because that is now a baseline expectation, not a bonus, in 2026 hiring.

### 1.2 High-level 2-year summary

| Stage | Months | Focus |
|---|---|---|
| Stage A — Foundations | 1–4 | Python (basic → advanced), CS fundamentals, Git, Linux/CLI |
| Stage B — Web & Data Basics | 4–6 | HTTP, REST, SQL, relational data modeling |
| Stage C — Framework Mastery | 6–9 | FastAPI deep dive (+ Django overview), ORMs, migrations |
| Stage D — Production Skills | 9–13 | Auth, security, testing, Docker, CI/CD, cloud deployment |
| Stage E — Scaling & Systems | 13–18 | Caching, background jobs, observability, system design |
| Stage F — AI-Native Engineering | 18–19 | Deep agentic AI workflows, legacy code, verification skills |
| Stage G — Capstone | 19–22 | One large, portfolio-defining production-grade project |
| Stage H — Job Hunt | 22–24+ | Resume, portfolio polish, interviews, applications (continues until hired) |

### 1.3 Phase list (used throughout this document)

| Phase | Weeks | Title |
|---|---|---|
| 0 | 1 | Orientation & Environment Setup |
| 1 | 2–9 | Python Foundations |
| 2 | 10–17 | Python Advanced + DSA Basics + Git/Linux |
| 3 | 18–25 | HTTP, REST & SQL Fundamentals |
| 4 | 26–34 | FastAPI Framework Deep Dive |
| 5 | 35–42 | Databases & ORMs Deep Dive |
| 6 | 43–50 | Auth, Security & Testing |
| 7 | 51–58 | Docker, CI/CD & Cloud Deployment |
| 8 | 59–66 | Caching, Background Jobs & Observability |
| 9 | 67–76 | System Design & Advanced Backend Topics |
| 10 | 77–84 | AI-Assisted Engineering Deep Dive |
| 11 | 85–98 | Capstone Project |
| 12 | 99–104+ | Portfolio Polish, Resume & Job Search |

> **AI tools used throughout:** ChatGPT/Claude for explanations, Cursor or Windsurf as your daily AI-powered IDE from Phase 2 onward, GitHub Copilot for inline completion, and Aider (or Claude Code) as your autonomous multi-file agent from Phase 6 onward. Introducing agentic tools *after* you can already code the fundamentals yourself is deliberate — you need to be able to judge AI output critically before you lean on it heavily.

---

## 2. Weekly Schedule (Full 2 Years)

**Format note:** Weeks 1–9 (the first 2 months, Phases 0–1) are given in **full detail** — topic, subtopics, hours, practice tasks, deliverables, checklist, and resources — so you can see exactly what "highly detailed" looks like. From Week 10 onward, the same fields are given in a **compact table format, one row per week**, to keep this document usable as a single file across 104 weeks. Full resource lists, easy/medium/hard tasks, and acceptance criteria for every topic named in the tables are in **Section 3** and **Section 4** — cross-reference by topic name. Every week assumes **30 hours** unless marked otherwise (Buffer Weeks are lighter, ~15–20 hours, deliberately).

### Phase 0 — Orientation & Environment Setup

#### Week 1 — Tooling, Git, and Your AI Stack
- **Subtopics:** Install Python 3.12+ (via `pyenv` or official installer); install VS Code *and* Cursor; install Git; create a GitHub account; install Docker Desktop (just to have it ready); sign up for Claude and ChatGPT; learn Markdown basics; set up a terminal you like (iTerm2/Windows Terminal + a shell like zsh).
- **Estimated hours:** 30
- **Practice tasks:** Write and run a 20-line "hello world" script that takes CLI input and prints formatted output. Initialize a git repo, make 5 commits, push to GitHub. Ask an AI assistant to explain what a virtual environment is and why backend devs use one — then verify the answer against the official Python docs.
- **Deliverables:** A GitHub repo called `learning-log` with a `README.md` containing a template you'll fill in weekly (topic, hours, what you built, blockers).
- **Success checklist:** ☐ `python3 --version` works ☐ `git --version` works ☐ GitHub repo exists with ≥5 commits ☐ Cursor/VS Code + Copilot installed and authenticated ☐ Can explain, in your own words, what a REPL is.
- **Resources:** [python.org downloads](https://www.python.org/downloads/), [Git Book ch. 1–2](https://git-scm.com/book/en/v2), [GitHub Quickstart](https://docs.github.com/en/get-started/quickstart), Cursor docs.

### Phase 1 — Python Foundations

#### Week 2 — Core Syntax
- **Subtopics:** Variables & naming, primitive types (int, float, str, bool), type conversion, operators (arithmetic, comparison, logical, assignment), f-strings, `input()`/`print()`, if/elif/else, basic debugging with `print()`.
- **Estimated hours:** 30
- **Practice tasks:** Build a BMI calculator, a temperature converter, a simple grade classifier (if/elif chains), a number-guessing game.
- **Deliverables:** 4 small scripts committed to `learning-log/week02/`.
- **Success checklist:** ☐ Can explain mutability of str vs list ☐ Comfortable with f-strings ☐ No `print()`-only debugging by end of week — used a debugger once.
- **Resources:** [Python official tutorial ch. 3–4](https://docs.python.org/3/tutorial/), *Automate the Boring Stuff with Python* (free online) ch. 1–3, Corey Schafer's Python Basics YouTube series.

#### Week 3 — Loops, Lists, Tuples, First Functions
- **Subtopics:** `for`/`while` loops, `range()`, `break`/`continue`, lists (indexing, slicing, mutation, common methods), tuples & immutability, nested loops, writing your first functions with parameters and return values.
- **Estimated hours:** 30
- **Practice tasks:** FizzBuzz, a list of student scores → compute average/max/min, a simple text-based Rock-Paper-Scissors game, a function library of 10 small utility functions (is_prime, reverse_string, etc.).
- **Deliverables:** `learning-log/week03/` with 5 scripts + a `utils.py` module.
- **Success checklist:** ☐ Can slice a list confidently ☐ Understands list vs tuple use cases ☐ Every function has a docstring.
- **Resources:** Python tutorial ch. 5, LeetCode "Easy" array problems (untimed), CS50P (Harvard, free) lectures 1–3.

#### Week 4 — Dictionaries, Sets, Functions Deep Dive, Error Handling
- **Subtopics:** Dicts (creation, access, `.get()`, iteration), sets & set operations, `*args`/`**kwargs`, default arguments, variable scope (LEGB), `try`/`except`/`else`/`finally`, raising custom exceptions.
- **Estimated hours:** 30
- **Practice tasks:** Word-frequency counter from a text file, a contact book (dict of dicts) with add/search/delete, a calculator that handles divide-by-zero and invalid input gracefully.
- **Deliverables:** `contact_book.py` with full error handling, committed with a README explaining design choices.
- **Success checklist:** ☐ Can explain LEGB scope ☐ Uses specific exceptions, not bare `except:` ☐ Wrote at least one custom exception class.
- **Resources:** Python tutorial ch. 8–9, Real Python "Python Exceptions: An Introduction".

#### Week 5 — File I/O, Modules, Virtual Environments, Stdlib Tour
- **Subtopics:** Reading/writing text and CSV files, `with` statement, JSON serialization (`json` module), creating your own modules/packages, `venv` + `pip`, `requirements.txt`, tour of `os`, `sys`, `datetime`, `pathlib`, `argparse`.
- **Estimated hours:** 30
- **Practice tasks:** Build a CLI expense tracker that persists to a JSON file, using `argparse` for commands (`add`, `list`, `delete`, `summary`).
- **Deliverables:** Expense-tracker CLI, run from `venv`, with a `requirements.txt` (even if empty) and a usage README.
- **Success checklist:** ☐ App state survives restarts (real persistence) ☐ Uses `pathlib` not string paths ☐ Runs cleanly in a fresh venv on first try.
- **Resources:** Real Python "Working With JSON Data", `argparse` official docs, Real Python "Python Virtual Environments: A Primer".

#### Week 6 — OOP Part 1: Classes & Objects
- **Subtopics:** `class`/`__init__`/`self`, instance vs class attributes, methods, `__str__`/`__repr__`, basic encapsulation conventions (`_private`), simple class relationships.
- **Estimated hours:** 30
- **Practice tasks:** Rewrite the Week 5 expense tracker using an `Expense` class and an `ExpenseManager` class instead of raw dicts. Build a `BankAccount` class with deposit/withdraw and balance validation.
- **Deliverables:** Refactored, class-based expense tracker.
- **Success checklist:** ☐ No business logic sitting outside classes ☐ `__repr__` implemented and useful for debugging ☐ Can explain difference between instance and class attributes.
- **Resources:** Python tutorial ch. 9, Corey Schafer OOP YouTube series (parts 1–2).

#### Week 7 — OOP Part 2: Inheritance, Polymorphism, Composition
- **Subtopics:** Inheritance & `super()`, method overriding, polymorphism, abstract base classes (`abc`), composition vs inheritance, dunder methods (`__eq__`, `__lt__`, `__len__`).
- **Estimated hours:** 30
- **Practice tasks:** Model a `Shape` hierarchy (Circle, Rectangle, Triangle) with polymorphic `area()`/`perimeter()`. Build a small library-management console app (Book, Member, Library classes) using composition.
- **Deliverables:** Library-management console app with ≥3 related classes.
- **Success checklist:** ☐ Used `super()` correctly ☐ Can articulate when to prefer composition over inheritance ☐ Implemented at least 2 dunder methods.
- **Resources:** Real Python "Inheritance and Composition: A Python OOP Guide", `abc` module docs.

#### Week 8 — Comprehensions, Generators, Decorators, Context Managers
- **Subtopics:** List/dict/set comprehensions, generator functions & `yield`, iterators/`__iter__`/`__next__`, first-class functions, closures, writing simple decorators, `contextlib`/custom context managers.
- **Estimated hours:** 30
- **Practice tasks:** Rewrite loops from earlier weeks as comprehensions. Write a generator that lazily reads a huge file line-by-line. Write a `@timer` decorator and a `@retry(times=3)` decorator. Write a custom context manager for a "fake" DB connection.
- **Deliverables:** `decorators.py` and `generators.py` mini-libraries with tests you can run manually.
- **Success checklist:** ☐ Can explain why generators save memory ☐ Decorator preserves function metadata (`functools.wraps`) ☐ Comfortable reading `with` statements you didn't write.
- **Resources:** Real Python "Primer on Python Decorators", Real Python "How to Use Generators and yield".

#### Week 9 — Buffer Week + Consolidation Project
- **Subtopics:** Review weeks 2–8, close knowledge gaps, first real AI-workflow practice (using AI to review your own code for style and bugs).
- **Estimated hours:** 20 (buffer week)
- **Practice tasks:** Build a **"Personal CLI Toolkit"** — a single Python package combining a to-do list, expense tracker, and contact book behind one CLI entry point, fully class-based, with JSON persistence, `argparse` subcommands, and proper error handling. Then ask an AI coding assistant to review the whole codebase and produce a list of concrete improvements; implement the ones you agree with and note *why* you rejected the ones you didn't.
- **Deliverables:** `personal-cli-toolkit` repo, published on GitHub with a proper README (install instructions, usage examples, screenshot of a run).
- **Success checklist:** ☐ Code passes a fresh AI code review with no major flags ☐ You can defend every design decision out loud ☐ Repo has a real README, not just code.
- **Resources:** N/A (integration week) — use Claude/ChatGPT as your code reviewer.


### Phase 2 — Python Advanced + DSA Basics + Git/Linux (Weeks 10–17)

| Wk | Topic | Subtopics | Hrs | Practice Tasks | Deliverable |
|---|---|---|---|---|---|
| 10 | Git for real workflows | Branching, merging, rebasing vs merging, `.gitignore`, resolving conflicts, PR workflow | 30 | Simulate a feature-branch workflow solo: branch → commit → PR → merge; deliberately create and resolve a merge conflict | A repo with a clean branch history and 3 merged PRs |
| 11 | Linux & CLI fundamentals | Filesystem hierarchy, permissions (`chmod`/`chown`), piping & redirection, `grep`/`sed`/`awk` basics, `ssh`, process management (`ps`, `top`, `kill`) | 30 | Write 5 one-liners combining `grep`/`awk`/`sort` on a log file; SSH into a free cloud VM (e.g., free-tier instance) and navigate it | `cli-cheatsheet.md` in learning-log with your own working commands |
| 12 | DSA: Complexity & Arrays | Big-O notation, time/space tradeoffs, array/string algorithms (two-pointer, sliding window) | 30 | Solve 12 Easy array/string problems (LeetCode/NeetCode) untimed, then timed | Solutions repo `dsa-practice` with Big-O noted per solution |
| 13 | DSA: Linked Lists, Stacks, Queues | Singly/doubly linked lists, stack & queue implementations, when each is used in backend systems | 30 | Implement a linked list from scratch (no libraries); solve 8 related Easy/Medium problems | `data_structures.py` with tested implementations |
| 14 | DSA: Hashing & Recursion | Hash maps under the hood, collision handling, recursion & recursion trees, memoization | 30 | Implement a hash map from scratch; solve 10 hashing/recursion problems | Hash map implementation + solved problem set |
| 15 | DSA: Trees & Graphs (Intro) | Binary trees, BST, tree traversals (DFS/BFS), basic graph representation (adjacency list) | 30 | Implement BST insert/search/delete; solve 8 tree problems; implement BFS/DFS on a small graph | Tree/graph implementation notebook |
| 16 | DSA: Sorting & Searching | Bubble/merge/quick sort tradeoffs, binary search and variants | 30 | Implement merge sort and quicksort from scratch; solve 8 binary-search problems | Sorting algorithms with Big-O comparison table you wrote yourself |
| 17 | Buffer + AI-agent intro | Review DSA weak spots; first real use of an AI coding agent (Cursor/Aider) for refactoring your Week 9 CLI toolkit | 20 | Ask an AI agent to refactor `personal-cli-toolkit` into cleaner modules across multiple files in one pass; review every diff line-by-line before accepting | Refactored toolkit + a short note on what the AI got wrong |

### Phase 3 — HTTP, REST & SQL Fundamentals (Weeks 18–25)

| Wk | Topic | Subtopics | Hrs | Practice Tasks | Deliverable |
|---|---|---|---|---|---|
| 18 | Networking & HTTP | TCP/IP basics (conceptual), DNS, HTTP request/response cycle, methods, status codes, headers, cookies | 30 | Use `curl`/Postman to manually construct 10 requests to public APIs; inspect headers in browser dev tools | `http-notes.md` mapping every status code you used to a real scenario |
| 19 | REST API design + first API | REST principles, resource naming, statelessness, building a minimal API with Flask (bridge framework) | 30 | Build a 5-endpoint in-memory "bookshelf" API with Flask (no DB yet) | Working Flask API tested with Postman/curl scripts |
| 20 | SQL basics | `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`, basic `JOIN`, `INSERT`/`UPDATE`/`DELETE` | 30 | Install PostgreSQL locally; complete SQLBolt or Mode SQL tutorial exercises; write 15 queries against a sample dataset | `sql-basics.sql` file with commented queries |
| 21 | SQL intermediate | `JOIN` types deep dive, `GROUP BY`/`HAVING`, aggregate functions, subqueries, `CASE` | 30 | Solve 15 intermediate SQL exercises (e.g., on a Northwind/Chinook sample DB) | Query set with explanations of *why* each join type was chosen |
| 22 | Relational design | Normalization (1NF–3NF), ER diagrams, primary/foreign keys, choosing data types | 30 | Design an ER diagram for a "library system" from scratch, then implement the schema in Postgres | ER diagram (image) + `schema.sql` |
| 23 | SQL advanced | Indexes (B-tree basics), transactions & ACID, constraints (`CHECK`, `UNIQUE`), views | 30 | Add indexes to the library schema and measure query speed before/after with `EXPLAIN ANALYZE` | Before/after performance notes |
| 24 | Python ↔ Postgres | `psycopg2`/`asyncpg` basics, parameterized queries (SQL injection prevention), connection pooling concepts | 30 | Rewrite the Flask bookshelf API to persist to Postgres using raw SQL (no ORM yet) | DB-backed Flask API |
| 25 | Buffer + Milestone 1 | Consolidation, first portfolio-quality project | 20 | See **Milestone Project 1** in Section 5 | Milestone 1 shipped & on GitHub |

### Phase 4 — FastAPI Framework Deep Dive (Weeks 26–34)

| Wk | Topic | Subtopics | Hrs | Practice Tasks | Deliverable |
|---|---|---|---|---|---|
| 26 | FastAPI basics | Routing, path/query params, Pydantic models for validation, automatic docs (Swagger/OpenAPI) | 30 | Rebuild the bookshelf API in FastAPI; compare ergonomics vs Flask | FastAPI version of bookshelf API |
| 27 | Request/response handling | Request bodies, response models, status codes, exception handlers, `HTTPException` | 30 | Add full validation + custom error responses to bookshelf API | API with consistent, documented error format |
| 28 | Dependency injection & structure | `Depends()`, routers (`APIRouter`), recommended project layout (routers/services/schemas) | 30 | Refactor bookshelf API into a proper multi-file project structure | Restructured project following FastAPI best-practice layout |
| 29 | Async Python in FastAPI | `async`/`await` fundamentals, event loop basics, async DB drivers, when async actually helps | 30 | Convert DB calls to async; write a small benchmark comparing sync vs async under concurrent load | Benchmark write-up with numbers |
| 30 | Django survey week | MVT pattern, models, admin panel, templates, URL routing — enough to be conversant in interviews | 30 | Build the same bookshelf app's core CRUD in Django to feel the contrast | Small Django app (not deeply polished — survey only) |
| 31 | DRF overview + stack decision | Django REST Framework basics, serializers, viewsets; explicitly decide FastAPI as your primary stack going forward | 25 | Build 3 DRF endpoints; write a short comparison doc: FastAPI vs Django/DRF, when you'd pick each | `fastapi-vs-django.md` comparison doc (great interview talking point) |
| 32 | FastAPI + SQLAlchemy | Wiring FastAPI to SQLAlchemy models, session management, dependency-injected DB sessions | 30 | Swap raw SQL in bookshelf API for SQLAlchemy models | ORM-backed FastAPI app |
| 33 | Uploads, background tasks, pagination | File uploads, `BackgroundTasks`, pagination/filtering/sorting patterns, query param validation | 30 | Add cover-image upload, pagination, and filtering to bookshelf API | Feature-complete bookshelf API v1 |
| 34 | Buffer + consolidation | Polish bookshelf API into a genuinely presentable small project | 20 | AI-assisted code review pass (Section 4 AI workflows) | Bookshelf API pushed with full README, ready to show recruiters as an early sample |

### Phase 5 — Databases & ORMs Deep Dive (Weeks 35–42)

| Wk | Topic | Subtopics | Hrs | Practice Tasks | Deliverable |
|---|---|---|---|---|---|
| 35 | SQLAlchemy Core & ORM | Engine, Session, declarative models, Core vs ORM query styles | 30 | Rebuild a schema using pure SQLAlchemy Core, then again with ORM; compare | Two implementations + comparison notes |
| 36 | Relationships | One-to-one, one-to-many, many-to-many, `relationship()`, lazy vs eager loading | 30 | Model a "blog" domain: User, Post, Comment, Tag (many-to-many) | Blog schema with relationships, seeded with sample data |
| 37 | Alembic migrations | Migration concepts, autogenerate, upgrade/downgrade, handling data migrations | 30 | Set up Alembic on the blog project; write 3 manual migrations including one data migration | Migration history you can upgrade/downgrade cleanly |
| 38 | Data modeling in practice | Denormalization tradeoffs, soft deletes, audit columns (`created_at`/`updated_at`), seed scripts | 30 | Add soft-delete and audit fields to blog schema; write a seed script with fake data (Faker library) | `seed.py` producing realistic sample data |
| 39 | Query optimization | `EXPLAIN ANALYZE`, N+1 query problem, eager loading fixes, index strategy | 30 | Deliberately introduce an N+1 bug in the blog API, measure it, then fix it and re-measure | Before/after query-count and latency comparison |
| 40 | NoSQL intro | Document stores vs relational (conceptual), MongoDB basics, Redis as a data store (not just cache) | 25 | Store blog comments in MongoDB as an experiment; compare querying experience to Postgres | `nosql-vs-sql.md` notes doc |
| 41 | Full layered CRUD API | Layered architecture: routers → services → repositories → models, dependency injection throughout | 30 | Rebuild the blog API with a clean layered architecture and full CRUD on all resources | Layered blog API, ready for Milestone 2 |
| 42 | Buffer + Milestone 2 | Consolidation, first "real" multi-resource project | 20 | See **Milestone Project 2** in Section 5 | Milestone 2 shipped & on GitHub |

### Phase 6 — Auth, Security & Testing (Weeks 43–50)

| Wk | Topic | Subtopics | Hrs | Practice Tasks | Deliverable |
|---|---|---|---|---|---|
| 43 | Auth concepts | Sessions vs tokens, password hashing (`bcrypt`/`argon2`), why plaintext passwords are a firing offense | 30 | Implement registration + login with hashed passwords (no JWT yet, session-based) | Working session-based auth on blog API |
| 44 | JWT auth | Access/refresh tokens, JWT structure & signing, token expiry, storing tokens client-side safely | 30 | Replace session auth with JWT auth; implement refresh-token rotation | JWT-secured blog API |
| 45 | OAuth2 & RBAC | OAuth2 flow (conceptual + "Login with Google"), role-based access control, permission decorators | 30 | Add "admin" vs "author" vs "reader" roles to blog API with route-level permission checks | RBAC-secured blog API |
| 46 | Security hardening | Input validation, SQL injection, XSS/CSRF concepts, CORS, basic rate limiting, secrets management (`.env`, never committing secrets) | 30 | Run an OWASP ZAP or manual checklist audit against your own API; fix every issue found | Security audit write-up + fixes committed |
| 47 | Testing fundamentals | `pytest` basics, assertions, fixtures, parametrize, test organization | 30 | Write unit tests for all pure-logic functions in blog API (target 70%+ coverage on services layer) | Test suite + coverage report |
| 48 | Integration testing | Test DB setup (separate test database or transactions-per-test), `TestClient`, mocking external calls | 30 | Write integration tests hitting real endpoints against a test DB; mock an external email/notification call | Full integration test suite, CI-runnable |
| 49 | TDD + AI-assisted TDD | Red-green-refactor cycle, writing tests before code, using AI to generate edge-case test lists | 30 | Build one new feature (e.g., "post likes") strictly test-first; use AI to brainstorm edge cases you missed, then write those tests yourself | New feature built TDD-style with a documented test list |
| 50 | Buffer + Milestone 3 | Consolidation | 20 | See **Milestone Project 3** in Section 5 (roughly your 1-year mark) | Milestone 3 shipped & on GitHub |

### Phase 7 — Docker, CI/CD & Cloud Deployment (Weeks 51–58)

| Wk | Topic | Subtopics | Hrs | Practice Tasks | Deliverable |
|---|---|---|---|---|---|
| 51 | Docker fundamentals | Images vs containers, `Dockerfile` syntax, layers & caching, multi-stage builds | 30 | Dockerize the blog API with a multi-stage `Dockerfile`; optimize image size | Dockerized app, image under a size target you set |
| 52 | Docker Compose | Multi-container apps, networking between containers, volumes, `.env` in Compose | 30 | Write `docker-compose.yml` for app + Postgres + Redis; make `docker compose up` fully bootstrap the dev environment | One-command local dev environment |
| 53 | Team Git workflows | PR etiquette, code review as a skill, conventional commits, semantic versioning basics | 25 | Find a small open-source repo, open one real PR (typo fix, small feature, or doc improvement) | A real merged (or submitted) open-source PR |
| 54 | CI basics | GitHub Actions syntax, running lint/tests on every push, caching dependencies in CI | 30 | Set up a GitHub Actions workflow: lint → test → build on every PR | Green CI pipeline on blog API repo |
| 55 | CD basics | Deploying to Render/Fly.io/Railway, environment variables & secrets in production, zero-downtime basics | 30 | Deploy the Dockerized blog API to a free-tier cloud host with a working public URL | Live, publicly accessible API URL |
| 56 | Cloud fundamentals (AWS/GCP) | Compute (EC2/Compute Engine), storage (S3/Cloud Storage), IAM basics — conversational fluency, not mastery | 30 | Manually deploy a container to a free-tier cloud VM once, by hand, to understand what platforms like Render automate | Notes doc: what Render/Fly.io actually does under the hood |
| 57 | Production readiness | 12-factor app principles, health-check endpoints, structured config, graceful shutdown | 25 | Add `/health` and `/ready` endpoints; externalize all config to environment variables | Production-readiness checklist, all items checked |
| 58 | Buffer + full pipeline | End-to-end: push to `main` → CI runs → deploys automatically | 20 | Wire CD into the GitHub Actions pipeline (deploy on merge to `main`) | Fully automated CI/CD pipeline, demoable |

### Phase 8 — Caching, Background Jobs & Observability (Weeks 59–66)

| Wk | Topic | Subtopics | Hrs | Practice Tasks | Deliverable |
|---|---|---|---|---|---|
| 59 | Redis & caching | Caching patterns (cache-aside, write-through), TTLs, cache invalidation strategies | 30 | Add Redis caching to the blog API's most-read endpoint; measure latency improvement | Before/after latency benchmark |
| 60 | Background jobs | Celery or RQ basics, task queues, worker processes, why you can't do everything in the request/response cycle | 30 | Move "send welcome email" and "resize uploaded image" to background tasks | Async job pipeline with a visible worker log |
| 61 | Advanced background jobs | Retries with backoff, scheduled/periodic tasks (Celery beat / RQ scheduler), idempotency | 30 | Add a nightly "digest email" scheduled job with retry logic | Scheduled job running reliably in dev |
| 62 | Performance & profiling | `cProfile`, identifying bottlenecks, sync vs async tradeoffs revisited, connection pool tuning | 30 | Profile the blog API under simulated load (e.g., `locust`); fix the top 2 bottlenecks found | Load-test report, before/after |
| 63 | Logging | Structured (JSON) logging, log levels, correlation/request IDs, avoiding logging secrets | 25 | Replace all `print()` debugging with structured logging across the app | Consistent logging setup, sample log output in README |
| 64 | Observability | Metrics basics (Prometheus/Grafana concepts), tracing concepts, error tracking with Sentry | 30 | Wire up Sentry (free tier) for error tracking; add a basic `/metrics` endpoint | Working error-tracking dashboard |
| 65 | Rate limiting & webhooks | API gateway concepts, rate limiting middleware, designing and consuming webhooks | 30 | Add rate limiting to public endpoints; implement an outbound webhook system for "new post published" | Rate-limited API + working webhook demo |
| 66 | Buffer + integration | Bring caching, jobs, logging, and observability together into one cohesive app | 20 | Full regression pass: does everything still work together? | Updated blog API — this is now a strong portfolio piece on its own |

### Phase 9 — System Design & Advanced Backend Topics (Weeks 67–76)

| Wk | Topic | Subtopics | Hrs | Practice Tasks | Deliverable |
|---|---|---|---|---|---|
| 67 | System design vocabulary | Vertical vs horizontal scaling, load balancers, stateless services, CDNs | 30 | Read/watch 3 system-design primers; summarize each in your own words (no copy-paste) | `system-design-notes.md` started |
| 68 | Data at scale | CAP theorem, consistency models, replication, sharding/partitioning concepts | 30 | Explain, in writing, how you'd shard the blog API's `posts` table if it hit 500M rows | Written design note |
| 69 | Message queues & events | Kafka/RabbitMQ concepts, pub/sub, event-driven architecture basics | 30 | Add a simple pub/sub flow using Redis Pub/Sub or a lightweight queue between two services | Working event-driven mini-flow |
| 70 | Microservices vs monolith | Tradeoffs, API gateway pattern, service-to-service auth/communication | 25 | Split one feature of the blog API (e.g., notifications) into a separate service communicating over HTTP | Two small services talking to each other |
| 71 | System design practice 1 | Practice designing: URL shortener, rate limiter | 30 | Write full design docs (requirements → high-level design → deep dive → tradeoffs) for both, using AI as a critique partner, not an answer generator | 2 design docs |
| 72 | System design practice 2 | Practice designing: news-feed system, notification system | 30 | Same design-doc process for both | 2 more design docs |
| 73 | Advanced SQL / warehousing | Read replicas, basic data-warehousing concepts, materialized views | 25 | Set up a read replica locally (or simulate with a second Postgres instance) and route read traffic to it | Notes + working local read-replica demo |
| 74 | API design best practices | Versioning strategies, idempotency keys, GraphQL overview (conceptual), REST maturity model | 25 | Add API versioning (`/v1/`) to blog API; write a short GraphQL vs REST comparison | Versioned API + comparison doc |
| 75 | OWASP Top 10 hands-on | Injection, broken auth, sensitive data exposure, SSRF, etc. — hands-on exercises | 30 | Deliberately introduce and then fix 3 OWASP Top 10 vulnerabilities in a sandbox copy of your app | Vulnerability + fix write-up |
| 76 | Buffer + Milestone 4 | Consolidation | 20 | See **Milestone Project 4** in Section 5 | Milestone 4 shipped & on GitHub |

### Phase 10 — AI-Assisted Engineering Deep Dive (Weeks 77–84)

| Wk | Topic | Subtopics | Hrs | Practice Tasks | Deliverable |
|---|---|---|---|---|---|
| 77 | Prompt engineering for devs | Context management, giving AI the right files/scope, iterative prompting, prompt templates for common tasks | 25 | Build a personal library of 10 reusable prompts (e.g., "generate pytest cases for this function", "explain this stack trace") | `ai-prompts.md` library |
| 78 | AI-powered IDEs mastery | Cursor/Windsurf codebase-aware chat, multi-file edit mode, `.cursorrules`/agent config files | 30 | Use Cursor to implement a medium feature across 4+ files in one guided session; review every change | Feature shipped via AI-IDE, with a diff review note |
| 79 | Autonomous coding agents | Aider or Claude Code: multi-file refactors, agent planning, giving agents test suites as a safety net | 30 | Have an agent perform a non-trivial refactor (e.g., extract a service layer) on the blog API with your test suite as the guardrail | Refactor completed by agent, verified green by your tests |
| 80 | Legacy code comprehension | Using AI to summarize unfamiliar codebases, generate architecture diagrams from code, find dead code | 30 | Pick a mid-size open-source repo you've never seen; use AI to produce an architecture summary; verify 3 claims manually against the actual code | Architecture summary + verification notes |
| 81 | AI-assisted debugging | Feeding stack traces effectively, bisecting with AI help, asking "what would falsify this hypothesis" | 25 | Deliberately break something subtly (e.g., an off-by-one or race condition); debug it using AI as a collaborator, documenting the process | Debugging log (bug → AI hypotheses → what was actually wrong) |
| 82 | AI code review workflows | Setting up AI review in CI (PR-time review bots), what to always double-check | 30 | Add an AI review step to your CI pipeline; review 5 of your own past PRs with it and log what it caught that you missed | AI-reviewed CI pipeline + findings log |
| 83 | Limits of AI | Hallucination patterns in code (fake APIs, wrong library versions), security risks of pasting AI-generated code unreviewed, licensing concerns | 25 | Find (deliberately, in a sandbox) 3 real examples of AI hallucinating an API that doesn't exist; document how you'd have caught it | `ai-failure-modes.md` |
| 84 | Buffer + verified AI feature | Add one meaningful feature almost entirely via AI agent, with full human verification | 20 | Ship it, but write a paragraph on exactly what you personally verified and how | Feature + verification statement (great interview story) |

### Phase 11 — Capstone Project (Weeks 85–98)

| Wk | Topic | Practice Tasks / Deliverable |
|---|---|---|
| 85 | Planning | Choose capstone idea (see Milestone 5/6 in Section 5); write full requirements + design doc |
| 86 | Architecture & schema | Finalize DB schema, ER diagram, service architecture diagram |
| 87 | Core CRUD + auth | Implement base resources and JWT/RBAC auth |
| 88 | Feature 1 | Implement first major business-logic feature end-to-end (with tests) |
| 89 | Feature 2 | Implement second major business-logic feature end-to-end (with tests) |
| 90 | Async/background features | Add background jobs relevant to the domain (e.g., notifications, report generation) |
| 91 | Caching & performance pass | Add caching where it matters; load-test and tune |
| 92 | Testing pass | Reach your target coverage; add missing integration tests |
| 93 | Dockerize + CI | Full Docker Compose setup + CI pipeline (lint/test/build) |
| 94 | Deploy + observability | Deploy to production host; wire up logging, error tracking, health checks |
| 95 | Security review | Run through OWASP checklist; fix findings |
| 96 | Documentation | OpenAPI docs polished, architecture diagram, ADRs (architecture decision records) for key choices |
| 97 | Polish & storytelling | Record a 3–5 min demo video; write a technical blog post explaining the system and your AI-assisted workflow |
| 98 | Buffer + final review | Full end-to-end walkthrough as if presenting to an interviewer |

### Phase 12 — Portfolio Polish, Resume & Job Search (Weeks 99–104+)

| Wk | Topic | Practice Tasks / Deliverable |
|---|---|---|
| 99 | Resume + LinkedIn | Draft resume (see Section 7); optimize LinkedIn headline/About/experience sections |
| 100 | Portfolio & GitHub profile | Build a simple portfolio site; pin best repos; clean up GitHub profile README |
| 101 | Coding interview ramp-up | Daily timed DSA practice resumes (45–60 min/day within the 5-hour block) alongside light job-search admin |
| 102 | Backend/system design interview prep | Practice explaining your capstone and Milestone projects out loud; system-design mock questions |
| 103 | Mock interviews | 2–3 AI-run mock interviews + at least 1 human mock interview (peer, mentor, or paid service) |
| 104+ | Applications & continued prep | Begin applying in volume (target in Section 7); interview prep and applications continue in parallel until an offer lands |


---

## 3. Detailed Topic Breakdown

Each topic below follows the same structure: **What / Why it matters / Prerequisites / Time / Objectives / Resources / Easy–Medium–Hard tasks / Acceptance criteria.**

### 3.1 Python Fundamentals
- **What:** Syntax, types, control flow, functions, collections, file I/O, error handling.
- **Why:** Every later topic is written in Python. Shaky fundamentals compound into painful debugging later.
- **Prerequisites:** None.
- **Time:** ~8 weeks (Phase 1).
- **Objectives:** Write correct, readable Python without constant reference-lookups; handle errors deliberately, not accidentally.
- **Resources:** Official Python Tutorial; *Automate the Boring Stuff with Python* (free); CS50P (Harvard, free); Corey Schafer YouTube.
- **Easy:** FizzBuzz, temperature converter, palindrome checker.
- **Medium:** CLI expense tracker with JSON persistence; word-frequency analyzer on a real text file.
- **Hard:** A multi-command CLI toolkit (Section 2, Week 9) with modules, classes, and full error handling.
- **Acceptance criteria:** You can write a 100+ line script without looking up basic syntax; you use specific exceptions, not bare `except:`.

### 3.2 Advanced Python (OOP, Decorators, Generators, Async)
- **What:** Classes/inheritance/composition, comprehensions, generators/iterators, decorators, context managers, `async`/`await`.
- **Why:** Frameworks like FastAPI and libraries like SQLAlchemy are built entirely on these patterns; you can't read their source or debug them without this.
- **Prerequisites:** 3.1.
- **Time:** ~4 weeks (Phase 1 weeks 6–8, revisited in Phase 4 week 29).
- **Objectives:** Design small class hierarchies correctly; write a decorator from scratch; explain why `async` helps (or doesn't) for a given workload.
- **Resources:** Real Python OOP & decorators guides; *Fluent Python* (book, for reference); Python docs on `asyncio`.
- **Easy:** `Shape` class hierarchy with polymorphic `area()`.
- **Medium:** `@retry` and `@timer` decorators; a generator-based lazy file reader.
- **Hard:** Convert a sync data-pipeline script to async and benchmark the difference under concurrent load.
- **Acceptance criteria:** Can explain LEGB scoping, MRO (method resolution order), and the difference between concurrency and parallelism, unaided.

### 3.3 Data Structures & Algorithms
- **What:** Big-O analysis, arrays/strings, linked lists, stacks/queues, hash maps, trees/graphs, sorting/searching, recursion.
- **Why:** Still the dominant format for first-round technical screens at most companies, and the underlying mental model helps you reason about performance in real systems (e.g., why an index turns an O(n) scan into O(log n)).
- **Prerequisites:** 3.1.
- **Time:** ~8 weeks initial (Phase 2), plus ongoing 45–60 min/day maintenance from Phase 9 onward.
- **Objectives:** Solve Easy problems in <20 min and most Mediums in <35 min without hints; explain time/space complexity of your own solutions.
- **Resources:** NeetCode 150 (free video explanations); *Grokking Algorithms* (book); LeetCode Easy/Medium filtered by pattern.
- **Easy:** Two-sum, valid parentheses, reverse linked list.
- **Medium:** Longest substring without repeating characters, binary tree level-order traversal, merge intervals.
- **Hard:** LRU cache implementation from scratch (a favorite because it mirrors real caching work); course-schedule (topological sort).
- **Acceptance criteria:** 100+ problems solved and logged with pattern tags; can whiteboard a Medium problem out loud, narrating your thinking.

### 3.4 Command Line & Linux
- **What:** Filesystem navigation, permissions, piping/redirection, text-processing tools (`grep`/`sed`/`awk`), process management, `ssh`.
- **Why:** Deployment, debugging production issues, and most backend tooling happens in a terminal on a Linux box.
- **Prerequisites:** None.
- **Time:** ~1 week dedicated (Phase 2 week 11), used continuously after.
- **Objectives:** Comfortable navigating and diagnosing a remote Linux server over SSH without a GUI.
- **Resources:** *The Linux Command Line* (free book, William Shotts); OverTheWire "Bandit" wargame (free, gamified CLI practice).
- **Easy:** Chain `grep`/`wc` to count error lines in a log file.
- **Medium:** Write a bash script that rotates and compresses log files older than 7 days.
- **Hard:** Diagnose a "server out of memory" scenario on a VM using `top`, `ps`, `df`, and logs alone.
- **Acceptance criteria:** Can SSH into a fresh Linux VM and get a Python app running from zero, no GUI, no hand-holding.

### 3.5 Git & GitHub
- **What:** Commits, branches, merging/rebasing, PRs, conflict resolution, `.gitignore`, conventional commits.
- **Why:** The default collaboration and version-control tool at virtually every backend job; interviewers assume fluency.
- **Prerequisites:** CLI basics.
- **Time:** ~2 weeks dedicated, used every single day after.
- **Objectives:** Never lose work, never force-push over a teammate, resolve conflicts calmly.
- **Resources:** *Pro Git* (free official book); GitHub Skills interactive courses.
- **Easy:** Fix a merge conflict you create deliberately in a solo repo.
- **Medium:** Rebase a feature branch onto an updated `main` cleanly.
- **Hard:** Recover a "lost" commit using `git reflog` after a bad reset.
- **Acceptance criteria:** Can explain merge vs. rebase and when to use each; has ≥1 real open-source PR submitted.

### 3.6 Networking & HTTP
- **What:** TCP/IP basics, DNS, the HTTP request/response cycle, methods, status codes, headers, cookies, TLS at a conceptual level.
- **Why:** REST APIs *are* HTTP; you cannot debug a 403 vs a 500 vs a CORS error without this.
- **Prerequisites:** None.
- **Time:** ~1 week dedicated (Phase 3 week 18).
- **Objectives:** Correctly choose status codes and methods for a new endpoint without guessing; read raw HTTP headers.
- **Resources:** MDN HTTP docs; *HTTP: The Definitive Guide* (reference chapters as needed).
- **Easy:** Use `curl -v` to inspect headers on 5 different real websites.
- **Medium:** Build a raw TCP echo server with Python's `socket` module to see what HTTP is built on top of.
- **Hard:** Diagnose and fix a real CORS misconfiguration between a frontend and your API.
- **Acceptance criteria:** Can explain, from memory, when to use 400 vs 401 vs 403 vs 404 vs 422.

### 3.7 SQL & Relational Databases
- **What:** DDL/DML, joins, aggregation, subqueries, normalization, indexes, transactions/ACID, `EXPLAIN ANALYZE`.
- **Why:** Nearly every backend job touches a relational database daily; SQL is also a very common interview topic.
- **Prerequisites:** None (parallel-track friendly with Python).
- **Time:** ~6 weeks dedicated (Phase 3), deepened in Phase 5.
- **Objectives:** Design a normalized schema from a word problem; write non-trivial joins/aggregations without an ORM; explain what an index actually does.
- **Resources:** SQLBolt (free interactive); Mode Analytics SQL tutorial (free); PostgreSQL official docs.
- **Easy:** Top-5 customers by order total (`GROUP BY` + `ORDER BY`).
- **Medium:** Find users who have never placed an order (`LEFT JOIN ... WHERE NULL` or `NOT EXISTS`).
- **Hard:** Diagnose and fix a slow query using `EXPLAIN ANALYZE`, adding the correct index.
- **Acceptance criteria:** Can design a 5+ table normalized schema for a new domain from scratch in under an hour.

### 3.8 ORMs (SQLAlchemy focus, Django ORM as secondary exposure)
- **What:** Models, sessions/engines, relationships, migrations (Alembic), query building, eager vs lazy loading.
- **Why:** Production code rarely hand-writes raw SQL everywhere; you need to know the ORM *and* know when to drop to raw SQL for performance.
- **Prerequisites:** 3.7, 3.2.
- **Time:** ~4 weeks dedicated (Phase 5).
- **Objectives:** Model complex relationships correctly; recognize and fix an N+1 query problem.
- **Resources:** SQLAlchemy official tutorial (2.0-style); Alembic docs; Django ORM docs (for the survey week).
- **Easy:** Define a `User`/`Post` one-to-many relationship.
- **Medium:** Add a many-to-many `Post`/`Tag` relationship with a proper association table.
- **Hard:** Find and fix a real N+1 query bug you introduced yourself, verifying the fix with query-count assertions in a test.
- **Acceptance criteria:** Can explain lazy vs. eager loading and pick the right one for a given endpoint.

### 3.9 FastAPI (primary framework)
- **What:** Routing, Pydantic validation, dependency injection, routers, async endpoints, background tasks, OpenAPI docs.
- **Why:** One of the most in-demand modern Python frameworks, async-native, and produces self-documenting APIs — strong fit for a portfolio built in 2026.
- **Prerequisites:** 3.1–3.8.
- **Time:** ~9 weeks dedicated (Phase 4), used through the rest of the roadmap.
- **Objectives:** Build a multi-resource, validated, documented, layered API independently.
- **Resources:** Official FastAPI docs (excellent and free); FastAPI tutorial by Sebastián Ramírez (its creator).
- **Easy:** A single-resource CRUD API with Pydantic validation.
- **Medium:** Multi-resource API with routers, dependency-injected DB sessions, and pagination.
- **Hard:** A layered (router/service/repository) API with async DB access, file uploads, and background tasks.
- **Acceptance criteria:** Can add a new fully-validated, documented, tested endpoint to an existing FastAPI app in under 30 minutes.

### 3.10 Django (secondary exposure)
- **What:** MVT pattern, ORM, admin panel, Django REST Framework basics.
- **Why:** Still extremely common in job postings; you should be conversant even if FastAPI is your primary tool.
- **Prerequisites:** 3.1–3.8.
- **Time:** ~2 weeks (Phase 4 weeks 30–31).
- **Objectives:** Be able to read and modestly contribute to an existing Django codebase in an interview or take-home context.
- **Resources:** Official Django tutorial ("polls app"); Django REST Framework quickstart.
- **Easy:** The official Django polls tutorial, completed fully.
- **Medium:** Add a DRF API on top of the polls app.
- **Hard:** Recreate one feature from your FastAPI bookshelf API in Django, and write down the concrete tradeoffs you noticed.
- **Acceptance criteria:** Can explain, correctly, at least 4 real differences between Django and FastAPI beyond "one is sync and one is async."

### 3.11 Authentication & Authorization
- **What:** Password hashing, sessions vs. JWTs, OAuth2, refresh tokens, role-based access control (RBAC).
- **Why:** Almost every real API needs this, and it's a classic area for both security bugs and interview questions.
- **Prerequisites:** 3.9.
- **Time:** ~3 weeks (Phase 6 weeks 43–45).
- **Objectives:** Implement secure auth from memory, without copy-pasting a tutorial blindly.
- **Resources:** OWASP Authentication Cheat Sheet; FastAPI's official security docs; `python-jose`/`PyJWT` docs.
- **Easy:** Hash and verify a password with `bcrypt`.
- **Medium:** Full JWT login/refresh flow.
- **Hard:** RBAC with route-level and object-level permission checks (e.g., "can only edit your own posts").
- **Acceptance criteria:** Can explain why you never store plaintext passwords and why JWTs shouldn't be treated as infinitely trustworthy (expiry, revocation strategy).

### 3.12 Security
- **What:** OWASP Top 10, input validation, SQL injection, CORS, rate limiting, secrets management.
- **Why:** Security bugs are the most expensive kind of bug; even junior devs are expected to avoid the basics.
- **Prerequisites:** 3.11.
- **Time:** ~2 weeks dedicated (Phase 6 week 46, Phase 9 week 75), an ongoing mindset after.
- **Objectives:** Recognize and prevent the OWASP Top 10 classes of vulnerability in code you write.
- **Resources:** OWASP Top 10 (official, free); OWASP Cheat Sheet Series.
- **Easy:** Identify which of your own endpoints are missing input validation.
- **Medium:** Deliberately introduce and then patch a SQL injection vulnerability using raw string formatting vs. parameterized queries.
- **Hard:** Run a security audit against your Milestone 3 project and produce a written findings report with severity ratings.
- **Acceptance criteria:** Can name and explain at least 6 of the OWASP Top 10 unaided, with a real example of each.

### 3.13 Testing (Unit, Integration, TDD)
- **What:** `pytest`, fixtures, mocking, test databases, `TestClient`, coverage, red-green-refactor TDD.
- **Why:** Untested code is not production code; testing ability is now routinely checked in interviews and take-homes.
- **Prerequisites:** 3.9.
- **Time:** ~3 weeks dedicated (Phase 6 weeks 47–49), applied continuously after.
- **Objectives:** Write tests that actually catch regressions, not tests that just pad a coverage number.
- **Resources:** Official `pytest` docs; *Test-Driven Development with Python* (free online, Percival & Gregory — Django-flavored but excellent for the TDD mindset); FastAPI testing docs.
- **Easy:** Unit test for a single pure function with 3 edge cases.
- **Medium:** Integration test suite for a full CRUD resource, using a real test database.
- **Hard:** Build one feature strictly test-first (TDD), with tests written and failing before any implementation code exists.
- **Acceptance criteria:** A red test genuinely goes green only after correct implementation — you've verified this by deliberately breaking the implementation once and watching the test catch it.

### 3.14 Docker
- **What:** Images, containers, `Dockerfile`, multi-stage builds, Docker Compose, volumes, networking.
- **Why:** The standard way to package and ship backend services; expected knowledge for almost any 2026 backend role.
- **Prerequisites:** 3.4.
- **Time:** ~2 weeks dedicated (Phase 7 weeks 51–52).
- **Objectives:** Containerize a multi-service app so a stranger can run it with one command.
- **Resources:** Official Docker "Get Started" docs; Docker Compose docs.
- **Easy:** Dockerize a single-file Python script.
- **Medium:** Multi-stage `Dockerfile` for the FastAPI app, minimizing final image size.
- **Hard:** `docker-compose.yml` running app + Postgres + Redis with proper healthchecks and volume persistence.
- **Acceptance criteria:** `docker compose up` on a clean machine (or a friend's laptop) brings the whole stack up with zero manual steps.

### 3.15 CI/CD
- **What:** GitHub Actions, automated lint/test/build pipelines, automated deployment on merge.
- **Why:** Manual deployment doesn't scale and is a common interview/take-home differentiator.
- **Prerequisites:** 3.13, 3.14.
- **Time:** ~2 weeks dedicated (Phase 7 weeks 54–55).
- **Objectives:** A push to `main` results in tested, deployed code with no manual steps.
- **Resources:** GitHub Actions official docs; "Awesome Actions" curated list.
- **Easy:** A workflow that runs `pytest` on every push.
- **Medium:** Add linting (`ruff`/`flake8`) and type-checking (`mypy`) as required CI checks.
- **Hard:** Full pipeline: lint → test → build Docker image → deploy to your cloud host on merge to `main`.
- **Acceptance criteria:** A genuinely broken PR (failing test) is blocked from merging by CI, verified by trying it once.

### 3.16 Cloud Deployment
- **What:** Deploying to Render/Fly.io/Railway (fast path) and enough raw AWS/GCP to be conversant (EC2/Compute Engine, S3, IAM).
- **Why:** "It works on my machine" isn't a job-ready skill; you must be able to ship something real people can hit.
- **Prerequisites:** 3.14.
- **Time:** ~2 weeks dedicated (Phase 7 weeks 55–56).
- **Objectives:** Deploy and operate a live service, including handling secrets and environment config correctly.
- **Resources:** Render/Fly.io official docs; AWS Free Tier docs; "AWS in Plain English" free primers.
- **Easy:** Deploy a static "hello world" API to a free-tier PaaS.
- **Medium:** Deploy the full Dockerized FastAPI + Postgres app with environment secrets managed properly.
- **Hard:** Manually stand up the same app on a raw AWS/GCP VM to understand what the PaaS was automating.
- **Acceptance criteria:** You have a live public URL you can hand to anyone, right now, that works.

### 3.17 Caching (Redis)
- **What:** Cache-aside/write-through patterns, TTLs, invalidation strategies, Redis data structures beyond simple key-value.
- **Why:** The cheapest, highest-leverage performance fix in most systems; a very common system-design interview topic.
- **Prerequisites:** 3.7, 3.9.
- **Time:** ~1 week dedicated (Phase 8 week 59).
- **Objectives:** Correctly identify what's cacheable and implement invalidation without introducing stale-data bugs.
- **Resources:** Redis official docs; "Caching Best Practices" (AWS/Redis blog primers).
- **Easy:** Cache a single expensive read-only endpoint with a TTL.
- **Medium:** Implement cache invalidation on write (update/delete triggers cache clear).
- **Hard:** Handle a cache-stampede scenario (many requests miss cache simultaneously) with a lock or early-expiry strategy.
- **Acceptance criteria:** Can explain, with a real example from your own project, "cache invalidation is one of the two hard problems in computer science."

### 3.18 Background Jobs
- **What:** Task queues (Celery/RQ), workers, retries with backoff, scheduled/periodic tasks, idempotency.
- **Why:** Anything slow (emails, image processing, reports) must not block the request/response cycle.
- **Prerequisites:** 3.9, 3.17.
- **Time:** ~2 weeks dedicated (Phase 8 weeks 60–61).
- **Objectives:** Move a slow operation out of the request path correctly, including failure handling.
- **Resources:** Celery official docs; RQ official docs (simpler, good starting point).
- **Easy:** Move "send confirmation email" to a background task.
- **Medium:** Add retry-with-backoff to a background task that calls a flaky external API.
- **Hard:** A scheduled nightly job that is idempotent (safe to accidentally run twice).
- **Acceptance criteria:** Can explain why a background job must be idempotent and show a job you wrote that actually is.

### 3.19 Logging, Monitoring & Observability
- **What:** Structured logging, log levels, correlation IDs, metrics (Prometheus concepts), tracing concepts, error tracking (Sentry).
- **Why:** "How would you know if this broke in production?" is a real interview question, and a real production requirement.
- **Prerequisites:** 3.14, 3.16.
- **Time:** ~2 weeks dedicated (Phase 8 weeks 63–64).
- **Objectives:** Diagnose a production issue using logs/metrics/traces alone, without SSHing in to add print statements.
- **Resources:** Sentry docs (free tier); "12-Factor App" (official site, logs section); Prometheus getting-started docs.
- **Easy:** Replace all `print()` calls with structured logging.
- **Medium:** Add request correlation IDs that appear in every log line for a given request.
- **Hard:** Wire up Sentry, then deliberately trigger and diagnose an error using only the dashboard, not local reproduction.
- **Acceptance criteria:** Can find the root cause of a deliberately-planted bug using only logs/dashboards within 10 minutes.

### 3.20 System Design Fundamentals
- **What:** Scalability vocabulary, load balancing, CAP theorem, replication/sharding, message queues, microservices tradeoffs, API design at scale.
- **Why:** Standard part of interviews even for many junior roles now, and the conceptual backbone for every "why" decision in this roadmap.
- **Prerequisites:** Everything in Phases 1–8.
- **Time:** ~7 weeks dedicated (Phase 9), a lifelong skill after.
- **Objectives:** Produce a structured design document for a medium-complexity system under time pressure.
- **Resources:** *Designing Data-Intensive Applications* (book — the standard reference); "System Design Primer" (free GitHub repo); ByteByteGo free content.
- **Easy:** Design a URL shortener (classic starter problem).
- **Medium:** Design a rate limiter as a reusable service.
- **Hard:** Design a Twitter-like news feed with fan-out considerations.
- **Acceptance criteria:** Can produce a requirements → high-level design → deep-dive → tradeoffs document, unaided, in 45 minutes.

### 3.21 AI-Assisted Software Engineering & AI Agents
- **What:** Prompt engineering for code, AI-powered IDEs (Cursor/Windsurf), autonomous coding agents (Aider, Claude Code, SWE-agent-style tools), AI code review, legacy-code comprehension with AI, AI-assisted debugging, and — critically — the **limits** of AI and how to verify its output.
- **Why:** By 2026 this is a baseline professional skill, not a novelty; the differentiator is no longer "do you use AI" but "can you use it critically and catch what it gets wrong."
- **Prerequisites:** Solid fundamentals first (Phases 1–6) so you can actually judge AI output — this is deliberately sequenced *after* you can code independently.
- **Time:** ~8 weeks dedicated (Phase 10), used as a daily tool throughout the entire roadmap from Phase 2 onward.
- **Objectives:** Use AI to multiply your output on well-understood tasks while catching hallucinations, security issues, and subtly wrong logic on everything else.
- **Resources:** Anthropic's prompt engineering guide (docs.claude.com); Cursor/Windsurf official docs; Aider official docs; "Awesome AI Agents" curated lists (vet carefully — this space moves fast).
- **Easy:** Use AI to generate boilerplate (a new CRUD resource's skeleton) and manually verify every field/type.
- **Medium:** Use an AI agent to perform a multi-file refactor guarded by your existing test suite.
- **Hard:** Use AI to help debug a real, non-obvious bug (race condition, N+1 query, memory leak) — but arrive at the actual root cause through your own verification, not by trusting the first AI explanation.
- **Acceptance criteria:** You can point to at least 3 concrete instances where you caught an AI tool being wrong (a hallucinated API, an insecure default, an inefficient query) and describe exactly how you caught it — this is a genuinely strong interview answer.


---

## 4. Tasks, Challenges & AI Workflows

Section 3 already gives Easy/Medium/Hard tasks per topic. This section adds (4.1) a **quick-reference challenge bank** organized by the specific categories requested, for extra practice or spaced repetition, and (4.2) a **phase-by-phase AI workflow table** so AI usage is concrete and scheduled, not vague.

### 4.1 Cross-Cutting Challenge Bank

| Category | Easy | Medium | Hard |
|---|---|---|---|
| Python fundamentals | Reverse a string without slicing | Parse a CSV and compute per-column stats without pandas | Build a mini template engine (`{{var}}` substitution) from scratch |
| Advanced Python | Write a class with custom `__eq__`/`__hash__` | Build a plugin system using `__init_subclass__` | Implement your own simplified `functools.lru_cache` |
| Data structures & algorithms | Two-sum | Group anagrams | Design and implement an LRU cache with O(1) ops |
| CLI & Linux | List all `.py` files modified in the last 24h | Write a bash script that alerts if disk usage > 90% | Set up a passwordless SSH + basic firewall (`ufw`) on a VM |
| Git & GitHub | Undo an uncommitted change | Interactive rebase to squash 3 commits into 1 | Recover a commit after a bad `reset --hard` via `reflog` |
| HTTP, REST & API design | Curl a public API and print just the status code | Design REST endpoints for a "podcast app" from a spec | Add proper API versioning + deprecation headers to an existing API |
| Database queries & data modeling | Write a query for "orders placed in the last 7 days" | Design a schema for a multi-tenant SaaS app | Optimize a genuinely slow query using `EXPLAIN ANALYZE` and indexing |
| Auth, authz & security | Hash/verify a password | Implement JWT refresh-token rotation | Implement object-level permissions ("edit only your own resources") |
| Testing, debugging & error handling | Unit test a pure function with edge cases | Mock an external API call in a test | Reproduce and fix a flaky test (non-deterministic failure) |
| Deployment, caching & background jobs | Dockerize a single script | Add Redis caching with TTL + invalidation | Full CI/CD pipeline deploying on merge, with a background job worker included |

### 4.2 AI Workflows by Phase

| Phase | AI Tool(s) | Concrete Workflow Task |
|---|---|---|
| 1–2 (Foundations) | ChatGPT/Claude (chat only) | Ask AI to **explain, not write** — e.g., "explain what a generator is, then quiz me with 3 questions" — building understanding before leaning on generation. |
| 2 (Week 17) | Cursor or Windsurf | First supervised multi-file refactor: ask the AI-IDE to reorganize your CLI toolkit into modules, and manually review every changed line before accepting. |
| 3–4 | GitHub Copilot + Claude | Use Copilot for inline boilerplate (Pydantic models, route skeletons); use Claude/ChatGPT to **explain unfamiliar error messages** line-by-line rather than just pasting a fix. |
| 5 | Claude/ChatGPT | Prompt an LLM to write a complex SQL query (e.g., a 3-table join with aggregation) from a plain-English spec, then manually verify the output against `EXPLAIN ANALYZE` and by hand-checking results on sample data — never trust a generated query blind. |
| 6 | Claude/ChatGPT | **AI-assisted TDD:** describe a feature in plain English, ask the AI to brainstorm edge cases (not write the tests), then write the tests yourself first, then implement. |
| 7 | Claude/ChatGPT | Ask AI to draft a multi-stage `Dockerfile` and a GitHub Actions workflow from a description of your stack; verify every line — check base image versions, confirm no secrets are hardcoded, confirm the build actually runs locally before trusting it. |
| 8 | Claude/ChatGPT | Paste a slow-query `EXPLAIN ANALYZE` output and ask AI to hypothesize causes; test each hypothesis yourself rather than applying the first suggested fix. |
| 9 | Claude/ChatGPT (as critique partner) | Write a system-design doc yourself first, *then* ask AI to poke holes in it ("what would break at 10x scale?") — using AI to stress-test your thinking, not generate the thinking. |
| 10 (dedicated) | Aider / Claude Code | Full agentic workflow: give the agent a test suite as a guardrail, assign it a real refactor (e.g., "extract a repository layer"), and review the resulting diff commit-by-commit. |
| 10 (dedicated) | Any AI-IDE | **Legacy code comprehension:** point the AI at an unfamiliar open-source repo, ask for an architecture summary, then manually verify 3 of its claims by reading the actual source — this catches AI overconfidence. |
| 10 (dedicated) | Any LLM | **Stack-trace debugging:** paste a real, full stack trace (not a summary) and ask the AI to walk through it frame-by-frame; independently verify its root-cause claim by reproducing the bug. |
| 11 (Capstone) | Aider/Claude Code + Copilot + Claude chat | Use agents for scaffolding and boilerplate-heavy work (CRUD, Docker, CI config); do core business logic and all security-sensitive code yourself, with AI only reviewing afterward. |
| 12 (Job search) | Claude/ChatGPT | Mock technical interviews: have the AI role-play an interviewer asking you to explain your capstone's architecture and defend design decisions under follow-up questions. |

> **A standing rule for the whole roadmap:** never merge AI-generated code you haven't read line-by-line and could not explain to an interviewer. If you can't explain *why* a line is there, treat that as a signal to slow down, not a reason to trust the AI more.


---

## 5. Milestone Projects

Five milestone projects are placed at key checkpoints. Each should be pushed to a **separate, clean GitHub repo** with its own README (problem, architecture, how to run, screenshots/GIF of it working).

### Milestone 1 — "Bookshelf API" (Week 25, ~Month 6)

- **Scenario:** A small bookstore needs an internal API to manage its book catalog — no customers yet, just staff-facing CRUD.
- **Technical requirements:** Flask or FastAPI; PostgreSQL persistence via raw SQL or `psycopg2` (ORM not required yet); input validation; consistent JSON error responses; Postman/curl collection for manual testing.
- **Database design hints:** Single `books` table (id, title, author, isbn, price, stock_quantity, created_at) is enough — resist the urge to over-model this early.
- **API endpoints:** `GET /books`, `GET /books/{id}`, `POST /books`, `PUT /books/{id}`, `DELETE /books/{id}`, `GET /books?author=&min_price=` (basic filtering).
- **Auth/testing/deployment:** No auth required yet. At least 5 manual test cases documented in the README (happy path + 2 error cases). Local-only deployment is acceptable (Docker optional bonus).
- **AI integration requirement:** Use an AI assistant to review your finished code for style/bugs (not to write it); document at least 2 concrete suggestions you accepted and 1 you rejected, with reasoning.
- **Stretch goals:** Add pagination; add a `/books/low-stock` endpoint; Dockerize it.
- **Evaluation rubric:** ☐ All endpoints work as documented ☐ No SQL injection vulnerabilities (parameterized queries only) ☐ README lets a stranger run it in <5 minutes ☐ Code is organized into more than one file.

### Milestone 2 — "Blog Platform API" (Week 42, ~Month 9–10)

- **Scenario:** A small media startup needs a backend for a multi-author blog: authors write posts, readers comment, posts have tags.
- **Technical requirements:** FastAPI + SQLAlchemy + Alembic migrations; layered architecture (router → service → repository); Pydantic schemas separate from DB models.
- **Database design hints:** `users`, `posts` (FK to users), `comments` (FK to posts and users), `tags`, `post_tags` (many-to-many join table). Add `created_at`/`updated_at` on everything.
- **API endpoints:** Full CRUD on posts and comments; `GET /posts?tag=&author_id=` filtering; `GET /posts/{id}/comments`; nested response option (post with embedded comment count).
- **Auth/testing/deployment:** No auth required *yet* (added in Milestone 3) but design models with a future `user_id` owner field in mind. Unit tests for the service layer (aim 60%+ coverage). Deployed to a free-tier cloud host with a public URL.
- **AI integration requirement:** Use an AI coding agent (Cursor/Aider) to generate the initial Alembic migration boilerplate for one table, then manually verify the generated migration against your actual model before applying it — document what you checked.
- **Stretch goals:** Full-text search on post titles/bodies; a `/posts/{id}/related` endpoint using tag overlap.
- **Evaluation rubric:** ☐ Schema is properly normalized (no repeated data) ☐ N+1 queries checked and avoided in list endpoints ☐ Migrations run cleanly from empty DB ☐ Deployed and reachable via public URL.

### Milestone 3 — "Secure Blog API" (Week 50, ~Month 11–12, your ~1-year mark)

- **Scenario:** The blog platform is going live to real users — it now needs real authentication, authorization, and a real safety net of tests before anyone can trust it.
- **Technical requirements:** JWT auth (access + refresh tokens); RBAC with at least 2 roles (`author`, `admin`); object-level permissions (authors can only edit their own posts, admins can edit anything); full `pytest` suite (unit + integration).
- **Database design hints:** Add `role` to `users`; add `owner_id` checks in the service layer, not just the DB.
- **API endpoints:** `POST /auth/register`, `POST /auth/login`, `POST /auth/refresh`, plus all Milestone 2 endpoints now behind auth where appropriate (reading is public, writing requires auth and ownership).
- **Auth/testing/deployment:** This *is* the auth milestone — see Technical requirements. Target 75%+ test coverage on services/auth logic. CI pipeline (GitHub Actions) running the full test suite on every push, required to pass before merge.
- **AI integration requirement:** Practice AI-assisted TDD for one new feature ("post likes" or "post bookmarking"): ask an AI assistant only to brainstorm edge cases for the feature, write the tests yourself from that list, then implement. Include the AI-generated edge-case list in your README as evidence of the process.
- **Stretch goals:** Add "Login with Google" (OAuth2); add account lockout after repeated failed logins.
- **Evaluation rubric:** ☐ Passwords are hashed, never logged, never returned in API responses ☐ A user cannot edit another user's post (verified by a test that tries and expects a 403) ☐ CI blocks a genuinely broken PR (test this once for real) ☐ No secrets committed to the repo, ever (check git history too).

### Milestone 4 — "Job Board API with Real-Time Notifications" (Week 76, ~Month 17–18)

- **Scenario:** A job-board startup needs a backend where companies post jobs, candidates apply, and both sides get notified of relevant events (new application, application status change) without polling.
- **Technical requirements:** FastAPI core API + a separate small notification service communicating over an event/message layer (Redis Pub/Sub is sufficient — full Kafka/RabbitMQ is a stretch goal, not required); Redis caching on hot read endpoints (e.g., job listings); Celery/RQ background jobs for anything slow (sending emails, generating a "new matching jobs" digest); structured logging + Sentry error tracking.
- **Database design hints:** `companies`, `jobs` (FK company), `candidates`, `applications` (FK job + candidate, with a `status` enum: applied/reviewed/rejected/hired), `notifications` (FK user, type, payload, read_at).
- **API endpoints:** Full CRUD on jobs; `POST /jobs/{id}/apply`; `PATCH /applications/{id}/status` (triggers a notification event); `GET /notifications` (paginated, filterable by unread); `GET /jobs?search=&location=&remote=`.
- **Auth/testing/deployment:** JWT auth with `company` and `candidate` roles; integration tests covering the full "apply → status change → notification created" flow; Dockerized multi-service setup (`docker-compose.yml`: API, notification service, Postgres, Redis); deployed with a working CI/CD pipeline (auto-deploy on merge).
- **AI integration requirement:** Use an autonomous coding agent (Aider or Claude Code) to implement the notification-service skeleton across multiple files in one guided session, with your test suite as the safety net; review and note any part of the agent's output you rejected and why.
- **Stretch goals:** Rate-limit the `/apply` endpoint per candidate; add a `/jobs/{id}/similar` recommendation endpoint using simple tag/skill overlap; swap Redis Pub/Sub for a real message broker (RabbitMQ/Kafka) as a learning exercise.
- **Evaluation rubric:** ☐ An application status change reliably produces a notification (tested, not just eyeballed) ☐ Hot endpoints show a measurable caching improvement (numbers in README) ☐ A background job failure doesn't silently vanish (retries + logging visible) ☐ Whole stack comes up with `docker compose up`.

### Milestone 5 — Capstone Project (Weeks 85–98, ~Month 19–22)

- **Scenario:** Your capstone should be the single project you'll spend the most interview time discussing — pick something with enough real-world texture to generate good design conversations. Recommended default (swap for a domain you personally care about — genuine interest produces better polish): **a multi-tenant SaaS "Project & Task Management" API** (think a small Trello/Asana backend) — chosen because it naturally exercises multi-tenancy, permissions, real-time-ish updates, and reporting, all attractive interview topics.
- **Technical requirements:** Everything from Phases 1–10 integrated: FastAPI, SQLAlchemy + Alembic, JWT + RBAC + multi-tenant data isolation, Redis caching, Celery/RQ background jobs, Docker Compose, GitHub Actions CI/CD, deployed to a real cloud host, structured logging + Sentry + basic metrics endpoint, OpenAPI docs polished, an architecture diagram, and 2–3 written **ADRs** (Architecture Decision Records) explaining key tradeoffs you made.
- **Database design hints:** `organizations` (tenant boundary), `users` (FK organization, role), `projects` (FK organization), `tasks` (FK project, assignee, status, due_date), `comments` (FK task), `activity_log` (audit trail). Every query must be scoped to the requesting user's organization — this is your multi-tenancy discipline test.
- **API endpoints:** Full CRUD on organizations/projects/tasks/comments; `GET /projects/{id}/tasks?status=&assignee=`; `PATCH /tasks/{id}/status`; `GET /projects/{id}/activity`; `GET /reports/workload` (aggregation — tasks per assignee, useful for a "can you write real reporting queries" interview story).
- **Auth/testing/deployment:** Full JWT + RBAC (owner/admin/member roles) with strict tenant isolation (a test that verifies Organization A can *never* see Organization B's data is mandatory); 80%+ test coverage target on business logic; full CI/CD; live deployment with health checks and monitoring dashboards you can screen-share in an interview.
- **AI integration requirement:** Document your AI usage explicitly in the README under an "AI-Assisted Development" section: which parts were AI-scaffolded (e.g., CRUD boilerplate, Docker/CI config), which parts you wrote and verified yourself (auth, tenant-isolation logic, core business rules), and at least one real example where you caught and corrected an AI mistake during this project.
- **Stretch goals:** WebSocket support for live task updates; a simple analytics dashboard (even a basic HTML page hitting your `/reports` endpoints); rate limiting per organization tier (free vs. paid).
- **Evaluation rubric:** ☐ Tenant isolation is provably correct (a failing-then-passing test exists for it) ☐ You can explain every architectural decision out loud in under 2 minutes each ☐ A stranger can clone, `docker compose up`, and be running the full stack in under 10 minutes ☐ Live demo URL works when you send it cold, without you needing to "warm it up" first ☐ README reads like a real project, not a tutorial ☐ You could defend this project as your best work in a final-round interview.


---

## 6. Core Topic Coverage Map

Quick reference confirming every required area is covered and where.

| Required Area | Primary Coverage |
|---|---|
| Python fundamentals & advanced Python | Phase 1 (Weeks 2–9), Phase 2, §3.1–3.2 |
| Data structures, algorithms & system design fundamentals | Phase 2 (Weeks 12–16), Phase 9, §3.3, §3.20 |
| Git, GitHub, Linux, Networking/HTTP | Phase 2 (Weeks 10–11), Phase 3 (Week 18), §3.4–3.6 |
| Relational databases, SQL & ORMs | Phase 3 (Weeks 20–24), Phase 5, §3.7–3.8 |
| FastAPI (primary) & Django (secondary) | Phase 4, §3.9–3.10 |
| Auth, security, testing & performance/caching | Phase 6, Phase 8 (Week 59, 62), §3.11–3.13, §3.17 |
| Docker, CI/CD & cloud deployment | Phase 7, §3.14–3.16 |
| Logging, monitoring & observability | Phase 8 (Weeks 63–64), §3.19 |
| Prompt engineering for developers | Phase 10 (Week 77), §3.21, §4.2 |
| AI-powered IDEs (Cursor/Windsurf) | Phase 2 (Week 17), Phase 10 (Week 78), §4.2 |
| Autonomous coding agents (Aider/SWE-agent-style) | Phase 6+ (background), Phase 10 (Week 79), Milestones 2, 4, 5 |
| AI-driven code review & legacy code comprehension | Phase 10 (Weeks 80, 82), §4.2 |
| AI-assisted debugging | Phase 10 (Week 81), §4.2 |
| Limits of AI & verifying AI-generated code | Phase 10 (Week 83), standing rule in §4.2 |
| Portfolio building, resume, job search, interviews | Phase 12, Section 7 |

---

## 7. Job Preparation Plan

### 7.1 Portfolio & GitHub profile

- **Repo hygiene:** Every portfolio repo needs a real README: problem statement, tech stack, architecture diagram/image, setup instructions that actually work, and a screenshot or short GIF/video of it running. Delete or privatize abandoned tutorial-following repos before you start applying — a cluttered profile reads worse than a sparse, high-quality one.
- **Pin your best 4–6 repos**, ordered so the capstone is first.
- **Add a GitHub profile README** (the special `username/username` repo) summarizing your stack, what you're looking for, and linking your best projects and any blog posts.
- **Showcase AI-assisted work explicitly.** Don't hide AI usage — frame it as a skill. In your capstone README's "AI-Assisted Development" section (see Milestone 5), be specific and honest about what AI did vs. what you verified. This is increasingly what strong candidates are expected to demonstrate.
- **Write 2–3 short technical blog posts** (dev.to, personal site, or even a long-form GitHub README) explaining a real design decision from your capstone or Milestone 4 — e.g., "Why I chose Redis Pub/Sub over a full message broker for this project." These are excellent, low-effort interview conversation-starters and hiring-manager reading material.

### 7.2 Resume & LinkedIn

- **Resume structure:** Contact info → 2–3 line summary (stack + what you're looking for) → Projects (your strongest section — treat each milestone project like a mini case study: **what it does, your stack, one quantified detail** if possible, e.g., "reduced endpoint latency 60% via Redis caching") → Skills (grouped: Languages / Frameworks / Databases / DevOps / AI Tools) → Education/self-study → (Experience, if any, even non-tech — frame transferable skills).
- **Every bullet should follow "did X, using Y, resulting in Z"** where Z is a real, honest outcome — even "shipped a fully tested, deployed multi-tenant API" is a legitimate Z if that's the truth.
- **LinkedIn:** Headline states target role + core stack (e.g., "Backend Developer | Python, FastAPI, PostgreSQL"). About section: 3–4 sentences, human-written, not AI-boilerplate-sounding. Post about your projects as you finish milestones — recruiters and hiring managers do look.
- **Use AI to tailor, not fabricate:** feed your base resume + a specific job description to an AI assistant and ask it to suggest which existing bullets to emphasize/reorder for that role. Never let AI invent skills or experience you don't have — that's a fast way to fail a technical screen.

### 7.3 Job search strategy & application tracking

- **Start applying during Phase 12, not only after it.** Job searches take weeks-to-months; don't wait for "perfect" to begin.
- **Target mix:** roughly 60% straightforward job-board applications, 30% warm outreach (LinkedIn messages to engineers/hiring managers at target companies, referrals), 10% cold applications to dream companies. Warm outreach converts at a much higher rate than blind applications.
- **Tracking table** — keep this in a spreadsheet or simple Notion/Airtable board:

| Company | Role | Date Applied | Source | Status | Next Action | Notes |
|---|---|---|---|---|---|---|
| _(example)_ Acme Co | Backend Engineer I | 2027-06-01 | LinkedIn (referral) | Phone screen scheduled | Prep system design for their stack | Uses FastAPI too |

- **Volume target:** aim for a steady 5–10 quality applications/week during active search rather than a huge unfocused burst — quality of tailoring matters more than raw count.

### 7.4 Coding, backend, database & API interview preparation

- **Coding (DSA):** By Phase 12 you should have 100+ problems solved (from Phase 2/9 practice). Maintain with 45–60 min/day, focusing on patterns you're weaker in (use your own solved-problem log to find them).
- **Backend/API interview questions to be ready for:** "Design a REST API for X," "Walk me through what happens when a request hits your API," "How would you add rate limiting to this endpoint," "Explain the N+1 problem and how you'd fix it" — all of these map directly to things you've *actually built* in this roadmap, so answer with your own project examples, not generic textbook answers.
- **Database interview prep:** Practice writing SQL live (no autocomplete) — joins, aggregations, subqueries under time pressure. Be ready to explain indexing tradeoffs and normalization from your own schema decisions.
- **Take-home assignments:** Treat these exactly like a mini milestone project — tests, README, and a short note on your AI usage if you used any tools, since many companies now explicitly ask about this.

### 7.5 System design & behavioral interview preparation

- **System design:** Practice the same structured format from Phase 9 (requirements → high-level design → deep dive → tradeoffs) under a 30–45 minute clock. For junior roles, expect scaled-down versions (e.g., "design a URL shortener," not "design Twitter") — you've already practiced exactly these in Phase 9.
- **Behavioral prep:** Prepare 5–6 STAR-format stories (Situation, Task, Action, Result) drawn from your milestone projects — e.g., "tell me about a bug you struggled with," "tell me about a time you had to learn something fast," "tell me about a design decision you changed your mind on." Your Phase 10 AI-debugging log and Milestone READMEs are a ready-made source of real stories.

### 7.6 Leveraging AI agents for job search

- **Mock interviews:** Have an AI assistant role-play a technical interviewer asking about your capstone's architecture, with follow-up "why" questions — this is one of the single highest-leverage uses of AI in this whole roadmap.
- **Resume tailoring:** See 7.2 — use AI to reorder/emphasize truthful content per job description, never to fabricate.
- **Interview research:** Ask AI to summarize a target company's engineering blog posts or public tech stack (verify against the actual sources) so you walk in with informed, specific questions to ask them.
- **Always verify anything AI tells you about a specific company** (funding status, tech stack, culture) against a primary source before repeating it in an interview — AI can be confidently out of date or simply wrong here.


---

## 8. Progress Tracking

### 8.1 Phase completion checklist

| Phase | Weeks | Complete? |
|---|---|---|
| 0 — Orientation | 1 | ☐ |
| 1 — Python Foundations | 2–9 | ☐ |
| 2 — Advanced Python / DSA / Git / Linux | 10–17 | ☐ |
| 3 — HTTP, REST & SQL | 18–25 | ☐ |
| 4 — FastAPI Deep Dive | 26–34 | ☐ |
| 5 — Databases & ORMs | 35–42 | ☐ |
| 6 — Auth, Security & Testing | 43–50 | ☐ |
| 7 — Docker, CI/CD & Cloud | 51–58 | ☐ |
| 8 — Caching, Jobs & Observability | 59–66 | ☐ |
| 9 — System Design | 67–76 | ☐ |
| 10 — AI-Assisted Engineering | 77–84 | ☐ |
| 11 — Capstone | 85–98 | ☐ |
| 12 — Job Search | 99–104+ | ☐ (ongoing until hired) |

### 8.2 Milestone completion criteria

A milestone is only "done" — not just "code exists" — when **all** of the following are true:

☐ Every endpoint in the spec works and is manually tested at least once
☐ The evaluation rubric for that milestone (Section 5) is fully checked off
☐ Repo has a complete README a stranger could follow
☐ Tests exist and pass in a clean environment (not just "on my machine")
☐ You can explain every major design decision out loud, unaided, in under 2 minutes
☐ The AI Integration Requirement for that milestone is documented in the README

### 8.3 Weekly review template

Copy this into your `learning-log` repo every week:

```
## Week [N] — [Phase Name] — [Main Topic]

**Hours studied:** ___ / 30
**What I built:** 
**What clicked this week:**
**What I'm still fuzzy on:**
**Biggest blocker & how I resolved it (or didn't):**
**AI tool usage this week — what worked, what I had to override/correct:**
**Next week's focus:**
**Confidence check (1-5) on this week's main topic:** ___
```

### 8.4 Readiness self-assessment

Use this at three checkpoints: after Milestone 2 (~internship readiness), after Milestone 3 (~junior-role readiness), and after the Capstone (~full-time first-job readiness). Be honest — these are meant to catch gaps *before* an interviewer does.

**Internship / junior-adjacent readiness (target: ~Month 9–10)**
☐ Can build a CRUD REST API with a database from a spec, unaided, within a few hours
☐ Comfortable with Git branching/PR workflow
☐ Has solved 50+ DSA problems and can explain Big-O of your own solutions
☐ Has at least one deployed, publicly-accessible project

**Junior backend role readiness (target: ~Month 12–13)**
☐ Everything above, plus:
☐ Can implement auth (JWT/RBAC) from memory
☐ Has a real automated test suite with meaningful coverage on at least one project
☐ Can explain the N+1 query problem and demonstrate a fix
☐ Comfortable in a Linux terminal and with basic Docker
☐ Can describe, accurately, what AI tools you use and *don't* trust blindly

**First full-time backend role readiness (target: ~Month 22–24)**
☐ Everything above, plus:
☐ Has a capstone project demonstrating the full lifecycle: design → build → test → containerize → CI/CD → deploy → monitor
☐ Can produce a structured system-design document under time pressure
☐ Can talk through at least 3 real instances of catching an AI tool's mistake
☐ Has 5+ STAR-format behavioral stories ready
☐ Has done at least 2 mock interviews (AI or human) and incorporated the feedback
☐ Resume and LinkedIn are tailored, honest, and reviewed by at least one other person

### 8.5 Two-year progress table (fill in as you go)

| Month | Phase reached | Milestone shipped | Confidence (1–5) | Notes |
|---|---|---|---|---|
| 1 | | | | |
| 3 | | | | |
| 6 | | Milestone 1 | | |
| 9 | | Milestone 2 | | |
| 12 | | Milestone 3 | | |
| 15 | | | | |
| 18 | | Milestone 4 | | |
| 21 | | | | |
| 22–24 | | Capstone | | |

---

*This document is meant to be a living file — edit it as your actual pace diverges from the plan (it will). The structure matters more than the exact week numbers: fundamentals → framework → production skills → systems thinking → AI-native workflows → one great capstone → job search. Good luck.*
