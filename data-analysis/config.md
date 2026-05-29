# Data Analysis — Configuration

## Default Standards

### SQL Style
- CTEs for readability
- Explicit column names (no SELECT *)
- Comments for business logic
- Version controlled queries

### Python Style
- pandas for data manipulation
- matplotlib/seaborn for viz
- jupyter for exploration
- .py files for production

### Metric Contracts
Every KPI must define:
1. **Entity** — What is being counted?
2. **Grain** — One row per what?
3. **Numerator** — The thing being measured
4. **Denominator** — The population (if rate)
5. **Time window** — Rolling or fixed?
6. **Timezone** — Critical for daily metrics
7. **Filters** — What's included/excluded?

## Analysis Checklist

Before starting any analysis:
- [ ] What decision does this support?
- [ ] What would change your mind?
- [ ] Do you have the right data?
- [ ] Is the timeframe appropriate?

After analysis:
- [ ] Sample size sufficient?
- [ ] Comparison groups fair?
- [ ] Effect size meaningful?
- [ ] Uncertainty quantified?

## Output Templates

### Decision Brief
```
ANSWER: [the finding]
EVIDENCE: [the data]
CONFIDENCE: [high/medium/low]
CAVEATS: [limitations]
RECOMMENDATION: [next action]
```

## Common Data Sources

| Source | Location | Access |
|--------|----------|--------|
| Local CSV | `~/data-analysis/datasets/` | Direct |
| SQLite | `*.db` files | sqlite3 |
| PostgreSQL | Configurable | connection string |
| APIs | Via requests | credentials in env |

## Visualization Defaults

### Chart Selection
- **Trends** → Line chart
- **Comparisons** → Bar chart
- **Distributions** → Histogram/box plot
- **Relationships** → Scatter plot
- **Composition** → Stacked bar/pie (use sparingly)
- **Funnels** → Funnel chart
- **Cohorts** → Retention matrix

### Style
- Clear titles
- Axis labels
- Legends when needed
- Annotations for key points

---

*Analysis without a decision is just arithmetic.*
