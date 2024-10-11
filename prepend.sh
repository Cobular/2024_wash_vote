#!/bin/bash

content_to_prepend='---
layout: ../../components/Prose.astro
---
'

find ./src/pages/positions -name "*.md" -type f | while read file; do
    temp_file=$(mktemp)
    echo "$content_to_prepend" > "$temp_file"
    cat "$file" >> "$temp_file"
    mv "$temp_file" "$file"
done