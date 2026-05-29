# Power Apps Full Course - Brian Knight (Pragmatic Works)

**Source:** YouTube Video  
**URL:** https://www.youtube.com/watch?v=rJsHc-4w60g  
**Duration:** ~3.5 hours  
**Instructor:** Brian Knight, Power Apps MVP  
**Organization:** Pragmatic Works

---

## Overview

This is a comprehensive, hands-on Power Apps course covering the full spectrum of Power Platform app development. The instructor builds multiple applications from scratch in a live workshop format with real-time Q&A.

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

## Key Technical Concepts Covered

### Dataverse Fundamentals
- **Tables:** Creating custom tables with proper naming (always singular)
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
- **Formulas:** Variables, collections, lookups

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
    Filter(
        TimeCards,
        Project.Project = Gallery1.Selected.Project
    ),
    BillDate,
    Descending
)
```

**Current User Lookup:**
```powerapps
LookUp(
    Contacts,
    Email = User().Email
)
```

**Auto-Default Fields:**
```powerapps
// Date to today
Now()

// Current user
LookUp(Contacts, Email = User().Email)

// Selected project
Gallery1.Selected
```

**Submit Form Pattern:**
```powerapps
// OnSelect of Save Button
SubmitForm(Form1);

// OnSuccess of Form
Notify("Time card saved", NotificationType.Success, 2000);
NewForm(Form1)
```

### Common Gotchas & Solutions

**1. "No item to display" Error**
- Cause: Form in Edit mode without selected record
- Fix: Set Form DefaultMode to "New"

**2. Lookup Column Relationships**
- Pattern: `Table.Column` for the relationship field
- Pattern: `Table.Column.Column` to access related data

**3. Gallery Template vs Selected**
- Template row (first row): Design-time changes
- Entire gallery: Runtime properties

**4. Time Zone Handling**
- Use "Date Only" data type for date columns
- Set "Behavior" to "Date Only" in Advanced options

---

## App Types Explained

| Type | Best For | Data Sources | License |
|------|----------|--------------|---------|
| **Canvas** | Custom UI, 1200+ connectors | Any | Per app/user |
| **Model-Driven** | Data-heavy, forms/lists | Dataverse only | Included |
| **Teams** | Teams-embedded apps | Dataverse (2GB) | Free with Teams |
| **Power Pages** | External portals, websites | Dataverse | Per site |

---

## Advanced Features Mentioned

- **Power Automate Integration:** Workflow triggers
- **Power BI:** Embedded dashboards, ad-hoc reports
- **AI Builder:** Form processing, prediction
- **Business Rules:** Client-side validation without code
- **JavaScript:** Custom web resources
- **Security Roles:** Form-level access control
- **Excel Import/Export:** Bulk data operations
- **Sample Data:** Demo environment setup

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
- On-demand learning platform

---

**Status:** Fully ingested  
**Word Count:** ~45,000 words (transcript)  
**Primary Use:** Power Apps development reference  
**Prerequisites:** None (beginner to advanced)
