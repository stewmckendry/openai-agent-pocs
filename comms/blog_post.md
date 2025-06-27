AI Agents: Beyond the Buzzword — What They Are, Why They Matter, and How to Build Them Responsibly

Real-world examples of AI agents built with OpenAI’s SDK and MCP —what they are, how they work, and how they’ll reshape teams, tools, and trust.

---

By Stewart McKendry

Everyone’s Talking About Agents. But Can They Really Help?
AI agents are quickly becoming part of mainstream business strategy. According to recent surveys, over half of companies already run agents in production, and nearly 80% are actively developing new ones.

And yet, the term "AI agent" remains loosely defined. Most people still encounter AI as basic copilots or chat interfaces, like using ChatGPT to draft a document or Microsoft Copilot to summarize a Teams call. These tools provide productivity value but are only the starting point.

We’re just beginning to unlock what’s possible when AI agents take on more responsibility and autonomy. There’s a continuum emerging:

Small tasks (extract a name from a form)

Persistent roles (daily workout planner)

Chained processes (onboarding new employees)

This trend underpins the mission that Shopify CEO Tobi Lütke described in a memo: teams will need to demonstrate why new roles can't be handled by AI before asking for headcount or budget. That mindset is spreading and may become the norm faster than we think.

That leaves leaders with important strategic questions:

What are the capabilities AI agents can provide—and how do we take best advantage of them for our organization, clients, and people?

What does my organization need to look like to support this? What skills and infrastructure—technology, data, governance—makes this sustainable?

How do we go beyond pilots and experiments to scale these systems responsibly? Do we centralize efforts—or empower teams across the organization?

This post shares three practical applications of AI agents to show what’s already possible—how they’re built, how they work, and how they can support real-world use cases both for individuals and organizations.

From Custom GPTs to AI Agent Teams
In earlier posts, we shared projects like ConcussionGPT (for youth sports safety), GovDoc Copilot (for public sector writing), and MyHealth AI Assistant (for exploring personal health data). These were useful single-agent tools built with ChatGPT—often enhanced with retrieval or templates—but they were limited to one model, one interface, and offered little visibility or flexibility under the hood.

Now, frameworks like the OpenAI Agents SDK and the Model Context Protocol (MCP) make it possible to build full teams of AI agents that work together through clear handoffs. The SDK provides a simple yet powerful foundation to create multi-agent systems without reinventing the wheel. It comes with:

Agents – LLMs equipped with specific goals, instructions, and tools

Handoffs – Agents can delegate tasks to each other in a defined chain

Guardrails – Checks on both inputs and outputs to keep things on track

Headless design – Deploy agents in any interface (chatbot, app, dashboard)

Model flexibility – Easily switch between GPT-4, Claude, Gemini, and more

MCP support – A new open standard that lets agents work with files, tools, and context like a developer would

Built-in tracing + visualization – Auto-generated flow diagrams and logs to help you debug and iterate faster

In the rest of this post, I’ll share three example agents I built using the OpenAI Agents SDK and MCP. Each is tailored to a different use case—some for everyday consumers, others for teams inside organizations. They’re not complete products, but they show what’s possible when you go beyond a single prompt or chatbot.

Three Real Agent Teams in Action
🏅 Run Coach Agent: Train Smarter With Your Data
I gave the agent team this goal: I want to run a marathon in under 3:05 this October. Inspired by my real attempt to qualify for Boston.

Behind the scenes, the agents got to work:

Goal Agent parsed my target pace and date, and even used a tool to retrieve the current date to get oriented (the model initially thought it was still 2023!).

Collect Agent loaded my recent workouts from Activities.csv, a file I exported from Garmin Connect containing my running and cycling logs from the past month.

Analyze Agent identified strengths and gaps in my training based on my workouts and my race goal.

Plan Agent generated a full 14-week training schedule.

Check Agent reviewed the plan for feasibility and risk.

The result included long runs, speed intervals, hill workouts, and a structured taper—saved as Markdown, with a visual workflow diagram. 📄 View output run plan

Later, I re-ran the same input using Google’s Gemini model to get a "second opinion". The output was nearly as strong, with a few different insights (minus a formatting hiccup): 📄 View Gemini version

Why it matters:

Makes coaching logic accessible to anyone with a goal and some data.

Demonstrates agents reasoning across personal data, tools, and structured planning.

Highlights the benefits of model-switching—getting multiple perspectives.

🧠 Reflection: The analysis of my recent runs was pretty accurate. But the plan was ambitious—I wouldn’t feel confident racing 42K if my longest training run only reached 26K! I’d want to embed domain knowledge from trusted coaching plans, or even better, personalize it with what’s worked for me in the past.

You could imagine a next version of this agent acting as a daily check-in coach—adapting your plan based on recent runs, mood, recovery, or life schedule. We’re just getting started.

✈️ Trip Planner Agent: From Dream to Itinerary
"My son and I want to go on a road trip to watch Sidney Crosby play in what might be his final year before retiring."

That’s the kind of dream Liam (my son) and I are chasing. We’ve started doing annual NHL or MLB road trips, including a trip last year to a Leafs vs. Sabres game in Buffalo. This year, we want to see the Penguins before Crosby retires.

Here’s how the agent team helped:

Topic Agent generated specific topics to research, like the Penguins’ 2025 schedule, road trip routes between games, hotel options near NHL arenas, things to do in host cities, and where to buy tickets.

Research Agent used a built-in web search tool (available out-of-the-box in the OpenAI Agents SDK) to gather and summarize useful links and insights.

Planner Agent synthesized the research into a multi-city, 7-day itinerary with games in Pittsburgh, Detroit and Toronto, travel plans, accomodations and other relevant attractions. Check it out: 📄 View output travel plan

Why it matters:

Turns open-ended dreams into structured, bookable plans.

Showcases real-time research, summarization, and planning across multiple tools.

Demonstrates how agents can tailor plans to user interests, locations, and logistics.

🧠 Reflection: The plan looks awesome—and Liam would love it! But attending three NHL games might stretch the budget, so next time I’d tune the prompt to include time and budget constraints.

I also fact-checked it against the 2025–26 preseason schedule, and it mostly lined up. Interestingly, it swapped in a Leafs game for a Sabres one—maybe it knew we’re Leafs fans.

If I were refining this for real use, I’d:

Add a sub-agent to verify schedule accuracy and surface game dates.

Include agents that surface travel advisories, vaccination requirements, and customs info.

Together, these would make the trip planner even more complete—and safer—for families like ours.

🛠️ Agile Team Copilot: From Idea to Implementation
On many agile projects, I’ve seen similar challenges crop up: the handoff between the people writing user stories and the ones building them isn’t always smooth. When stories and specs aren’t well-defined or aligned to the team’s architecture, it leads to bugs, rework, delays and frustration.

This agent was built to address that pain. Picture it sitting in your refinement sessions, helping the product owner and team flesh out high-quality stories—complete with requirements, acceptance criteria, architecture impacts, estimates, and dependencies. All ready to feed the developers’ queue.

We tested this agent using a real-world enhancement request for an online portal for a national postal service:

"My packages often get stolen when left by the courier at the door. I want to see a real-time map of where my package is, be able to chat with the courier via text, and hold my packages at a nearby post office when I'm away."

Here’s how the agent team generated the story:

UX Agent gathered personas and usage goals

Functional Agent outlined key features for tracking, chat, and package holds

Technical Agent suggested backend and frontend designs

Acceptance Agent wrote Gherkin-style test criteria

Impact Agent scanned local files using the built-in MCP FileSystem Server to assess code and architecture changes

Estimation Agent scoped the effort across three sprints

Writer Agent assembled the full story

Verifier Agent checked it against Definition of Ready

Check out the user story and specs it produced: 📄 View output story

🧠 Reflection: The output was detailed, beyond what’s usually available at the start of most projects. With real documentation and tooling integrations, this could easily become a go-to accelerator for agile teams.

By connecting agents to trusted sources like GitHub, Confluence, or Jira (via a secure MCP server), we could enable them to reason across your actual backlog, designs, and codebase.

This isn’t just about better stories—it’s about:

Accelerating requirements and sprint planning

Reducing rework and inconsistency

Creating structured, traceable artifacts that can evolve as your project does

Wrapping Up the Examples
Across these three agent-powered demos—personal fitness planning, travel logistics, and agile delivery prep—we saw what it looks like when AI agents collaborate to complete real tasks and deliver transparent, structured results. All built in a couple days with OpenAI Agents SDK + MCP (with the help of my developer Codex Agent).

What makes these agentic apps especially powerful isn’t just the quality of their outputs—it’s the system-level benefits they unlock:

Traceability: You can see how each agent contributed and what decisions were made, step by step. Explore these flows at platform.openai.com/traces, or refer to the appendix for a screenshot.

Visualization: The SDK automatically creates visual flow diagrams of agent handoffs and logic, making the system easier to explain, debug, and improve (see appendix for a sample).

Headless by design: These apps were run directly from VS Code, just like any developer-built tool. But they can be deployed through any interface you choose, whether that's a chatbot, dashboard, or public-facing app. You’re not locked into any single platform or product.

These features unlock the ability to build responsibly, iterate quickly, and deploy flexibly—wherever the value is needed.

Reflections: What This Means for You
💼 For Organizations
These new SDKs unlock the ability to rethink how work gets done:

Redefine tasks, roles, and processes by introducing AI agents that can take on more responsibility and autonomy. Think of them as accelerators—or extensions—of your team.

Why now?

Productivity: Do more with less

Quality: LLMs, when embedded in agents, bring a Swiss-army knife of skills and knowledge

Personalization: Tailor tone, style, literacy for every user

24/7 support: Agents don’t sleep

Bonus: I like Exponential View’s “Rule of 5”—if you do something five or more times, you can probably automate it

Success depends on setting up the right conditions:

Provide the right tech, data access, and guardrails

Then empower your people—those closest to the work—with the skills and tools to experiment and iterate

Focus on turning ideas → solutions → results through safe, traceable, human-in-the-loop development

🤖 For Individuals (Worried About AI Taking Your Job)
The best way to prepare? Try something.

Open ChatGPT, Copilot, or another tool and explore

Ask ChatGPT or your peers for help leveling up

You don’t need to be a coder to work with agents. I’m not one either. But curiosity, plus tools like ChatGPT and Codex agents, can take you surprisingly far.

You don’t have to build agents yourself, but understanding what they are and how they work will help you stay a step ahead. Staying one step ahead starts with learning by doing.

👨‍🎓 For Parents (Like Me)
I often wonder what my son’s path will look like and whether we’re truly preparing him for it.

There’s reason to be cautious. Studies show that when we rely too heavily on ChatGPT-like tools, we may not internalize knowledge the same way as when we learn through doing.

That’s why it’s more important than ever to:

Focus on foundational knowledge and critical thinking

Use tools like ChatGPT to amplify learning, not replace it

Teach kids Socratic reasoning—understanding the “why” behind the “what”

And help them grow into curious, capable, and empathetic people who combine domain expertise, STEM literacy, and a commitment to doing good with technology.

Final Word: It’s Time to Coach the Agents
AI agents aren’t coming. They’re already here.

But the future isn’t about replacing people. It’s about building teams of humans and AI that learn, adapt, and do good work together.

And just like we coach people, we must design, guide, and evolve our AI teammates to be useful, reliable, and aligned with our values.

That’s what CoachingTheMachine is all about. Let’s keep going.

Want to explore more?
Links:

3 PoCs in GitHub Repo

Run Coach Agent Overview

Trip Planning Agent Overview

Agile Team Copilot Overview

OpenAI-Agents SDK Repo

Model Context Protocol

Screenshots:

Here’s examples of Run Coach Agent workflow (i.e. the steps it did) in platform.openai.com/trace:
(insert screenshot of Run Coach Agent trace webpage)

And here is a visual of the Run Coach Agent flow that is generated with the SDK:
(insert screenshot of Run Coach Agent flow diagram)