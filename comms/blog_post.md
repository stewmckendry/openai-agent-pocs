**Title:** AI Agents: Beyond the Buzzword — What They Are, Why They Matter, and How to Build Them Responsibly

---

### Everyone’s Talking About Agents. But What Are They Really?

"AI agent." It’s everywhere now. In press releases, platform updates, product roadmaps, think tank papers. Everyone’s using the term.

But if you ask someone what an AI agent actually *does* — or how one might be useful in your organization, your team, or your daily life — the answers get fuzzy. Fast.

That’s why I built three AI agents of my own.

I wanted to *make it real*.

Not just to tinker with the latest SDK. But to show what agents can do for good. How they actually work. What it takes to build them. And why they matter — not only for technologists, but for public sector leaders, frontline workers, parents, and anyone thinking about the future.

This post walks through what I learned building three Proof-of-Concept AI agents using OpenAI's new `openai-agents` SDK. These are:

* A **Run Coach Agent** to create a personalized training plan from your fitness data.
* A **Trip Planner Agent** to build a 2-week family NHL road trip from a one-line idea.
* A **User Story Agent** to turn a vague feature request into a fully specified development story.

Each one is grounded in a real use case. Each one teaches something about what agents are, how they work, and where the future is going. I’ll also reflect on what this means for organizations, workers, and parents alike.

---

### From Custom GPTs to AI Agent Teams: What’s Evolving?

In earlier CoachingTheMachine posts, I shared projects like:

* **ConcussionGPT**, a custom assistant for sports safety;
* **GovDoc Copilot**, a copilot for writing public sector submissions;
* **MyHealth AI Assistant**, a conversational tool to explore your own health data.

Each of those tools was a *conversational interface* to a single LLM, perhaps enhanced with retrieval or external tools.

This next wave is different.

With the [OpenAI Agents SDK](https://github.com/openai/openai-agents-python), we can now create **teams of agents**, each with their own role, memory, tools, and output. They don’t just respond — they collaborate. They hand off work. They analyze, plan, revise.

They act more like humans.

That shift matters. And the best way to understand it is to see it in action.

---

### Three Real Agent Teams in Action

#### 🏅 Run Coach Agent: Train Smarter With Your Data

Imagine this: you’ve been logging runs with your Garmin, and now you want to train for a sub-20 minute 5K in two months. You type:

> "Run a 4:00 per km pace 5K in 2 months."

Behind the scenes, the agent team kicks in:

1. **Goal Agent** parses your race target: distance, pace, and date.
2. **Collect Agent** loads recent workouts from your `Activities.csv`.
3. **Analyze Agent** identifies your training strengths and gaps.
4. **Plan Agent** creates a week-by-week schedule tailored to your goal.
5. **Check Agent** reviews the plan for safety, realism, and completeness.

The result? A full 8-week training plan with long runs, speed work, hill repeats, and race taper guidance. All saved as Markdown, with a workflow diagram to show exactly how the plan was built.

Why it matters:

* Makes coaching logic accessible to anyone.
* Shows how agents can interpret personal data, reason across roles, and produce helpful, human-friendly outputs.
* Designed with responsibility: guards against unrealistic inputs and prioritizes safe planning.

#### ✈️ Trip Planner Agent: From Dream to Itinerary

Prompt:

> "I want to take my son on an NHL road trip next season."

Sounds fun. But vague. Where? When? What games? What logistics?

Here’s how the agent team handled it:

1. **Topic Agent** extracted research goals: season start date, best cities, transport, family-friendly hotels, special NHL events.
2. **Research Agent** searched the web for each topic and summarized the findings.
3. **Planner Agent** wrote a day-by-day itinerary: Chicago to Toronto to Boston to Miami to Tampa to New York to Philly.

Each segment had:

* Travel recommendations
* Family-friendly hotels near arenas
* Games to attend
* Side activities like museums and markets

Why it matters:

* Turns vague intentions into structured, actionable plans.
* Shows agents collaborating with real-time search and summarization.
* Offers a glimpse into what agent-powered travel assistants could be.

#### 🛠️ User Story Agent: From Idea to Implementation

Prompt:

> "Search for dog walkers in my area."

The result?

A **ready-to-develop user story**, including:

* UX spec with personas and journeys
* Functional and technical specs
* Acceptance criteria
* Impact analysis
* Effort estimate

How?
The agent team handled the entire flow:

1. **UX Agent** outlined personas and user flows.
2. **Functional Agent** defined features: search, filters, profiles, booking.
3. **Technical Agent** translated features into APIs, DB tables, components.
4. **Acceptance Agent** wrote Gherkin-style criteria.
5. **Impact Agent** assessed code and doc changes.
6. **Estimation Agent** assigned story points.
7. **Writer Agent** compiled the full spec.
8. **Verifier Agent** checked it met the Definition of Ready.

Why it matters:

* Shows how agents can simulate team-based design and planning work.
* Greatly accelerates requirements generation for delivery teams.
* Produces structured, reviewable artifacts you can trace.

---

### How It Works (And Why That Matters)

These agents weren’t coded line-by-line. They were scaffolded using:

* **Codex Agents**: I typed what I wanted; the agents scaffolded code for me.
* **MCP (Model Context Protocol)**: a reusable file system that agents can access safely. Think of it as a shared drive *the AI understands*.
* **Model switching**: While this uses OpenAI’s SDK, I can swap in Gemini, Claude, or others depending on task, preference, or platform.

This isn’t about one model. It’s about a *pattern* for working with AI.

---

### Reflections: What This Means for You

#### 💼 For Organizations

* You don’t need to wait for an "AI platform" to get started.
* What you do need:

  * Tools and infra to run agentic workflows
  * **A sandbox** where people can explore safely
  * Light governance: security, traceability, and human-in-the-loop design
* The real magic? Empower your people to iterate on *real use cases*. That’s where the impact is.

#### 🤖 For Individuals (Worried About AI Taking Your Job)

* The best way to prepare is to **build something**.
* Don’t fear the code. Use Codex. Copy a POC. Try a tutorial.
* Understanding agents means understanding how decisions get made.

#### 👨‍🎓 For Parents (Like Me)

* I have an 8-year-old son. I don’t just think about the job he’ll have.
* I think about the *team* he’ll lead.
* The future belongs to those who:

  * Understand a domain deeply
  * Can collaborate with tools and people
  * Are curious, creative, and responsible

Teaching our kids to explore, build, and reflect is the best gift we can give them.

---

### Final Word: It’s Time to Coach the Agents

AI agents aren’t coming. They’re already here.

But the future isn’t about replacing people. It’s about building *teams of humans and AI* that learn, adapt, and do good work together.

That’s what CoachingTheMachine is all about. Let’s keep going.
