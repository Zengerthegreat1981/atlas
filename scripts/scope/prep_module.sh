#!/bin/bash
# usage: prep_module.sh <part> <Label> <prefix> <quota-json> <new-json>
set -e
part="$1"; label="$2"; prefix="$3"; quota="$4"; new="$5"
SP="C:/Users/HP/AppData/Local/Temp/claude/19ef3e7a5f94f486/9f724022-fc83-42d3-8ed5-4fb83c1b342c/scratchpad"
python scripts/select_scope.py "$part" > /dev/null
python scripts/scope/make_scope.py "$part" "$quota" "$new" "$SP" "${prefix}t" 21
sed -e "s/linguistics/$part/g; s/Linguistics/$label/g" "$SP/trans_prompt_ling.txt" > "$SP/trans_prompt_${prefix}.txt"
sed -e "s/linguistics/$part/g; s/LINGUISTICS/$label/g; s/Linguistics/$label/g" "$SP/verify_prompt_ling.txt" > "$SP/verify_prompt_${prefix}.txt"
echo prepared
