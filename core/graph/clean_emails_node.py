from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

from core.common.processing_file import ProcessingFile
from core.environment import environment
from core.file_operations.file_writer import read_file, write_string_temp_file
from core.graph import NewsPodcastState


def clean_emails(state: NewsPodcastState):
    print(f"\n🧹 Cleaning files")

    open_api_model = "gpt-4o"
    open_api_key = environment.get_openapi_key()

    llm = ChatOpenAI(model=open_api_model,
                     api_key=open_api_key,
                     temperature=0)

    files_to_clean = state["file_to_clean"]
    files_cleaned = []
    for file in files_to_clean:
        print(f" - load file{file.path}")
        file_content = read_file(file.path)

        print(f" - invoke LLM to perform cleaning")
        result = llm.invoke([SystemMessage(content=cleaning_prompt), HumanMessage(content=file_content)])

        clean_content = result.content

        cleaned_file_path = write_string_temp_file(clean_content)
        print(f"   > clean file wrote to {cleaned_file_path}")

        cleaned_file = ProcessingFile(
            path=cleaned_file_path,
            podcast_id=file.podcast_id
        )

        files_cleaned.append(cleaned_file)

    return {**state, "file_to_convert": files_cleaned}


cleaning_prompt = """
You are an expert HTML content extraction agent specialized in parsing newsletter documents.

## Objective
Your task is to process an input HTML document and extract only the meaningful textual content of the newsletter.

## Rules

### 1. Primary Goal
Extract the main textual content of the newsletter, preserving logical reading order.

### 2. Content to INCLUDE
- Article body text
- Paragraphs (`<p>`)
- Headings (`<h1>`, `<h2>`, `<h3>`, etc.) only if they are part of the article content
- Relevant inline text (e.g., `<span>`, `<strong>`, `<em>`)
- Text inside content sections that contribute to the narrative

### 3. Content to EXCLUDE
- Headers (e.g., logo areas, navigation bars, “view in browser” links)
- Footers (e.g., unsubscribe links, legal disclaimers, addresses)
- Image captions and alt text unless they are clearly part of the article content
- Decorative or layout elements
- Repeated elements (e.g., social media links, buttons like “Read more”)
- Scripts, styles, and metadata
- Hidden elements (e.g., `display: none`)

### 4. Heuristics for Identifying Main Content
- Prefer content within large container blocks (e.g., `<main>`, `<article>`, or dominant `<div>` sections)
- Prioritize areas with the highest density of continuous text
- Ignore sections with many links but little text
- Ignore typical newsletter boilerplate patterns (unsubscribe, privacy policy, etc.)

### 5. Output Requirements
- Return **plain text only**
- Preserve paragraph separation using line breaks
- Maintain original reading order
- Do NOT include HTML tags
- Do NOT include explanations or metadata

### 6. Edge Cases
- If multiple articles exist, extract all of them in order
- If structure is unclear, choose the largest coherent block of meaningful text
- If no meaningful content is found, return an empty string

### 7. Language Preservation
- Keep the original language of the text
- Do not translate or summarize

## Final Constraint
Your output must contain only the cleaned textual content of the newsletter, nothing else.
"""
