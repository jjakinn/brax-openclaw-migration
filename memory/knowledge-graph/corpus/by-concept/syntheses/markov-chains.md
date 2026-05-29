# Synthesis: Markov Chains
*Cross-reference from Veritasium video + historical context + modern applications*

---

## One-Sentence Definition

A Markov chain is a stochastic process where the next state depends **only on the current state**, not on the sequence of events that preceded it (memoryless property).

---

## Historical Origin: The Math Feud That Changed History

### The Setup (1905 Russia)

**Pavel Nekrasov** (Tsarist side):
- Deeply religious, conservative mathematician
- "Tsar of Probability"
- Believed math could prove free will and God's existence

**Andrey Markov** (Socialist side):
- Atheist, "Andrey the Furious"
- Had no patience for unrigorous math
- Publicly criticized Nekrasov's work

### The Core Dispute

**Law of Large Numbers** (Jacob Bernoulli, 1713):
- For independent events (coin flips), averages converge to expected values
- Nekrasov: "If you see convergence, events must be independent"
- Nekrasov's conclusion: Social statistics converging → individual decisions are independent → free will exists

**Markov's Counter:**
> "Thus free will is not necessary to do probability."

### Markov's Proof

**The Innovation:** Use dependent events that STILL follow the law of large numbers.

**Method:** Analyze text from Pushkin's *Eugene Onegin*
1. Took first 20,000 letters
2. Stripped punctuation/spaces
3. Found: 43% vowels, 57% consonants
4. Created **transition probabilities** between vowel/consonant states

**State Machine:**
```
[Vowel] --0.13--> [Vowel]
   |--0.87--> [Consonant]

[Consonant] --0.33--> [Vowel]
       |--0.67--> [Consonant]
```

**Result:** Even though letters are dependent (vowels rarely follow vowels), the ratio still converges to 43/57.

---

## Formal Definition

**Memoryless Property:**
```
P(Xₙ₊₁ = s | Xₙ = sₙ, Xₙ₋₁ = sₙ₋₁, ..., X₀ = s₀) = P(Xₙ₊₁ = s | Xₙ = sₙ)
```

**Transition Matrix:**
```
     |  Vowel  | Consonant |
-----|---------|-----------|
Vowel|   0.13  |    0.87   |
Cons |   0.33  |    0.67   |
```

Each row sums to 1 (probability distribution).

---

## Key Insight: Memoryless = Powerful

> "The beautiful thing Markov and others found is that for many of these systems, you can ignore almost all of that [history]. You can just look at the current state and forget about the rest." — *Veritasium*

**Why this matters:**
- Complex systems with long histories become tractable
- Predictions require only current state
- Enables computational modeling of real-world phenomena

---

## Major Applications

### 1. Nuclear Physics (1940s) — Monte Carlo Method

**Problem:** How much uranium-235 needed for a bomb?

**Stanislaw Ulam:**
- Recovering from encephalitis, played solitaire
- Question: Probability of winning random solitaire game?
- Solution: Play hundreds of games, count wins

**Neutron Simulation:**
- Model neutron behavior in uranium core
- States: traveling, scattered, absorbed, fission
- Transition probabilities depend on neutron velocity, position, energy
- **Multiplication factor K:** Average neutrons produced per fission
  - K < 1: Reaction dies
  - K = 1: Self-sustaining
  - K > 1: Exponential growth (bomb)

**Von Neumann + Ulam:**
- Named method after Monte Carlo Casino
- First use: ENIAC computer (1946)

### 2. Google PageRank (1998)

**Problem:** How to rank web pages by quality?

**Insight (Larry Page & Sergey Brin):**
- Links = endorsements (like library book stamps)
- More incoming links = higher quality
- Weighted by outgoing links (diluted votes)

**Markov Chain Model:**
- **States:** Web pages
- **Transitions:** Links between pages
- **Random surfer:** Follows links 85% of time, jumps randomly 15%
- **PageRank:** Stationary distribution (time spent on each page)

**Anti-gaming:**
- Creating 100 pages linking to your site doesn't help
- Pages with no incoming links contribute nothing over time
- Quality links matter, not quantity

> "At the heart of this trillion dollar algorithm is a Markov chain." — *Veritasium*

### 3. AI Language Models

**Claude Shannon (1940s):**
- Extended Markov's idea to text prediction
- Letter-level: `P(next letter | current letter)`
- Word-level: `P(next word | previous N words)`

**Modern LLMs:**
- Use tokens (letters, words, punctuation)
- **Game:** Given 30 tokens, predict probability of next token
- **Attention mechanism:** Not all tokens weighted equally
  - "cell" after "blood" and "mitochondria" = biology context
  - "cell" after "prison" = incarceration context

**Warning — Model Collapse:**
> "When [LLM output] becomes training data for future models... the game is very soon over. You come to a very dull stable state." — *Veritasium*

---

## Where Markov Chains DON'T Work

**Feedback Loops:**
- Global warming: CO₂ → temperature ↑ → water vapor ↑ → temperature ↑↑
- Positive feedback makes prediction difficult
- Systems where history matters exponentially

**Long-Range Dependencies:**
- Grammar that depends on sentence start
- Complex conditional logic
- Context that spans thousands of tokens

---

## Key Quotes

> "Problem solving is often a matter of cooking up an appropriate Markov chain."

> "It's kind of ridiculous to me that this basic fact of mathematics would come out of a fight like that which really had nothing to do with it."

> "All these systems have extremely long histories... but the beautiful thing... is that for many of these systems, you can ignore almost all of that."

---

## Prerequisites

**Required:**
- Basic probability theory
- Understanding of state machines

**Helpful:**
- Linear algebra (for transition matrices)
- Statistics (law of large numbers)

**Next Steps:**
- [neural-networks](neural-networks.md) — Modern prediction methods
- [transformers](transformers.md) — Attention-based prediction

---

## Sources

- **Primary:** Veritasium — "The Math Feud That Changed History" (32 min, 5,429 words)
- **Referenced:** Markov's original 1906 paper, Shannon 1948, Page & Brin 1998

---

*Synthesized from 5,429 words + historical context*
