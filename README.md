# Query builder bug

https://github.com/supabase/postgrest-py/issues/550


1. Copy `.env.sample` to `.env` and update the values
2. Run `uv sync`
3. Run `uv run main.py`
4. Notice that two conditions (one for each `in_`) are added to the second query
