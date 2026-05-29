# Synthesis: Bug Bounty Methodology
*Cross-reference from Jason Haddix live recon + application analysis + manual hacking guide*

---

## Philosophy

**Goal:** Find critical vulnerabilities (P1/P2) in programs that pay for responsible disclosure — including "hidden bounties" that don't advertise themselves.

> "There are a class of hidden bounties out there... responsible disclosure programs that pay if you find a critical bug. They're public but they don't really advertise themselves." — *Jason Haddix*

---

## The Methodology: Phase-by-Phase

### Phase 1: Identify Root Domains (Seeds)

**Primary Targets:**
1. Main domain (e.g., officedepot.com)
2. Known subdomains in scope

**Expand via Acquisitions:**
- Tool: **Crunchbase**
- Look for acquisitions < 2 years old (older = less likely to have active infrastructure)
- Check for legacy systems still connected
- Example acquisitions: OfficeMax (2013), CompuCom (2017)

**Why:** Old acquisitions may still have infrastructure with customer data connections

**Command:**
```bash
# Crunchbase lookup for acquisitions
curl -s "https://www.crunchbase.com/organization/{company}/acquisitions"
```

---

### Phase 2: ASN Enumeration (IP Space Discovery)

**What is ASN?**
Autonomous System Number — reference identifier for all registered IP space of an organization.

**Tool:** bgp.he.net
```
Search: officedepot
Result: AS14898 (Office Depot, Inc.)
```

**Extract IP Ranges:**
- Click ASN → See all IPv4 ranges
- Grab ranges for: primary company + recent acquisitions

**Tool:** amass intel
```bash
# Parse certificates from ASN IP space
amass intel -asn 14898
```

**Output:** Additional seed domains found in SSL certificates

**Why it matters:**
> "The more seeds or roots we get, the more subdomains we're able to enumerate. The more websites we find, the more chance we find of getting into their infrastructure." — *Haddix*

---

### Phase 3: Reverse WHOIS (Domain Discovery)

**Tool:** **Waxy** (whoxy.com)

**Method:**
1. Search company name: "office depot"
2. Filter by: Registered Contact → Company Name
3. See all domains registered to same entity

**Fidelity:** Medium
- Returns 100+ domains (may include parked domains)
- Requires manual verification
- API available for automation: `domlink` tool

**Example findings:**
- officemax.com
- maxdepot.com
- school.com (valuable domain)

---

### Phase 4: Ad/Analytics Tracker Mapping

**Tool:** **BuiltWith** (builtwith.com)

**Method:**
1. Search target domain
2. Go to **Relationship Profile** tab
3. Find all sites using same Google Analytics/Ad codes

**Logic:** Same tracker code = same organization

**Example findings for Office Depot:**
- officedepotrewards.com
- elfyourself.com (holiday campaign)
- solutions.officedepot.com
- myworkliferewards.com
- officemaxperks.com

**Automation:**
```bash
# Command-line alternative
getrelationship -domain officedepot.com
```

---

### Phase 5: Subdomain Enumeration (The Big Phase)

**Tool:** **Burp Suite** (prefer v1.7 for this workflow)

**LinkedIn JavaScript Discovery:**
1. Spider target with Burp
2. Look for JavaScript files
3. Parse for API endpoints, subdomains, URLs

**Tools for automation:**
- **amass:** DNS brute forcing, certificate transparency logs, archive scraping
- **subfinder:** Passive subdomain discovery
- **chaos:** ProjectDiscovery subdomain enumeration

**Key mindset:**
> "We're looking for login portals for vendors or partners... any login portal for vendors or partners or whatever is usually interesting." — *Haddix*

---

### Phase 6: Technology Stack Analysis

**Tool:** **Shodan**

**Capabilities:**
- Find specific tech stacks (Apache, Nginx, specific versions)
- Search by headers, banners, response codes
- Find exposed services (databases, admin panels)

**Resources:**
- Shodan ebooks (official search operator guides)
- `shodan.io/search?query=hostname:officedepot.com`

**Example searches:**
```
org:"Office Depot, Inc."
ssl:"Office Depot"
http.title:"Office Depot"
```

---

## Key Techniques Summary

| Technique | Tool | Fidelity | Output |
|-----------|------|----------|--------|
| Acquisitions | Crunchbase | High | New root domains |
| ASN Lookup | bgp.he.net | High | IP ranges |
| Cert Parsing | amass intel | High | Seed domains |
| Reverse WHOIS | whoxy.com | Medium | Domain lists |
| Ad Tracker Mapping | BuiltWith | Medium | Related sites |
| Copyright Search | Google Dorks | Medium | Subdomains |
| JS Discovery | Burp Suite | High | API endpoints |
| Port Scanning | Shodan | High | Exposed services |

---

## Live Recon Workflow (from @ITSecurityGuard)

**Tools:**
- **amass:** Subdomain enumeration
- **FFUF:** Directory/file fuzzing
- **SecurityTrails:** Historical DNS data

**Command chain:**
```bash
# Full recon pipeline
amass enum -d target.com -o domains.txt
subfinder -d target.com -o subdomains.txt
cat domains.txt subdomains.txt | sort -u | httprobe | tee live_hosts.txt
```

---

## Critical Vulnerability Targets

**Priority targets:**
1. **Vendor/Partner portals** — Often less secure than main site
2. **Old acquisitions** — Legacy infrastructure, forgotten systems
3. **API endpoints** — Business logic vulnerabilities
4. **File upload functions** — Remote code execution
5. **Authentication flows** — OAuth, SAML, JWT issues

**Scope tricks:**
- Check if program accepts "at discretion" findings
- Old acquisitions may still process customer data
- Subdomains of acquisitions often in scope

---

## Tools Stack

| Category | Primary | Alternatives |
|----------|---------|--------------|
| Subdomain Enum | amass | subfinder, chaos, assetfinder |
| Visualization | XMind | MindManager, FreeMind |
| Proxy/Spider | Burp Suite | OWASP ZAP, Caido |
| Search Engine | Shodan | Censys, FOFA |
| WHOIS Lookup | whoxy.com | viewdns.info, domlink |
| Tech Detection | BuiltWith | Wappalyzer, WhatWeb |
| Directory Fuzz | FFUF | gobuster, dirsearch |

---

## Prerequisites

**Required:**
- Understanding of DNS, HTTP, SSL/TLS
- Basic command line proficiency
- Familiarity with web application architecture

**Helpful:**
- [osint-5hr-course](osint-5hr-course.md) — The Cyber Mentor's comprehensive OSINT
- [network-security](network-security.md) — Packet analysis, MiTM

**Next Steps:**
- [web-application-security](web-application-security.md) — OWASP Top 10, injection flaws
- [api-security](api-security.md) — REST/GraphQL testing

---

## Key Quotes

> "We're going to do a large scale bounty on this target... the larger we build this scope up, the better it's going to be for us."

> "There are a class of hidden bounties... semi-public bounty programs."

> "Vendor portals, partner portals... usually interesting to me."

---

## Sources

- **Primary:** Jason Haddix — The Bug Hunter's Methodology (1h 54m, 12,600 words)
- **Secondary:** Jason Haddix — Application Analysis (47 min, 7,000 words)
- **Live Demo:** @ITSecurityGuard — Live Recon on Snapchat (1h 42m, 12,900 words)
- **Comprehensive:** JakSec — Manual Hacking Full Guide (1h 26m, 13,700 words)

---

*Synthesized from ~46,000 words of elite bug bounty methodology*
