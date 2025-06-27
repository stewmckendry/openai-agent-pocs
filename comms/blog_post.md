**Title:** AI Agents: Beyond the Buzzword — What They Are, Why They Matter, and How to Build Them Responsibly

---

### Everyone’s Talking About Agents. But Can They Really Help?

AI agents are quickly becoming part of mainstream business strategy. According to recent surveys, over half of companies already run agents in production, and nearly 80% are actively developing new ones.

And yet, the term "AI agent" remains loosely defined. Most people still encounter AI as basic copilots or chat interfaces—like using ChatGPT to draft a document or Microsoft Copilot to summarize a Teams call. These tools provide real productivity value but are only the starting point.

We’re just beginning to unlock what’s possible when AI agents take on more responsibility and autonomy. There’s a clear continuum emerging:

* **Small tasks** (like extracting data from a file)
* → **Persistent roles** (like an AI planner or researcher)
* → **Chained processes** (like onboarding or trip planning)
* → **Functional agents** managing entire workflows across systems

This trend underpins the mission that Shopify CEO Tobi Lütke described in a memo: teams will need to demonstrate why new roles can't be handled by AI before asking for headcount or budget. That mindset is spreading—and may become the norm faster than we think.

That leaves leaders with important strategic questions:

1. *What are the real capabilities AI agents can provide—and how do we take best advantage of them for our business, customers, and people?*
2. *What does my organization need to look like to support this? What infrastructure—technical, data, governance—makes this sustainable?*
3. *How do we go beyond pilots and experiments to scale these systems responsibly? Do we centralize efforts—or empower teams across the organization?*

👉 This post shares three practical applications of AI agents to show what’s already possible—how they’re built, how they work, and how they can support real-world use cases both for individuals and organizations.

---

### From Custom GPTs to AI Agent Teams

In earlier CoachingTheMachine posts, I shared projects like **ConcussionGPT** (for youth sports safety), **GovDoc Copilot** (for public sector writing), and **MyHealth AI Assistant** (for exploring your own health data). These were helpful single-agent tools built with ChatGPT, often enhanced with retrieval or templates—but limited to one model and one interface, with little flexibility or visibility into how they worked.

Now, with frameworks like the [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) and the **Model Context Protocol (MCP)**, we can go much further.

These tools let us build teams of AI agents that work together—each with its own job, memory, and tools. The SDK gives you a simple but robust platform to build agents without reinventing the wheel. It comes ready-to-use with:

* **Agents** – LLMs equipped with specific instructions and tools
* **Handoffs** – the ability to delegate tasks to other agents in a chain
* **Guardrails** – safeguards to check inputs before agents act
* **Headless design** – deploy agents through any frontend (e.g. Streamlit, Slack, custom apps)
* **Model and provider flexibility** – switch between GPT-4, Claude, Gemini, or others as needed
* **MCP support** – a new open standard that lets AI agents interact with files, tools, and context like a developer would
* **Built-in trace + visualization** – to debug, iterate, and improve your flows

In the rest of this post, I’ll walk through **three working examples**, each tailored to a different kind of use case—some consumer-facing, some built for project or product teams inside organizations. They’re not meant to be exclusive patterns, but rather to spark ideas and show what’s now possible.&#x20;

---

### Three Real Agent Teams in Action

#### 🏅 Run Coach Agent: Train Smarter With Your Data

> "I want to run a marathon in less than 3 hours 5 minutes in my race coming up in October."

That’s the kind of input I gave the agent team, inspired by my real-life goal of qualifying for the Boston Marathon.

Behind the scenes, the agents got to work:

1. **Goal Agent** parsed my target pace and date—and even used a tool to retrieve the current date to get oriented (the model initially thought it was still 2023).
2. **Collect Agent** loaded my recent workouts from `Activities.csv`, a file exported from Garmin Connect containing my running and cycling logs from the past month.
3. **Analyze Agent** identified strengths and gaps in my training based on my workouts *and* my race goal.
4. **Plan Agent** generated a full 8-week training schedule.
5. **Check Agent** reviewed the plan for feasibility and risk.

📝 [View README](https://github.com/stewmckendry/openai-agent-pocs/blob/main/pocs/run_coach_agent/README.md)
📄 [View output plan](https://github.com/stewmckendry/openai-agent-pocs/blob/main/pocs/run_coach_agent/outputs/plan_20250627_105713.md)

The result included long runs, speed intervals, hill workouts, and a structured taper—saved as Markdown, with a visual workflow diagram.

Later, I re-ran the same input using Google’s Gemini model to get a "second opinion"—the output was nearly as strong, with a few different insights (minus a formatting hiccup):
📄 [View Gemini version](https://github.com/stewmckendry/openai-agent-pocs/blob/main/pocs/run_coach_agent/outputs/plan_20250627_120310.md)

Why it matters:

* Makes coaching logic accessible to anyone with a goal and some data.
* Demonstrates agents reasoning across personal data, tools, and structured planning.
* Highlights the benefits of model-switching—getting multiple perspectives.

🧠 **Reflection:**
The analysis of my recent runs was surprisingly accurate. But the plan was *ambitious*—I wouldn’t feel ready to race 42K if my longest training run capped out at 26K! I’d want to embed domain knowledge from trusted coaching plans, or even better, personalize it with what’s worked for me in the past.

You could imagine a next version of this agent acting as a **daily check-in coach**—adapting your plan based on recent runs, mood, recovery, or life schedule. We’re just getting started.

#### ✈️ Trip Planner Agent: From Dream to Itinerary

> "My son and I want to go on a road trip to watch Sidney Crosby play in what might be his final year before retiring."

That’s the kind of dream Liam (my son) and I are chasing. We’ve started doing annual NHL or MLB road trips—last year we hit a Sabres game in Buffalo. This year, we want to see the Penguins.

Here’s how the agent team helped:

1. **Topic Agent** generated specific topics to research—like the Penguins’ 2025 schedule, road trip routes between games, hotel options near NHL arenas, things to do in host cities, and where to buy tickets.
2. **Research Agent** used a built-in web search tool (available out-of-the-box in the OpenAI Agents SDK) to gather and summarize useful links and insights.
3. **Planner Agent** synthesized the research into a multi-city, 6-day road trip itinerary:

* **Day 1**: Arrive in Pittsburgh, check in at Cambria Hotel Downtown, explore downtown and Point State Park.
* **Day 2**: Visit the Andy Warhol Museum and attend a Penguins home game at PPG Paints Arena.
* **Day 3**: Drive to Detroit (\~5 hours), stay at Marriott Renaissance Center, visit Detroit Institute of Arts.
* **Day 4**: Visit Motown Museum and attend Penguins vs. Red Wings.
* **Day 5**: Drive to Toronto (\~4 hours), stay at Fairmont Royal York, visit the CN Tower.
* **Day 6**: Visit Royal Ontario Museum and attend Penguins vs. Maple Leafs.
* **Day 7**: Stroll through High Park and head home.

📝 [View README](https://github.com/stewmckendry/openai-agent-pocs/blob/main/pocs/trip_planner_agent/README.md)
📄 [View output plan](https://github.com/stewmckendry/openai-agent-pocs/blob/main/pocs/trip_planner_agent/outputs/trip_20250627_110149.md)

Why it matters:

* Turns open-ended dreams into structured, bookable plans.
* Showcases real-time research, summarization, and planning across multiple tools.
* Demonstrates how agents can tailor plans to user interests, locations, and logistics.

🧠 **Reflection:**
The plan looks awesome—and Liam would love it! But attending three NHL games might stretch the budget, so next time I’d tune the prompt to include time and budget constraints.

I also fact-checked it against the 2025–26 preseason schedule, and it mostly lined up. Interestingly, it swapped in a Leafs game for a Sabres one (it must know we’re Leafs fans).

If I were refining this for real use, I’d:

* Add a **sub-agent to verify** schedule accuracy and surface game dates.
* Include agents that surface **travel advisories, vaccination requirements, and customs info**.

Together, these would make the trip planner even more complete—and safer—for families like ours.

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
