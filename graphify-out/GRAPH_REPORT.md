# Graph Report - remove-political-content-x-  (2026-09-29)

## Corpus Check
- 8 files · ~3,409 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 81 nodes · 103 edges · 8 communities (7 shown, 1 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 20 edges (avg confidence: 0.65)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]

## God Nodes (most connected - your core abstractions)
1. `BridgeClient` - 15 edges
2. `X Political Content & Journalist Purge Engine` - 11 edges
3. `ContentFilter` - 10 edges
4. `main()` - 8 edges
5. `DaemonManager` - 6 edges
6. `FollowingCleaner` - 6 edges
7. `SidebarCrawler` - 6 edges
8. `Getting Started & Usage` - 6 edges
9. `Core Engineering Highlights` - 5 edges
10. `Graphify Knowledge Graph & Codebase Navigation` - 5 edges

## Surprising Connections (you probably didn't know these)
- `FollowingCleaner` --uses--> `BridgeClient`  [INFERRED]
  following_cleaner.py → bridge_client.py
- `SidebarCrawler` --uses--> `BridgeClient`  [INFERRED]
  sidebar_crawler.py → bridge_client.py
- `SidebarCrawler` --uses--> `ContentFilter`  [INFERRED]
  sidebar_crawler.py → filter_rules.py
- `main()` --calls--> `FollowingCleaner`  [INFERRED]
  main.py → following_cleaner.py
- `main()` --calls--> `SidebarCrawler`  [INFERRED]
  main.py → sidebar_crawler.py

## Communities (8 total, 1 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.47
Nodes (3): Recursive Sidebar Recommendation Crawler. Visits target accounts, extracts recom, Executes the BFS recommendation discovery and blocking loop., SidebarCrawler

### Community 1 - "Community 1"
Cohesion: 0.15
Nodes (10): BridgeClient, Resilient client interface for Kimi WebBridge Daemon. Manages HTTP command dispa, Checks if the local WebBridge daemon is active and responding., Checks if the browser extension WebSocket is attached to the daemon., DaemonManager, Daemon lifecycle manager for Kimi WebBridge. Handles independent process startup, Ensures the daemon is listening. Starts it detached if stopped., Waits for the browser extension to connect. (+2 more)

### Community 2 - "Community 2"
Cohesion: 0.20
Nodes (7): ContentFilter, Political and News Content Classification Rules. Provides fast heuristic filteri, Returns True if the handle belongs to the protected tech/creator whitelist., Evaluates whether an account matches political, government, or news media heuris, FollowingCleaner, Following Cleaner Module. Audits the authenticated user's Following list, identi, Iterates over targeted handles and blocks them sequentially.

### Community 3 - "Community 3"
Cohesion: 0.12
Nodes (16): 1. Zero-Credential In-Browser Automation via Kimi WebBridge, 2. Recursive Sidebar Recommendation Crawler (BFS Discovery Loop), 3. Precision Heuristic Classifier & Whitelisting Guardrail, 4. Resilient Multi-Stage DOM Action Pipeline, Codebase Components, code:mermaid (flowchart TD), code:mermaid (sequenceDiagram), code:python (PROTECTED_WHITELIST = {) (+8 more)

### Community 4 - "Community 4"
Cohesion: 0.33
Nodes (3): Dispatches an action payload to the Kimi WebBridge HTTP daemon., Navigates the browser session to the target URL., Evaluates JavaScript asynchronously in the active page context.

### Community 5 - "Community 5"
Cohesion: 0.18
Nodes (11): 1. Prerequisites, 2. Installation, 3. Verify Daemon & Extension Status, 4. Run Recursive Sidebar Crawler, 5. Run Following Purge, code:bash (git clone https://github.com/roshan-pixel/remove-political-c), code:bash (python main.py --mode status), code:block6 ([+] Kimi WebBridge daemon and extension are operational.) (+3 more)

### Community 6 - "Community 6"
Cohesion: 0.33
Nodes (6): code:bash (# Query architectural paths between components), Core Abstractions (God Nodes), Graph Metrics, Graph Queries, Graphify Knowledge Graph & Codebase Navigation, Visual Interactive Graphs

## Knowledge Gaps
- **21 isolated node(s):** `Table of Contents`, `Overview`, `code:mermaid (flowchart TD)`, `1. Zero-Credential In-Browser Automation via Kimi WebBridge`, `2. Recursive Sidebar Recommendation Crawler (BFS Discovery Loop)` (+16 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BridgeClient` connect `Community 1` to `Community 0`, `Community 2`, `Community 4`?**
  _High betweenness centrality (0.179) - this node is a cross-community bridge._
- **Why does `X Political Content & Journalist Purge Engine` connect `Community 3` to `Community 5`, `Community 6`?**
  _High betweenness centrality (0.141) - this node is a cross-community bridge._
- **Why does `ContentFilter` connect `Community 2` to `Community 0`?**
  _High betweenness centrality (0.093) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `BridgeClient` (e.g. with `DaemonManager` and `FollowingCleaner`) actually correct?**
  _`BridgeClient` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 6 inferred relationships involving `ContentFilter` (e.g. with `FollowingCleaner` and `SidebarCrawler`) actually correct?**
  _`ContentFilter` has 6 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `main()` (e.g. with `DaemonManager` and `BridgeClient`) actually correct?**
  _`main()` has 7 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `DaemonManager` (e.g. with `BridgeClient` and `main()`) actually correct?**
  _`DaemonManager` has 2 INFERRED edges - model-reasoned connections that need verification._