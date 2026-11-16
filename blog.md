**Filename:** `needs-for-experimentation-in-data-science.md`

# Why Data Science Needs Experiments (and How to Run Them Fairly!)

Imagine your favorite café changes its cookie recipe. Customers buy more cookies the next week. Was the new recipe a hit—or did a school trip bring a busload of hungry students? 🍪

That’s a challenge data scientists face all the time: **When something changes, did the change cause the outcome, or did something else?** Experiments help us answer that question more fairly.

## Correlation is a clue, not a cause

Suppose students who use a homework reminder app tend to turn in more assignments on time. That’s a useful clue—but it doesn’t prove the app caused the improvement. Maybe students who already plan ahead are more likely to use it.

Data scientists call this the difference between **correlation** and **causation**:

- **Correlation:** Two things change together.
- **Causation:** Changing one thing helps produce a change in another.

Experiments give us a structured way to test whether a change—such as a new app feature, lesson, or website design—makes a difference.

### Why run an experiment?

A well-designed experiment can help teams:

- **Make better decisions:** Test a change before rolling it out to everyone.
- **Spot unwanted side effects:** A faster checkout might accidentally make it harder for some people to use a discount.
- **Learn who benefits:** A feature might help new users but make little difference to experienced users.
- **Avoid confusing coincidence with impact:** The world has plenty of surprises; experiments help us investigate whether a change made a difference.

Think of an experiment like a fair taste test. If you want to know which cookie recipe people prefer, you shouldn’t give one recipe to all the cookie fans and the other to people who already dislike cookies. 🍪

## Common ways to test an idea

### 1. Randomized experiments: the fair coin flip

An **A/B test** is a type of randomized experiment. People—or another suitable unit—are assigned by chance to one of two groups:

- **Control:** Gets the current experience.
- **Treatment:** Gets the new version.

Then the team compares an outcome, such as whether people finish checkout or remember a lesson.

Random assignment helps make the groups comparable **on average**. It’s a bit like shuffling a deck before dealing: the goal is to avoid stacking one group with people who were already more likely to succeed. Random assignment does not guarantee perfectly matched groups, especially in small experiments.

**Choose the assignment unit carefully.** If students in the same classroom influence one another, assigning individual students to different groups could blur the results. One student might share a new study tip with classmates in the control group. In that case, it may be more appropriate to assign whole classrooms, schools, or other groups. The right choice depends on where people might affect one another—a problem called **interference**.

### 2. Quasi-experiments: learning when a coin flip isn’t possible

Sometimes random assignment is impractical, unfair, or impossible. Researchers can use **quasi-experimental methods** to estimate the effect of a change without random assignment.

Examples include:

- **Difference-in-differences:** Compare how outcomes change over time in a group affected by a policy with changes in a similar group that wasn’t affected. This method relies on the groups having followed comparable trends if the policy had not happened.
- **Regression discontinuity:** Compare cases just above and just below a cutoff, such as an eligibility score threshold. The comparison is most informative when people close to the cutoff are similar and cannot precisely manipulate which side they land on.
- **Interrupted time series:** Look for a change in a trend after an intervention begins, while considering other events that might also explain the change.

These methods can be powerful, but they rely on assumptions. Researchers should explain those assumptions and check how plausible they are.

### 3. Offline tests and simulations: a useful rehearsal

Before a change reaches real users, teams may test it on existing data or in a simulation. This can be a useful rehearsal: it may reveal bugs or help rule out ideas that seem unlikely to work.

But historical data has limits. It reflects what happened under earlier conditions, not necessarily what would happen after a new change. And if information from the future accidentally sneaks into a model’s training data, that’s **data leakage**—like seeing the answer key before taking the test. Offline results can provide useful evidence, but they don’t always predict what will happen in the real world.

### 4. Online tests: trying a change in a live setting

An **online experiment** tests a change where people actually use the product or service—for example, trying a new checkout button on a website.

Because live tests affect real people, they need safeguards. Teams should monitor safety and user experience, protect privacy, and have a plan to stop or change the experiment if something goes wrong.

## How to design a fair experiment

Good experiments start with a clear plan—not with “Let’s change something and see what happens.” 🧪

### Step 1: Ask a decision-focused question

Make the question specific enough to guide a decision.

> “Does the new checkout layout help more customers complete a purchase without increasing accidental orders?”

That’s more useful than “Is the new layout better?”

### Step 2: Write down a hypothesis

A **hypothesis** is a testable prediction.

> “People who see the new checkout layout will be more likely to complete a purchase than people who see the current layout.”

A hypothesis doesn’t need to be right. It needs to be clear enough that evidence can support or challenge it.

### Step 3: Choose the unit of randomization

Decide what gets assigned by chance: a person, account, classroom, store, or something else. Think about whether people can influence one another, whether the same person may appear more than once, and whether the chosen unit fits the question.

### Step 4: Pick a primary metric and guardrails

A **primary metric** is the main outcome the experiment is designed to evaluate. For a homework reminder app, it might be the percentage of assignments handed in on time.

**Guardrail metrics** help catch important side effects. The app team might also monitor notification opt-outs or reports that reminders are arriving at the wrong time.

Choose metrics that reflect what you truly care about. A weak proxy can send you in the wrong direction: more clicks, for instance, don’t automatically mean people are happier or better served.

### Step 5: Plan the sample size and duration

A study that is too small may not detect an effect that matters. One that runs too briefly may miss normal patterns, such as differences between weekdays and weekends.

Plan the sample size and duration before starting, based on the question, the expected outcome, and the smallest effect that would matter for the decision. Consider **seasonality**, too: a shopping feature tested only during a holiday rush may behave differently in an ordinary month.

### Step 6: Decide how you’ll analyze the results

Write down the analysis plan in advance—including the primary metric and any planned subgroup comparisons. This helps reduce the temptation to search through many results until one looks exciting.

Also check that assignment worked as intended. If the experiment was meant to split eligible users evenly, for example, investigate a surprising imbalance rather than simply carrying on.

## Reading the results without fooling yourself

When results come in, ask more than “Did it work?”

### Look at effect size

**Effect size** describes how large the difference was. A result can be statistically detectable but too small to matter in practice. If a change saves only a tiny amount of time, is that enough to justify the cost and effort of building it?

### Look at uncertainty

Experiment results are estimates, not perfect measurements. They have uncertainty. A confidence interval, for example, gives a range of effect sizes that are reasonably compatible with the data under the study’s assumptions.

A **p-value is not the probability that a hypothesis is true**. It also doesn’t tell you whether a result is important in everyday life. Statistical significance is not the same thing as practical importance. 📊

### Check for differences across groups—carefully

A feature may affect different groups differently. That can matter for both product decisions and fairness. But subgroup results can be noisy, especially when groups are small or many comparisons are made. Treat unexpected patterns as clues to investigate, not automatic proof that a group is affected.

### Keep the setting in mind

A result from one group, school term, or website may not apply everywhere. Consider who took part, what was tested, and whether conditions have changed before generalizing.

## Common experiment pitfalls 🚧

- **Selection bias:** The way people enter or end up in groups can make the groups systematically different.
- **Peeking and stopping early:** Repeatedly checking results and stopping as soon as they look promising can increase false alarms if the analysis plan does not account for repeated checks.
- **Too many metrics or comparisons:** The more things you test, the easier it is to find a pattern that appeared by chance.
- **Weak proxies:** A measure like clicks may not capture the outcome you actually care about.
- **Interference:** People in one group influence people in another.
- **Logging or data-quality failures:** Missing, duplicated, or incorrectly recorded events can distort the results.
- **Overgeneralizing:** A result in one setting doesn’t prove the same change will work for everyone, everywhere.

**Fun fact:** A/B testing isn’t limited to buttons and websites. Experiments can compare lesson formats, reminder schedules, product designs, or many other changes—as long as the question, outcome, and ethical safeguards are clear.

## Experiments need ethics, too 💛

A technically sound experiment can still be a bad idea if it treats people unfairly or exposes them to unnecessary risk.

Responsible experiments consider:

- **Privacy:** Collect only the data needed, and protect it.
- **Consent:** Seek consent where appropriate, and explain participation clearly.
- **Fairness and accessibility:** Consider whether the experiment could exclude, disadvantage, or confuse particular groups.
- **Potential harm:** Monitor for negative effects and set a plan for stopping or changing the test.
- **Extra care in high-impact settings:** Experiments involving areas such as health, education, finance, or essential services deserve particular scrutiny.
- **Children and other vulnerable groups:** Use additional safeguards, appropriate consent processes, and careful review.

The goal isn’t simply to find a winning version. It’s to learn in a way that respects the people affected.

## So, does the new idea work?

Picture a streaming service testing different artwork for a show. An experiment can help the service learn how a particular image performs for a particular audience or setting. It cannot prove that one image is universally best—people and contexts differ.

Netflix has written about personalizing artwork for its service. That’s an example of using data to tailor product design; the article is not, by itself, evidence that a particular experiment was conducted.

That’s the heart of experimentation in data science: **ask a focused question, compare fairly, measure thoughtfully, and stay honest about what the evidence can—and can’t—tell you.**

### The takeaway

**Experiments help data scientists move from “these things happened together” to stronger evidence about whether a change made a difference.** Plan carefully, watch for side effects, respect participants, and treat every result as evidence—not magic. ✨

## Further reading

- Kohavi, Tang & Xu, *Trustworthy Online Controlled Experiments* (Cambridge University Press, 2020); experimentguide.com
- American Statistical Association, *Statement on Statistical Significance and P-Values* (2016); amstat.org
- Hernán & Robins, *Causal Inference: What If*; hsph.harvard.edu/miguel-hernan/causal-inference-book
- NIST/SEMATECH, *e-Handbook of Statistical Methods*; itl.nist.gov/div898/handbook
- Netflix Technology Blog, “Artwork Personalization at Netflix”

*Further-reading references are provided as starting points; links and publication details should be checked before publication.*