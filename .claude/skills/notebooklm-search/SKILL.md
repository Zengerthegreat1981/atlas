---
name: notebooklm-search
description: >
  Search the user's Google NotebookLM notebooks (built from books/PDFs they uploaded) and bring
  the answer back into Claude Code. Works by driving the user's real Chrome browser (via the
  "Claude in Chrome" MCP tools), since NotebookLM has no public API and requires the user's
  logged-in Google session — this only works when running locally on the user's own machine,
  never from a cloud/remote session.
  Use when the user asks to "search NotebookLM", "دور في الكتب/النوتبوك", "اسأل NotebookLM",
  references a specific notebook by name, or asks a question that should be answered from their
  uploaded source books rather than general knowledge.
---

# NotebookLM search via Chrome

The user keeps several research notebooks in Google NotebookLM (notebooklm.google.com), each
built from specific books/PDFs they uploaded. There is no API — the only way in is driving their
real Chrome (already logged into their Google account) with the **Claude in Chrome** MCP tools.

**Precondition:** this only works in a session running on the user's own machine (real Chrome
session). If Claude in Chrome tools aren't available, tell the user this skill needs to run
locally and stop.

## 0. Load the tools

Batch-load in one `ToolSearch` call before doing anything:

```
select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__tabs_close_mcp,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__find
```

## 1. Make sure the right Google account is active

The user has **multiple Google accounts** signed into Chrome. NotebookLM must always be opened
under the account recorded in `.claude/skills/notebooklm-search/config.json`
(`account_email`, e.g. `gmini1762@gmail.com`), never whichever account Google happens to default
to.

Google apps expose this via the `authuser` URL query param (an index into the browser's list of
signed-in Google accounts, e.g. `?authuser=1`). `config.json` also caches the last-known-good
`authuser` index for that email.

Every time you navigate to `notebooklm.google.com` (home page or a specific notebook URL):

1. Append `authuser=<cached index>` as a query param (e.g.
   `https://notebooklm.google.com/notebook/<id>?authuser=1`). If the URL already has other query
   params, add `&authuser=<index>` instead.
2. After the page loads, verify the active account without necessarily clicking anything first:
   use `read_page` (or `find`) to look for the account avatar button in the top-right corner —
   it normally carries an `aria-label`/tooltip like "Google Account: <name> (<email>)". Check the
   email matches `account_email`.
3. **If it matches:** continue — no need to open the switcher.
4. **If it does NOT match (or you can't read the email from the aria-label):** click the avatar
   in the top-right corner to open the account switcher panel, find the row containing
   `account_email` (it's a list of the accounts already signed into this Chrome profile — exactly
   the "pick which Google account" panel the user described), and click it. The page reloads
   under that account, and its URL will now contain the correct `?authuser=N`. Read that value
   back out of the URL and update `authuser` in `config.json` so future runs skip step 4 (unless
   the cached index still turns out wrong, in which case repeat this step).
5. Only once the correct account is confirmed active, proceed to resolve/open the actual
   notebook.

## 2. Resolve which notebook to use

The user has **multiple notebooks**, so a name/topic must be resolved to a specific one each time.

1. Check `.claude/skills/notebooklm-search/registry.json` in this repo for a `title -> url`
   mapping built from previous runs.
2. If the request names a notebook that matches an entry (fuzzy match on title is fine), use that
   URL directly — skip to step 3.
3. Otherwise, open a Chrome tab at `https://notebooklm.google.com` (with `?authuser=` already
   appended per step 1), use `get_page_text` / `read_page` to list the notebook titles on the home
   page, and match against what the user asked for.
   - Exactly one plausible match → use it.
   - Ambiguous or no match → ask the user which notebook they mean (list the titles you found).
4. Whenever you resolve a title to a URL (new or confirmed), write/update it in
   `registry.json` (create the file with `{}` first if missing) so future searches skip the
   listing step. Keep it a flat JSON object of `{ "notebook title": "https://notebooklm.google.com/notebook/...?authuser=N" }`
   — store the URL **with** the correct `authuser` param already on it, so future runs of step 2
   open straight into the right account+notebook without re-deriving it.

## 3. Ask the question in NotebookLM's chat

1. Navigate to the resolved notebook URL (open a new tab rather than hijacking one the user might
   be using).
2. Use `find` to locate the chat/question input (placeholder text like "Ask a question" or "Start
   typing").
3. Type the user's question (translate/rephrase only if needed for clarity — keep their actual
   intent) and submit (Enter or the send button).
4. Wait for the response to finish streaming — poll with `read_page`/`get_page_text` every couple
   of seconds until the answer text stops growing / the generating indicator is gone. Don't wait
   more than ~30s per poll cycle; if it seems stuck, take a screenshot-equivalent (`read_page`) to
   check for an error state.
5. Extract the full answer text, and note any inline citations/source markers NotebookLM shows if
   visible (these tell the user which source book the fact came from).

## 4. Return the result

Default: relay the answer directly in the chat reply, clearly marked as coming from NotebookLM
and which notebook, e.g. "من نوتبوك **<title>** في NotebookLM:". Keep quoting under the usual
copyright limits — summarize NotebookLM's answer rather than reproducing it verbatim at length.

Only write the result to a file in the project instead of (or in addition to) the chat reply when
the user explicitly asks to save it, or when they're clearly doing an ongoing research task where
a running notes file makes sense — in that case ask once where they want it saved (e.g.
`research/notebooklm/<topic>.md`) and reuse that location for the rest of the session.

## 5. Cleanup

Close the tab you opened for the search (`tabs_create_mcp`/`tabs_close_mcp`) unless the user is
clearly going to keep interacting with that notebook themselves.
