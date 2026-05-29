# Synthesis: Neural Networks
*Cross-reference from 3Blue1Brown series (9 chapters) + Neural Network from Scratch*

---

## Core Definition

A neural network is a function composed of layered transformations that maps input data to output predictions through learned parameters (weights and biases).

> "The entire network is just a function... It's an absurdly complicated function, one that involves 13,000 parameters... but it's just a function nonetheless." — *3Blue1Brown, Ch1*

---

## Architecture Components

### 1. Neurons (Nodes)
- **What they hold:** A single number between 0 and 1 called "activation"
- **Intuition:** Think of them as "lit up" when activation is high
- **Input layer (MNIST example):** 784 neurons (28×28 pixels)
- **Output layer:** 10 neurons (digits 0-9)
- **Hidden layers:** Arbitrary depth/width (example: 2 layers × 16 neurons)

### 2. Connections (Weights)
- Each connection has a **weight** (strength of connection)
- Organized as **weight matrices** between layers
- Positive weights = green (activating)
- Negative weights = red (inhibiting)

### 3. Biases
- Added to weighted sum before activation
- Determines threshold for neuron activation
- Formula: `activation = σ(weighted_sum + bias)`

### 4. Activation Functions

| Function | Formula | Use Case |
|----------|---------|----------|
| **Sigmoid** | `σ(x) = 1 / (1 + e^(-x))` | Classic, squashes to [0,1] |
| **ReLU** | `max(0, x)` | Modern default, easier to train |

> "Early networks used sigmoid... But relatively few modern networks actually use sigmoid anymore... ReLU seems to be much easier to train." — *Leysa Lee, PhD, Ch1*

---

## Forward Pass (Inference)

```
Input → [Weights × Input + Bias] → σ → Hidden Layer → [Weights × Hidden + Bias] → σ → Output
```

**Matrix notation (compact form):**
```
a^(l) = σ(W^(l) · a^(l-1) + b^(l))
```

Where:
- `a^(l)` = activation vector at layer l
- `W^(l)` = weight matrix between layer l-1 and l
- `b^(l)` = bias vector at layer l
- `σ` = sigmoid (element-wise)

---

## The "Learning" Intuition

### Layer Hierarchy (Hopes for What Each Layer Learns)

**Layer 1 (Input):** Raw pixel values (784 activations)

**Layer 2 (Hidden):** **Edge detectors**
- Vertical lines, horizontal lines, curves
- Small local patterns

**Layer 3 (Hidden):** **Pattern detectors**
- Loops, long lines, specific shapes
- Combinations of edges

**Layer 4 (Output):** **Digit classifiers**
- 9 = loop (top) + line (right)
- 8 = loop (top) + loop (bottom)
- 4 = three specific lines

> "In a perfect world, we might hope that each neuron in the second-to-last layer corresponds with one of these subcomponents." — *3Blue1Brown, Ch1*

**Reality check:** Training finds *some* structure, but not necessarily human-interpretable features.

---

## Parameter Count (MNIST Example)

| Connection | Calculation | Count |
|------------|-------------|-------|
| Input → Hidden 1 | 784 × 16 | 12,544 weights |
| Hidden 1 biases | 16 | 16 biases |
| Hidden 1 → Hidden 2 | 16 × 16 | 256 weights |
| Hidden 2 biases | 16 | 16 biases |
| Hidden 2 → Output | 16 × 10 | 160 weights |
| Output biases | 10 | 10 biases |
| **TOTAL** | | **~13,000 parameters** |

> "13,000 knobs and dials that can be tweaked and turned to make this network behave in different ways." — *3Blue1Brown, Ch1*

---

## Training (Preview — See Ch2 for Details)

**What "learning" means:**
Finding values for all 13,000 weights and biases such that the network correctly classifies digits.

**Method:**
1. Initialize weights randomly
2. Feed training examples
3. Calculate error (loss)
4. Backpropagate error to adjust weights
5. Repeat millions of times

---

## Key Insights from Multiple Sources

### From 3Blue1Brown Ch1:
- Neural networks are inspired by the brain but are mathematical functions
- The magic is in the layered structure allowing hierarchical feature learning
- Each layer transforms representation into slightly more abstract form

### From "Neural Network from Scratch" (Green Code):
- Practical implementation uses numpy for matrix operations
- Forward pass: matrix multiplication + bias + activation
- Even simple 2-layer network can learn XOR problem

---

## Prerequisites

**Required:**
- Linear algebra (matrix multiplication, vectors)
- Basic calculus (functions, derivatives)

**Helpful:**
- Python programming
- Understanding of classification tasks

**Next Steps:**
- [gradient-descent](gradient-descent.md) — How networks learn
- [backpropagation](backpropagation.md) — How gradients flow backward

---

## Cross-References

- **Sources:** 3b1b-ch1 through ch9, neural-network-scratch
- **Related:** markov-chains (different approach to prediction)
- **Applications:** Computer vision, NLP, speech recognition

---

*Synthesized from ~31,000 words of source material*
