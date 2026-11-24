# Agent prompts and work lists (copied from the scratchpad of the original PC)

- `trans_prompt_<prefix>.txt` / `verify_prompt_<prefix>.txt`: Haiku translation and Sonnet fact-check instructions per module
  (`trans_prompt_ling.txt` / `verify_prompt_ling.txt` are the templates `scripts/scope/prep_module.sh` copies with sed).
- `lists/`: batch work lists (`<prefix>t<N>.txt` = `slug|ar_file|en_dest`), field-intro specs (`*new.txt`), fact-check lists (`*v_N.txt`).
- Prompts and lists contain absolute scratchpad paths from the original PC (C:\Users\HP\AppData\Local\Temp\claude\...);
  replace them with your own paths. `scripts/scope/prep_module.sh` has the same hard-coded `SP=` path.
- `scripts/scope/waitlist.py` waits until all destination files of a batch list exist (it prepends its own scratchpad path; adjust `SP`).
- Rules in force: one subagent at a time; Haiku translates, Sonnet writes field intros and fact-checks; commit and push after each module.
