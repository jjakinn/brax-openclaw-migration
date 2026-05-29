# Power Apps Full Course - Pragmatic Works (Brian Knight)

**Source:** YouTube Video  
**URL:** https://www.youtube.com/watch?v=rJsHc-4w60g  
**Duration:** 3.5+ hours  
**Instructor:** Brian Knight (Power Apps MVP)  
**Organization:** Pragmatic Works  
**Ingested:** 2026-03-30  
**Transcript Size:** 123KB, 3,324 lines

---

## Course Overview

Comprehensive hands-on workshop covering the full spectrum of Power Platform app development. Builds multiple applications from scratch with real-time Q&A.

## Applications Built

### 1. Dataverse Model-Driven App (Time Card Admin)
- Complete data modeling
- Tables, views, forms creation
- Security and auditing features
- Sample data import from Excel

### 2. Canvas App (Employee Time Entry)
- 4-zone responsive layout
- Galleries and forms
- Lookup columns and relationships
- Formula-driven interactions
- Auto-populating user data

### 3. Power Pages Portal (Bonus)
- External-facing application
- Contractor access without AD accounts

---

## Key Technical Concepts

### Dataverse Fundamentals
- **Tables:** Creating custom tables (always singular naming)
- **Columns:** Data types, auto-numbering, validation rules
- **Relationships:** Lookup columns connecting tables
- **Views:** Filtering, sorting, column selection
- **Forms:** Main forms, field organization, business rules
- **Security:** Row-level, column-level, business unit, hierarchical
- **Auditing:** Built-in change tracking

### Canvas App Architecture
- **Containers:** Vertical/horizontal layout management
- **Responsive Design:** Parent.width patterns
- **Galleries:** Displaying and filtering data
- **Forms:** Edit vs New mode (critical concept)
- **Navigation:** Screen transitions, passing context

### Critical Formula Patterns

**Theme Variables:**
```powerapps
Set(varThemePrimary, RGBA(30, 58, 95, 1));
Set(varThemeSecondary, RGBA(201, 162, 39, 1));
Set(varThemeAccent, RGBA(46, 125, 50, 1));
```

**Filter + Sort Gallery:**
```powerapps
Sort(
    Filter(TimeCards, Project.Project = Gallery1.Selected.Project),
    BillDate, Descending
)
```

**Current User Lookup:**
```powerapps
LookUp(Contacts, Email = User().Email)
```

**Submit Form Pattern:**
```powerapps
SubmitForm(Form1);
Notify("Saved", NotificationType.Success, 2000);
NewForm(Form1)
```

### Common Gotchas & Solutions

**1. "No item to display" Error**
- Cause: Form in Edit mode without selected record
- Fix: Set Form DefaultMode to "New"

**2. Lookup Column Relationships**
- Pattern: `Table.Column` for relationship field
- Pattern: `Table.Column.Column` to access related data

**3. Gallery Template vs Selected**
- Template row: Design-time changes
- Entire gallery: Runtime properties

---

## App Types Explained

| Type | Best For | Data Sources | License |
|------|----------|--------------|---------|
| **Canvas** | Custom UI, 1200+ connectors | Any | Per app/user |
| **Model-Driven** | Data-heavy, forms/lists | Dataverse only | Included |
| **Teams** | Teams-embedded apps | Dataverse (2GB) | Free with Teams |
| **Power Pages** | External portals | Dataverse | Per site |

---

## Key Quotes

> "Canvas apps connect to almost 1,200 data sources."

> "Model-driven apps are best for technically proficient audiences."

> "The form is in edit mode and you haven't told it what row to edit."

> "SubmitForm translates to native queries regardless of data source."

> "One language serves them all."

---

## Related Resources

- Pragmatic Works cheat sheets
- Microsoft Learn documentation
- Power Apps certification (PL-200, PL-400)

---

**Status:** Fully ingested  
**Primary Use:** Power Apps development reference  
**Prerequisites:** None (beginner to advanced)
