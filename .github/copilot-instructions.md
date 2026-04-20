---
name: "Python Comprehensions Learning Project"
description: "Structured self-learning project for mastering Python list/dict comprehensions, generators, and functional programming. Progressive 5-level challenges with pedagogical examples and auto-verified exercises."
applyTo: "**"
---

# Python Comprehensions Learning Project

## Project Overview

This is a **self-directed learning workspace** teaching Python comprehensions, functional programming patterns, and algorithmic thinking through progressive exercises.

**Learning Path**: 
- **basics/**: Foundational patterns (enumerate, filtering, routing)
- **lists/**, **dictionaries/**, **sets/**, **conditionals/**: Topic-focused examples
- **challenges/**: 5-level progression (for-loops → comprehensions → one-liners → no-imports → functional)

**Target Audience**: Self-learner building mastery through hands-on, gradually increasing difficulty.

## Project Structure

```
main.py              # Entry point (simple CLI runner)
practice.py          # Spanish auto-verified exercises with assert feedback
challenges/
  ├── data.py        # Shared test data across levels
  ├── level_1_*.py   # Solve using traditional for loops
  ├── level_2_*.py   # Solve using list/dict comprehensions
  ├── level_3_*.py   # Solve as one-liners (no intermediate variables)
  ├── level_4_*.py   # Solve without importing libraries
  ├── level_5_*.py   # Solve using map/filter/lambda (functional)
  └── solutions/     # Reference implementations (study after solving)
basics/              # Working examples demonstrating patterns
```

## Key Patterns & Conventions

### Challenge Files
- **Placeholders**: Use `___` as exercise placeholders for solutions
- **Comments**: Exercise instructions appear above `___` placeholders
- **Feedback**: Solutions are validated with `assert` statements in dedicated sections
- **Spanish**: Comments and instructions may be in Spanish (practice reading technical Spanish)

### Solutions
- **Reference Quality**: Solutions are clean, Pythonic implementations
- **Study Guide**: Only review AFTER attempting the challenge yourself
- **Patterns**: Reference function names, naming conventions, and algorithm approaches

### Code Style
- **Python 3.12+**: Project targets Python 3.12 and newer
- **No external dependencies**: All challenges solve using stdlib only
- **Comprehensions**: Preferred over imperative loops when readable
- **Functional style**: Encouraged for level 5 (map/filter/lambda)
- **Type hints**: Not required but encouraged for clarity

## Working with Challenges

### Recommended Workflow
1. **Read** the challenge instructions in the file
2. **Replace** `___` with your solution (don't use intermediate variables for level 3+)
3. **Run** the file to verify against assertions
4. **If stuck**: Review the corresponding solution and re-attempt
5. **Progress**: Move to next level only after understanding the pattern

### Running a Challenge
```bash
python challenges/level_1_for_loops.py
python challenges/level_2_comprehensions.py
```

If assertions pass, output is silent. If assertions fail, you'll see the error.

### Checking Solutions
```bash
python challenges/solutions/level_1_solution.py
```

## Agent Guidance

When working on this project:

- **Clarify learning intent**: Ask whether you're solving for the first time, debugging, or analyzing patterns
- **Scaffold progressively**: Don't jump to functional solutions if the challenge is about learning comprehensions
- **Explain comprehensions**: Show *why* comprehensions are preferable (brevity, performance, readability)
- **Encourage Spanish reading**: Point out when comments/instructions contain idiomatic Spanish
- **Avoid spoilers**: If the user is actively solving, offer hints rather than full solutions
- **Compare levels**: Help connect patterns across difficulty levels (how level 1 for-loop becomes level 2 comprehension, then level 5 map/filter)

## Common Development Patterns

### List Comprehension
```python
# Instead of:
result = []
for item in items:
    if condition(item):
        result.append(transform(item))

# Use:
result = [transform(item) for item in items if condition(item)]
```

### Dictionary Comprehension
```python
# Build a dict from lists:
result = {key: value for key, value in zip(keys, values)}

# Build from iterable:
result = {item: process(item) for item in items}
```

### Generators
```python
# Memory-efficient iteration:
gen = (item * 2 for item in range(1000000))  # Not evaluated yet
result = list(gen)  # Only evaluated when consumed
```

### Functional Approach (level 5)
```python
# map/filter/lambda instead of comprehensions:
result = list(map(lambda x: x * 2, filter(lambda x: x > 5, numbers)))
```

## Debugging Tips

- **"Expected vs Actual"**: When assertions fail, modify the assertion temporarily to print both sides
- **Test data**: Check `challenges/data.py` to understand test inputs
- **Compare solutions**: Diff your solution against `solutions/` to spot differences
- **Python REPL**: Use `python -i challenges/level_2_comprehensions.py` to inspect variables after error

## Next Steps After This Project

Once comfortable with comprehensions:
- Study list slicing and advanced unpacking
- Explore itertools, functools for advanced patterns
- Apply comprehensions in real projects (data processing, web scraping)
- Learn generator-based data pipelines

## Project Metadata

- **Python**: 3.12+
- **Dependencies**: None (stdlib only)
- **Duration**: Self-paced, typically 2-4 hours per level
- **Language**: English + Spanish (exercise comments)
