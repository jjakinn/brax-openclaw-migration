# Library Inbox

Drop files here for ingestion into the Knowledge Graph.

## Supported Formats

- **Books:** PDF, EPUB, TXT, MD
- **Courses:** MP4, MKV, URL files
- **Videos:** YouTube URLs (paste in text file)
- **Documents:** DOCX, HTML, any text

## How to Ingest

1. Drop file(s) in this folder
2. Tell me: "Process the new book" or "Ingest the library inbox"
3. I'll extract, chunk, tag, and index everything
4. Check `knowledge-graph/indexes/master-catalog.md` for status

## Ingestion Process

```
File → Extract Text → Chunk (500-1000 tokens) → 
Tag Concepts → Update Indexes → Cross-Reference → Store
```

## Token Checkpointing

Large files (300+ page books, 12+ hour courses) will take multiple sessions:
- I work until 78% tokens (~204k)
- Save checkpoint
- Spawn continuation agent
- Resume seamlessly
- You can ask questions anytime about completed portions

## Organization

Processed files remain here as backup. Active content lives in:
- `knowledge-graph/corpus/by-source/`
- `knowledge-graph/summaries/`
- `knowledge-graph/by-concept/`
