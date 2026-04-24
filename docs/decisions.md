# Design Decisions

## 01 - Full load vs delta load on bronze tables
**Decision:**
Currently doing a full load of all entities daily for simplicity.

**Reasoning:**
Getting the pipeline working end to end is the priority.
Storage costs are negligible at this scale.

**Known tradeoff:**
Fixtures and teams tables will accumulate redundant rows.
380 fixtures reloaded daily is wasteful when most are unchanged.

**Revisit when:**
Pipeline is stable and running daily. Implement delta loading
for fixtures (only load finished/changed), and consider loading
teams and positions once per season only.