---
name: "national-focus-ideas"
description: "Adds ideas/spirits to national focuses in Hearts of Iron IV modding. Invoke when user needs to assign ideas to focuses or create new ideas for focus trees."
---

# National Focus Ideas Manager

## Overview

This skill helps manage the assignment of ideas (national spirits) to national focuses in Hearts of Iron IV modding projects. It ensures proper mapping between focus names and their corresponding ideas.

## Key Features

1. **Assign Ideas to Focuses**: Link existing ideas to national focuses via `completion_reward = { add_ideas = { <idea_id> } }`
2. **Create New Ideas**: Generate new idea definitions with modifiers and icons
3. **Add Localization**: Create Chinese localization for ideas (`_name` and optional `_desc`)
4. **Validation**: Ensure ideas match focus themes (e.g., "小畑机动主义" → "小畑机动主义理论" focus)

## Usage Guidelines

### 1. Assigning Ideas to Focuses

When adding ideas to focuses, ensure the idea theme matches the focus name:

| Focus ID | Focus Name | Appropriate Idea |
|----------|------------|------------------|
| `JAP_obata_mobility_theory` | 小畑机动主义理论 | `JAP_obata_mobility` |
| `JAP_bamboo_spear_doctrine` | 竹枪主义 | `JAP_bamboo_spear_doctrine` |
| `JAP_clarify_the_kokutai` | 阐明国体 | `JAP_imperial_way_jurisprudence` |

### 2. Creating New Ideas

Add ideas to `common/ideas/<file_name>.txt`:

```yaml
JAP_example_idea = {
    on_add = { log = "[GetDateText]: [Root.GetName]: add idea JAP_example_idea"}
    picture = GFX_<icon_name>
    modifier = {
        stability_factor = 0.1
        war_support_factor = 0.05
    }
}
```

### 3. Adding Localization

Add to `localisation/<file_name>_simp_chinese.yml`:

```yaml
JAP_example_idea_name:0 "中文名称"
JAP_example_idea_desc:0 "描述文本（可选）"
```

## Best Practices

1. **Match Theme**: Ideas should thematically match the focus (e.g., "宪兵队之影" focus → "宪兵政治" idea)
2. **Avoid Exact Name Matching**: Ideas don't need exact same name as focus, just related theme
3. **Localization**: Always add `_name` localization; `_desc` is optional
4. **Use Existing Icons**: Reuse existing GFX icons where appropriate

## Error Prevention

- ❌ Don't assign idea to wrong focus (e.g., don't put `JAP_obata_mobility` in `JAP_special_military_operation_manchuria`)
- ❌ Don't add unnecessary `_desc` if user specifies not to
- ❌ Don't use PowerShell for file operations that may cause encoding issues
- ✅ Use `Edit` tool for precise text modifications
- ✅ Verify mappings before finalizing
