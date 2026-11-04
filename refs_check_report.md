# 删除前的引用检查

检查对象：删除集 = §A ∪ §B 去掉 §C（被排除项），共 **3025** 个文件；存活集 = 本 mod 其余全部文件（41988 个）。

## 概览

| 项目 | 数量 |
|---|---|
| 删除集文件 | 3025 |
| 删除集里的 .gfx | 123 |
| 删除集里的图片 | 2729 |
| 删除集 .gfx 注册的 sprite 条数 | 8649 |
| **被存活文件引用、不能删的 sprite** | **660** |
| 这些 sprite 落在的 .gfx 文件数 | 42 |
| **被存活文件引用、不能删的图片** | **586** |
| 引用它们的存活文件数 | 91 |
| 坏注册块（name 被截断，如 `GFX_`） | 157 |

说明：sprite 若在存活 .gfx 里也有同名定义，则不算冲突（已排除）；图片按路径字符串匹配（含存活 .gfx 的 texturefile/mask 行）。name 长度 ≤5 的块（例如整段被截断成 `GFX_`）单独列在下面，不计入上面的“不能删”统计。

## 不能删的注册块（按 .gfx 分组）

### `interface/focus-VNQ_2_customicons.gfx` — 需保留 95 块 / 共 190 块

- 行 2–5，`GFX_VNQ_2_promote_nationalist_clubs-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_promote_nationalist_clubs-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_promote_nationalist_clubs-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:327`

- 行 40–43，`GFX_VNQ_2_paternalist_outlook-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_paternalist_outlook-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_paternalist_outlook-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:345`

- 行 78–81，`GFX_VNQ_2_vietnamschiang-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_vietnamschiang-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_vietnamschiang-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:368`

- 行 116–119，`GFX_VNQ_2_pragmatic_economics-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_pragmatic_economics-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_pragmatic_economics-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:387`

- 行 154–157，`GFX_VNQ_2_an_economic_consensus-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_an_economic_consensus-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_an_economic_consensus-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:413`

- 行 192–195，`GFX_VNQ_2_strengthen_the_nvbis-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_strengthen_the_nvbis-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_strengthen_the_nvbis-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:432`

- 行 230–233，`GFX_VNQ_2_the_human_spirit_of_revolution-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_the_human_spirit_of_revolution-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_the_human_spirit_of_revolution-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:455`

- 行 268–271，`GFX_VNQ_2_organize_the_viet_duy_dan_dang-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_organize_the_viet_duy_dan_dang-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_organize_the_viet_duy_dan_dang-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:471`

- 行 306–309，`GFX_VNQ_2_thai_hoc_holds-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_thai_hoc_holds-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_thai_hoc_holds-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:491`

- 行 344–347，`GFX_VNQ_2_consolidate_grassroots_policies-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_consolidate_grassroots_policies-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_consolidate_grassroots_policies-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:510`

- 行 382–385，`GFX_VNQ_2_anti_vietminh_campaigns-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_anti_vietminh_campaigns-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_anti_vietminh_campaigns-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:529`

- 行 420–423，`GFX_VNQ_2_a_new_manifesto-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_a_new_manifesto-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_a_new_manifesto-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:548`

- 行 458–461，`GFX_VNQ_2_the_socialist_market_economy-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_the_socialist_market_economy-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_the_socialist_market_economy-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:564`

- 行 496–499，`GFX_VNQ_2_pragmatism-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_pragmatism-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_pragmatism-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:592`

- 行 534–537，`GFX_VNQ_2_victory_of_the_jingwei_faction-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_victory_of_the_jingwei_faction-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_victory_of_the_jingwei_faction-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:619`

- 行 572–575，`GFX_VNQ_2_reach_out_to_the_peasants-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_reach_out_to_the_peasants-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_reach_out_to_the_peasants-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:638`

- 行 610–613，`GFX_VNQ_2_welfare_for_all-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_welfare_for_all-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_welfare_for_all-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:656`

- 行 648–651，`GFX_VNQ_2_abolish_monopolies-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_abolish_monopolies-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_abolish_monopolies-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:673`

- 行 686–689，`GFX_VNQ_2_political_tutelage-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_political_tutelage-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_political_tutelage-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:691`

- 行 724–727，`GFX_VNQ_2_tear_down_the_syndicates-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_tear_down_the_syndicates-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_tear_down_the_syndicates-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:710`

- 行 762–765，`GFX_VNQ_2_takesomeleavesome-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_takesomeleavesome-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_takesomeleavesome-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:734`

- 行 800–803，`GFX_VNQ_2_loyalty_to_vietnam-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_loyalty_to_vietnam-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_loyalty_to_vietnam-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:759`

- 行 838–841，`GFX_VNQ_2_the_basics_of_humanity-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_the_basics_of_humanity-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_the_basics_of_humanity-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:775`

- 行 876–879，`GFX_VNQ_2_build_the_collective_strength-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_build_the_collective_strength-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_build_the_collective_strength-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:791`

- 行 914–917，`GFX_VNQ_2_reforming_the_party-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_reforming_the_party-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_reforming_the_party-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:809`

- 行 952–955，`GFX_VNQ_2_destroy_the_old_elites-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_destroy_the_old_elites-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_destroy_the_old_elites-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:825`

- 行 990–993，`GFX_VNQ_2_promote_land_reform-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_promote_land_reform-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_promote_land_reform-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:843`

- 行 1028–1031，`GFX_VNQ_2_legacy_of_the_nam_dong_commune-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_legacy_of_the_nam_dong_commune-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_legacy_of_the_nam_dong_commune-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:859`

- 行 1066–1069，`GFX_VNQ_2_national_heroism-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_national_heroism-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_national_heroism-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:877`

- 行 1104–1107，`GFX_VNQ_2_unify_nationalist_organizations-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_unify_nationalist_organizations-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_unify_nationalist_organizations-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:896`

- 行 1142–1145，`GFX_VNQ_2_nrav_supremacy-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_nrav_supremacy-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_nrav_supremacy-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:915`

- 行 1180–1183，`GFX_VNQ_2_social_realism-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_social_realism-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_social_realism-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:933`

- 行 1218–1221，`GFX_VNQ_2_transform_agricultural_communes-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_transform_agricultural_communes-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_transform_agricultural_communes-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:949`

- 行 1256–1259，`GFX_VNQ_2_expandtulucvandoan-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_expandtulucvandoan-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_expandtulucvandoan-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:995`

- 行 1294–1297，`GFX_VNQ_2_learnfromchausrepublicanism-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_learnfromchausrepublicanism-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_learnfromchausrepublicanism-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1012`

- 行 1332–1335，`GFX_VNQ_2_uphold_the_caravelle_manifesto-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_uphold_the_caravelle_manifesto-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_uphold_the_caravelle_manifesto-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1031`

- 行 1370–1373，`GFX_VNQ_2_promotion_of_equality-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_promotion_of_equality-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_promotion_of_equality-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1049`

- 行 1408–1411，`GFX_VNQ_2_unity_is_our_strength-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_unity_is_our_strength-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_unity_is_our_strength-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1066`

- 行 1446–1449，`GFX_VNQ_2_cut_out_tu_anh-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_cut_out_tu_anh-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_cut_out_tu_anh-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1082`

- 行 1484–1487，`GFX_VNQ_2_in_honour_of_phan_boi_chau-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_in_honour_of_phan_boi_chau-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_in_honour_of_phan_boi_chau-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1102`

- 行 1522–1525，`GFX_VNQ_2_treasury_bonds-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_treasury_bonds-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_treasury_bonds-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1120`

- 行 1560–1563，`GFX_VNQ_2_food_surplus-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_food_surplus-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_food_surplus-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1138`

- 行 1598–1601，`GFX_VNQ_2_encourage_commercialism-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_encourage_commercialism-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_encourage_commercialism-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1156`

- 行 1636–1639，`GFX_VNQ_2_revolutionaryoligarchy-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_revolutionaryoligarchy-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_revolutionaryoligarchy-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1184`

- 行 1674–1677，`GFX_VNQ_2_the_star_and_the_sun-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_the_star_and_the_sun-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_the_star_and_the_sun-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1204`

- 行 1712–1715，`GFX_VNQ_2_reach_out_to_radicals_in_shanghai-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_reach_out_to_radicals_in_shanghai-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_reach_out_to_radicals_in_shanghai-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1224`

- 行 1750–1753，`GFX_VNQ_2_meeting_of_the_national_congress-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_meeting_of_the_national_congress-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_meeting_of_the_national_congress-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1244`

- 行 1788–1791，`GFX_VNQ_2_ultra_nationalist_victory-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_ultra_nationalist_victory-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_ultra_nationalist_victory-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1264`

- 行 1826–1829，`GFX_VNQ_2_purist_of_the_purist-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_purist_of_the_purist-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_purist_of_the_purist-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1283`

- 行 1864–1867，`GFX_VNQ_2_the_question_of_tutelage-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_the_question_of_tutelage-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_the_question_of_tutelage-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1301`

- 行 1902–1905，`GFX_VNQ_2_expropriate_the_landlords-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_expropriate_the_landlords-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_expropriate_the_landlords-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1317`

- 行 1940–1943，`GFX_VNQ_2_continue_the_democracy_express-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_continue_the_democracy_express-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_continue_the_democracy_express-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1333`

- 行 1978–1981，`GFX_VNQ_2_corporatist_controls-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_corporatist_controls-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_corporatist_controls-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1355`

- 行 2016–2019，`GFX_VNQ_2_secure_rubber_resources-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_secure_rubber_resources-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_secure_rubber_resources-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1375`

- 行 2054–2057，`GFX_VNQ_2_ports_on_the_mekong-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_ports_on_the_mekong-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_ports_on_the_mekong-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1398`

- 行 2092–2095，`GFX_VNQ_2_tamsbenevolence-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_tamsbenevolence-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_tamsbenevolence-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1484`

- 行 2130–2133，`GFX_VNQ_2_unemployment_reduction-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_unemployment_reduction-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_unemployment_reduction-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1503`

- 行 2168–2171，`GFX_VNQ_2_slay_the_russian_beast-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_slay_the_russian_beast-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_slay_the_russian_beast-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1522`

- 行 2206–2209，`GFX_VNQ_2_unitedandfree-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_unitedandfree-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_unitedandfree-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1545`

- 行 2244–2247，`GFX_VNQ_2_greater_dai_viet-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_greater_dai_viet-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_greater_dai_viet-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1563`

- 行 2282–2285，`GFX_VNQ_2_call_upon_the_youth-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_call_upon_the_youth-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_call_upon_the_youth-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1580`

- 行 2320–2323，`GFX_VNQ_2_intellectual_patriotism-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_intellectual_patriotism-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_intellectual_patriotism-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1596`

- 行 2358–2361，`GFX_VNQ_2_new_phung_hoa-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_new_phung_hoa-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_new_phung_hoa-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1612`

- 行 2396–2399，`GFX_VNQ_2_join_our_nvbis-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_join_our_nvbis-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_join_our_nvbis-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1628`

- 行 2434–2437，`GFX_VNQ_2_thenationunited-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_thenationunited-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_thenationunited-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1645`

- 行 2472–2475，`GFX_VNQ_2_push_back_against_syndicalism-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_push_back_against_syndicalism-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_push_back_against_syndicalism-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1665`

- 行 2510–2513，`GFX_VNQ_2_exploitationbegone-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_exploitationbegone-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_exploitationbegone-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1682`

- 行 2548–2551，`GFX_VNQ_2_letitend-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_letitend-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_letitend-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1698`

- 行 2586–2589，`GFX_VNQ_2_it_has_only_begun-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_it_has_only_begun-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_it_has_only_begun-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1715`

- 行 2624–2627，`GFX_VNQ_2_antigerman_propaganda-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_antigerman_propaganda-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_antigerman_propaganda-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1734`

- 行 2662–2665，`GFX_VNQ_2_align_with_the_national_socialists-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_align_with_the_national_socialists-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_align_with_the_national_socialists-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1750`

- 行 2700–2703，`GFX_VNQ_2_vietnamsnewera-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_vietnamsnewera-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_vietnamsnewera-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1773`

- 行 2738–2741，`GFX_VNQ_2_the_fist_smashes_our_enemies-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_the_fist_smashes_our_enemies-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_the_fist_smashes_our_enemies-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1793`

- 行 2776–2779，`GFX_VNQ_2_encourage_class_collaboration-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_encourage_class_collaboration-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_encourage_class_collaboration-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1809`

- 行 2814–2817，`GFX_VNQ_2_vietnamsdemocraticera-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_vietnamsdemocraticera-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_vietnamsdemocraticera-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1826`

- 行 2852–2855，`GFX_VNQ_2_a_land_of_riches-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_a_land_of_riches-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_a_land_of_riches-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1842`

- 行 2890–2893，`GFX_VNQ_2_the_revolution_is_ours-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_the_revolution_is_ours-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_the_revolution_is_ours-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1861`

- 行 2928–2931，`GFX_VNQ_2_economic_miracle-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_economic_miracle-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_economic_miracle-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1883`

- 行 2966–2969，`GFX_VNQ_2_the_republic_shall_live_on-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_the_republic_shall_live_on-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_the_republic_shall_live_on-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1901`

- 行 3004–3007，`GFX_VNQ_2_haithanslegacy-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_haithanslegacy-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_haithanslegacy-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1920`

- 行 3042–3045，`GFX_VNQ_2_our_first_election-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_our_first_election-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_our_first_election-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1939`

- 行 3080–3083，`GFX_VNQ_2_vietnam_on_the_world_stage-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_vietnam_on_the_world_stage-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_vietnam_on_the_world_stage-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1955`

- 行 3118–3121，`GFX_VNQ_2_seeking_friends-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_seeking_friends-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_seeking_friends-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1972`

- 行 3156–3159，`GFX_VNQ_2_uniting_indochina-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_uniting_indochina-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_uniting_indochina-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:1988`

- 行 3194–3197，`GFX_VNQ_2_saving_asia_from_imperialism_and_syndicalism-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_saving_asia_from_imperialism_and_syndicalism-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_saving_asia_from_imperialism_and_syndicalism-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:2018`

- 行 3232–3235，`GFX_VNQ_2_ultranationalist_expansion-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_ultranationalist_expansion-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_ultranationalist_expansion-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:2038`

- 行 3270–3273，`GFX_VNQ_2_secure_the_peninsula-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_secure_the_peninsula-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_secure_the_peninsula-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:2055`

- 行 3308–3311，`GFX_VNQ_2_saving_the_chinese_revolution-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_saving_the_chinese_revolution-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_saving_the_chinese_revolution-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:2083`

- 行 3346–3349，`GFX_VNQ_2_defend_against_japanese_imperialism-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_defend_against_japanese_imperialism-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_defend_against_japanese_imperialism-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:2099`

- 行 3384–3387，`GFX_VNQ_2_burn_bangkok-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_burn_bangkok-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_burn_bangkok-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:2115`

- 行 3422–3425，`GFX_VNQ_2_strangle_the_burmese_python-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_strangle_the_burmese_python-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_strangle_the_burmese_python-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:2146`

- 行 3460–3463，`GFX_VNQ_2_our_chinese_claims-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_our_chinese_claims-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_our_chinese_claims-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:2171`

- 行 3498–3501，`GFX_VNQ_2_south_east_asia_shall_fall-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_south_east_asia_shall_fall-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_south_east_asia_shall_fall-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:2196`

- 行 3536–3539，`GFX_VNQ_2_vietnamesepeopleunite-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_vietnamesepeopleunite-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_vietnamesepeopleunite-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:2213`

- 行 3574–3577，`GFX_VNQ_2_destroy_the_asian_syndicalists-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_2_destroy_the_asian_syndicalists-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_2_destroy_the_asian_syndicalists-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:2229`

### `interface/focus-JAPCOMMUNIST_customicons.gfx` — 需保留 92 块 / 共 184 块

- 行 2–5，`GFX_JAPCOMMUNIST_struggle_of_the_literary_left-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_struggle_of_the_literary_left-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_struggle_of_the_literary_left-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1469`

- 行 40–43，`GFX_JAPCOMMUNIST_the_struggle_of_2-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_the_struggle_of_2-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_the_struggle_of_2-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1490`

- 行 78–81，`GFX_JAPCOMMUNIST_strengthening_the_ideological_united_front-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_strengthening_the_ideological_united_front-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_strengthening_the_ideological_united_front-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1505`

- 行 116–119，`GFX_JAPCOMMUNIST_militant_syndicalists_take_over_the_party-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_militant_syndicalists_take_over_the_party-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_militant_syndicalists_take_over_the_party-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1521`

- 行 154–157，`GFX_JAPCOMMUNIST_the_joint_rural_struggle-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_the_joint_rural_struggle-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_the_joint_rural_struggle-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1537`

- 行 192–195，`GFX_JAPCOMMUNIST_securing_the_state-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_securing_the_state-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_securing_the_state-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1558`

- 行 230–233，`GFX_JAPCOMMUNIST_promoting_the_social_revolution-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_promoting_the_social_revolution-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_promoting_the_social_revolution-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1577`

- 行 268–271，`GFX_JAPCOMMUNIST_question_of_the_emperor-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_question_of_the_emperor-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_question_of_the_emperor-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1598`

- 行 306–309，`GFX_JAPCOMMUNIST_reach_out_to_the_workers-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_reach_out_to_the_workers-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_reach_out_to_the_workers-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1617`

- 行 344–347，`GFX_JAPCOMMUNIST_antiimperialist_rationalization-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_antiimperialist_rationalization-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_antiimperialist_rationalization-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1636`

- 行 382–385，`GFX_JAPCOMMUNIST_legacy_of_the_new_men_society-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_legacy_of_the_new_men_society-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_legacy_of_the_new_men_society-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1655`

- 行 420–423，`GFX_JAPCOMMUNIST_socialism_in_one_country-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_socialism_in_one_country-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_socialism_in_one_country-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1674`

- 行 458–461，`GFX_JAPCOMMUNIST_denounce_the_liberal_menace-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_denounce_the_liberal_menace-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_denounce_the_liberal_menace-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1695`

- 行 496–499，`GFX_JAPCOMMUNIST_mobilise_the_masses-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_mobilise_the_masses-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_mobilise_the_masses-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1714`

- 行 534–537，`GFX_JAPCOMMUNIST_a_revolution_under_party_control-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_a_revolution_under_party_control-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_a_revolution_under_party_control-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1735`

- 行 572–575，`GFX_JAPCOMMUNIST_promote_the_student_labour_society-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_promote_the_student_labour_society-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_promote_the_student_labour_society-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1754`

- 行 610–613，`GFX_JAPCOMMUNIST_increase_the_peasant_livelihood-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_increase_the_peasant_livelihood-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_increase_the_peasant_livelihood-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1775`

- 行 648–651，`GFX_JAPCOMMUNIST_unification_of_the_trade_unions-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_unification_of_the_trade_unions-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_unification_of_the_trade_unions-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1796`

- 行 686–689，`GFX_JAPCOMMUNIST_invigorate_the_three_stage_program-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_invigorate_the_three_stage_program-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_invigorate_the_three_stage_program-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1818`

- 行 724–727，`GFX_JAPCOMMUNIST_therevolutionsnewhome-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_therevolutionsnewhome-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_therevolutionsnewhome-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1836`

- 行 762–765，`GFX_JAPCOMMUNIST_changingthecourseofjapansproletariat-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_changingthecourseofjapansproletariat-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_changingthecourseofjapansproletariat-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1871`

- 行 800–803，`GFX_JAPCOMMUNIST_paris_syndicalists_secure_the_party-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_paris_syndicalists_secure_the_party-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_paris_syndicalists_secure_the_party-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1887`

- 行 838–841，`GFX_JAPCOMMUNIST_international_contacts-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_international_contacts-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_international_contacts-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1903`

- 行 876–879，`GFX_JAPCOMMUNIST_representing_all_the_workers_unions-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_representing_all_the_workers_unions-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_representing_all_the_workers_unions-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1928`

- 行 914–917，`GFX_JAPCOMMUNIST_legacy_of_japanese_syndicalism-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_legacy_of_japanese_syndicalism-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_legacy_of_japanese_syndicalism-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1950`

- 行 952–955，`GFX_JAPCOMMUNIST_foreverapartyforeverarevolution-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_foreverapartyforeverarevolution-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_foreverapartyforeverarevolution-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1970`

- 行 990–993，`GFX_JAPCOMMUNIST_revive_the_labourliberty_society-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_revive_the_labourliberty_society-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_revive_the_labourliberty_society-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1991`

- 行 1028–1031，`GFX_JAPCOMMUNIST_question_of_the_socialreactionaries-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_question_of_the_socialreactionaries-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_question_of_the_socialreactionaries-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2011`

- 行 1066–1069，`GFX_JAPCOMMUNIST_denounce_fukumotoism-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_denounce_fukumotoism-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_denounce_fukumotoism-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2036`

- 行 1104–1107，`GFX_JAPCOMMUNIST_appealing_for_3rd_internationale_support-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_appealing_for_3rd_internationale_support-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_appealing_for_3rd_internationale_support-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2058`

- 行 1142–1145，`GFX_JAPCOMMUNIST_universal_suffrage-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_universal_suffrage-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_universal_suffrage-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2094`

- 行 1180–1183，`GFX_JAPCOMMUNIST_a_general_strike_for_the_proletarian-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_a_general_strike_for_the_proletarian-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_a_general_strike_for_the_proletarian-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2113`

- 行 1218–1221，`GFX_JAPCOMMUNIST_formthekantowomensleague-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_formthekantowomensleague-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_formthekantowomensleague-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2134`

- 行 1256–1259，`GFX_JAPCOMMUNIST_legacy_of_the_farm_labour_party-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_legacy_of_the_farm_labour_party-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_legacy_of_the_farm_labour_party-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2156`

- 行 1294–1297，`GFX_JAPCOMMUNIST_the_red_banner_over_tokyo-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_the_red_banner_over_tokyo-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_the_red_banner_over_tokyo-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2177`

- 行 1332–1335，`GFX_JAPCOMMUNIST_found_the_national_pioneer_association-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_found_the_national_pioneer_association-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_found_the_national_pioneer_association-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2197`

- 行 1370–1373，`GFX_JAPCOMMUNIST_honour_the_martyrs_of_the_revolution-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_honour_the_martyrs_of_the_revolution-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_honour_the_martyrs_of_the_revolution-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2218`

- 行 1408–1411，`GFX_JAPCOMMUNIST_dealing_with_the_emperor-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_dealing_with_the_emperor-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_dealing_with_the_emperor-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2239`

- 行 1446–1449，`GFX_JAPCOMMUNIST_strengthen_old_guard_influence-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_strengthen_old_guard_influence-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_strengthen_old_guard_influence-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2260`

- 行 1484–1487，`GFX_JAPCOMMUNIST_promotion_of_revolutionary_marxism-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_promotion_of_revolutionary_marxism-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_promotion_of_revolutionary_marxism-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2281`

- 行 1522–1525，`GFX_JAPCOMMUNIST_a_new_form_of_socialist_unity-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_a_new_form_of_socialist_unity-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_a_new_form_of_socialist_unity-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2300`

- 行 1560–1563，`GFX_JAPCOMMUNIST_birth_of_the_proletarian_youth_league-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_birth_of_the_proletarian_youth_league-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_birth_of_the_proletarian_youth_league-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2331`

- 行 1598–1601，`GFX_JAPCOMMUNIST_akahata_no_uta-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_akahata_no_uta-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_akahata_no_uta-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2350`

- 行 1636–1639，`GFX_JAPCOMMUNIST_purge_the_antiproletarian_factions-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_purge_the_antiproletarian_factions-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_purge_the_antiproletarian_factions-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2369`

- 行 1674–1677，`GFX_JAPCOMMUNIST_kenzossyndicalistdream-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_kenzossyndicalistdream-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_kenzossyndicalistdream-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2390`

- 行 1712–1715，`GFX_JAPCOMMUNIST_yamakawasrevolution-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_yamakawasrevolution-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_yamakawasrevolution-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2421`

- 行 1750–1753，`GFX_JAPCOMMUNIST_marching_for_the_true_proletariat-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_marching_for_the_true_proletariat-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_marching_for_the_true_proletariat-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2452`

- 行 1788–1791，`GFX_JAPCOMMUNIST_embracing_smiling_communism-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_embracing_smiling_communism-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_embracing_smiling_communism-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2468`

- 行 1826–1829，`GFX_JAPCOMMUNIST_a_struggle_against_spies-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_a_struggle_against_spies-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_a_struggle_against_spies-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2484`

- 行 1864–1867，`GFX_JAPCOMMUNIST_reach_out_to_the_masses-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_reach_out_to_the_masses-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_reach_out_to_the_masses-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2505`

- 行 1902–1905，`GFX_JAPCOMMUNIST_outsidethenationsborders-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_outsidethenationsborders-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_outsidethenationsborders-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2526`

- 行 1940–1943，`GFX_JAPCOMMUNIST_agitative_propaganda-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_agitative_propaganda-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_agitative_propaganda-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2547`

- 行 1978–1981，`GFX_JAPCOMMUNIST_revolutionary_intellectualism-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_revolutionary_intellectualism-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_revolutionary_intellectualism-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2569`

- 行 2016–2019，`GFX_JAPCOMMUNIST_founding_of_the_industrial_labour_institute-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_founding_of_the_industrial_labour_institute-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_founding_of_the_industrial_labour_institute-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2590`

- 行 2054–2057，`GFX_JAPCOMMUNIST_promoting_socialist_feminism-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_promoting_socialist_feminism-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_promoting_socialist_feminism-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2611`

- 行 2092–2095，`GFX_JAPCOMMUNIST_upholding_true_leninism-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_upholding_true_leninism-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_upholding_true_leninism-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2630`

- 行 2130–2133，`GFX_JAPCOMMUNIST_cherry_blossoms_died_red-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_cherry_blossoms_died_red-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_cherry_blossoms_died_red-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2652`

- 行 2168–2171，`GFX_JAPCOMMUNIST_form_the_investigation_committee-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_form_the_investigation_committee-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_form_the_investigation_committee-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2673`

- 行 2206–2209，`GFX_JAPCOMMUNIST_formation_of_a_grass_roots_faction-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_formation_of_a_grass_roots_faction-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_formation_of_a_grass_roots_faction-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2695`

- 行 2244–2247，`GFX_JAPCOMMUNIST_proper_party_reconstruction-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_proper_party_reconstruction-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_proper_party_reconstruction-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2711`

- 行 2282–2285，`GFX_JAPCOMMUNIST_proletarian_papers-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_proletarian_papers-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_proletarian_papers-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2732`

- 行 2320–2323，`GFX_JAPCOMMUNIST_revive_akahata-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_revive_akahata-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_revive_akahata-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2751`

- 行 2358–2361，`GFX_JAPCOMMUNIST_support_okinawan_independence-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_support_okinawan_independence-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_support_okinawan_independence-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2770`

- 行 2396–2399，`GFX_JAPCOMMUNIST_scientific_socialist_outlook-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_scientific_socialist_outlook-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_scientific_socialist_outlook-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2807`

- 行 2434–2437，`GFX_JAPCOMMUNIST_emphasis_on_theory-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_emphasis_on_theory-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_emphasis_on_theory-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2828`

- 行 2472–2475，`GFX_JAPCOMMUNIST_revolutionary_bureaucracy-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_revolutionary_bureaucracy-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_revolutionary_bureaucracy-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2849`

- 行 2510–2513，`GFX_JAPCOMMUNIST_control_the_political_line-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_control_the_political_line-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_control_the_political_line-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2871`

- 行 2548–2551，`GFX_JAPCOMMUNIST_focus_on_self_reliance-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_focus_on_self_reliance-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_focus_on_self_reliance-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2890`

- 行 2586–2589，`GFX_JAPCOMMUNIST_defendingthepeoplesinterests-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_defendingthepeoplesinterests-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_defendingthepeoplesinterests-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2911`

- 行 2624–2627，`GFX_JAPCOMMUNIST_legacy_of_the_action_group-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_legacy_of_the_action_group-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_legacy_of_the_action_group-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2931`

- 行 2662–2665，`GFX_JAPCOMMUNIST_longing_for_armed_struggle-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_longing_for_armed_struggle-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_longing_for_armed_struggle-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2952`

- 行 2700–2703，`GFX_JAPCOMMUNIST_a_revolutionary_research_cult-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_a_revolutionary_research_cult-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_a_revolutionary_research_cult-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2973`

- 行 2738–2741，`GFX_JAPCOMMUNIST_question_of_the_royal_family-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_question_of_the_royal_family-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_question_of_the_royal_family-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:2992`

- 行 2776–2779，`GFX_JAPCOMMUNIST_enforce_democratic_centralism-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_enforce_democratic_centralism-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_enforce_democratic_centralism-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3011`

- 行 2814–2817，`GFX_JAPCOMMUNIST_promoting_a_true_party_of_the_masses-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_promoting_a_true_party_of_the_masses-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_promoting_a_true_party_of_the_masses-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3030`

- 行 2852–2855，`GFX_JAPCOMMUNIST_denounce_the_yamakawaists-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_denounce_the_yamakawaists-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_denounce_the_yamakawaists-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3049`

- 行 2890–2893，`GFX_JAPCOMMUNIST_the_rising_sun_under_the_hammer_and_sickle-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_the_rising_sun_under_the_hammer_and_sickle-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_the_rising_sun_under_the_hammer_and_sickle-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3070`

- 行 2928–2931，`GFX_JAPCOMMUNIST_victory_of_the_communist_hardliners-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_victory_of_the_communist_hardliners-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_victory_of_the_communist_hardliners-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3112`

- 行 2966–2969，`GFX_JAPCOMMUNIST_realisation_of_2_staged_revolution-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_realisation_of_2_staged_revolution-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_realisation_of_2_staged_revolution-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3128`

- 行 3004–3007，`GFX_JAPCOMMUNIST_japanslenin-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_japanslenin-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_japanslenin-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3147`

- 行 3042–3045，`GFX_JAPCOMMUNIST_a_struggle_against_socialreactionarism-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_a_struggle_against_socialreactionarism-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_a_struggle_against_socialreactionarism-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3170`

- 行 3080–3083，`GFX_JAPCOMMUNIST_remove_the_stain_of_feudalism-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_remove_the_stain_of_feudalism-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_remove_the_stain_of_feudalism-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3196`

- 行 3118–3121，`GFX_JAPCOMMUNIST_denounce_the_syndicalist_revisionists-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_denounce_the_syndicalist_revisionists-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_denounce_the_syndicalist_revisionists-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3218`

- 行 3156–3159，`GFX_JAPCOMMUNIST_injecting_the_marxist_conscious-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_injecting_the_marxist_conscious-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_injecting_the_marxist_conscious-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3240`

- 行 3194–3197，`GFX_JAPCOMMUNIST_promoting_a_writers_revolution-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_promoting_a_writers_revolution-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_promoting_a_writers_revolution-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3261`

- 行 3232–3235，`GFX_JAPCOMMUNIST_red_intellectuals-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_red_intellectuals-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_red_intellectuals-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3282`

- 行 3270–3273，`GFX_JAPCOMMUNIST_glory_under_the_vanguard_party-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_glory_under_the_vanguard_party-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_glory_under_the_vanguard_party-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3301`

- 行 3308–3311，`GFX_JAPCOMMUNIST_crush_yamakawa-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_crush_yamakawa-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_crush_yamakawa-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3320`

- 行 3346–3349，`GFX_JAPCOMMUNIST_peasant_collaboration-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_peasant_collaboration-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_peasant_collaboration-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3341`

- 行 3384–3387，`GFX_JAPCOMMUNIST_a_japanese_renaissance-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_a_japanese_renaissance-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_a_japanese_renaissance-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3362`

- 行 3422–3425，`GFX_JAPCOMMUNIST_a_japanese_cultural_revolution-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_a_japanese_cultural_revolution-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_a_japanese_cultural_revolution-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3381`

- 行 3460–3463，`GFX_JAPCOMMUNIST_true_japanese_communism-248360`

```
	SpriteType = { 
		name = "GFX_JAPCOMMUNIST_true_japanese_communism-248360"
		texturefile = "gfx/interface/goals/GFX_JAPCOMMUNIST_true_japanese_communism-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3402`

### `interface/focus-SQI_customicons.gfx` — 需保留 58 块 / 共 116 块

- 行 2–5，`GFX_SQI_the_shandong_takeover-248360`

```
	SpriteType = { 
		name = "GFX_SQI_the_shandong_takeover-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_the_shandong_takeover-248360.dds"
	}
```

  被引用：`SAVE_/Fengtian.txt:4452`、`common/national_focus/Fengtian.txt:4478`、`common/national_focus/Shandong_Clique.txt:2681`

- 行 40–43，`GFX_SQI_neutral_political_view-248360`

```
	SpriteType = { 
		name = "GFX_SQI_neutral_political_view-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_neutral_political_view-248360.dds"
	}
```

  被引用：`common/national_focus/Qing_Manchu.txt:6845`、`common/national_focus/Shandong_Clique.txt:2699`

- 行 78–81，`GFX_SQI_denounce_the_manchu_overlords-248360`

```
	SpriteType = { 
		name = "GFX_SQI_denounce_the_manchu_overlords-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_denounce_the_manchu_overlords-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:2731`

- 行 116–119，`GFX_SQI_taoist_revival-248360`

```
	SpriteType = { 
		name = "GFX_SQI_taoist_revival-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_taoist_revival-248360.dds"
	}
```

  被引用：`common/national_focus/Qing_Manchu.txt:6209`、`common/national_focus/Shandong_Clique.txt:2750`

- 行 154–157，`GFX_SQI_abstention_from_western_politics-248360`

```
	SpriteType = { 
		name = "GFX_SQI_abstention_from_western_politics-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_abstention_from_western_politics-248360.dds"
	}
```

  被引用：`common/national_focus/Qing_Manchu.txt:6872`、`common/national_focus/Shandong_Clique.txt:2767`

- 行 192–195，`GFX_SQI_soup_kitchens_for_the_poor-248360`

```
	SpriteType = { 
		name = "GFX_SQI_soup_kitchens_for_the_poor-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_soup_kitchens_for_the_poor-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:2789`

- 行 230–233，`GFX_SQI_a_republic_worthy_under_heaven-248360`

```
	SpriteType = { 
		name = "GFX_SQI_a_republic_worthy_under_heaven-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_a_republic_worthy_under_heaven-248360.dds"
	}
```

  被引用：`common/national_focus/Qing_Manchu.txt:6797`、`common/national_focus/Shandong_Clique.txt:2808`

- 行 268–271，`GFX_SQI_developing_the_education_of_the_people-248360`

```
	SpriteType = { 
		name = "GFX_SQI_developing_the_education_of_the_people-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_developing_the_education_of_the_people-248360.dds"
	}
```

  被引用：`common/national_focus/Qing_Manchu.txt:5905`、`common/national_focus/Shandong_Clique.txt:2826`

- 行 306–309，`GFX_SQI_disaster_relief_squads-248360`

```
	SpriteType = { 
		name = "GFX_SQI_disaster_relief_squads-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_disaster_relief_squads-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:2842`

- 行 344–347，`GFX_SQI_uphold_confucian_values-248360`

```
	SpriteType = { 
		name = "GFX_SQI_uphold_confucian_values-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_uphold_confucian_values-248360.dds"
	}
```

  被引用：`SAVE_/Fengtian.txt:4679`、`common/national_focus/Fengtian.txt:4705`、`common/national_focus/Qing_Manchu.txt:6669`、`common/national_focus/Shandong_Clique.txt:2860`

- 行 382–385，`GFX_SQI_han_revival-248360`

```
	SpriteType = { 
		name = "GFX_SQI_han_revival-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_han_revival-248360.dds"
	}
```

  被引用：`common/national_focus/Qing_Manchu.txt:6548`、`common/national_focus/Shandong_Clique.txt:2894`

- 行 420–423，`GFX_SQI_fate_of_two_dragons-248360`

```
	SpriteType = { 
		name = "GFX_SQI_fate_of_two_dragons-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_fate_of_two_dragons-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:2914`

- 行 458–461，`GFX_SQI_stick_with_xiling-248360`

```
	SpriteType = { 
		name = "GFX_SQI_stick_with_xiling-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_stick_with_xiling-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:2931`

- 行 496–499，`GFX_SQI_align_with_shili-248360`

```
	SpriteType = { 
		name = "GFX_SQI_align_with_shili-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_align_with_shili-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:2957`

- 行 534–537，`GFX_SQI_the_ying_verse_the_yang-248360`

```
	SpriteType = { 
		name = "GFX_SQI_the_ying_verse_the_yang-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_the_ying_verse_the_yang-248360.dds"
	}
```

  被引用：`common/national_focus/Qing_Manchu.txt:5879`、`common/national_focus/Shandong_Clique.txt:2983`

- 行 572–575，`GFX_SQI_retaining_a_nationalist_outlook-248360`

```
	SpriteType = { 
		name = "GFX_SQI_retaining_a_nationalist_outlook-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_retaining_a_nationalist_outlook-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:3067`

- 行 610–613，`GFX_SQI_the_moon_shines_throughout_china-248360`

```
	SpriteType = { 
		name = "GFX_SQI_the_moon_shines_throughout_china-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_the_moon_shines_throughout_china-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:3093`

- 行 648–651，`GFX_SQI_the_red_poet-248360`

```
	SpriteType = { 
		name = "GFX_SQI_the_red_poet-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_the_red_poet-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:3115`

- 行 686–689，`GFX_SQI_new_outlook_for_democracy-248360`

```
	SpriteType = { 
		name = "GFX_SQI_new_outlook_for_democracy-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_new_outlook_for_democracy-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:3132`

- 行 724–727，`GFX_SQI_legacy_of_the_doctor-248360`

```
	SpriteType = { 
		name = "GFX_SQI_legacy_of_the_doctor-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_legacy_of_the_doctor-248360.dds"
	}
```

  被引用：`common/national_focus/Qing_Manchu.txt:6647`、`common/national_focus/Shandong_Clique.txt:3149`

- 行 762–765，`GFX_SQI_expanding_new_culture-248360`

```
	SpriteType = { 
		name = "GFX_SQI_expanding_new_culture-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_expanding_new_culture-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:3173`

- 行 800–803，`GFX_SQI_anti_monarchist_outlook-248360`

```
	SpriteType = { 
		name = "GFX_SQI_anti_monarchist_outlook-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_anti_monarchist_outlook-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:3191`

- 行 838–841，`GFX_SQI_borrowing_kmt_economics-248360`

```
	SpriteType = { 
		name = "GFX_SQI_borrowing_kmt_economics-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_borrowing_kmt_economics-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:3210`

- 行 876–879，`GFX_SQI_the_question_of_unification-248360`

```
	SpriteType = { 
		name = "GFX_SQI_the_question_of_unification-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_the_question_of_unification-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:3228`

- 行 914–917，`GFX_SQI_align_with_the_kmt-248360`

```
	SpriteType = { 
		name = "GFX_SQI_align_with_the_kmt-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_align_with_the_kmt-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:3247`

- 行 952–955，`GFX_SQI_our_own_republic-248360`

```
	SpriteType = { 
		name = "GFX_SQI_our_own_republic-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_our_own_republic-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:3356`

- 行 990–993，`GFX_SQI_liberalismstriumph-248360`

```
	SpriteType = { 
		name = "GFX_SQI_liberalismstriumph-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_liberalismstriumph-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:3447`

- 行 1028–1031，`GFX_SQI_embracing_the_liberal_era-248360`

```
	SpriteType = { 
		name = "GFX_SQI_embracing_the_liberal_era-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_embracing_the_liberal_era-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:3472`

- 行 1066–1069，`GFX_SQI_foundations_of_may_4th-248360`

```
	SpriteType = { 
		name = "GFX_SQI_foundations_of_may_4th-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_foundations_of_may_4th-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:3489`

- 行 1104–1107，`GFX_SQI_build_up_chinese_monopolies-248360`

```
	SpriteType = { 
		name = "GFX_SQI_build_up_chinese_monopolies-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_build_up_chinese_monopolies-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:3507`

- 行 1142–1145，`GFX_SQI_art_for_politics_sake-248360`

```
	SpriteType = { 
		name = "GFX_SQI_art_for_politics_sake-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_art_for_politics_sake-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:3526`

- 行 1180–1183，`GFX_SQI_proposition_to_the_landlords-248360`

```
	SpriteType = { 
		name = "GFX_SQI_proposition_to_the_landlords-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_proposition_to_the_landlords-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:3546`

- 行 1218–1221，`GFX_SQI_on_new_democracy-248360`

```
	SpriteType = { 
		name = "GFX_SQI_on_new_democracy-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_on_new_democracy-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:3567`

- 行 1256–1259，`GFX_SQI_purge_the_peasants_association-248360`

```
	SpriteType = { 
		name = "GFX_SQI_purge_the_peasants_association-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_purge_the_peasants_association-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:3588`

- 行 1294–1297，`GFX_SQI_the_issue_of_reunification-248360`

```
	SpriteType = { 
		name = "GFX_SQI_the_issue_of_reunification-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_the_issue_of_reunification-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:3610`

- 行 1332–1335，`GFX_SQI_negotiate_with_zhili_republicans-248360`

```
	SpriteType = { 
		name = "GFX_SQI_negotiate_with_zhili_republicans-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_negotiate_with_zhili_republicans-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:3632`

- 行 1370–1373，`GFX_SQI_topple_the_manchu_menace-248360`

```
	SpriteType = { 
		name = "GFX_SQI_topple_the_manchu_menace-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_topple_the_manchu_menace-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:3724`

- 行 1408–1411，`GFX_SQI_denounce_socialist_totalitarianism-248360`

```
	SpriteType = { 
		name = "GFX_SQI_denounce_socialist_totalitarianism-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_denounce_socialist_totalitarianism-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:3812`

- 行 1446–1449，`GFX_SQI_denounce_the_warlord_tyrants-248360`

```
	SpriteType = { 
		name = "GFX_SQI_denounce_the_warlord_tyrants-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_denounce_the_warlord_tyrants-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:3840`

- 行 1484–1487，`GFX_SQI_control_the_concessions-248360`

```
	SpriteType = { 
		name = "GFX_SQI_control_the_concessions-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_control_the_concessions-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:3856`

- 行 1522–1525，`GFX_SQI_national_rejuvination-248360`

```
	SpriteType = { 
		name = "GFX_SQI_national_rejuvination-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_national_rejuvination-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:3872`

- 行 1560–1563，`GFX_SQI_the_banner_above_beijing-248360`

```
	SpriteType = { 
		name = "GFX_SQI_the_banner_above_beijing-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_the_banner_above_beijing-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:3888`

- 行 1598–1601，`GFX_SQI_avictoryforthechinesepeople-248360`

```
	SpriteType = { 
		name = "GFX_SQI_avictoryforthechinesepeople-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_avictoryforthechinesepeople-248360.dds"
	}
```

  被引用：`common/national_focus/Qing_Manchu.txt:6104`、`common/national_focus/Shandong_Clique.txt:3917`

- 行 1636–1639，`GFX_SQI_a_leftwing_approach-248360`

```
	SpriteType = { 
		name = "GFX_SQI_a_leftwing_approach-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_a_leftwing_approach-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:3946`

- 行 1674–1677，`GFX_SQI_teaching_moderate_agrarianism-248360`

```
	SpriteType = { 
		name = "GFX_SQI_teaching_moderate_agrarianism-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_teaching_moderate_agrarianism-248360.dds"
	}
```

  被引用：`common/national_focus/Qing_Manchu.txt:6735`、`common/national_focus/Shandong_Clique.txt:3972`

- 行 1712–1715，`GFX_SQI_the_revolutionary_teacher-248360`

```
	SpriteType = { 
		name = "GFX_SQI_the_revolutionary_teacher-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_the_revolutionary_teacher-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:3995`

- 行 1750–1753，`GFX_SQI_a_country_in_need-248360`

```
	SpriteType = { 
		name = "GFX_SQI_a_country_in_need-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_a_country_in_need-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4011`

- 行 1788–1791，`GFX_SQI_form_the_tao_study_society-248360`

```
	SpriteType = { 
		name = "GFX_SQI_form_the_tao_study_society-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_form_the_tao_study_society-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4030`

- 行 1826–1829，`GFX_SQI_reforming_nationalism-248360`

```
	SpriteType = { 
		name = "GFX_SQI_reforming_nationalism-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_reforming_nationalism-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4047`

- 行 1864–1867，`GFX_SQI_continuation_of_secular_thinking-248360`

```
	SpriteType = { 
		name = "GFX_SQI_continuation_of_secular_thinking-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_continuation_of_secular_thinking-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4070`

- 行 1902–1905，`GFX_SQI_denounce_lu_xun-248360`

```
	SpriteType = { 
		name = "GFX_SQI_denounce_lu_xun-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_denounce_lu_xun-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4090`

- 行 1940–1943，`GFX_SQI_separation_from_the_kmt-248360`

```
	SpriteType = { 
		name = "GFX_SQI_separation_from_the_kmt-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_separation_from_the_kmt-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4107`

- 行 1978–1981，`GFX_SQI_putting_forward_progressive_education-248360`

```
	SpriteType = { 
		name = "GFX_SQI_putting_forward_progressive_education-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_putting_forward_progressive_education-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4126`

- 行 2016–2019，`GFX_SQI_saving_the_masses-248360`

```
	SpriteType = { 
		name = "GFX_SQI_saving_the_masses-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_saving_the_masses-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4142`

- 行 2054–2057，`GFX_SQI_protection_against_imperialism-248360`

```
	SpriteType = { 
		name = "GFX_SQI_protection_against_imperialism-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_protection_against_imperialism-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4162`

- 行 2092–2095，`GFX_SQI_advocating_for_a_new_republic-248360`

```
	SpriteType = { 
		name = "GFX_SQI_advocating_for_a_new_republic-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_advocating_for_a_new_republic-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4184`

- 行 2130–2133，`GFX_SQI_ally_with_the_peasants-248360`

```
	SpriteType = { 
		name = "GFX_SQI_ally_with_the_peasants-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_ally_with_the_peasants-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4270`

- 行 2168–2171，`GFX_SQI_a_new_xinhai-248360`

```
	SpriteType = { 
		name = "GFX_SQI_a_new_xinhai-248360"
		texturefile = "gfx/interface/goals/GFX_SQI_a_new_xinhai-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4287`

### `interface/focus-JAPANA_customicons.gfx` — 需保留 56 块 / 共 112 块

- 行 2–5，`GFX_JAPANA_burnthecrown-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_burnthecrown-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_burnthecrown-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:218`

- 行 40–43，`GFX_JAPANA_court_the_jcp-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_court_the_jcp-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_court_the_jcp-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:241`

- 行 78–81，`GFX_JAPANA_the_fight_against_discrimination-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_the_fight_against_discrimination-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_the_fight_against_discrimination-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:269`

- 行 116–119，`GFX_JAPANA_the_anarchist_shogunate-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_the_anarchist_shogunate-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_the_anarchist_shogunate-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:288`

- 行 154–157，`GFX_JAPANA_rule_of_the_council-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_rule_of_the_council-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_rule_of_the_council-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:304`

- 行 192–195，`GFX_JAPANA_capitalshallcrumble-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_capitalshallcrumble-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_capitalshallcrumble-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:319`

- 行 230–233，`GFX_JAPANA_integrate_the_imperial_unions-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_integrate_the_imperial_unions-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_integrate_the_imperial_unions-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:340`

- 行 268–271，`GFX_JAPANA_revolution_for_the_young-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_revolution_for_the_young-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_revolution_for_the_young-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:360`

- 行 306–309，`GFX_JAPANA_revolution_against_the_old-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_revolution_against_the_old-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_revolution_against_the_old-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:381`

- 行 344–347，`GFX_JAPANA_smash_the_zaibatsu-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_smash_the_zaibatsu-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_smash_the_zaibatsu-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:401`

- 行 382–385，`GFX_JAPANA_align_with_christian_socialists-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_align_with_christian_socialists-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_align_with_christian_socialists-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:422`

- 行 420–423，`GFX_JAPANA_purge_the_nobility-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_purge_the_nobility-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_purge_the_nobility-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:445`

- 行 458–461，`GFX_JAPANA_unite_the_zenkoku_and_kyushu_organizations-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_unite_the_zenkoku_and_kyushu_organizations-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_unite_the_zenkoku_and_kyushu_organizations-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:466`

- 行 496–499，`GFX_JAPANA_a_loyal_figure-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_a_loyal_figure-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_a_loyal_figure-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:491`

- 行 534–537，`GFX_JAPANA_work_with_the_national_socialists-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_work_with_the_national_socialists-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_work_with_the_national_socialists-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:531`

- 行 572–575，`GFX_JAPANA_from_our_declaration-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_from_our_declaration-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_from_our_declaration-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:554`

- 行 610–613，`GFX_JAPANA_reconciliation_movement-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_reconciliation_movement-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_reconciliation_movement-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:573`

- 行 648–651，`GFX_JAPANA_our_korean_comrades-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_our_korean_comrades-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_our_korean_comrades-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:592`

- 行 686–689，`GFX_JAPANA_idolize_the_cooperative_movement-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_idolize_the_cooperative_movement-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_idolize_the_cooperative_movement-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:614`

- 行 724–727，`GFX_JAPANA_form_the_eight_days_committee-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_form_the_eight_days_committee-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_form_the_eight_days_committee-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:635`

- 行 762–765，`GFX_JAPANA_construct_proletarian_councils-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_construct_proletarian_councils-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_construct_proletarian_councils-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:654`

- 行 800–803，`GFX_JAPANA_the_path_of_liberation-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_the_path_of_liberation-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_the_path_of_liberation-248360.dds"
	}
```

  被引用：`SAVE_/Fengtian.txt:8789`、`common/national_focus/Fengtian.txt:8832`、`common/national_focus/JAP_socialist_revolution.txt:675`

- 行 838–841，`GFX_JAPANA_revolutionary_expansion-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_revolutionary_expansion-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_revolutionary_expansion-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:697`

- 行 876–879，`GFX_JAPANA_taking_revenge_on_the_yakuza-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_taking_revenge_on_the_yakuza-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_taking_revenge_on_the_yakuza-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:731`

- 行 914–917，`GFX_JAPANA_japanshallbefree-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_japanshallbefree-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_japanshallbefree-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:759`

- 行 952–955，`GFX_JAPANA_sanshirosanarchismleadsthenation-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_sanshirosanarchismleadsthenation-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_sanshirosanarchismleadsthenation-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:801`

- 行 990–993，`GFX_JAPANA_writing_the_true_anarchist_manifesto-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_writing_the_true_anarchist_manifesto-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_writing_the_true_anarchist_manifesto-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:816`

- 行 1028–1031，`GFX_JAPANA_upholding_the_showa-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_upholding_the_showa-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_upholding_the_showa-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:835`

- 行 1066–1069，`GFX_JAPANA_in_the_embrace_of_pure_anarchism-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_in_the_embrace_of_pure_anarchism-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_in_the_embrace_of_pure_anarchism-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:857`

- 行 1104–1107，`GFX_JAPANA_mutualist_economic_program-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_mutualist_economic_program-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_mutualist_economic_program-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:876`

- 行 1142–1145，`GFX_JAPANA_uniting_the_japanese_anarchist_movement-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_uniting_the_japanese_anarchist_movement-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_uniting_the_japanese_anarchist_movement-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:897`

- 行 1180–1183，`GFX_JAPANA_crush_the_foreign_reactionaries-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_crush_the_foreign_reactionaries-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_crush_the_foreign_reactionaries-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:920`

- 行 1218–1221，`GFX_JAPANA_reforming_the_zenkoku_jiren-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_reforming_the_zenkoku_jiren-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_reforming_the_zenkoku_jiren-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:941`

- 行 1256–1259，`GFX_JAPANA_promotingcommunalagrarianism-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_promotingcommunalagrarianism-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_promotingcommunalagrarianism-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:960`

- 行 1294–1297，`GFX_JAPANA_anarchosyndicalist_programme-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_anarchosyndicalist_programme-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_anarchosyndicalist_programme-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:981`

- 行 1332–1335，`GFX_JAPANA_promotingthelocallife-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_promotingthelocallife-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_promotingthelocallife-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1006`

- 行 1370–1373，`GFX_JAPANA_syncretic_anarchist_ethos-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_syncretic_anarchist_ethos-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_syncretic_anarchist_ethos-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1028`

- 行 1408–1411，`GFX_JAPANA_legacy_of_imperial_anarchism-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_legacy_of_imperial_anarchism-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_legacy_of_imperial_anarchism-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1049`

- 行 1446–1449，`GFX_JAPANA_the_towers_surpass_the_clouds_again-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_the_towers_surpass_the_clouds_again-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_the_towers_surpass_the_clouds_again-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1070`

- 行 1484–1487，`GFX_JAPANA_radicalize_the_art_circles-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_radicalize_the_art_circles-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_radicalize_the_art_circles-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1109`

- 行 1522–1525，`GFX_JAPANA_the_old_guard_of_japanese_socialism-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_the_old_guard_of_japanese_socialism-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_the_old_guard_of_japanese_socialism-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1128`

- 行 1560–1563，`GFX_JAPANA_true_anarchism_rises-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_true_anarchism_rises-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_true_anarchism_rises-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1154`

- 行 1598–1601，`GFX_JAPANA_a_liberated_lifestyle-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_a_liberated_lifestyle-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_a_liberated_lifestyle-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1169`

- 行 1636–1639，`GFX_JAPANA_expression_through_living-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_expression_through_living-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_expression_through_living-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1190`

- 行 1674–1677，`GFX_JAPANA_denounce_the_crown_of_evil-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_denounce_the_crown_of_evil-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_denounce_the_crown_of_evil-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1209`

- 行 1712–1715，`GFX_JAPANA_dadaism_realized-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_dadaism_realized-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_dadaism_realized-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1231`

- 行 1750–1753，`GFX_JAPANA_the_literary_revolution-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_the_literary_revolution-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_the_literary_revolution-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1253`

- 行 1788–1791，`GFX_JAPANA_removing_the_oppressive_classes-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_removing_the_oppressive_classes-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_removing_the_oppressive_classes-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1274`

- 行 1826–1829，`GFX_JAPANA_forming_workers_cooperatives-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_forming_workers_cooperatives-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_forming_workers_cooperatives-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1295`

- 行 1864–1867，`GFX_JAPANA_understanding_the_peasantry-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_understanding_the_peasantry-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_understanding_the_peasantry-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1316`

- 行 1902–1905，`GFX_JAPANA_denounce_the_monks-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_denounce_the_monks-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_denounce_the_monks-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1337`

- 行 1940–1943，`GFX_JAPANA_embrace_the_monks-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_embrace_the_monks-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_embrace_the_monks-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1359`

- 行 1978–1981，`GFX_JAPANA_iamthetengu-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_iamthetengu-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_iamthetengu-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1381`

- 行 2016–2019，`GFX_JAPANA_formthetsujijunkoenkai-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_formthetsujijunkoenkai-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_formthetsujijunkoenkai-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1402`

- 行 2054–2057，`GFX_JAPANA_whatsgoingoninthepsychward-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_whatsgoingoninthepsychward-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_whatsgoingoninthepsychward-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1423`

- 行 2092–2095，`GFX_JAPANA_renounce_feudalism-248360`

```
	SpriteType = { 
		name = "GFX_JAPANA_renounce_feudalism-248360"
		texturefile = "gfx/interface/goals/GFX_JAPANA_renounce_feudalism-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:1445`

### `interface/focus-ZHU_customicons.gfx` — 需保留 49 块 / 共 98 块

- 行 2–5，`GFX_ZHU_realization_of_a_new_republican_dream-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_realization_of_a_new_republican_dream-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_realization_of_a_new_republican_dream-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:21`

- 行 40–43，`GFX_ZHU_glorification_of_a_new_china-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_glorification_of_a_new_china-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_glorification_of_a_new_china-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:36`

- 行 78–81，`GFX_ZHU_fortheredmarshal-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_fortheredmarshal-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_fortheredmarshal-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:55`

- 行 116–119，`GFX_ZHU_formation_of_the_coalition_government-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_formation_of_the_coalition_government-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_formation_of_the_coalition_government-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:73`

- 行 154–157，`GFX_ZHU_opium_prohibition-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_opium_prohibition-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_opium_prohibition-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:102`

- 行 192–195，`GFX_ZHU_electionofworkersandpeasantscouncils-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_electionofworkersandpeasantscouncils-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_electionofworkersandpeasantscouncils-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:120`

- 行 230–233，`GFX_ZHU_start_a_national_health_campaign-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_start_a_national_health_campaign-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_start_a_national_health_campaign-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:137`

- 行 268–271，`GFX_ZHU_invite_revolutionary_parties-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_invite_revolutionary_parties-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_invite_revolutionary_parties-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:155`

- 行 306–309，`GFX_ZHU_invite_revolutionary_parties-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_invite_revolutionary_parties-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_invite_revolutionary_parties-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:155`

- 行 344–347，`GFX_ZHU_socialist_nationalism-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_socialist_nationalism-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_socialist_nationalism-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:179`

- 行 382–385，`GFX_ZHU_start_the_national_reclamation_war-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_start_the_national_reclamation_war-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_start_the_national_reclamation_war-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:196`

- 行 420–423，`GFX_ZHU_a_proclamation_at_beijing-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_a_proclamation_at_beijing-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_a_proclamation_at_beijing-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:322`

- 行 458–461，`GFX_ZHU_forming_an_autonomy_system-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_forming_an_autonomy_system-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_forming_an_autonomy_system-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:342`

- 行 496–499，`GFX_ZHU_new_industrial_progress-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_new_industrial_progress-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_new_industrial_progress-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:361`

- 行 534–537，`GFX_ZHU_offering_autonomy-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_offering_autonomy-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_offering_autonomy-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:387`

- 行 572–575，`GFX_ZHU_intellectual_revolution-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_intellectual_revolution-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_intellectual_revolution-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:405`

- 行 610–613，`GFX_ZHU_liberate_the_rest_of_china-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_liberate_the_rest_of_china-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_liberate_the_rest_of_china-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:421`

- 行 648–651，`GFX_ZHU_sailing_the_seas_depends_on_the_marshal-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_sailing_the_seas_depends_on_the_marshal-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_sailing_the_seas_depends_on_the_marshal-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:492`

- 行 686–689，`GFX_ZHU_start_the_national_cwpdp_congress-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_start_the_national_cwpdp_congress-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_start_the_national_cwpdp_congress-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:510`

- 行 724–727，`GFX_ZHU_zhudewinsthenation-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_zhudewinsthenation-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_zhudewinsthenation-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:529`

- 行 762–765，`GFX_ZHU_growthepeopleslivelihood-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_growthepeopleslivelihood-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_growthepeopleslivelihood-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:545`

- 行 800–803，`GFX_ZHU_fostering_a_new_republican_identity-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_fostering_a_new_republican_identity-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_fostering_a_new_republican_identity-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:561`

- 行 838–841，`GFX_ZHU_continuing_the_ideas_of_democratic_socialism-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_continuing_the_ideas_of_democratic_socialism-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_continuing_the_ideas_of_democratic_socialism-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:581`

- 行 876–879，`GFX_ZHU_limit_nationalisation-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_limit_nationalisation-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_limit_nationalisation-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:598`

- 行 914–917，`GFX_ZHU_expand_unionisation-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_expand_unionisation-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_expand_unionisation-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:616`

- 行 952–955，`GFX_ZHU_double_hundred_policy-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_double_hundred_policy-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_double_hundred_policy-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:632`

- 行 990–993，`GFX_ZHU_a_nation_isolated-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_a_nation_isolated-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_a_nation_isolated-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:649`

- 行 1028–1031，`GFX_ZHU_join_our_international_comrades-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_join_our_international_comrades-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_join_our_international_comrades-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:667`

- 行 1066–1069，`GFX_ZHU_a_new_sun_tzu-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_a_new_sun_tzu-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_a_new_sun_tzu-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:684`

- 行 1104–1107，`GFX_ZHU_syndicalist_victory-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_syndicalist_victory-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_syndicalist_victory-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:701`

- 行 1142–1145，`GFX_ZHU_legacy_of_chinese_unionism-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_legacy_of_chinese_unionism-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_legacy_of_chinese_unionism-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:717`

- 行 1180–1183，`GFX_ZHU_an_expression_of_gender_equality-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_an_expression_of_gender_equality-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_an_expression_of_gender_equality-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:734`

- 行 1218–1221，`GFX_ZHU_split_from_the_csp-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_split_from_the_csp-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_split_from_the_csp-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:750`

- 行 1256–1259，`GFX_ZHU_communal_organisation-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_communal_organisation-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_communal_organisation-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:770`

- 行 1294–1297，`GFX_ZHU_union_based_industrialism-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_union_based_industrialism-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_union_based_industrialism-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:788`

- 行 1332–1335，`GFX_ZHU_join_the_internationale-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_join_the_internationale-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_join_the_internationale-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:813`

- 行 1370–1373，`GFX_ZHU_red_stars_are_shining-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_red_stars_are_shining-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_red_stars_are_shining-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:829`

- 行 1408–1411，`GFX_ZHU_baigesproletarianvictory-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_baigesproletarianvictory-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_baigesproletarianvictory-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:848`

- 行 1446–1449，`GFX_ZHU_help_from_the_league-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_help_from_the_league-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_help_from_the_league-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:864`

- 行 1484–1487，`GFX_ZHU_democratic_continuance-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_democratic_continuance-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_democratic_continuance-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:880`

- 行 1522–1525，`GFX_ZHU_crushing_old_culture-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_crushing_old_culture-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_crushing_old_culture-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:896`

- 行 1560–1563，`GFX_ZHU_studyingluxunsideas-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_studyingluxunsideas-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_studyingluxunsideas-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:914`

- 行 1598–1601，`GFX_ZHU_encourage_farmer_self_sufficiency-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_encourage_farmer_self_sufficiency-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_encourage_farmer_self_sufficiency-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:930`

- 行 1636–1639，`GFX_ZHU_reworking_a_new_culture-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_reworking_a_new_culture-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_reworking_a_new_culture-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:948`

- 行 1674–1677，`GFX_ZHU_unifying_the_masses-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_unifying_the_masses-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_unifying_the_masses-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:969`

- 行 1712–1715，`GFX_ZHU_welfare_opportunities-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_welfare_opportunities-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_welfare_opportunities-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:987`

- 行 1750–1753，`GFX_ZHU_aproletariansparadise-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_aproletariansparadise-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_aproletariansparadise-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:1005`

- 行 1788–1791，`GFX_ZHU_support_the_youth_organisations-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_support_the_youth_organisations-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_support_the_youth_organisations-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:1026`

- 行 1826–1829，`GFX_ZHU_a_new_proletarian_banner-248360`

```
	SpriteType = { 
		name = "GFX_ZHU_a_new_proletarian_banner-248360"
		texturefile = "gfx/interface/goals/GFX_ZHU_a_new_proletarian_banner-248360.dds"
	}
```

  被引用：`common/national_focus/zhudetree.txt:1048`

### `interface/focus-JAPRECOVERY_customicons.gfx` — 需保留 42 块 / 共 84 块

- 行 2–5，`GFX_JAPRECOVERY_communalisation-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_communalisation-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_communalisation-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3439`

- 行 40–43，`GFX_JAPRECOVERY_collectivisation-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_collectivisation-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_collectivisation-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3461`

- 行 78–81，`GFX_JAPRECOVERY_i_am_a_black_smith-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_i_am_a_black_smith-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_i_am_a_black_smith-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3483`

- 行 116–119，`GFX_JAPRECOVERY_civil_war_recovery_plan-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_civil_war_recovery_plan-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_civil_war_recovery_plan-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3505`

- 行 154–157，`GFX_JAPRECOVERY_fixing_the_economy-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_fixing_the_economy-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_fixing_the_economy-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3523`

- 行 192–195，`GFX_JAPRECOVERY_centralized_approach-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_centralized_approach-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_centralized_approach-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3539`

- 行 230–233，`GFX_JAPRECOVERY_starting_the_land_reformation-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_starting_the_land_reformation-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_starting_the_land_reformation-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3558`、`common/national_focus/KXX_Bourgogne.txt:98`、`common/national_focus/gru_Revolution.txt:7568`

- 行 268–271，`GFX_JAPRECOVERY_decentralized_economics-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_decentralized_economics-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_decentralized_economics-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3582`

- 行 306–309，`GFX_JAPRECOVERY_form_industrial_cooperatives-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_form_industrial_cooperatives-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_form_industrial_cooperatives-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3601`

- 行 344–347，`GFX_JAPRECOVERY_land_moderation-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_land_moderation-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_land_moderation-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3622`

- 行 382–385，`GFX_JAPRECOVERY_violent_land_revolution-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_violent_land_revolution-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_violent_land_revolution-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3655`

- 行 420–423，`GFX_JAPRECOVERY_committing_to_the_5_year_plan-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_committing_to_the_5_year_plan-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_committing_to_the_5_year_plan-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3689`

- 行 458–461，`GFX_JAPRECOVERY_strengthen_urban_industrial_centres-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_strengthen_urban_industrial_centres-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_strengthen_urban_industrial_centres-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3708`

- 行 496–499，`GFX_JAPRECOVERY_national_railroad_construction-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_national_railroad_construction-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_national_railroad_construction-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3727`

- 行 534–537，`GFX_JAPRECOVERY_radical_redistribution-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_radical_redistribution-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_radical_redistribution-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3746`

- 行 572–575，`GFX_JAPRECOVERY_land_lord_trials-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_land_lord_trials-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_land_lord_trials-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3773`

- 行 610–613，`GFX_JAPRECOVERY_land_to_the_tiller-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_land_to_the_tiller-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_land_to_the_tiller-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3792`

- 行 648–651，`GFX_JAPRECOVERY_working_on_the_agrarian_economy-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_working_on_the_agrarian_economy-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_working_on_the_agrarian_economy-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3821`

- 行 686–689，`GFX_JAPRECOVERY_communalised_cafeterias-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_communalised_cafeterias-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_communalised_cafeterias-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3843`

- 行 724–727，`GFX_JAPRECOVERY_working_another_day_for_the_masses_of_the_commune-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_working_another_day_for_the_masses_of_the_commune-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_working_another_day_for_the_masses_of_the_commune-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3864`

- 行 762–765，`GFX_JAPRECOVERY_cooperative_farming-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_cooperative_farming-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_cooperative_farming-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3886`

- 行 800–803，`GFX_JAPRECOVERY_organizingthepeoplesarmy-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_organizingthepeoplesarmy-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_organizingthepeoplesarmy-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3919`

- 行 838–841，`GFX_JAPRECOVERY_birth_of_the_red_army-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_birth_of_the_red_army-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_birth_of_the_red_army-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3938`

- 行 876–879，`GFX_JAPRECOVERY_keep_the_militias-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_keep_the_militias-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_keep_the_militias-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3960`

- 行 914–917，`GFX_JAPRECOVERY_son_kosakutai-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_son_kosakutai-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_son_kosakutai-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:3982`

- 行 952–955，`GFX_JAPRECOVERY_rehabilitatingpows-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_rehabilitatingpows-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_rehabilitatingpows-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:4018`、`common/national_focus/gru_Revolution.txt:7616`

- 行 990–993，`GFX_JAPRECOVERY_massmobilization_doctrine-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_massmobilization_doctrine-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_massmobilization_doctrine-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:4039`

- 行 1028–1031，`GFX_JAPRECOVERY_understanding_motorization-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_understanding_motorization-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_understanding_motorization-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:4060`

- 行 1066–1069，`GFX_JAPRECOVERY_commissars_of_the_revolution-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_commissars_of_the_revolution-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_commissars_of_the_revolution-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:4083`、`common/national_focus/KXX_Champagne.txt:326`、`common/national_focus/gru_Revolution.txt:7642`

- 行 1104–1107，`GFX_JAPRECOVERY_centralize_army_discipline-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_centralize_army_discipline-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_centralize_army_discipline-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:4104`

- 行 1142–1145，`GFX_JAPRECOVERY_up_high_in_the_mountains-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_up_high_in_the_mountains-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_up_high_in_the_mountains-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:4123`

- 行 1180–1183，`GFX_JAPRECOVERY_bicycle_brigades-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_bicycle_brigades-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_bicycle_brigades-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:4147`

- 行 1218–1221，`GFX_JAPRECOVERY_night_raids-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_night_raids-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_night_raids-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:4166`

- 行 1256–1259，`GFX_JAPRECOVERY_bring_out_the_armoured_beasts-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_bring_out_the_armoured_beasts-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_bring_out_the_armoured_beasts-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:4187`

- 行 1294–1297，`GFX_JAPRECOVERY_a_true_army_of_socialism-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_a_true_army_of_socialism-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_a_true_army_of_socialism-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:4244`

- 行 1332–1335，`GFX_JAPRECOVERY_thepeoplesnavy-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_thepeoplesnavy-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_thepeoplesnavy-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:4281`

- 行 1370–1373，`GFX_JAPRECOVERY_protecting_the_revolutionary_red_sun-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_protecting_the_revolutionary_red_sun-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_protecting_the_revolutionary_red_sun-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:4302`

- 行 1408–1411，`GFX_JAPRECOVERY_new_radar_links-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_new_radar_links-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_new_radar_links-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:4381`

- 行 1446–1449，`GFX_JAPRECOVERY_oursoldiersshallswimfly-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_oursoldiersshallswimfly-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_oursoldiersshallswimfly-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:4404`

- 行 1484–1487，`GFX_JAPRECOVERY_rebuild_the_hiroshima_shipyards-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_rebuild_the_hiroshima_shipyards-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_rebuild_the_hiroshima_shipyards-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:4454`

- 行 1522–1525，`GFX_JAPRECOVERY_a_new_red_fleet-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_a_new_red_fleet-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_a_new_red_fleet-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:4497`

- 行 1560–1563，`GFX_JAPRECOVERY_flying_high_above_the_sky-248360`

```
	SpriteType = { 
		name = "GFX_JAPRECOVERY_flying_high_above_the_sky-248360"
		texturefile = "gfx/interface/goals/GFX_JAPRECOVERY_flying_high_above_the_sky-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:4519`

### `interface/RD_ideology_picture.gfx` — 需保留 38 块 / 共 41 块

- 行 7–11，`GFX_ideology_fukumotoism_bar`

```
	spriteType = {
		name = "GFX_ideology_fukumotoism_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/fukumotoism.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1058`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1269`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1272`

- 行 12–16，`GFX_ideology_hashimoto_bar`

```
	spriteType = {
		name = "GFX_ideology_hashimoto_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/hashimoto.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:885`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:888`

- 行 17–21，`GFX_ideology_ho_chi_minh_bar`

```
	spriteType = {
		name = "GFX_ideology_ho_chi_minh_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/ho_chi_minh.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1106`

- 行 22–26，`GFX_ideology_ikedaism_bar`

```
	spriteType = {
		name = "GFX_ideology_ikedaism_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/ikedaism.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1097`

- 行 27–31，`GFX_ideology_japanese_militarism_bar`

```
	spriteType = {
		name = "GFX_ideology_japanese_militarism_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/japanese_militarism.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:917`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:962`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:965`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:968`

- 行 32–36，`GFX_ideology_kaysone_bar`

```
	spriteType = {
		name = "GFX_ideology_kaysone_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/kaysone.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1029`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1032`

- 行 37–41，`GFX_ideology_kita_ikki_bar`

```
	spriteType = {
		name = "GFX_ideology_kita_ikki_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/kita_ikki.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:879`

- 行 42–46，`GFX_ideology_lu_xun_bar`

```
	spriteType = {
		name = "GFX_ideology_lu_xun_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/lu_xun.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1037`

- 行 47–51，`GFX_ideology_mayakovskyism_bar`

```
	spriteType = {
		name = "GFX_ideology_mayakovskyism_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/mayakovskyism.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:891`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:894`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:897`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:900`

- 行 52–56，`GFX_ideology_socdem_national_socialism_bar`

```
	spriteType = {
		name = "GFX_ideology_socdem_national_socialism_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/national_socialism.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:903`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:906`

- 行 57–61，`GFX_ideology_new_khemerism_bar`

```
	spriteType = {
		name = "GFX_ideology_new_khemerism_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/new_khemerism.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1052`

- 行 62–66，`GFX_ideology_new_legalism_bar`

```
	spriteType = {
		name = "GFX_ideology_new_legalism_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/new_legalism.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1119`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1122`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1125`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1128`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1131`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1134`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1143`

- 行 67–71，`GFX_ideology_nichirenism_bar`

```
	spriteType = {
		name = "GFX_ideology_nichirenism_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/nichirenism.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1076`

- 行 72–76，`GFX_ideology_okawa_bar`

```
	spriteType = {
		name = "GFX_ideology_okawa_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/okawa.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:882`

- 行 77–81，`GFX_ideology_revolutionary_khmerism_bar`

```
	spriteType = {
		name = "GFX_ideology_revolutionary_khmerism_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/revolutionary_khmerism.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1161`

- 行 87–91，`GFX_ideology_sangkum_bar`

```
	spriteType = {
		name = "GFX_ideology_sangkum_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/sangkum.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:870`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:873`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:876`

- 行 92–96，`GFX_ideology_showa_anarchism_bar`

```
	spriteType = {
		name = "GFX_ideology_showa_anarchism_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/showa_anarchism.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:932`

- 行 98–102，`GFX_ideology_showa_statism_bar`

```
	spriteType = {
		name = "GFX_ideology_showa_statism_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/showa_statism.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:920`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:923`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:926`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:929`

- 行 103–107，`GFX_ideology_social_anarchism_bar`

```
	spriteType = {
		name = "GFX_ideology_social_anarchism_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/social_anarchism.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1568`、`localisation/RN_ideologies_l_simp_chinese.yml:3`

- 行 108–112，`GFX_ideology_social_nichirenism_bar`

```
	spriteType = {
		name = "GFX_ideology_social_nichirenism_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/social_nichirenism.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1067`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1070`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1073`

- 行 113–117，`GFX_ideology_state_shintoism_bar`

```
	spriteType = {
		name = "GFX_ideology_state_shintoism_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/state_shintoism.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:971`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:974`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1362`

- 行 118–122，`GFX_ideology_survival_nationalism_bar`

```
	spriteType = {
		name = "GFX_ideology_survival_nationalism_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/survival_nationalism.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1049`

- 行 123–127，`GFX_ideology_tot_national_socialism_bar`

```
	spriteType = {
		name = "GFX_ideology_tot_national_socialism_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/tot_national_socialism.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:909`

- 行 128–132，`GFX_ideology_yamakawaism_bar`

```
	spriteType = {
		name = "GFX_ideology_yamakawaism_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/yamakawaism.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1061`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1064`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1260`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1263`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1266`

- 行 133–137，`GFX_ideology_pan_turanism_bar`

```
	spriteType = {
		name = "GFX_ideology_pan_turanism_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/pan_turanism.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:867`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1649`、`localisation/RN_ideologies_l_simp_chinese.yml:55`

- 行 138–142，`GFX_ideology_moderate_revolutuionary_agarianism_bar`

```
	spriteType = {
		name = "GFX_ideology_moderate_revolutuionary_agarianism_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/moderate_revolutuionary_agarianism.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1040`

- 行 148–152，`GFX_ideology_anarcho_buddhism_bar`

```
	spriteType = {
		name = "GFX_ideology_anarcho_buddhism_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/anarcho_buddhism.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1026`

- 行 153–157，`GFX_ideology_natpop_kemalism_bar`

```
	spriteType = {
		name = "GFX_ideology_natpop_kemalism_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/natpop_kemalism.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1158`

- 行 158–162，`GFX_ideology_datong_shu_bar`

```
	spriteType = {
		name = "GFX_ideology_datong_shu_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/datong_shu.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1079`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1082`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1085`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1088`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1091`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1094`

- 行 163–167，`GFX_ideology_deng_bar`

```
	spriteType = {
		name = "GFX_ideology_deng_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/deng.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1100`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1103`

- 行 168–172，`GFX_ideology_chiang_bar`

```
	spriteType = {
		name = "GFX_ideology_chiang_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/chiang.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1046`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1170`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1173`

- 行 173–177，`GFX_ideology_indiv_anar_bar`

```
	spriteType = {
		name = "GFX_ideology_indiv_anar_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/indiv_anar.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KR_00_Political_l_simp_chinese.yml:1940`、`localisation/KR_00_Political_l_simp_chinese.yml:1944`、`localisation/KR_00_Political_l_simp_chinese.yml:1946`、`localisation/KR_00_Political_l_simp_chinese.yml:3190`、`localisation/KR_00_Political_l_simp_chinese.yml:3198`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:124`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1023`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1577` …共 9 处

- 行 178–182，`GFX_ideology_prag_syn_bar`

```
	spriteType = {
		name = "GFX_ideology_prag_syn_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/prag_syn.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1043`

- 行 183–187，`GFX_ideology_new_citizen_bar`

```
	spriteType = {
		name = "GFX_ideology_new_citizen_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/new_citizen.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1191`

- 行 188–192，`GFX_ideology_daijitao_bar`

```
	spriteType = {
		name = "GFX_ideology_daijitao_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/daijitao.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1176`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1179`

- 行 193–197，`GFX_ideology_new_life_movement_bar`

```
	spriteType = {
		name = "GFX_ideology_new_life_movement_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/new_life_movement.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1182`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1185`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:1188`

- 行 203–207，`GFX_ideology_moncadoism_bar`

```
	spriteType = {
		name = "GFX_ideology_moncadoism_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/moncadoism.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:2124`

- 行 208–212，`GFX_ideology_lapiang_malaya_bar`

```
	spriteType = {
		name = "GFX_ideology_lapiang_malaya_bar"
		textureFile = "gfx/interface/ideologies/ideology_bars/rd/lapiang_malaya.png"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_new_Ideologies_l_simp_chinese.yml:2127`、`localisation/KXX_new_Ideologies_l_simp_chinese.yml:2130`

### `interface/focus-SQITWO_customicons.gfx` — 需保留 38 块 / 共 102 块

- 行 2–5，`GFX_SQITWO_talks_with_korean_exiles-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_talks_with_korean_exiles-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_talks_with_korean_exiles-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4310`

- 行 40–43，`GFX_SQITWO_pulling_the_bolt-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_pulling_the_bolt-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_pulling_the_bolt-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4333`

- 行 116–119，`GFX_SQITWO_local_pogroms-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_local_pogroms-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_local_pogroms-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4354`

- 行 154–157，`GFX_SQITWO_the_fire_of_revolution_shines_through_shandong-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_the_fire_of_revolution_shines_through_shandong-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_the_fire_of_revolution_shines_through_shandong-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4372`

- 行 192–195，`GFX_SQITWO_hunt_down_suspected_spies-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_hunt_down_suspected_spies-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_hunt_down_suspected_spies-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4390`

- 行 230–233，`GFX_SQITWO_support_the_korean_revolution-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_support_the_korean_revolution-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_support_the_korean_revolution-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4411`

- 行 268–271，`GFX_SQITWO_denouncing_the_japanese_menance-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_denouncing_the_japanese_menance-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_denouncing_the_japanese_menance-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4459`

- 行 344–347，`GFX_SQITWO_ultranationalist_victory-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_ultranationalist_victory-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_ultranationalist_victory-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4485`

- 行 382–385，`GFX_SQITWO_inspiration_from_deng_xiaoping_economics-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_inspiration_from_deng_xiaoping_economics-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_inspiration_from_deng_xiaoping_economics-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4509`

- 行 420–423，`GFX_SQITWO_denouncing_the_fake_ones-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_denouncing_the_fake_ones-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_denouncing_the_fake_ones-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4527`

- 行 572–575，`GFX_SQITWO_anti_japanese_revanchism-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_anti_japanese_revanchism-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_anti_japanese_revanchism-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4551`

- 行 610–613，`GFX_SQITWO_connecting_with_local_communist_cells-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_connecting_with_local_communist_cells-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_connecting_with_local_communist_cells-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4567`

- 行 648–651，`GFX_SQITWO_jiejidibuduijiejidiyingxiong-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_jiejidibuduijiejidiyingxiong-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_jiejidibuduijiejidiyingxiong-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4585`

- 行 686–689，`GFX_SQITWO_arrest_japanese_diplomats-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_arrest_japanese_diplomats-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_arrest_japanese_diplomats-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4603`

- 行 724–727，`GFX_SQITWO_organic_economic_growth-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_organic_economic_growth-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_organic_economic_growth-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4625`

- 行 762–765，`GFX_SQITWO_zhongguomeng-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_zhongguomeng-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_zhongguomeng-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4665`

- 行 800–803，`GFX_SQITWO_denounce_internationalist_theory-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_denounce_internationalist_theory-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_denounce_internationalist_theory-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4683`

- 行 838–841，`GFX_SQITWO_translatingmarxstruewords-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_translatingmarxstruewords-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_translatingmarxstruewords-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4704`

- 行 952–955，`GFX_SQITWO_uniting_the_left_against_japan-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_uniting_the_left_against_japan-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_uniting_the_left_against_japan-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4722`

- 行 990–993，`GFX_SQITWO_contact_with_japanese_socialists-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_contact_with_japanese_socialists-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_contact_with_japanese_socialists-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4752`

- 行 1028–1031，`GFX_SQITWO_humiliate_hirohito-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_humiliate_hirohito-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_humiliate_hirohito-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4778`

- 行 1066–1069，`GFX_SQITWO_the_red_sun_on_the_frontier-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_the_red_sun_on_the_frontier-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_the_red_sun_on_the_frontier-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4795`

- 行 1104–1107，`GFX_SQITWO_crush_the_anarchists-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_crush_the_anarchists-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_crush_the_anarchists-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4813`

- 行 1142–1145，`GFX_SQITWO_hunt_down_ishii-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_hunt_down_ishii-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_hunt_down_ishii-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4837`

- 行 1180–1183，`GFX_SQITWO_deal_with_factionalism-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_deal_with_factionalism-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_deal_with_factionalism-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4855`

- 行 1218–1221，`GFX_SQITWO_our_national_duty-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_our_national_duty-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_our_national_duty-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4879`

- 行 1256–1259，`GFX_SQITWO_calling_the_first_rectification-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_calling_the_first_rectification-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_calling_the_first_rectification-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4895`

- 行 1294–1297，`GFX_SQITWO_introduce_antiimperialist_struggle_sessions-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_introduce_antiimperialist_struggle_sessions-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_introduce_antiimperialist_struggle_sessions-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4913`

- 行 1484–1487，`GFX_SQITWO_melting_the_azure_dragon-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_melting_the_azure_dragon-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_melting_the_azure_dragon-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:4933`

- 行 1522–1525，`GFX_SQITWO_enmingseducationrevolution-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_enmingseducationrevolution-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_enmingseducationrevolution-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:5025`

- 行 1560–1563，`GFX_SQITWO_a_promise_to_the_peasants-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_a_promise_to_the_peasants-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_a_promise_to_the_peasants-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:5041`

- 行 1598–1601，`GFX_SQITWO_jiefangquanzhongguo-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_jiefangquanzhongguo-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_jiefangquanzhongguo-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:5059`

- 行 1636–1639，`GFX_SQITWO_balujunjiuladashuan-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_balujunjiuladashuan-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_balujunjiuladashuan-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:5147`

- 行 1674–1677，`GFX_SQITWO_shasifanyi-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_shasifanyi-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_shasifanyi-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:5166`

- 行 1712–1715，`GFX_SQITWO_tying_up_lose_ends-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_tying_up_lose_ends-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_tying_up_lose_ends-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:5188`

- 行 1750–1753，`GFX_SQITWO_saving_the_colonies-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_saving_the_colonies-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_saving_the_colonies-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:5209`

- 行 1864–1867，`GFX_SQITWO_thepeoplesantijapaneserevolution-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_thepeoplesantijapaneserevolution-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_thepeoplesantijapaneserevolution-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:5227`

- 行 1902–1905，`GFX_SQITWO_our_future_in_asia-248360`

```
	SpriteType = { 
		name = "GFX_SQITWO_our_future_in_asia-248360"
		texturefile = "gfx/interface/goals/GFX_SQITWO_our_future_in_asia-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:5248`

### `interface/RD_ministers.gfx` — 需保留 21 块 / 共 21 块

- 行 3–6，`GFX_An_Ziwen`

```
	spriteType = {
		name = "GFX_An_Ziwen"
		texturefile = "gfx/interface/ministers/CNH/CNH_Ai_Ziwen.png"
	}	
```

  被引用：`common/ideas/KX_commiechina_Minister.txt:607`、`common/ideas/KX_commiechina_Minister.txt:671`

- 行 8–11，`GFX_Chen_Yi`

```
	spriteType = {
		name = "GFX_Chen_Yi"
		texturefile = "gfx/interface/ministers/CNH/CNH_Chen_Yi.png"
	}
```

  被引用：`common/ideas/KX_commiechina_Minister.txt:888`

- 行 13–16，`GFX_Chen_Yonggui`

```
	spriteType = {
		name = "GFX_Chen_Yonggui"
		texturefile = "gfx/interface/ministers/CNH/CNH_Chen_Yonggui.png"
	}
```

  被引用：`common/ideas/KX_commiechina_Minister.txt:930`、`common/ideas/KX_commiechina_Minister.txt:1073`、`common/ideas/KX_commiechina_Minister.txt:1094`、`common/ideas/KX_commiechina_Minister.txt:1115`、`common/ideas/KX_commiechina_Minister.txt:1136`

- 行 18–21，`GFX_Chen_Yun`

```
	spriteType = {
		name = "GFX_Chen_Yun"
		texturefile = "gfx/interface/ministers/CNH/CNH_Chen_Yun.png"
	}
```

  被引用：`common/ideas/KX_commiechina_Minister.txt:586`

- 行 22–25，`GFX_Cheng_Zihua`

```
	spriteType = {
		name = "GFX_Cheng_Zihua"
		texturefile = "gfx/interface/ministers/CNH/CNH_Cheng_Zihua.png"
	}
```

  被引用：`common/ideas/KX_commiechina_Minister.txt:951`

- 行 26–29，`GFX_Deng_Xiaoping`

```
	spriteType = {
		name = "GFX_Deng_Xiaoping"
		texturefile = "gfx/interface/ministers/CNH/CNH_Deng_Xiaoping.png"
	}
```

  被引用：`common/ideas/KX_commiechina_Minister.txt:9`、`common/ideas/KX_commiechina_Minister.txt:629`

- 行 30–33，`GFX_Ding_Ling`

```
	spriteType = {
		name = "GFX_Ding_Ling"
		texturefile = "gfx/interface/ministers/CNH/CNH_Ding_Ling.png"
	}
```

  被引用：`common/ideas/KX_commiechina_Minister.txt:70`、`common/ideas/KX_commiechina_Minister.txt:91`、`common/ideas/KX_commiechina_Minister.txt:111`、`common/ideas/KX_commiechina_Minister.txt:133`、`common/ideas/KX_commiechina_Minister.txt:153`、`common/ideas/KX_commiechina_Minister.txt:175`、`common/ideas/KX_commiechina_Minister.txt:195`、`common/ideas/KX_commiechina_Minister.txt:215` …共 24 处

- 行 34–37，`GFX_Gu_Shunzhang`

```
	spriteType = {
		name = "GFX_Gu_Shunzhang"
		texturefile = "gfx/interface/ministers/CNH/CNH_Gu_Shunzhang.png"
	}
```

  被引用：`common/ideas/KX_commiechina_Minister.txt:1032`

- 行 38–41，`GFX_Hu_Yepin`

```
	spriteType = {
		name = "GFX_Hu_Yepin"
		texturefile = "gfx/interface/ministers/CNH/CNH_Hu_Yepin.png"
	}
```

  被引用：`common/ideas/KX_commiechina_Minister.txt:650`

- 行 42–45，`GFX_Li_Xiannian`

```
	spriteType = {
		name = "GFX_Li_Xiannian"
		texturefile = "gfx/interface/ministers/CNH/CNH_Li_Xiannian.png"
	}
```

  被引用：`common/ideas/KX_commiechina_Minister.txt:566`、`common/ideas/KX_commiechina_Minister.txt:695`、`common/ideas/KX_commiechina_Minister.txt:716`、`common/ideas/KX_commiechina_Minister.txt:737`、`common/ideas/KX_commiechina_Minister.txt:758`、`common/ideas/KX_commiechina_Minister.txt:779`、`common/ideas/KX_commiechina_Minister.txt:800`、`common/ideas/KX_commiechina_Minister.txt:821` …共 10 处

- 行 46–49，`GFX_Liu_Shaoqi`

```
	spriteType = {
		name = "GFX_Liu_Shaoqi"
		texturefile = "gfx/interface/ministers/CNH/CNH_Liu_Shaoqi.png"
	}
```

  被引用：`common/ideas/KX_commiechina_Minister.txt:991`

- 行 50–53，`GFX_Qiao_Guanhua`

```
	spriteType = {
		name = "GFX_Qiao_Guanhua"
		texturefile = "gfx/interface/ministers/CNH/CNH_Qiao_Guanhua.png"
	}
```

  被引用：`common/ideas/KX_commiechina_Minister.txt:909`

- 行 54–57，`GFX_Ruo_Shi`

```
	spriteType = {
		name = "GFX_Ruo_Shi"
		texturefile = "gfx/interface/ministers/CNH/CNH_Ruo_Shi.png"
	}
```

  被引用：`common/ideas/KX_commiechina_Minister.txt:50`

- 行 58–61，`GFX_Wang_Dongxing`

```
	spriteType = {
		name = "GFX_Wang_Dongxing"
		texturefile = "gfx/interface/ministers/CNH/CNH_Wang_Dongxing.png"
	}
```

  被引用：`common/ideas/KX_commiechina_Minister.txt:1219`、`common/ideas/KX_commiechina_Minister.txt:1239`、`common/ideas/KX_commiechina_Minister.txt:1259`、`common/ideas/KX_commiechina_Minister.txt:1279`、`common/ideas/KX_commiechina_Minister.txt:1299`、`common/ideas/KX_commiechina_Minister.txt:1318`、`common/ideas/KX_commiechina_Minister.txt:1338`、`common/ideas/KX_commiechina_Minister.txt:1357`

- 行 62–65，`GFX_Xiang_Zhingfa`

```
	spriteType = {
		name = "GFX_Xiang_Zhingfa"
		texturefile = "gfx/interface/ministers/CNH/CNH_Xiang_Zhingfa.png"
	}
```

  被引用：`common/ideas/KX_commiechina_Minister.txt:971`

- 行 67–70，`GFX_Xiang_Jingyu`

```
	spriteType = {
		name = "GFX_Xiang_Jingyu"
		texturefile = "gfx/interface/ministers/CNH/CNH_Xiang_Jingyu.png"
	}
```

  被引用：`common/ideas/KX_commiechina_Minister.txt:1052`

- 行 71–74，`GFX_Zhang_Wentian`

```
	spriteType = {
		name = "GFX_Zhang_Wentian"
		texturefile = "gfx/interface/ministers/CNH/CNH_Zhang_Wentian.png"
	}
```

  被引用：`common/ideas/KX_commiechina_Minister.txt:1011`

- 行 75–78，`GFX_Zhang_Yunyi`

```
	spriteType = {
		name = "GFX_Zhang_Yunyi"
		texturefile = "gfx/interface/ministers/CNH/CNH_Zhang_Yunyi.png"
	}
```

  被引用：`common/ideas/KX_commiechina_Minister.txt:1179`

- 行 79–82，`GFX_Zhou_Yang`

```
	spriteType = {
		name = "GFX_Zhou_Yang"
		texturefile = "gfx/interface/ministers/CNH/CNH_Zhou_Yang.png"
	}
```

  被引用：`common/ideas/KX_commiechina_Minister.txt:30`

- 行 84–87，`GFX_Kang_Sheng`

```
	spriteType = {
		name = "GFX_Kang_Sheng"
		texturefile = "gfx/interface/ministers/CNH/CNH_Kang_Sheng.png"
	}
```

  被引用：`common/ideas/KX_commiechina_Minister.txt:1159`

- 行 89–92，`GFX_Zhang_Guotao`

```
	spriteType = {
		name = "GFX_Zhang_Guotao"
		texturefile = "gfx/interface/ministers/CNH/CNH_Zhang_Guotao.png"
	}
```

  被引用：`common/ideas/KX_commiechina_Minister.txt:1199`

### `interface/focus-JAPARAKI_customicons.gfx` — 需保留 18 块 / 共 92 块

- 行 192–195，`GFX_JAPARAKI_the_military_leap-248360`

```
	SpriteType = { 
		name = "GFX_JAPARAKI_the_military_leap-248360"
		texturefile = "gfx/interface/goals/GFX_JAPARAKI_the_military_leap-248360.dds"
	}
```

  被引用：`common/national_focus/SCB_JAP_natunity_bureaucracy_military.txt:1271`

- 行 230–233，`GFX_JAPARAKI_the_spiritual_leap-248360`

```
	SpriteType = { 
		name = "GFX_JAPARAKI_the_spiritual_leap-248360"
		texturefile = "gfx/interface/goals/GFX_JAPARAKI_the_spiritual_leap-248360.dds"
	}
```

  被引用：`common/national_focus/SCB_JAP_natunity_bureaucracy_military.txt:1416`

- 行 306–309，`GFX_JAPARAKI_extending_the_fist_of_military_might-248360`

```
	SpriteType = { 
		name = "GFX_JAPARAKI_extending_the_fist_of_military_might-248360"
		texturefile = "gfx/interface/goals/GFX_JAPARAKI_extending_the_fist_of_military_might-248360.dds"
	}
```

  被引用：`common/national_focus/SCB_JAP_natunity_bureaucracy_military.txt:1292`

- 行 382–385，`GFX_JAPARAKI_reinforce_security_of_the_state-248360`

```
	SpriteType = { 
		name = "GFX_JAPARAKI_reinforce_security_of_the_state-248360"
		texturefile = "gfx/interface/goals/GFX_JAPARAKI_reinforce_security_of_the_state-248360.dds"
	}
```

  被引用：`common/ideas/SCB_JAP_democracy_ideas.txt:292`、`common/ideas/SCB_JAP_democracy_ideas.txt:457`、`common/ideas/SCB_JAP_democracy_ideas.txt:466`、`common/ideas/SCB_JAP_democracy_ideas.txt:477`、`common/ideas/SCB_JAP_democracy_ideas.txt:490`、`common/ideas/SCB_JAP_democracy_ideas.txt:741`、`common/ideas/SCB_JAP_democracy_ideas.txt:752`、`common/ideas/SCB_JAP_democracy_ideas.txt:765` …共 13 处

- 行 762–765，`GFX_JAPARAKI_connectingtheemperorthelandandthepeople-248360`

```
	SpriteType = { 
		name = "GFX_JAPARAKI_connectingtheemperorthelandandthepeople-248360"
		texturefile = "gfx/interface/goals/GFX_JAPARAKI_connectingtheemperorthelandandthepeople-248360.dds"
	}
```

  被引用：`common/ideas/SCB_JAP_democracy_ideas.txt:313`、`common/ideas/SCB_JAP_democracy_ideas.txt:872`、`common/ideas/SCB_JAP_democracy_ideas.txt:1050`、`common/ideas/SCB_JAP_democracy_ideas.txt:1513`、`common/national_focus/SCB_JAP_natunity_bureaucracy_military.txt:1010`

- 行 838–841，`GFX_JAPARAKI_rally_the_tonarigumi-248360`

```
	SpriteType = { 
		name = "GFX_JAPARAKI_rally_the_tonarigumi-248360"
		texturefile = "gfx/interface/goals/GFX_JAPARAKI_rally_the_tonarigumi-248360.dds"
	}
```

  被引用：`common/national_focus/SCB_JAP_natunity_bureaucracy_military.txt:1112`

- 行 952–955，`GFX_JAPARAKI_kokutai_no_hongi-248360`

```
	SpriteType = { 
		name = "GFX_JAPARAKI_kokutai_no_hongi-248360"
		texturefile = "gfx/interface/goals/GFX_JAPARAKI_kokutai_no_hongi-248360.dds"
	}
```

  被引用：`common/ideas/SCB_JAP_democracy_ideas.txt:303`、`common/ideas/SCB_JAP_democracy_ideas.txt:395`、`common/ideas/SCB_JAP_democracy_ideas.txt:941`、`common/ideas/SCB_JAP_democracy_ideas.txt:961`、`common/ideas/SCB_JAP_democracy_ideas.txt:971`、`common/ideas/SCB_JAP_democracy_ideas.txt:1060`、`common/ideas/SCB_JAP_democracy_ideas.txt:1185`、`common/ideas/SCB_JAP_democracy_ideas.txt:1224` …共 13 处

- 行 990–993，`GFX_JAPARAKI_attack_the_socialist_resistance-248360`

```
	SpriteType = { 
		name = "GFX_JAPARAKI_attack_the_socialist_resistance-248360"
		texturefile = "gfx/interface/goals/GFX_JAPARAKI_attack_the_socialist_resistance-248360.dds"
	}
```

  被引用：`common/national_focus/SCB_JAP_natunity_bureaucracy_military.txt:1045`

- 行 1066–1069，`GFX_JAPARAKI_preparing_for_total_war-248360`

```
	SpriteType = { 
		name = "GFX_JAPARAKI_preparing_for_total_war-248360"
		texturefile = "gfx/interface/goals/GFX_JAPARAKI_preparing_for_total_war-248360.dds"
	}
```

  被引用：`common/ideas/SCB_JAP_democracy_ideas.txt:333`、`common/ideas/SCB_JAP_democracy_ideas.txt:506`、`common/ideas/SCB_JAP_democracy_ideas.txt:515`、`common/ideas/SCB_JAP_democracy_ideas.txt:526`、`common/ideas/SCB_JAP_democracy_ideas.txt:682`、`common/ideas/SCB_JAP_democracy_ideas.txt:691`、`common/ideas/SCB_JAP_democracy_ideas.txt:702`、`common/national_focus/SCB_JAP_natunity_bureaucracy_military.txt:1325`

- 行 1104–1107，`GFX_JAPARAKI_crush_ugaki_thought-248360`

```
	SpriteType = { 
		name = "GFX_JAPARAKI_crush_ugaki_thought-248360"
		texturefile = "gfx/interface/goals/GFX_JAPARAKI_crush_ugaki_thought-248360.dds"
	}
```

  被引用：`common/national_focus/SCB_JAP_natunity_bureaucracy_military.txt:1060`

- 行 1180–1183，`GFX_JAPARAKI_spiritual_training-248360`

```
	SpriteType = { 
		name = "GFX_JAPARAKI_spiritual_training-248360"
		texturefile = "gfx/interface/goals/GFX_JAPARAKI_spiritual_training-248360.dds"
	}
```

  被引用：`common/ideas/SCB_JAP_democracy_ideas.txt:385`、`common/ideas/SCB_JAP_democracy_ideas.txt:852`、`common/ideas/SCB_JAP_democracy_ideas.txt:1404`、`common/ideas/SCB_JAP_democracy_ideas.txt:1733`、`common/ideas/SCB_JAP_democracy_ideas.txt:1769`、`common/ideas/SCB_JAP_democracy_ideas.txt:1778`、`common/national_focus/SCB_JAP_natunity_bureaucracy_military.txt:1436`

- 行 1218–1221，`GFX_JAPARAKI_national_spiritual_mobilisation-248360`

```
	SpriteType = { 
		name = "GFX_JAPARAKI_national_spiritual_mobilisation-248360"
		texturefile = "gfx/interface/goals/GFX_JAPARAKI_national_spiritual_mobilisation-248360.dds"
	}
```

  被引用：`common/ideas/SCB_JAP_democracy_ideas.txt:353`、`common/ideas/SCB_JAP_democracy_ideas.txt:375`、`common/ideas/SCB_JAP_democracy_ideas.txt:715`、`common/ideas/SCB_JAP_democracy_ideas.txt:861`、`common/ideas/SCB_JAP_democracy_ideas.txt:1343`、`common/national_focus/SCB_JAP_natunity_bureaucracy_military.txt:1339`

- 行 1294–1297，`GFX_JAPARAKI_the_bamboo_spear_slay_our_enemies-248360`

```
	SpriteType = { 
		name = "GFX_JAPARAKI_the_bamboo_spear_slay_our_enemies-248360"
		texturefile = "gfx/interface/goals/GFX_JAPARAKI_the_bamboo_spear_slay_our_enemies-248360.dds"
	}
```

  被引用：`common/ideas/SCB_JAP_democracy_ideas.txt:364`、`common/ideas/SCB_JAP_democracy_ideas.txt:1040`、`common/ideas/SCB_JAP_democracy_ideas.txt:1384`、`common/national_focus/SCB_JAP_natunity_bureaucracy_military.txt:1360`

- 行 1370–1373，`GFX_JAPARAKI_araki_at_the_helm-248360`

```
	SpriteType = { 
		name = "GFX_JAPARAKI_araki_at_the_helm-248360"
		texturefile = "gfx/interface/goals/GFX_JAPARAKI_araki_at_the_helm-248360.dds"
	}
```

  被引用：`common/ideas/SCB_JAP_democracy_ideas.txt:323`、`common/ideas/SCB_JAP_democracy_ideas.txt:951`、`common/ideas/SCB_JAP_democracy_ideas.txt:1010`、`common/ideas/SCB_JAP_democracy_ideas.txt:1214`、`common/ideas/SCB_JAP_democracy_ideas.txt:1332`、`common/ideas/SCB_JAP_democracy_ideas.txt:1364`、`common/national_focus/SCB_JAP_natunity_bureaucracy_military.txt:1075`

- 行 1484–1487，`GFX_JAPARAKI_a_promise_to_the_peasant_soldiers-248360`

```
	SpriteType = { 
		name = "GFX_JAPARAKI_a_promise_to_the_peasant_soldiers-248360"
		texturefile = "gfx/interface/goals/GFX_JAPARAKI_a_promise_to_the_peasant_soldiers-248360.dds"
	}
```

  被引用：`common/national_focus/SCB_JAP_natunity_bureaucracy_military.txt:1096`

- 行 1560–1563，`GFX_JAPARAKI_the_autarky_economic_solution-248360`

```
	SpriteType = { 
		name = "GFX_JAPARAKI_the_autarky_economic_solution-248360"
		texturefile = "gfx/interface/goals/GFX_JAPARAKI_the_autarky_economic_solution-248360.dds"
	}
```

  被引用：`common/national_focus/SCB_JAP_natunity_bureaucracy_military.txt:1162`

- 行 1598–1601，`GFX_JAPARAKI_continued_the_zaibatsu_nationalisation-248360`

```
	SpriteType = { 
		name = "GFX_JAPARAKI_continued_the_zaibatsu_nationalisation-248360"
		texturefile = "gfx/interface/goals/GFX_JAPARAKI_continued_the_zaibatsu_nationalisation-248360.dds"
	}
```

  被引用：`common/national_focus/SCB_JAP_natunity_bureaucracy_military.txt:1233`

- 行 1636–1639，`GFX_JAPARAKI_organize_rural_cooperatives-248360`

```
	SpriteType = { 
		name = "GFX_JAPARAKI_organize_rural_cooperatives-248360"
		texturefile = "gfx/interface/goals/GFX_JAPARAKI_organize_rural_cooperatives-248360.dds"
	}
```

  被引用：`common/national_focus/SCB_JAP_natunity_bureaucracy_military.txt:1249`

### `interface/focus-YUNJUCHE_customicons.gfx` — 需保留 18 块 / 共 36 块

- 行 2–5，`GFX_YUNJUCHE_a_monument_to_our_great_chairman-248360`

```
	SpriteType = { 
		name = "GFX_YUNJUCHE_a_monument_to_our_great_chairman-248360"
		texturefile = "gfx/interface/goals/GFX_YUNJUCHE_a_monument_to_our_great_chairman-248360.dds"
	}
```

  被引用：`common/national_focus/jucheyunnan.txt:19`

- 行 40–43，`GFX_YUNJUCHE_embracing_a_new_realm_of_socialism-248360`

```
	SpriteType = { 
		name = "GFX_YUNJUCHE_embracing_a_new_realm_of_socialism-248360"
		texturefile = "gfx/interface/goals/GFX_YUNJUCHE_embracing_a_new_realm_of_socialism-248360.dds"
	}
```

  被引用：`common/national_focus/jucheyunnan.txt:37`

- 行 78–81，`GFX_YUNJUCHE_setcoursetianlima-248360`

```
	SpriteType = { 
		name = "GFX_YUNJUCHE_setcoursetianlima-248360"
		texturefile = "gfx/interface/goals/GFX_YUNJUCHE_setcoursetianlima-248360.dds"
	}
```

  被引用：`common/national_focus/jucheyunnan.txt:55`

- 行 116–119，`GFX_YUNJUCHE_crush_the_cpwdp-248360`

```
	SpriteType = { 
		name = "GFX_YUNJUCHE_crush_the_cpwdp-248360"
		texturefile = "gfx/interface/goals/GFX_YUNJUCHE_crush_the_cpwdp-248360.dds"
	}
```

  被引用：`common/national_focus/jucheyunnan.txt:73`

- 行 154–157，`GFX_YUNJUCHE_destroy_the_warlords-248360`

```
	SpriteType = { 
		name = "GFX_YUNJUCHE_destroy_the_warlords-248360"
		texturefile = "gfx/interface/goals/GFX_YUNJUCHE_destroy_the_warlords-248360.dds"
	}
```

  被引用：`common/national_focus/jucheyunnan.txt:102`

- 行 192–195，`GFX_YUNJUCHE_push_for_a_greater_china-248360`

```
	SpriteType = { 
		name = "GFX_YUNJUCHE_push_for_a_greater_china-248360"
		texturefile = "gfx/interface/goals/GFX_YUNJUCHE_push_for_a_greater_china-248360.dds"
	}
```

  被引用：`common/national_focus/jucheyunnan.txt:119`

- 行 230–233，`GFX_YUNJUCHE_let_the_train_of_revolution_go_forth-248360`

```
	SpriteType = { 
		name = "GFX_YUNJUCHE_let_the_train_of_revolution_go_forth-248360"
		texturefile = "gfx/interface/goals/GFX_YUNJUCHE_let_the_train_of_revolution_go_forth-248360.dds"
	}
```

  被引用：`common/national_focus/jucheyunnan.txt:177`

- 行 268–271，`GFX_YUNJUCHE_support_for_our_dear_leader-248360`

```
	SpriteType = { 
		name = "GFX_YUNJUCHE_support_for_our_dear_leader-248360"
		texturefile = "gfx/interface/goals/GFX_YUNJUCHE_support_for_our_dear_leader-248360.dds"
	}
```

  被引用：`common/national_focus/jucheyunnan.txt:216`

- 行 306–309，`GFX_YUNJUCHE_topple_the_dragons_crown-248360`

```
	SpriteType = { 
		name = "GFX_YUNJUCHE_topple_the_dragons_crown-248360"
		texturefile = "gfx/interface/goals/GFX_YUNJUCHE_topple_the_dragons_crown-248360.dds"
	}
```

  被引用：`common/national_focus/jucheyunnan.txt:237`

- 行 344–347，`GFX_YUNJUCHE_unitary_strength-248360`

```
	SpriteType = { 
		name = "GFX_YUNJUCHE_unitary_strength-248360"
		texturefile = "gfx/interface/goals/GFX_YUNJUCHE_unitary_strength-248360.dds"
	}
```

  被引用：`common/national_focus/jucheyunnan.txt:254`

- 行 382–385，`GFX_YUNJUCHE_going_against_internationale_revisionism-248360`

```
	SpriteType = { 
		name = "GFX_YUNJUCHE_going_against_internationale_revisionism-248360"
		texturefile = "gfx/interface/goals/GFX_YUNJUCHE_going_against_internationale_revisionism-248360.dds"
	}
```

  被引用：`common/national_focus/jucheyunnan.txt:276`

- 行 420–423，`GFX_YUNJUCHE_a_retelling_of_history-248360`

```
	SpriteType = { 
		name = "GFX_YUNJUCHE_a_retelling_of_history-248360"
		texturefile = "gfx/interface/goals/GFX_YUNJUCHE_a_retelling_of_history-248360.dds"
	}
```

  被引用：`common/national_focus/jucheyunnan.txt:296`

- 行 458–461，`GFX_YUNJUCHE_denounce_the_false_idols-248360`

```
	SpriteType = { 
		name = "GFX_YUNJUCHE_denounce_the_false_idols-248360"
		texturefile = "gfx/interface/goals/GFX_YUNJUCHE_denounce_the_false_idols-248360.dds"
	}
```

  被引用：`common/national_focus/jucheyunnan.txt:313`

- 行 496–499，`GFX_YUNJUCHE_our_own_cultural_revolution-248360`

```
	SpriteType = { 
		name = "GFX_YUNJUCHE_our_own_cultural_revolution-248360"
		texturefile = "gfx/interface/goals/GFX_YUNJUCHE_our_own_cultural_revolution-248360.dds"
	}
```

  被引用：`common/national_focus/jucheyunnan.txt:341`

- 行 534–537，`GFX_YUNJUCHE_join_up_with_comrade_kim-248360`

```
	SpriteType = { 
		name = "GFX_YUNJUCHE_join_up_with_comrade_kim-248360"
		texturefile = "gfx/interface/goals/GFX_YUNJUCHE_join_up_with_comrade_kim-248360.dds"
	}
```

  被引用：`common/national_focus/jucheyunnan.txt:359`

- 行 572–575，`GFX_YUNJUCHE_new_era_of_socialist_development-248360`

```
	SpriteType = { 
		name = "GFX_YUNJUCHE_new_era_of_socialist_development-248360"
		texturefile = "gfx/interface/goals/GFX_YUNJUCHE_new_era_of_socialist_development-248360.dds"
	}
```

  被引用：`common/national_focus/jucheyunnan.txt:418`

- 行 610–613，`GFX_YUNJUCHE_beyondthehillofsocialism-248360`

```
	SpriteType = { 
		name = "GFX_YUNJUCHE_beyondthehillofsocialism-248360"
		texturefile = "gfx/interface/goals/GFX_YUNJUCHE_beyondthehillofsocialism-248360.dds"
	}
```

  被引用：`common/national_focus/jucheyunnan.txt:437`

- 行 648–651，`GFX_YUNJUCHE_zhongguowansui-248360`

```
	SpriteType = { 
		name = "GFX_YUNJUCHE_zhongguowansui-248360"
		texturefile = "gfx/interface/goals/GFX_YUNJUCHE_zhongguowansui-248360.dds"
	}
```

  被引用：`common/national_focus/jucheyunnan.txt:458`

### `interface/focus-CHINA_FOREIGN_POLICY_customicons.gfx` — 需保留 17 块 / 共 34 块

- 行 2–5，`GFX_CHINA_FOREIGN_POLICY_focus_on_the_liberation_of_the_far_east-248360`

```
	SpriteType = { 
		name = "GFX_CHINA_FOREIGN_POLICY_focus_on_the_liberation_of_the_far_east-248360"
		texturefile = "gfx/interface/goals/GFX_CHINA_FOREIGN_POLICY_focus_on_the_liberation_of_the_far_east-248360.dds"
	}
```

  被引用：`common/national_focus/FX_Philippines.txt:9418`、`common/national_focus/china-unification-foreign-policy.txt:5`

- 行 40–43，`GFX_CHINA_FOREIGN_POLICY_slaying_the_colonizers_of_the_south_east-248360`

```
	SpriteType = { 
		name = "GFX_CHINA_FOREIGN_POLICY_slaying_the_colonizers_of_the_south_east-248360"
		texturefile = "gfx/interface/goals/GFX_CHINA_FOREIGN_POLICY_slaying_the_colonizers_of_the_south_east-248360.dds"
	}
```

  被引用：`common/national_focus/china-unification-foreign-policy.txt:23`

- 行 78–81，`GFX_CHINA_FOREIGN_POLICY_focusing_on_central_asia-248360`

```
	SpriteType = { 
		name = "GFX_CHINA_FOREIGN_POLICY_focusing_on_central_asia-248360"
		texturefile = "gfx/interface/goals/GFX_CHINA_FOREIGN_POLICY_focusing_on_central_asia-248360.dds"
	}
```

  被引用：`common/national_focus/china-unification-foreign-policy.txt:51`

- 行 116–119，`GFX_CHINA_FOREIGN_POLICY_the_sinosphere_secured-248360`

```
	SpriteType = { 
		name = "GFX_CHINA_FOREIGN_POLICY_the_sinosphere_secured-248360"
		texturefile = "gfx/interface/goals/GFX_CHINA_FOREIGN_POLICY_the_sinosphere_secured-248360.dds"
	}
```

  被引用：`common/national_focus/china-unification-foreign-policy.txt:77`

- 行 154–157，`GFX_CHINA_FOREIGN_POLICY_beyond_the_walls_of_the_middle_kingdom-248360`

```
	SpriteType = { 
		name = "GFX_CHINA_FOREIGN_POLICY_beyond_the_walls_of_the_middle_kingdom-248360"
		texturefile = "gfx/interface/goals/GFX_CHINA_FOREIGN_POLICY_beyond_the_walls_of_the_middle_kingdom-248360.dds"
	}
```

  被引用：`common/national_focus/FX_Philippines.txt:9642`、`common/national_focus/china-unification-foreign-policy.txt:96`

- 行 192–195，`GFX_CHINA_FOREIGN_POLICY_securing_the_plateau-248360`

```
	SpriteType = { 
		name = "GFX_CHINA_FOREIGN_POLICY_securing_the_plateau-248360"
		texturefile = "gfx/interface/goals/GFX_CHINA_FOREIGN_POLICY_securing_the_plateau-248360.dds"
	}
```

  被引用：`common/national_focus/china-unification-foreign-policy.txt:118`

- 行 230–233，`GFX_CHINA_FOREIGN_POLICY_aligning_with_the_world-248360`

```
	SpriteType = { 
		name = "GFX_CHINA_FOREIGN_POLICY_aligning_with_the_world-248360"
		texturefile = "gfx/interface/goals/GFX_CHINA_FOREIGN_POLICY_aligning_with_the_world-248360.dds"
	}
```

  被引用：`common/national_focus/china-unification-foreign-policy.txt:136`

- 行 268–271，`GFX_CHINA_FOREIGN_POLICY_aligning_with_the_world-248360`

```
	SpriteType = { 
		name = "GFX_CHINA_FOREIGN_POLICY_aligning_with_the_world-248360"
		texturefile = "gfx/interface/goals/GFX_CHINA_FOREIGN_POLICY_aligning_with_the_world-248360.dds"
	}
```

  被引用：`common/national_focus/china-unification-foreign-policy.txt:136`

- 行 306–309，`GFX_CHINA_FOREIGN_POLICY_aligning_with_the_world-248360`

```
	SpriteType = { 
		name = "GFX_CHINA_FOREIGN_POLICY_aligning_with_the_world-248360"
		texturefile = "gfx/interface/goals/GFX_CHINA_FOREIGN_POLICY_aligning_with_the_world-248360.dds"
	}
```

  被引用：`common/national_focus/china-unification-foreign-policy.txt:136`

- 行 344–347，`GFX_CHINA_FOREIGN_POLICY_aligning_with_the_world-248360`

```
	SpriteType = { 
		name = "GFX_CHINA_FOREIGN_POLICY_aligning_with_the_world-248360"
		texturefile = "gfx/interface/goals/GFX_CHINA_FOREIGN_POLICY_aligning_with_the_world-248360.dds"
	}
```

  被引用：`common/national_focus/china-unification-foreign-policy.txt:136`

- 行 382–385，`GFX_CHINA_FOREIGN_POLICY_in_the_hands_of_global_revolution-248360`

```
	SpriteType = { 
		name = "GFX_CHINA_FOREIGN_POLICY_in_the_hands_of_global_revolution-248360"
		texturefile = "gfx/interface/goals/GFX_CHINA_FOREIGN_POLICY_in_the_hands_of_global_revolution-248360.dds"
	}
```

  被引用：`common/national_focus/china-unification-foreign-policy.txt:156`

- 行 420–423，`GFX_CHINA_FOREIGN_POLICY_imperial_legacy-248360`

```
	SpriteType = { 
		name = "GFX_CHINA_FOREIGN_POLICY_imperial_legacy-248360"
		texturefile = "gfx/interface/goals/GFX_CHINA_FOREIGN_POLICY_imperial_legacy-248360.dds"
	}
```

  被引用：`common/national_focus/china-unification-foreign-policy.txt:179`

- 行 458–461，`GFX_CHINA_FOREIGN_POLICY_claiming_outer_manchuria-248360`

```
	SpriteType = { 
		name = "GFX_CHINA_FOREIGN_POLICY_claiming_outer_manchuria-248360"
		texturefile = "gfx/interface/goals/GFX_CHINA_FOREIGN_POLICY_claiming_outer_manchuria-248360.dds"
	}
```

  被引用：`common/national_focus/china-unification-foreign-policy.txt:199`

- 行 496–499，`GFX_CHINA_FOREIGN_POLICY_secure_the_north_west_frontier-248360`

```
	SpriteType = { 
		name = "GFX_CHINA_FOREIGN_POLICY_secure_the_north_west_frontier-248360"
		texturefile = "gfx/interface/goals/GFX_CHINA_FOREIGN_POLICY_secure_the_north_west_frontier-248360.dds"
	}
```

  被引用：`common/national_focus/china-unification-foreign-policy.txt:241`

- 行 534–537，`GFX_CHINA_FOREIGN_POLICY_secure_the_mcmahon_line-248360`

```
	SpriteType = { 
		name = "GFX_CHINA_FOREIGN_POLICY_secure_the_mcmahon_line-248360"
		texturefile = "gfx/interface/goals/GFX_CHINA_FOREIGN_POLICY_secure_the_mcmahon_line-248360.dds"
	}
```

  被引用：`common/national_focus/china-unification-foreign-policy.txt:295`

- 行 572–575，`GFX_CHINA_FOREIGN_POLICY_extending_the_5_tibetan_fingers-248360`

```
	SpriteType = { 
		name = "GFX_CHINA_FOREIGN_POLICY_extending_the_5_tibetan_fingers-248360"
		texturefile = "gfx/interface/goals/GFX_CHINA_FOREIGN_POLICY_extending_the_5_tibetan_fingers-248360.dds"
	}
```

  被引用：`common/national_focus/china-unification-foreign-policy.txt:323`

- 行 610–613，`GFX_CHINA_FOREIGN_POLICY_eastern_subjugation-248360`

```
	SpriteType = { 
		name = "GFX_CHINA_FOREIGN_POLICY_eastern_subjugation-248360"
		texturefile = "gfx/interface/goals/GFX_CHINA_FOREIGN_POLICY_eastern_subjugation-248360.dds"
	}
```

  被引用：`common/national_focus/china-unification-foreign-policy.txt:355`

### `interface/focus-VNQ_customicons.gfx` — 需保留 17 块 / 共 34 块

- 行 2–5，`GFX_VNQ_white_sun_over_vietnam-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_white_sun_over_vietnam-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_white_sun_over_vietnam-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:14`

- 行 40–43，`GFX_VNQ_longlivethepeoplesstate-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_longlivethepeoplesstate-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_longlivethepeoplesstate-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:26`

- 行 78–81，`GFX_VNQ_finding_anything_we_can-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_finding_anything_we_can-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_finding_anything_we_can-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:42`

- 行 116–119，`GFX_VNQ_followingtheherosoftheyenbaimutinies-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_followingtheherosoftheyenbaimutinies-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_followingtheherosoftheyenbaimutinies-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:67`

- 行 154–157，`GFX_VNQ_mass_recruitment_campaign-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_mass_recruitment_campaign-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_mass_recruitment_campaign-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:84`

- 行 192–195，`GFX_VNQ_national_salvation_war-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_national_salvation_war-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_national_salvation_war-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:102`

- 行 230–233，`GFX_VNQ_the_economics_of_war-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_the_economics_of_war-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_the_economics_of_war-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:120`

- 行 268–271，`GFX_VNQ_chinese_volunteer_division-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_chinese_volunteer_division-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_chinese_volunteer_division-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:139`

- 行 306–309，`GFX_VNQ_syndie_scums_in_saigon-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_syndie_scums_in_saigon-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_syndie_scums_in_saigon-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:155`

- 行 344–347，`GFX_VNQ_imperial_dog_house_in_hue-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_imperial_dog_house_in_hue-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_imperial_dog_house_in_hue-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:173`

- 行 382–385，`GFX_VNQ_vietnam_for_vietnamese-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_vietnam_for_vietnamese-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_vietnam_for_vietnamese-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:191`

- 行 420–423，`GFX_VNQ_white_terror-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_white_terror-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_white_terror-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:211`

- 行 458–461，`GFX_VNQ_the_great_southern_push-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_the_great_southern_push-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_the_great_southern_push-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:235`

- 行 496–499，`GFX_VNQ_raising_the_republican_flag-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_raising_the_republican_flag-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_raising_the_republican_flag-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:252`

- 行 534–537，`GFX_VNQ_request_international_aid-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_request_international_aid-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_request_international_aid-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:272`

- 行 572–575，`GFX_VNQ_foundation_of_the_national_revolutionary_army-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_foundation_of_the_national_revolutionary_army-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_foundation_of_the_national_revolutionary_army-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:290`

- 行 610–613，`GFX_VNQ_drsunstrueheirs-248360`

```
	SpriteType = { 
		name = "GFX_VNQ_drsunstrueheirs-248360"
		texturefile = "gfx/interface/goals/GFX_VNQ_drsunstrueheirs-248360.dds"
	}
```

  被引用：`common/national_focus/democratic-vietname.txt:306`

### `interface/focus-QIE_customicons.gfx` — 需保留 16 块 / 共 36 块

- 行 2–5，`GFX_QIE_the_red_sun_over_the_dragon-90809`

```
	SpriteType = { 
		name = "GFX_QIE_the_red_sun_over_the_dragon-90809"
		texturefile = "gfx/interface/goals/GFX_QIE_the_red_sun_over_the_dragon-90809.dds"
	}
```

  被引用：`common/national_focus/Qing_Manchu.txt:6899`

- 行 40–43，`GFX_QIE_the_red_court-90832`

```
	SpriteType = { 
		name = "GFX_QIE_the_red_court-90832"
		texturefile = "gfx/interface/goals/GFX_QIE_the_red_court-90832.dds"
	}
```

  被引用：`common/national_focus/Qing_Manchu.txt:6918`

- 行 78–81，`GFX_QIE_the_league_of_yellow_dragons-90811`

```
	SpriteType = { 
		name = "GFX_QIE_the_league_of_yellow_dragons-90811"
		texturefile = "gfx/interface/goals/GFX_QIE_the_league_of_yellow_dragons-90811.dds"
	}
```

  被引用：`common/national_focus/Qing_Manchu.txt:6947`

- 行 154–157，`GFX_QIE_integration_with_the_csp-90816`

```
	SpriteType = { 
		name = "GFX_QIE_integration_with_the_csp-90816"
		texturefile = "gfx/interface/goals/GFX_QIE_integration_with_the_csp-90816.dds"
	}
```

  被引用：`common/national_focus/Qing_Manchu.txt:6988`

- 行 192–195，`GFX_QIE_new_five_year_plans-90821`

```
	SpriteType = { 
		name = "GFX_QIE_new_five_year_plans-90821"
		texturefile = "gfx/interface/goals/GFX_QIE_new_five_year_plans-90821.dds"
	}
```

  被引用：`common/national_focus/Qing_Manchu.txt:7055`

- 行 268–271，`GFX_QIE_the_royal_education-90823`

```
	SpriteType = { 
		name = "GFX_QIE_the_royal_education-90823"
		texturefile = "gfx/interface/goals/GFX_QIE_the_royal_education-90823.dds"
	}
```

  被引用：`common/national_focus/Qing_Manchu.txt:7078`

- 行 306–309，`GFX_QIE_the_devils_of_warlords-90818`

```
	SpriteType = { 
		name = "GFX_QIE_the_devils_of_warlords-90818"
		texturefile = "gfx/interface/goals/GFX_QIE_the_devils_of_warlords-90818.dds"
	}
```

  被引用：`common/national_focus/Qing_Manchu.txt:7095`

- 行 344–347，`GFX_QIE_beiyang_railway-90824`

```
	SpriteType = { 
		name = "GFX_QIE_beiyang_railway-90824"
		texturefile = "gfx/interface/goals/GFX_QIE_beiyang_railway-90824.dds"
	}
```

  被引用：`common/national_focus/Qing_Manchu.txt:7113`

- 行 382–385，`GFX_QIE_the_red_mandate-90820`

```
	SpriteType = { 
		name = "GFX_QIE_the_red_mandate-90820"
		texturefile = "gfx/interface/goals/GFX_QIE_the_red_mandate-90820.dds"
	}
```

  被引用：`common/national_focus/Qing_Manchu.txt:7139`

- 行 420–423，`GFX_QIE_the_yellow_purge-90825`

```
	SpriteType = { 
		name = "GFX_QIE_the_yellow_purge-90825"
		texturefile = "gfx/interface/goals/GFX_QIE_the_yellow_purge-90825.dds"
	}
```

  被引用：`common/national_focus/Qing_Manchu.txt:7228`

- 行 458–461，`GFX_QIE_beyond_the_han-90828`

```
	SpriteType = { 
		name = "GFX_QIE_beyond_the_han-90828"
		texturefile = "gfx/interface/goals/GFX_QIE_beyond_the_han-90828.dds"
	}
```

  被引用：`common/national_focus/Qing_Manchu.txt:7249`

- 行 496–499，`GFX_QIE_the_will_of_the_people-90827`

```
	SpriteType = { 
		name = "GFX_QIE_the_will_of_the_people-90827"
		texturefile = "gfx/interface/goals/GFX_QIE_the_will_of_the_people-90827.dds"
	}
```

  被引用：`common/national_focus/Qing_Manchu.txt:7306`

- 行 534–537，`GFX_QIE_the_yellow_guards-90826`

```
	SpriteType = { 
		name = "GFX_QIE_the_yellow_guards-90826"
		texturefile = "gfx/interface/goals/GFX_QIE_the_yellow_guards-90826.dds"
	}
```

  被引用：`common/national_focus/Qing_Manchu.txt:7326`

- 行 572–575，`GFX_QIE_looking_for_allies-90829`

```
	SpriteType = { 
		name = "GFX_QIE_looking_for_allies-90829"
		texturefile = "gfx/interface/goals/GFX_QIE_looking_for_allies-90829.dds"
	}
```

  被引用：`common/national_focus/Qing_Manchu.txt:7346`

- 行 610–613，`GFX_QIE_stoping_rightwing_imperialism-90830`

```
	SpriteType = { 
		name = "GFX_QIE_stoping_rightwing_imperialism-90830"
		texturefile = "gfx/interface/goals/GFX_QIE_stoping_rightwing_imperialism-90830.dds"
	}
```

  被引用：`common/national_focus/Qing_Manchu.txt:7367`

- 行 648–651，`GFX_QIE_the_empire_of_the_red_dragon-90831`

```
	SpriteType = { 
		name = "GFX_QIE_the_empire_of_the_red_dragon-90831"
		texturefile = "gfx/interface/goals/GFX_QIE_the_empire_of_the_red_dragon-90831.dds"
	}
```

  被引用：`common/national_focus/Qing_Manchu.txt:7520`

### `interface/focus-JAP_SOCFOR_customicons.gfx` — 需保留 13 块 / 共 26 块

- 行 2–5，`GFX_JAP_SOCFOR_the_china_solution-248360`

```
	SpriteType = { 
		name = "GFX_JAP_SOCFOR_the_china_solution-248360"
		texturefile = "gfx/interface/goals/GFX_JAP_SOCFOR_the_china_solution-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:4543`

- 行 40–43，`GFX_JAP_SOCFOR_reaching_out_to_socialist_allies-248360`

```
	SpriteType = { 
		name = "GFX_JAP_SOCFOR_reaching_out_to_socialist_allies-248360"
		texturefile = "gfx/interface/goals/GFX_JAP_SOCFOR_reaching_out_to_socialist_allies-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:4562`

- 行 78–81，`GFX_JAP_SOCFOR_a_revolution_on_the_world_stage-248360`

```
	SpriteType = { 
		name = "GFX_JAP_SOCFOR_a_revolution_on_the_world_stage-248360"
		texturefile = "gfx/interface/goals/GFX_JAP_SOCFOR_a_revolution_on_the_world_stage-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:4579`

- 行 116–119，`GFX_JAP_SOCFOR_saving_the_far_east-248360`

```
	SpriteType = { 
		name = "GFX_JAP_SOCFOR_saving_the_far_east-248360"
		texturefile = "gfx/interface/goals/GFX_JAP_SOCFOR_saving_the_far_east-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:4599`

- 行 154–157，`GFX_JAP_SOCFOR_liberate_the_former_colonies-248360`

```
	SpriteType = { 
		name = "GFX_JAP_SOCFOR_liberate_the_former_colonies-248360"
		texturefile = "gfx/interface/goals/GFX_JAP_SOCFOR_liberate_the_former_colonies-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:4633`

- 行 192–195，`GFX_JAP_SOCFOR_proclaiming_the_red_steppe-248360`

```
	SpriteType = { 
		name = "GFX_JAP_SOCFOR_proclaiming_the_red_steppe-248360"
		texturefile = "gfx/interface/goals/GFX_JAP_SOCFOR_proclaiming_the_red_steppe-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:4684`

- 行 230–233，`GFX_JAP_SOCFOR_our_own_path_of_liberation-248360`

```
	SpriteType = { 
		name = "GFX_JAP_SOCFOR_our_own_path_of_liberation-248360"
		texturefile = "gfx/interface/goals/GFX_JAP_SOCFOR_our_own_path_of_liberation-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:4726`

- 行 268–271，`GFX_JAP_SOCFOR_secure_central_asia-248360`

```
	SpriteType = { 
		name = "GFX_JAP_SOCFOR_secure_central_asia-248360"
		texturefile = "gfx/interface/goals/GFX_JAP_SOCFOR_secure_central_asia-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:4748`

- 行 306–309，`GFX_JAP_SOCFOR_hunting_the_big_bear-248360`

```
	SpriteType = { 
		name = "GFX_JAP_SOCFOR_hunting_the_big_bear-248360"
		texturefile = "gfx/interface/goals/GFX_JAP_SOCFOR_hunting_the_big_bear-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:4767`

- 行 344–347，`GFX_JAP_SOCFOR_crush_the_colonialists_of_the_southern_seas-248360`

```
	SpriteType = { 
		name = "GFX_JAP_SOCFOR_crush_the_colonialists_of_the_southern_seas-248360"
		texturefile = "gfx/interface/goals/GFX_JAP_SOCFOR_crush_the_colonialists_of_the_southern_seas-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:4792`

- 行 382–385，`GFX_JAP_SOCFOR_proclaiming_the_red_star_above_india-248360`

```
	SpriteType = { 
		name = "GFX_JAP_SOCFOR_proclaiming_the_red_star_above_india-248360"
		texturefile = "gfx/interface/goals/GFX_JAP_SOCFOR_proclaiming_the_red_star_above_india-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:4811`

- 行 420–423，`GFX_JAP_SOCFOR_promoting_the_global_revolution-248360`

```
	SpriteType = { 
		name = "GFX_JAP_SOCFOR_promoting_the_global_revolution-248360"
		texturefile = "gfx/interface/goals/GFX_JAP_SOCFOR_promoting_the_global_revolution-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:4830`

- 行 458–461，`GFX_JAP_SOCFOR_securing_asia_under_socialism-248360`

```
	SpriteType = { 
		name = "GFX_JAP_SOCFOR_securing_asia_under_socialism-248360"
		texturefile = "gfx/interface/goals/GFX_JAP_SOCFOR_securing_asia_under_socialism-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:4852`

### `interface/focus-JAPSOCIALISM_customicons.gfx` — 需保留 10 块 / 共 20 块

- 行 2–5，`GFX_JAPSOCIALISM_the_revolution_is_calling-248360`

```
	SpriteType = { 
		name = "GFX_JAPSOCIALISM_the_revolution_is_calling-248360"
		texturefile = "gfx/interface/goals/GFX_JAPSOCIALISM_the_revolution_is_calling-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:14`、`common/national_focus/gru_Revolution.txt:7460`

- 行 40–43，`GFX_JAPSOCIALISM_organize_the_farmers-248360`

```
	SpriteType = { 
		name = "GFX_JAPSOCIALISM_organize_the_farmers-248360"
		texturefile = "gfx/interface/goals/GFX_JAPSOCIALISM_organize_the_farmers-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:29`

- 行 78–81，`GFX_JAPSOCIALISM_cooperation_with_the_unions-248360`

```
	SpriteType = { 
		name = "GFX_JAPSOCIALISM_cooperation_with_the_unions-248360"
		texturefile = "gfx/interface/goals/GFX_JAPSOCIALISM_cooperation_with_the_unions-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:46`

- 行 116–119，`GFX_JAPSOCIALISM_war_socialism-248360`

```
	SpriteType = { 
		name = "GFX_JAPSOCIALISM_war_socialism-248360"
		texturefile = "gfx/interface/goals/GFX_JAPSOCIALISM_war_socialism-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:62`

- 行 154–157，`GFX_JAPSOCIALISM_seek_internationale_aid-248360`

```
	SpriteType = { 
		name = "GFX_JAPSOCIALISM_seek_internationale_aid-248360"
		texturefile = "gfx/interface/goals/GFX_JAPSOCIALISM_seek_internationale_aid-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:81`、`common/national_focus/gru_Revolution.txt:7475`

- 行 192–195，`GFX_JAPSOCIALISM_letsdoourbest-248360`

```
	SpriteType = { 
		name = "GFX_JAPSOCIALISM_letsdoourbest-248360"
		texturefile = "gfx/interface/goals/GFX_JAPSOCIALISM_letsdoourbest-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:114`

- 行 230–233，`GFX_JAPSOCIALISM_liaison_with_shanghai_contacts-248360`

```
	SpriteType = { 
		name = "GFX_JAPSOCIALISM_liaison_with_shanghai_contacts-248360"
		texturefile = "gfx/interface/goals/GFX_JAPSOCIALISM_liaison_with_shanghai_contacts-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:131`

- 行 268–271，`GFX_JAPSOCIALISM_striking_for_more_than_a_day-248360`

```
	SpriteType = { 
		name = "GFX_JAPSOCIALISM_striking_for_more_than_a_day-248360"
		texturefile = "gfx/interface/goals/GFX_JAPSOCIALISM_striking_for_more_than_a_day-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:150`

- 行 306–309，`GFX_JAPSOCIALISM_organize_peasant_uprisings-248360`

```
	SpriteType = { 
		name = "GFX_JAPSOCIALISM_organize_peasant_uprisings-248360"
		texturefile = "gfx/interface/goals/GFX_JAPSOCIALISM_organize_peasant_uprisings-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:167`

- 行 344–347，`GFX_JAPSOCIALISM_theredflagflieshighovertokyo-248360`

```
	SpriteType = { 
		name = "GFX_JAPSOCIALISM_theredflagflieshighovertokyo-248360"
		texturefile = "gfx/interface/goals/GFX_JAPSOCIALISM_theredflagflieshighovertokyo-248360.dds"
	}
```

  被引用：`common/national_focus/JAP_socialist_revolution.txt:183`

### `interface/RD_game_rules.gfx` — 需保留 9 块 / 共 52 块

- 行 157–161，`GFX_KR_game_rule_flag_FRA_Arthuys`

```
	spriteType = {
		name = "GFX_KR_game_rule_flag_FRA_Arthuys"
		texturefile = "gfx/flags/small/FRA_Arthuys.tga"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_game_rules_l_simp_chinese.yml:887`

- 行 167–171，`GFX_KR_game_rule_flag_FRA_Vanguard`

```
	spriteType = {
		name = "GFX_KR_game_rule_flag_FRA_Vanguard"
		texturefile = "gfx/flags/small/FRA_Vanguard.tga"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_game_rules_l_simp_chinese.yml:889`

- 行 172–176，`GFX_KR_game_rule_flag_FRA_orthodox`

```
	spriteType = {
		name = "GFX_KR_game_rule_flag_FRA_orthodox"
		texturefile = "gfx/flags/small/FRA_orthodox.tga"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_game_rules_l_simp_chinese.yml:891`

- 行 182–186，`GFX_KR_game_rule_flag_FRA_herve`

```
	spriteType = {
		name = "GFX_KR_game_rule_flag_FRA_herve"
		texturefile = "gfx/flags/small/FRA_herve.tga"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_game_rules_l_simp_chinese.yml:905`

- 行 187–191，`GFX_KR_game_rule_flag_FRA_consulat`

```
	spriteType = {
		name = "GFX_KR_game_rule_flag_FRA_consulat"
		texturefile = "gfx/flags/small/FRA_consulat.tga"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_game_rules_l_simp_chinese.yml:907`

- 行 192–196，`GFX_KR_game_rule_flag_FRA_christsoc`

```
	spriteType = {
		name = "GFX_KR_game_rule_flag_FRA_christsoc"
		texturefile = "gfx/flags/small/FRA_christsoc.tga"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_game_rules_l_simp_chinese.yml:909`

- 行 197–201，`GFX_KR_game_rule_flag_FRA_atheist`

```
	spriteType = {
		name = "GFX_KR_game_rule_flag_FRA_atheist"
		texturefile = "gfx/flags/small/FRA_atheist.tga"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_game_rules_l_simp_chinese.yml:911`

- 行 202–206，`GFX_KR_game_rule_flag_FRA_celt`

```
	spriteType = {
		name = "GFX_KR_game_rule_flag_FRA_celt"
		texturefile = "gfx/flags/small/FRA_celt.tga"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/KXX_game_rules_l_simp_chinese.yml:913`

- 行 208–212，`GFX_KR_game_rule_flag_TAI`

```
	spriteType = {
		name = "GFX_KR_game_rule_flag_TAI"
		texturefile = "gfx/flags/small/TWI_AN.tga"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/kxxfix_game_rules_l_simp_chinese.yml:42`、`localisation/kxxfix_game_rules_l_simp_chinese.yml:44`、`localisation/kxxfix_game_rules_l_simp_chinese.yml:46`、`localisation/kxxfix_game_rules_l_simp_chinese.yml:48`、`localisation/kxxfix_game_rules_l_simp_chinese.yml:54`、`localisation/kxxfix_game_rules_l_simp_chinese.yml:56`、`localisation/kxxfix_game_rules_l_simp_chinese.yml:58`、`localisation/kxxfix_game_rules_l_simp_chinese.yml:60` …共 14 处

### `interface/RD_ideas.gfx` — 需保留 9 块 / 共 17 块

- 行 13–16，`GFX_idea_kmt_power`

```
	spriteType = {
		name = "GFX_idea_kmt_power"
		texturefile = "gfx/interface/ideas/CNH/kmt_unions.png"
	}
```

  被引用：`common/bop/CNH.txt:30`、`common/bop/TIA.txt:30`

- 行 17–20，`GFX_idea_csp_power`

```
	spriteType = {
		name = "GFX_idea_csp_power"
		texturefile = "gfx/interface/ideas/CNH/csp_unions.png"
	}
```

  被引用：`common/bop/CNH.txt:18`、`common/bop/TIA.txt:18`

- 行 22–25，`GFX_idea_united_front_power`

```
	spriteType = {
		name = "GFX_idea_united_front_power"
		texturefile = "gfx/interface/ideas/CNH/united_front_csp_kmt.png"
	}
```

  被引用：`common/bop/CNH.txt:4`、`common/bop/CNH.txt:44`、`common/bop/TIA.txt:4`

- 行 27–30，`GFX_idea_a_divided_front_csp_kmt`

```
	spriteType = {
		name = "GFX_idea_a_divided_front_csp_kmt"
		texturefile = "gfx/interface/ideas/CNH/a_divided_frontt.png"
	}
```

  被引用：`common/ideas/commielegations_ideas.txt:754`、`common/ideas/commielegations_ideas.txt:797`、`common/ideas/commielegations_ideas.txt:888`、`common/ideas/commielegations_ideas.txt:905`、`common/ideas/commielegations_ideas.txt:966`、`common/ideas/commielegations_ideas.txt:1107`、`common/ideas/commielegations_ideas.txt:2005`、`common/ideas/commielegations_ideas.txt:2016` …共 18 处

- 行 37–40，`GFX_idea_jiang_qing_thought`

```
	spriteType = {
		name = "GFX_idea_jiang_qing_thought"
		texturefile = "gfx/interface/ideas/CNH/jiang_qing_thought.png"
	}
```

  被引用：`common/bop/CNH.txt:70`

- 行 42–45，`GFX_idea_lin_bioa_thought`

```
	spriteType = {
		name = "GFX_idea_lin_bioa_thought"
		texturefile = "gfx/interface/ideas/CNH/lin_bioa_thought.png"
	}
```

  被引用：`common/bop/CNH.txt:58`

- 行 47–50，`GFX_idea_chinese_power`

```
	spriteType = {
		name = "GFX_idea_chinese_power"
		texturefile = "gfx/interface/ideas/CNH/GFX_idea_sino_side.png"
	}
```

  被引用：`common/bop/CNH.txt:99`

- 行 51–54，`GFX_idea_unified_sino_soviets`

```
	spriteType = {
		name = "GFX_idea_unified_sino_soviets"
		texturefile = "gfx/interface/ideas/CNH/GFX_idea_sino_soviet_union.png"
	}
```

  被引用：`common/bop/CNH.txt:85`

- 行 55–58，`GFX_idea_soviet_power`

```
	spriteType = {
		name = "GFX_idea_soviet_power"
		texturefile = "gfx/interface/ideas/CNH/GFX_idea_soivet_side.png"
	}
```

  被引用：`common/bop/CNH.txt:111`

### `interface/RD_lu_xun_decisions.gfx` — 需保留 7 块 / 共 26 块

- 行 39–42，`GFX_decision_socialist_uprising_shanghai_icon`

```
	spriteType = {
		name = "GFX_decision_socialist_uprising_shanghai_icon"
		texturefile = "gfx/interface/decisions/LEC_LUXUN/socialist_uprising_shanghai.png"
	}
```

  被引用：`common/decisions/Shanghai_Commune_decisions.txt:293`、`common/decisions/Shanghai_Commune_decisions.txt:352`、`common/decisions/Shanghai_Commune_decisions.txt:409`、`common/decisions/Shanghai_Commune_decisions.txt:466`、`common/decisions/Shanghai_Commune_decisions.txt:518`、`common/decisions/Shanghai_Commune_decisions.txt:569`、`common/decisions/Shanghai_Commune_decisions.txt:620`、`common/decisions/Shanghai_Commune_decisions.txt:672` …共 19 处

- 行 44–47，`GFX_decision_rev_agriculture`

```
	spriteType = {
		name = "GFX_decision_rev_agriculture"
		texturefile = "gfx/interface/decisions/LEC_LUXUN/rev_agriculture.png"
	}
```

  被引用：`common/decisions/Japan_Socialist_decisions.txt:16`、`common/decisions/Japan_Socialist_decisions.txt:206`、`common/decisions/Shanghai_Commune_decisions.txt:1497`

- 行 69–72，`GFX_decision_revolution_agriculture`

```
	spriteType = {
		name = "GFX_decision_revolution_agriculture"
		texturefile = "gfx/interface/decisions/LEC_LUXUN/revolution_agriculture.png"
	}
```

  被引用：`common/decisions/categories/Shanghai_Commune_decision_categories.txt:83`

- 行 104–107，`GFX_category_image_uprising_shanghai_commune`

```
	spriteType = {
		name = "GFX_category_image_uprising_shanghai_commune"
		texturefile = "gfx/interface/decisions/LEC_LUXUN/GFX_decision_category_image_uprising_shanghai_commune.png"
	}
```

  被引用：`common/decisions/categories/Shanghai_Commune_decision_categories.txt:54`、`common/decisions/categories/Shanghai_Commune_decision_categories.txt:71`

- 行 109–112，`GFX_category_image_denounce_confucius`

```
	spriteType = {
		name = "GFX_category_image_denounce_confucius"
		texturefile = "gfx/interface/decisions/LEC_LUXUN/GFX_decision_category_image_denounce_confucius.png"
	}
```

  被引用：`common/decisions/categories/Shanghai_Commune_decision_categories.txt:108`

- 行 114–117，`GFX_category_image_new_arts`

```
	spriteType = {
		name = "GFX_category_image_new_arts"
		texturefile = "gfx/interface/decisions/LEC_LUXUN/GFX_decision_category_image_new_arts.png"
	}
```

  被引用：`common/decisions/categories/Shanghai_Commune_decision_categories.txt:123`

- 行 119–122，`GFX_category_image_leap_forward`

```
	spriteType = {
		name = "GFX_category_image_leap_forward"
		texturefile = "gfx/interface/decisions/LEC_LUXUN/GFX_decision_category_image_glf.png"
	}
```

  被引用：`common/decisions/categories/Shanghai_Commune_decision_categories.txt:144`、`common/decisions/categories/Shanghai_Commune_decision_categories.txt:156`、`common/decisions/categories/Shanghai_Commune_decision_categories.txt:168`

### `interface/focus-ZHA_customicons.gfx` — 需保留 5 块 / 共 58 块

- 行 40–43，`GFX_ZHA_integrate_zhongteju_members-248360`

```
	SpriteType = { 
		name = "GFX_ZHA_integrate_zhongteju_members-248360"
		texturefile = "gfx/interface/goals/GFX_ZHA_integrate_zhongteju_members-248360.dds"
	}
```

  被引用：`common/national_focus/Qing_Manchu.txt:7625`

- 行 78–81，`GFX_ZHA_rise_of_the_national_syndicalists-248360`

```
	SpriteType = { 
		name = "GFX_ZHA_rise_of_the_national_syndicalists-248360"
		texturefile = "gfx/interface/goals/GFX_ZHA_rise_of_the_national_syndicalists-248360.dds"
	}
```

  被引用：`common/national_focus/Qing_Manchu.txt:7580`

- 行 686–689，`GFX_ZHA_found_the_national_security_ministry-248360`

```
	SpriteType = { 
		name = "GFX_ZHA_found_the_national_security_ministry-248360"
		texturefile = "gfx/interface/goals/GFX_ZHA_found_the_national_security_ministry-248360.dds"
	}
```

  被引用：`common/national_focus/Qing_Manchu.txt:7709`

- 行 724–727，`GFX_ZHA_start_the_central_china_plan-248360`

```
	SpriteType = { 
		name = "GFX_ZHA_start_the_central_china_plan-248360"
		texturefile = "gfx/interface/goals/GFX_ZHA_start_the_central_china_plan-248360.dds"
	}
```

  被引用：`common/national_focus/Qing_Manchu.txt:7690`

- 行 762–765，`GFX_ZHA_continue_land_reform-248360`

```
	SpriteType = { 
		name = "GFX_ZHA_continue_land_reform-248360"
		texturefile = "gfx/interface/goals/GFX_ZHA_continue_land_reform-248360.dds"
	}
```

  被引用：`common/national_focus/Qing_Manchu.txt:7822`

### `interface/RD_event_pictures.gfx` — 需保留 4 块 / 共 42 块

- 行 71–74，`GFX_report_event_GXC_anarchist_rising`

```
		spriteType = {
		name = "GFX_report_event_GXC_anarchist_rising"
		texturefile = "gfx/event_pictures/East Asia/GXC_Anarchist/report_event_GXC_anarchist_rise.png"
		}
```

  被引用：`events/china_anarchists.txt:39`

- 行 77–80，`GFX_report_event_GXC_anarchist_fire`

```
		spriteType = {
		name = "GFX_report_event_GXC_anarchist_fire"
		texturefile = "gfx/event_pictures/East Asia/GXC_Anarchist/report_event_GXC_anarchist_fire.png"
		}
```

  被引用：`events/china_anarchists.txt:7`

- 行 82–85，`GFX_report_event_GXC_anarchist_fails`

```
		spriteType = {
		name = "GFX_report_event_GXC_anarchist_fails"
		texturefile = "gfx/event_pictures/East Asia/GXC_Anarchist/report_event_GXC_anarchist_fail.png"
		}
```

  被引用：`events/china_anarchists.txt:82`、`events/china_anarchists.txt:162`

- 行 87–90，`GFX_report_event_GXC_anarchist_succeed`

```
		spriteType = {
		name = "GFX_report_event_GXC_anarchist_succeed"
		texturefile = "gfx/event_pictures/East Asia/GXC_Anarchist/report_event_GXC_anarchist_succeed.png"
		}
```

  被引用：`events/china_anarchists.txt:111`、`events/china_anarchists.txt:196`、`events/china_anarchists.txt:233`、`events/china_anarchists.txt:274`、`events/china_anarchists.txt:320`、`events/china_anarchists.txt:366`、`events/china_anarchists.txt:402`、`events/china_anarchists.txt:438`

### `interface/focus-JAP_BLACKDRAG_customicons.gfx` — 需保留 4 块 / 共 78 块

- 行 40–43，`GFX_JAP_BLACKDRAG_the_path_of_war-248360`

```
	SpriteType = { 
		name = "GFX_JAP_BLACKDRAG_the_path_of_war-248360"
		texturefile = "gfx/interface/goals/GFX_JAP_BLACKDRAG_the_path_of_war-248360.dds"
	}
```

  被引用：`common/ideas/SCB_JAP_democracy_ideas.txt:343`、`common/national_focus/SCB_JAP_natunity_bureaucracy_military.txt:1217`

- 行 78–81，`GFX_JAP_BLACKDRAG_uchida_faction-248360`

```
	SpriteType = { 
		name = "GFX_JAP_BLACKDRAG_uchida_faction-248360"
		texturefile = "gfx/interface/goals/GFX_JAP_BLACKDRAG_uchida_faction-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:5995`

- 行 914–917，`GFX_JAP_BLACKDRAG_oomoto_faction_victory-248360`

```
	SpriteType = { 
		name = "GFX_JAP_BLACKDRAG_oomoto_faction_victory-248360"
		texturefile = "gfx/interface/goals/GFX_JAP_BLACKDRAG_oomoto_faction_victory-248360.dds"
	}
```

  被引用：`SAVE_/Fengtian.txt:4726`、`common/national_focus/Fengtian.txt:4752`

- 行 952–955，`GFX_JAP_BLACKDRAG_the_path_of_peace-248360`

```
	SpriteType = { 
		name = "GFX_JAP_BLACKDRAG_the_path_of_peace-248360"
		texturefile = "gfx/interface/goals/GFX_JAP_BLACKDRAG_the_path_of_peace-248360.dds"
	}
```

  被引用：`SAVE_/Fengtian.txt:11481`、`common/national_focus/Fengtian.txt:11543`

### `interface/rework_JAP_goal.gfx` — 需保留 4 块 / 共 16 块

- 行 26–29，`GFX_goal_KR_ideology_national_populist`

```
	spriteType = {
		name = "GFX_goal_KR_ideology_national_populist"
		texturefile = "gfx/interface/goals/rework_JAP/KR_ideology_national_populist.png"
	}
```

  被引用：`common/national_focus/KR_Bulgaria.txt:20598`、`common/national_focus/Serbia.txt:10473`

- 行 30–33，`GFX_goal_KR_ideology_paternal_autocrat`

```
	spriteType = {
		name = "GFX_goal_KR_ideology_paternal_autocrat"
		texturefile = "gfx/interface/goals/rework_JAP/KR_ideology_paternal_autocrat.png"
	}
```

  被引用：`common/national_focus/KR_Bulgaria.txt:15275`、`common/national_focus/KR_Bulgaria.txt:20617`

- 行 50–53，`GFX_goal_KR_ideology_syndicalist`

```
	spriteType = {
		name = "GFX_goal_KR_ideology_syndicalist"
		texturefile = "gfx/interface/goals/rework_JAP/KR_ideology_syndicalist.png"
	}
```

  被引用：`common/national_focus/KR_Bulgaria.txt:20579`

- 行 54–57，`GFX_goal_KR_ideology_totalist`

```
	spriteType = {
		name = "GFX_goal_KR_ideology_totalist"
		texturefile = "gfx/interface/goals/rework_JAP/KR_ideology_totalist.png"
	}
```

  被引用：`common/national_focus/KR_Bulgaria.txt:21130`、`common/national_focus/Serbia.txt:9643`

### `interface/RD_Philippines_ideas.gfx` — 需保留 2 块 / 共 347 块

- 行 1342–1345，`GFX_idea_PHI_Vincente_Soto_eco_sde`

```
	spriteType = {
		name = "GFX_idea_PHI_Vincente_Soto_eco_sde"
		texturefile = "gfx/interface/ministers/PHI/PHI_Vincente_Soto_eco_sde.png"
	}
```

  被引用：`common/ideas/Philippines_ministers_RD.txt:396`

- 行 1354–1357，`GFX_idea_PHI_Lius_Taruc_eco_rso`

```
	spriteType = {
		name = "GFX_idea_PHI_Lius_Taruc_eco_rso"
		texturefile = "gfx/interface/ministers/PHI/PHI_Luis_Taruc.png"
	}
```

  被引用：`common/ideas/Philippines_ministers_RD.txt:216`

### `interface/RD_Shanxi_ministers.gfx` — 需保留 2 块 / 共 18 块

- 行 3–6，`GFX_bop_SHX_yan_xishan_side`

```
	spriteType = {
		name = "GFX_bop_SHX_yan_xishan_side"
		texturefile = "gfx/interface/bop/bop_SHX_yan_xishan_side.png"
	}
```

  被引用：`common/bop/SHX.txt:11`

- 行 8–11，`GFX_bop_SHX_feng_yuxiang_side`

```
	spriteType = {
		name = "GFX_bop_SHX_feng_yuxiang_side"
		texturefile = "gfx/interface/bop/bop_SHX_feng_yuxiang_side.png"
	}
```

  被引用：`common/bop/SHX.txt:92`

### `interface/focus-GXCECON_customicons.gfx` — 需保留 2 块 / 共 764 块

- 行 3050–3053，`GFX_goal_QIO_revolutionary_zone`

```
	SpriteType = { 
		name = "GFX_goal_QIO_revolutionary_zone"
		texturefile = "gfx/interface/goals/GFX_goal_QIO_revolutionary_zone.png"
	}
```

  被引用：`common/national_focus/FX_Philippines.txt:1653`、`common/national_focus/FX_Philippines.txt:1676`、`common/national_focus/FX_Philippines.txt:9725`、`common/national_focus/FX_Philippines.txt:9757`、`common/national_focus/FX_Philippines.txt:9795`、`common/national_focus/FX_Philippines.txt:9821`、`common/national_focus/FX_Philippines.txt:9838`、`common/national_focus/FX_Philippines.txt:9856` …共 259 处

- 行 3088–3091，`GFX_goal_QIO_revolution`

```
	SpriteType = { 
		name = "GFX_goal_QIO_revolution"
		texturefile = "gfx/interface/goals/GFX_goal_QIO_revolution.png"
	}
```

  被引用：`common/national_focus/FX_Philippines.txt:9694`、`common/national_focus/FX_Philippines.txt:9990`、`common/national_focus/FX_Philippines.txt:10214`、`common/national_focus/FX_Philippines.txt:10481`、`common/national_focus/FX_Philippines.txt:10735`、`common/national_focus/FX_Philippines.txt:11036`、`common/national_focus/FX_Philippines.txt:11306`、`common/national_focus/FX_Philippines.txt:11527` …共 15 处

### `interface/focus-JAPARMY_customicons.gfx` — 需保留 2 块 / 共 112 块

- 行 116–119，`GFX_JAPARMY_reform_the_disarmament_policy-248360`

```
	SpriteType = { 
		name = "GFX_JAPARMY_reform_the_disarmament_policy-248360"
		texturefile = "gfx/interface/goals/GFX_JAPARMY_reform_the_disarmament_policy-248360.dds"
	}
```

  被引用：`common/national_focus/SCB_JAP_democracy_soccon_marlib.txt:1415`

- 行 1104–1107，`GFX_JAPARMY_new_organization_targets-248360`

```
	SpriteType = { 
		name = "GFX_JAPARMY_new_organization_targets-248360"
		texturefile = "gfx/interface/goals/GFX_JAPARMY_new_organization_targets-248360.dds"
	}
```

  被引用：`common/national_focus/SCB_JAP_democracy_soccon_marlib.txt:1467`

### `interface/focus-JAPKOKUMIN_customicons.gfx` — 需保留 2 块 / 共 36 块

- 行 534–537，`GFX_JAPKOKUMIN_maintaining_the_controlled_economy-248360`

```
	SpriteType = { 
		name = "GFX_JAPKOKUMIN_maintaining_the_controlled_economy-248360"
		texturefile = "gfx/interface/goals/GFX_JAPKOKUMIN_maintaining_the_controlled_economy-248360.dds"
	}
```

  被引用：`common/national_focus/SCB_JAP_democracy_soccon_marlib.txt:1249`

- 行 572–575，`GFX_JAPKOKUMIN_japanesemanchurian_union-248360`

```
	SpriteType = { 
		name = "GFX_JAPKOKUMIN_japanesemanchurian_union-248360"
		texturefile = "gfx/interface/goals/GFX_JAPKOKUMIN_japanesemanchurian_union-248360.dds"
	}
```

  被引用：`common/national_focus/SCB_JAP_natunity_bureaucracy_military.txt:1185`

### `interface/focus-JAPTOSEIHA_customicons.gfx` — 需保留 2 块 / 共 108 块

- 行 1750–1753，`GFX_JAPTOSEIHA_form_the_greater_asia_association-248360`

```
	SpriteType = { 
		name = "GFX_JAPTOSEIHA_form_the_greater_asia_association-248360"
		texturefile = "gfx/interface/goals/GFX_JAPTOSEIHA_form_the_greater_asia_association-248360.dds"
	}
```

  被引用：`common/national_focus/Shandong_Clique.txt:6422`

- 行 1940–1943，`GFX_JAPTOSEIHA_the_course_shall_shine_for_asia-248360`

```
	SpriteType = { 
		name = "GFX_JAPTOSEIHA_the_course_shall_shine_for_asia-248360"
		texturefile = "gfx/interface/goals/GFX_JAPTOSEIHA_the_course_shall_shine_for_asia-248360.dds"
	}
```

  被引用：`common/national_focus/SCB_JAP_democracy_soccon_marlib.txt:159`

### `interface/RD_Japan_Rework_decisions.gfx` — 需保留 1 块 / 共 5 块

- 行 7–10，`GFX_category_JAP_congress_icon`

```
	spriteType = {
		name = "GFX_category_JAP_congress_icon"
		texturefile = "gfx/interface/decisions/JAP_Rework/GFX_decision_JAP_congress_icon.png"
	}
```

  被引用：`common/decisions/categories/Japan_Socialist_decision_categoties.txt:3`、`common/decisions/categories/Japan_Socialist_decision_categoties.txt:22`、`common/decisions/categories/Japan_Socialist_decision_categoties.txt:35`、`common/decisions/categories/Japan_Socialist_decision_categoties.txt:49`

### `interface/RD_Japan_Rework_ideas.gfx` — 需保留 1 块 / 共 62 块

- 行 196–199，`GFX_idea_generic_agrarian_reform`

```
	spriteType = {
		name = "GFX_idea_generic_agrarian_reform"
		texturefile = "gfx/interface/ideas/JAP/generic_agrarian_reform.png"
	}
```

  被引用：`common/dynamic_modifiers/SHX dynamic_modifier.txt:103`、`common/dynamic_modifiers/SHX dynamic_modifier.txt:117`

### `interface/RD_game_rules_flags.gfx` — 需保留 1 块 / 共 13 块

- 行 31–35，`GFX_KR_game_rule_flag_TAI`

```
	spriteType = {
		name = "GFX_KR_game_rule_flag_TAI"
		texturefile = "gfx/flags/small/TWI_FORMOSA.tga"
		legacy_lazy_load = no
	}
```

  被引用：`localisation/kxxfix_game_rules_l_simp_chinese.yml:42`、`localisation/kxxfix_game_rules_l_simp_chinese.yml:44`、`localisation/kxxfix_game_rules_l_simp_chinese.yml:46`、`localisation/kxxfix_game_rules_l_simp_chinese.yml:48`、`localisation/kxxfix_game_rules_l_simp_chinese.yml:54`、`localisation/kxxfix_game_rules_l_simp_chinese.yml:56`、`localisation/kxxfix_game_rules_l_simp_chinese.yml:58`、`localisation/kxxfix_game_rules_l_simp_chinese.yml:60` …共 14 处

### `interface/RD_lu_xun_ideas.gfx` — 需保留 1 块 / 共 52 块

- 行 33–36，`GFX_idea_LEC_Ah_Q`

```
	spriteType = {
		name = "GFX_idea_LEC_Ah_Q"
		texturefile = "gfx/interface/ideas/LUXUN/GFX_idea_LEC_Ah_Q.png"
	}
```

  被引用：`common/ideas/lu_xun_ideas.txt:275`

### `interface/TAI_goals.gfx` — 需保留 1 块 / 共 96 块

- 行 182–186，`Taiwan_Colony`

```
		spriteType = {
		name = "Taiwan_Colony"
		texturefile = "gfx/interface/goals/taiwan/Taiwan_Colony.png"
		legacy_lazy_load = no
		}
```

  被引用：`interface/FX_goals.gfx:8412`、`interface/FX_goals_shine.gfx:67266`、`interface/FX_goals_shine.gfx:67269`、`interface/FX_goals_shine.gfx:67282`

### `interface/focus-CAMDEMSOC_customicons.gfx` — 需保留 1 块 / 共 50 块

- 行 496–499，`GFX_CAMDEMSOC_increase_resource_extraction-248360`

```
	SpriteType = { 
		name = "GFX_CAMDEMSOC_increase_resource_extraction-248360"
		texturefile = "gfx/interface/goals/GFX_CAMDEMSOC_increase_resource_extraction-248360.dds"
	}
```

  被引用：`common/national_focus/French_Nationalist_Empire.txt:4434`

### `interface/focus-JAPFOR_customicons.gfx` — 需保留 1 块 / 共 50 块

- 行 458–461，`GFX_JAPFOR_nanshinron-248360`

```
	SpriteType = { 
		name = "GFX_JAPFOR_nanshinron-248360"
		texturefile = "gfx/interface/goals/GFX_JAPFOR_nanshinron-248360.dds"
	}
```

  被引用：`common/national_focus/SCB_JAP_democracy_soccon_marlib.txt:1515`

### `interface/focus-JAPIRAARIGHTIST_customicons.gfx` — 需保留 1 块 / 共 86 块

- 行 268–271，`GFX_JAPIRAARIGHTIST_kiichirosvictory-248360`

```
	SpriteType = { 
		name = "GFX_JAPIRAARIGHTIST_kiichirosvictory-248360"
		texturefile = "gfx/interface/goals/GFX_JAPIRAARIGHTIST_kiichirosvictory-248360.dds"
	}
```

  被引用：`common/national_focus/SCB_JAP_democracy_soccon_marlib.txt:201`

### `interface/focus-JAPSOCDEM_customicons.gfx` — 需保留 1 块 / 共 62 块

- 行 952–955，`GFX_JAPSOCDEM_retain_the_parliamentary_system-248360`

```
	SpriteType = { 
		name = "GFX_JAPSOCDEM_retain_the_parliamentary_system-248360"
		texturefile = "gfx/interface/goals/GFX_JAPSOCDEM_retain_the_parliamentary_system-248360.dds"
	}
```

  被引用：`common/national_focus/SCB_JAP_democracy_soccon_marlib.txt:1210`

### `interface/focus-JAP_customicons.gfx` — 需保留 1 块 / 共 44 块

- 行 192–195，`GFX_JAP_instill_loyalty_to_the_military-2684`

```
	SpriteType = { 
		name = "GFX_JAP_instill_loyalty_to_the_military-2684"
		texturefile = "gfx/interface/goals/GFX_JAP_instill_loyalty_to_the_military-2684.dds"
	}
```

  被引用：`common/national_focus/SCB_JAP_democracy_soccon_marlib.txt:367`

### `interface/focus-PHI_customicons.gfx` — 需保留 1 块 / 共 110 块

- 行 1864–1867，`GFX_PHI_a_new_sun-445`

```
	SpriteType = { 
		name = "GFX_PHI_a_new_sun-445"
		texturefile = "gfx/interface/goals/GFX_PHI_a_new_sun-445.dds"
	}
```

  被引用：`common/national_focus/FX_Philippines.txt:9204`

### `interface/focus-RDHNNKMTUNI_customicons.gfx` — 需保留 1 块 / 共 96 块

- 行 458–461，`GFX_RDHNNKMTUNI_city_after_city_rises-248360`

```
	SpriteType = { 
		name = "GFX_RDHNNKMTUNI_city_after_city_rises-248360"
		texturefile = "gfx/interface/goals/GFX_RDHNNKMTUNI_city_after_city_rises-248360.dds"
	}
```

  被引用：`common/national_focus/French_Nationalist_Empire.txt:3936`

### `interface/focus-TAIECONO_customicons.gfx` — 需保留 1 块 / 共 58 块

- 行 230–233，`GFX_TAIECONO_claiming_austroneasia-248360`

```
	SpriteType = { 
		name = "GFX_TAIECONO_claiming_austroneasia-248360"
		texturefile = "gfx/interface/goals/GFX_TAIECONO_claiming_austroneasia-248360.dds"
	}
```

  被引用：`common/national_focus/FX_Philippines.txt:5746`


## 坏注册块（name 被截断，未计入“不能删”）

这些 spriteType 的 name 只剩很短的前缀（如 `GFX_`），贴图与引用都不可靠；保留它们只会引入无效注册。

### `interface/RD_Japan_event_pictures.gfx`（157 块）

```
行 359–362  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 364–367  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 369–372  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 374–377  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 379–382  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 384–387  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 389–392  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 394–397  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 399–402  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 404–407  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 409–412  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 414–417  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 419–422  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 424–427  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 429–432  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 434–437  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 439–442  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 444–447  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 449–452  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 454–457  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 459–462  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 464–467  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 469–472  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 474–477  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 479–482  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 484–487  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 489–492  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 494–497  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 499–502  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 504–507  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 509–512  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 514–517  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 519–522  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 524–527  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 529–532  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 534–537  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 539–542  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 544–547  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 549–552  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 554–557  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 559–562  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 564–567  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 569–572  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 574–577  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 579–582  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 584–587  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 589–592  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 594–597  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 599–602  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 604–607  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 609–612  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 614–617  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 619–622  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 624–627  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 629–632  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 634–637  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 639–642  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 644–647  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 649–652  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 654–657  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 659–662  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 664–667  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 669–672  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 674–677  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 679–682  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 684–687  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 689–692  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 694–697  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 699–702  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 704–707  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 709–712  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 714–717  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 719–722  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 724–727  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 729–732  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 734–737  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 739–742  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 744–747  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 749–752  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 754–757  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 759–762  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 764–767  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 769–772  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 774–777  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 779–782  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 784–787  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 789–792  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 794–797  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 799–802  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 804–807  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 809–812  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 814–817  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 819–822  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 824–827  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 829–832  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 834–837  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 839–842  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 844–847  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 849–852  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 854–857  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 859–862  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 864–867  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 869–872  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 874–877  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 879–882  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 884–887  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 889–892  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 894–897  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 899–902  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 904–907  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 909–912  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 914–917  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 919–922  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 924–927  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 929–932  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 934–937  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 939–942  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 944–947  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 949–952  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 954–957  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 959–962  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 964–967  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 969–972  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 974–977  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 979–982  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 984–987  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 989–992  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 994–997  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 999–1002  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 1004–1007  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 1009–1012  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 1014–1017  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 1019–1022  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 1024–1027  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 1029–1032  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 1034–1037  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 1039–1042  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 1044–1047  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 1049–1052  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 1054–1057  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 1059–1062  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 1064–1067  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 1069–1072  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 1074–1077  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 1079–1082  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 1084–1087  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 1089–1092  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 1094–1097  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 1099–1102  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 1104–1107  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 1109–1112  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 1114–1117  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 1119–1122  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 1124–1127  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 1129–1132  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 1134–1137  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
行 1139–1142  name=GFX_  tex=gfx/event_pictures/East Asia/Japan/Katayama.png
```


## 不能删的图片

| 图片 | 引用处（最多 5 个） |
|---|---|
| `gfx/enhancedsuperevents/spevnt_japanese_america.png` | `interface/KXX_Super_Events.gfx:613` |
| `gfx/event_pictures/chl/rise_of_japan.png` | `interface/AbsurdDrama/KX_Chile_event_pictures.gfx:49`、`interface/KX_Chile_event_pictures.gfx:49` |
| `gfx/event_pictures/jap/jap_daihonei_army.png` | `interface/KXX_JAP_event_pictures.gfx:20` |
| `gfx/event_pictures/jap/jap_kinzokugen_event.png` | `interface/KXX_JAP_event_pictures.gfx:25` |
| `gfx/event_pictures/jap/jap_koiso_kuniaki_event.png` | `interface/KXX_JAP_event_pictures.gfx:15` |
| `gfx/event_pictures/jap/jap_seiyukai_all_leader.png` | `interface/KXX_JAP_event_pictures.gfx:5` |
| `gfx/event_pictures/jap/jap_shinseiryujinkai.png` | `interface/KXX_JAP_event_pictures.gfx:10` |
| `gfx/event_pictures/jap/jap_tokugawa_yoshinobu.png` | `interface/KXX_JAP_event_pictures.gfx:30` |
| `gfx/event_pictures/world_news/gfx_attack_japs.dds` | `interface/RF_Yudabajiao_eventpictures.gfx:98` |
| `gfx/flags/medium/jap_red_army.tga` | `interface/KXX_welcome_splash.gfx:180` |
| `gfx/interface/decisions/gfx_decision_cat_jap_sakurakai_plot_picture.dds` | `interface/PB_decisions.gfx:169` |
| `gfx/interface/decisions/jap_rework/gfx_decision_jap_congress_icon.png` |  |
| `gfx/interface/goals/arz_arizona_and_japan.png` | `interface/KXX_ARZ_goals.gfx:60`、`interface/KXX_ARZ_goals_shine.gfx:452`、`interface/KXX_ARZ_goals_shine.gfx:455`、`interface/KXX_ARZ_goals_shine.gfx:468` |
| `gfx/interface/goals/blr/blr_finland_to_japan.tga` | `interface/BLR_goals.gfx:198`、`interface/BLR_goals_shine.gfx:1515`、`interface/BLR_goals_shine.gfx:1518`、`interface/BLR_goals_shine.gfx:1531`、`interface/RF_goals.gfx:1215` …共 8 处 |
| `gfx/interface/goals/cal/cal_another_tokyo.png` | `interface/CAL_goals.gfx:286`、`interface/CAL_goals_shine.gfx:2149`、`interface/CAL_goals_shine.gfx:2152`、`interface/CAL_goals_shine.gfx:2165` |
| `gfx/interface/goals/cal/cal_connect_jap.png` | `interface/CAL_goals.gfx:234`、`interface/CAL_goals_shine.gfx:1746`、`interface/CAL_goals_shine.gfx:1749`、`interface/CAL_goals_shine.gfx:1762` |
| `gfx/interface/goals/cal/cal_follow_pro_japanese_groups.png` | `interface/CAL_goals.gfx:242`、`interface/CAL_goals_shine.gfx:1808`、`interface/CAL_goals_shine.gfx:1811`、`interface/CAL_goals_shine.gfx:1824` |
| `gfx/interface/goals/cal/cal_fuck_u_jap.png` | `interface/CAL_goals.gfx:270`、`interface/CAL_goals_shine.gfx:2025`、`interface/CAL_goals_shine.gfx:2028`、`interface/CAL_goals_shine.gfx:2041` |
| `gfx/interface/goals/cal/cal_invite_japanese_enterprises.png` | `interface/CAL_goals.gfx:250`、`interface/CAL_goals_shine.gfx:1870`、`interface/CAL_goals_shine.gfx:1873`、`interface/CAL_goals_shine.gfx:1886` |
| `gfx/interface/goals/cal/cal_japan_is_watching_u.png` | `interface/CAL_goals.gfx:266`、`interface/CAL_goals_shine.gfx:1994`、`interface/CAL_goals_shine.gfx:1997`、`interface/CAL_goals_shine.gfx:2010` |
| `gfx/interface/goals/cal/cal_shadow_samurai.png` | `interface/CAL_goals.gfx:274`、`interface/CAL_goals_shine.gfx:2056`、`interface/CAL_goals_shine.gfx:2059`、`interface/CAL_goals_shine.gfx:2072` |
| `gfx/interface/goals/cal/destroy_japan.dds` | `interface/Ble_goals_shine.gfx:157`、`interface/Ble_goals_shine.gfx:160`、`interface/ble_goals.gfx:45` |
| `gfx/interface/goals/gea_incite_japanese_colonies.png` | `interface/GEA_goals.gfx:508`、`interface/GEA_goals_shine.gfx:4034`、`interface/GEA_goals_shine.gfx:4037`、`interface/GEA_goals_shine.gfx:4050` |
| `gfx/interface/goals/gfx_china_foreign_policy_extending_the_5_tibetan_fingers-248360.dds` |  |
| `gfx/interface/goals/gfx_jap_blackdrag_oomoto_faction_victory-248360.dds` |  |
| `gfx/interface/goals/gfx_jap_blackdrag_the_path_of_peace-248360.dds` |  |
| `gfx/interface/goals/gfx_jap_blackdrag_the_path_of_war-248360.dds` |  |
| `gfx/interface/goals/gfx_jap_blackdrag_uchida_faction-248360.dds` |  |
| `gfx/interface/goals/gfx_jap_instill_loyalty_to_the_military-2684.dds` |  |
| `gfx/interface/goals/gfx_jap_socfor_a_revolution_on_the_world_stage-248360.dds` |  |
| `gfx/interface/goals/gfx_jap_socfor_crush_the_colonialists_of_the_southern_seas-248360.dds` |  |
| `gfx/interface/goals/gfx_jap_socfor_hunting_the_big_bear-248360.dds` |  |
| `gfx/interface/goals/gfx_jap_socfor_liberate_the_former_colonies-248360.dds` |  |
| `gfx/interface/goals/gfx_jap_socfor_our_own_path_of_liberation-248360.dds` |  |
| `gfx/interface/goals/gfx_jap_socfor_proclaiming_the_red_star_above_india-248360.dds` |  |
| `gfx/interface/goals/gfx_jap_socfor_proclaiming_the_red_steppe-248360.dds` |  |
| `gfx/interface/goals/gfx_jap_socfor_promoting_the_global_revolution-248360.dds` |  |
| `gfx/interface/goals/gfx_jap_socfor_saving_the_far_east-248360.dds` |  |
| `gfx/interface/goals/gfx_jap_socfor_secure_central_asia-248360.dds` |  |
| `gfx/interface/goals/gfx_jap_socfor_securing_asia_under_socialism-248360.dds` |  |
| `gfx/interface/goals/gfx_jap_socfor_the_china_solution-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_a_liberated_lifestyle-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_a_loyal_figure-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_anarchosyndicalist_programme-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_burnthecrown-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_capitalshallcrumble-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_construct_proletarian_councils-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_court_the_jcp-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_crush_the_foreign_reactionaries-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_dadaism_realized-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_denounce_the_crown_of_evil-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_denounce_the_monks-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_embrace_the_monks-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_expression_through_living-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_form_the_eight_days_committee-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_forming_workers_cooperatives-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_formthetsujijunkoenkai-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_from_our_declaration-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_iamthetengu-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_idolize_the_cooperative_movement-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_in_the_embrace_of_pure_anarchism-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_integrate_the_imperial_unions-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_japanshallbefree-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_legacy_of_imperial_anarchism-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_mutualist_economic_program-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_our_korean_comrades-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_promotingcommunalagrarianism-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_promotingthelocallife-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_purge_the_nobility-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_radicalize_the_art_circles-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_reconciliation_movement-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_reforming_the_zenkoku_jiren-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_removing_the_oppressive_classes-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_renounce_feudalism-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_revolution_against_the_old-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_revolution_for_the_young-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_revolutionary_expansion-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_rule_of_the_council-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_sanshirosanarchismleadsthenation-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_smash_the_zaibatsu-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_syncretic_anarchist_ethos-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_taking_revenge_on_the_yakuza-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_the_anarchist_shogunate-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_the_fight_against_discrimination-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_the_literary_revolution-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_the_old_guard_of_japanese_socialism-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_the_path_of_liberation-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_the_towers_surpass_the_clouds_again-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_true_anarchism_rises-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_understanding_the_peasantry-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_unite_the_zenkoku_and_kyushu_organizations-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_uniting_the_japanese_anarchist_movement-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_upholding_the_showa-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_whatsgoingoninthepsychward-248360.dds` |  |
| `gfx/interface/goals/gfx_japana_writing_the_true_anarchist_manifesto-248360.dds` |  |
| `gfx/interface/goals/gfx_japaraki_a_promise_to_the_peasant_soldiers-248360.dds` |  |
| `gfx/interface/goals/gfx_japaraki_araki_at_the_helm-248360.dds` |  |
| `gfx/interface/goals/gfx_japaraki_connectingtheemperorthelandandthepeople-248360.dds` |  |
| `gfx/interface/goals/gfx_japaraki_continued_the_zaibatsu_nationalisation-248360.dds` |  |
| `gfx/interface/goals/gfx_japaraki_crush_ugaki_thought-248360.dds` |  |
| `gfx/interface/goals/gfx_japaraki_extending_the_fist_of_military_might-248360.dds` |  |
| `gfx/interface/goals/gfx_japaraki_kokutai_no_hongi-248360.dds` |  |
| `gfx/interface/goals/gfx_japaraki_national_spiritual_mobilisation-248360.dds` |  |
| `gfx/interface/goals/gfx_japaraki_organize_rural_cooperatives-248360.dds` |  |
| `gfx/interface/goals/gfx_japaraki_preparing_for_total_war-248360.dds` |  |
| `gfx/interface/goals/gfx_japaraki_rally_the_tonarigumi-248360.dds` |  |
| `gfx/interface/goals/gfx_japaraki_reinforce_security_of_the_state-248360.dds` |  |
| `gfx/interface/goals/gfx_japaraki_spiritual_training-248360.dds` |  |
| `gfx/interface/goals/gfx_japaraki_the_autarky_economic_solution-248360.dds` |  |
| `gfx/interface/goals/gfx_japaraki_the_bamboo_spear_slay_our_enemies-248360.dds` |  |
| `gfx/interface/goals/gfx_japaraki_the_military_leap-248360.dds` |  |
| `gfx/interface/goals/gfx_japaraki_the_spiritual_leap-248360.dds` |  |
| `gfx/interface/goals/gfx_japarmy_new_organization_targets-248360.dds` |  |
| `gfx/interface/goals/gfx_japarmy_reform_the_disarmament_policy-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_a_general_strike_for_the_proletarian-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_a_japanese_cultural_revolution-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_a_japanese_renaissance-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_a_revolution_under_party_control-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_a_revolutionary_research_cult-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_a_struggle_against_socialreactionarism-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_a_struggle_against_spies-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_agitative_propaganda-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_akahata_no_uta-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_antiimperialist_rationalization-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_appealing_for_3rd_internationale_support-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_birth_of_the_proletarian_youth_league-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_changingthecourseofjapansproletariat-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_cherry_blossoms_died_red-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_control_the_political_line-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_crush_yamakawa-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_dealing_with_the_emperor-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_defendingthepeoplesinterests-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_denounce_fukumotoism-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_denounce_the_liberal_menace-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_denounce_the_syndicalist_revisionists-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_denounce_the_yamakawaists-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_embracing_smiling_communism-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_emphasis_on_theory-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_enforce_democratic_centralism-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_focus_on_self_reliance-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_foreverapartyforeverarevolution-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_form_the_investigation_committee-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_formation_of_a_grass_roots_faction-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_formthekantowomensleague-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_found_the_national_pioneer_association-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_founding_of_the_industrial_labour_institute-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_glory_under_the_vanguard_party-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_honour_the_martyrs_of_the_revolution-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_increase_the_peasant_livelihood-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_injecting_the_marxist_conscious-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_international_contacts-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_invigorate_the_three_stage_program-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_japanslenin-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_kenzossyndicalistdream-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_legacy_of_japanese_syndicalism-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_legacy_of_the_action_group-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_legacy_of_the_farm_labour_party-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_legacy_of_the_new_men_society-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_longing_for_armed_struggle-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_marching_for_the_true_proletariat-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_militant_syndicalists_take_over_the_party-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_mobilise_the_masses-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_outsidethenationsborders-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_paris_syndicalists_secure_the_party-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_peasant_collaboration-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_proletarian_papers-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_promote_the_student_labour_society-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_promoting_a_true_party_of_the_masses-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_promoting_a_writers_revolution-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_promoting_the_social_revolution-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_promotion_of_revolutionary_marxism-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_proper_party_reconstruction-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_purge_the_antiproletarian_factions-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_question_of_the_emperor-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_question_of_the_royal_family-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_question_of_the_socialreactionaries-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_reach_out_to_the_masses-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_reach_out_to_the_workers-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_realisation_of_2_staged_revolution-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_red_intellectuals-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_remove_the_stain_of_feudalism-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_representing_all_the_workers_unions-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_revive_akahata-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_revive_the_labourliberty_society-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_revolutionary_bureaucracy-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_revolutionary_intellectualism-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_securing_the_state-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_socialism_in_one_country-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_strengthen_old_guard_influence-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_strengthening_the_ideological_united_front-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_struggle_of_the_literary_left-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_support_okinawan_independence-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_the_joint_rural_struggle-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_the_red_banner_over_tokyo-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_the_rising_sun_under_the_hammer_and_sickle-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_the_struggle_of_2-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_therevolutionsnewhome-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_true_japanese_communism-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_unification_of_the_trade_unions-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_universal_suffrage-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_upholding_true_leninism-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_victory_of_the_communist_hardliners-248360.dds` |  |
| `gfx/interface/goals/gfx_japcommunist_yamakawasrevolution-248360.dds` |  |
| `gfx/interface/goals/gfx_japfor_nanshinron-248360.dds` |  |
| `gfx/interface/goals/gfx_japiraarightist_kiichirosvictory-248360.dds` |  |
| `gfx/interface/goals/gfx_japkokumin_japanesemanchurian_union-248360.dds` |  |
| `gfx/interface/goals/gfx_japkokumin_maintaining_the_controlled_economy-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_a_new_red_fleet-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_a_true_army_of_socialism-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_bicycle_brigades-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_birth_of_the_red_army-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_bring_out_the_armoured_beasts-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_centralize_army_discipline-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_centralized_approach-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_civil_war_recovery_plan-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_collectivisation-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_commissars_of_the_revolution-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_committing_to_the_5_year_plan-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_communalisation-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_communalised_cafeterias-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_cooperative_farming-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_decentralized_economics-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_fixing_the_economy-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_flying_high_above_the_sky-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_form_industrial_cooperatives-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_i_am_a_black_smith-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_keep_the_militias-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_land_lord_trials-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_land_moderation-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_land_to_the_tiller-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_massmobilization_doctrine-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_national_railroad_construction-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_new_radar_links-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_night_raids-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_organizingthepeoplesarmy-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_oursoldiersshallswimfly-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_protecting_the_revolutionary_red_sun-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_radical_redistribution-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_rebuild_the_hiroshima_shipyards-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_rehabilitatingpows-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_son_kosakutai-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_starting_the_land_reformation-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_strengthen_urban_industrial_centres-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_thepeoplesnavy-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_understanding_motorization-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_up_high_in_the_mountains-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_violent_land_revolution-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_working_another_day_for_the_masses_of_the_commune-248360.dds` |  |
| `gfx/interface/goals/gfx_japrecovery_working_on_the_agrarian_economy-248360.dds` |  |
| `gfx/interface/goals/gfx_japsocdem_retain_the_parliamentary_system-248360.dds` |  |
| `gfx/interface/goals/gfx_japsocialism_cooperation_with_the_unions-248360.dds` |  |
| `gfx/interface/goals/gfx_japsocialism_letsdoourbest-248360.dds` |  |
| `gfx/interface/goals/gfx_japsocialism_liaison_with_shanghai_contacts-248360.dds` |  |
| `gfx/interface/goals/gfx_japsocialism_organize_peasant_uprisings-248360.dds` |  |
| `gfx/interface/goals/gfx_japsocialism_organize_the_farmers-248360.dds` |  |
| `gfx/interface/goals/gfx_japsocialism_seek_internationale_aid-248360.dds` |  |
| `gfx/interface/goals/gfx_japsocialism_striking_for_more_than_a_day-248360.dds` |  |
| `gfx/interface/goals/gfx_japsocialism_the_revolution_is_calling-248360.dds` |  |
| `gfx/interface/goals/gfx_japsocialism_theredflagflieshighovertokyo-248360.dds` |  |
| `gfx/interface/goals/gfx_japsocialism_war_socialism-248360.dds` |  |
| `gfx/interface/goals/gfx_japtoseiha_form_the_greater_asia_association-248360.dds` |  |
| `gfx/interface/goals/gfx_japtoseiha_the_course_shall_shine_for_asia-248360.dds` |  |
| `gfx/interface/goals/gfx_sqitwo_anti_japanese_revanchism-248360.dds` |  |
| `gfx/interface/goals/gfx_sqitwo_arrest_japanese_diplomats-248360.dds` |  |
| `gfx/interface/goals/gfx_sqitwo_denouncing_the_japanese_menance-248360.dds` |  |
| `gfx/interface/goals/gfx_sqitwo_humiliate_hirohito-248360.dds` |  |
| `gfx/interface/goals/gfx_sqitwo_support_the_korean_revolution-248360.dds` |  |
| `gfx/interface/goals/gfx_sqitwo_talks_with_korean_exiles-248360.dds` |  |
| `gfx/interface/goals/gfx_sqitwo_thepeoplesantijapaneserevolution-248360.dds` |  |
| `gfx/interface/goals/gfx_sqitwo_uniting_the_left_against_japan-248360.dds` |  |
| `gfx/interface/goals/gfx_taiecono_claiming_austroneasia-248360.dds` |  |
| `gfx/interface/goals/gfx_vnq_2_defend_against_japanese_imperialism-248360.dds` |  |
| `gfx/interface/goals/kmt/kmt_start_taichi.dds` | `interface/RF_Yudabajiao_goals.gfx:1025`、`interface/RF_Yudabajiao_goals_shine.gfx:7764`、`interface/RF_Yudabajiao_goals_shine.gfx:7767`、`interface/RF_Yudabajiao_goals_shine.gfx:7780` |
| `gfx/interface/goals/kxx_fx/generic_attack_tibet.png` | `interface/FX_goals.gfx:3012`、`interface/FX_goals_shine.gfx:24066`、`interface/FX_goals_shine.gfx:24069`、`interface/FX_goals_shine.gfx:24082` |
| `gfx/interface/goals/kxx_fx/korea_colony.png` | `interface/FX_goals.gfx:5764`、`interface/FX_goals_shine.gfx:46082`、`interface/FX_goals_shine.gfx:46085`、`interface/FX_goals_shine.gfx:46098` |
| `gfx/interface/goals/kxx_fx/phi_support_korea.png` | `interface/FX_goals.gfx:7064`、`interface/FX_goals_shine.gfx:56482`、`interface/FX_goals_shine.gfx:56485`、`interface/FX_goals_shine.gfx:56498` |
| `gfx/interface/goals/kxx_fx/taiwan_colony.png` | `interface/FX_goals.gfx:8412`、`interface/FX_goals_shine.gfx:67266`、`interface/FX_goals_shine.gfx:67269`、`interface/FX_goals_shine.gfx:67282` |
| `gfx/interface/goals/kxx_fx/the_korean_problem.png` | `interface/FX_goals.gfx:5768`、`interface/FX_goals_shine.gfx:46114`、`interface/FX_goals_shine.gfx:46117`、`interface/FX_goals_shine.gfx:46130` |
| `gfx/interface/goals/kxx_fx/zhi_tibet.png` | `interface/FX_goals.gfx:9028`、`interface/FX_goals_shine.gfx:72194`、`interface/FX_goals_shine.gfx:72197`、`interface/FX_goals_shine.gfx:72210` |
| `gfx/interface/goals/mns/gfx_mns_invite_japanese_scientists-82547.dds` | `interface/RF_goals.gfx:10338`、`interface/RF_goals_shine.gfx:82379`、`interface/RF_goals_shine.gfx:82382`、`interface/RF_goals_shine.gfx:82395` |
| `gfx/interface/goals/pb_goals/chi_attack_tibet.dds` | `interface/PB_Goals.gfx:3472`、`interface/PB_Goals_shine.gfx:20825`、`interface/PB_Goals_shine.gfx:20828`、`interface/PB_Goals_shine.gfx:20840` |
| `gfx/interface/goals/pb_goals/chi_imperial_federation_tibet.dds` | `interface/PB_Goals.gfx:3492`、`interface/PB_Goals_shine.gfx:20945`、`interface/PB_Goals_shine.gfx:20948`、`interface/PB_Goals_shine.gfx:20960` |
| `gfx/interface/goals/pb_goals/chi_tibet_campaign.dds` | `interface/PB_Goals.gfx:3377`、`interface/PB_Goals_shine.gfx:20255`、`interface/PB_Goals_shine.gfx:20258`、`interface/PB_Goals_shine.gfx:20270` |
| `gfx/interface/goals/pb_goals/generic_republican_japan.dds` | `interface/PB_Goals.gfx:1674`、`interface/PB_Goals_shine.gfx:9515`、`interface/PB_Goals_shine.gfx:9518`、`interface/PB_Goals_shine.gfx:9530` |
| `gfx/interface/goals/pb_goals/generic_republican_japanese_army.dds` | `interface/PB_Goals.gfx:894`、`interface/PB_Goals_shine.gfx:4835`、`interface/PB_Goals_shine.gfx:4838`、`interface/PB_Goals_shine.gfx:4850` |
| `gfx/interface/goals/pb_goals/generic_republican_japanese_diplomacy.dds` | `interface/PB_Goals.gfx:1299`、`interface/PB_Goals_shine.gfx:7265`、`interface/PB_Goals_shine.gfx:7268`、`interface/PB_Goals_shine.gfx:7280` |
| `gfx/interface/goals/pb_goals/generic_republican_japanese_tanks.dds` | `interface/PB_Goals.gfx:899`、`interface/PB_Goals_shine.gfx:4865`、`interface/PB_Goals_shine.gfx:4868`、`interface/PB_Goals_shine.gfx:4880` |
| `gfx/interface/goals/pb_goals/jap_co_prosperity_sphere.dds` | `interface/PB_Goals.gfx:4010`、`interface/PB_Goals_shine.gfx:23975`、`interface/PB_Goals_shine.gfx:23978`、`interface/PB_Goals_shine.gfx:23990` |
| `gfx/interface/goals/pb_goals/jap_exploit_the_chaos.dds` | `interface/PB_Goals.gfx:4020`、`interface/PB_Goals_shine.gfx:24035`、`interface/PB_Goals_shine.gfx:24038`、`interface/PB_Goals_shine.gfx:24050` |
| `gfx/interface/goals/pb_goals/jap_fate_of_hashimoto.dds` | `interface/PB_Goals.gfx:4005`、`interface/PB_Goals_shine.gfx:23945`、`interface/PB_Goals_shine.gfx:23948`、`interface/PB_Goals_shine.gfx:23960` |
| `gfx/interface/goals/pb_goals/jap_japanese_glory.dds` | `interface/PB_Goals.gfx:4030`、`interface/PB_Goals_shine.gfx:24095`、`interface/PB_Goals_shine.gfx:24098`、`interface/PB_Goals_shine.gfx:24110` |
| `gfx/interface/goals/pb_goals/jap_rightful_rule_returns.dds` | `interface/PB_Goals.gfx:4025`、`interface/PB_Goals_shine.gfx:24065`、`interface/PB_Goals_shine.gfx:24068`、`interface/PB_Goals_shine.gfx:24080` |
| `gfx/interface/goals/pb_goals/pb_eng_reconcile_japan.dds` | `interface/PB_Goals.gfx:6354`、`interface/PB_Goals_shine.gfx:41638`、`interface/PB_Goals_shine.gfx:41641`、`interface/PB_Goals_shine.gfx:41653` |
| `gfx/interface/goals/pb_goals/pb_eng_taiwan_issue.dds` | `interface/PB_Goals.gfx:6346`、`interface/PB_Goals_shine.gfx:41576`、`interface/PB_Goals_shine.gfx:41579`、`interface/PB_Goals_shine.gfx:41591` |
| `gfx/interface/goals/pb_goals/pb_jap_and_dont_deliver.dds` | `interface/PB_Goals.gfx:4970`、`interface/PB_Goals_shine.gfx:31145`、`interface/PB_Goals_shine.gfx:31148`、`interface/PB_Goals_shine.gfx:31160` |
| `gfx/interface/goals/pb_goals/pb_jap_contacts_in_army.dds` | `interface/PB_Goals.gfx:4978`、`interface/PB_Goals_shine.gfx:31205`、`interface/PB_Goals_shine.gfx:31208`、`interface/PB_Goals_shine.gfx:31220` |
| `gfx/interface/goals/pb_goals/pb_jap_contacts_in_navy.dds` | `interface/PB_Goals.gfx:4974`、`interface/PB_Goals_shine.gfx:31175`、`interface/PB_Goals_shine.gfx:31178`、`interface/PB_Goals_shine.gfx:31190` |
| `gfx/interface/goals/pb_goals/pb_jap_debates_on_military.dds` | `interface/PB_Goals.gfx:4934`、`interface/PB_Goals_shine.gfx:30875`、`interface/PB_Goals_shine.gfx:30878`、`interface/PB_Goals_shine.gfx:30890` |
| `gfx/interface/goals/pb_goals/pb_jap_debates_on_militias.dds` | `interface/PB_Goals.gfx:4930`、`interface/PB_Goals_shine.gfx:30845`、`interface/PB_Goals_shine.gfx:30848`、`interface/PB_Goals_shine.gfx:30860` |
| `gfx/interface/goals/pb_goals/pb_jap_debates_on_unions.dds` | `interface/PB_Goals.gfx:4926`、`interface/PB_Goals_shine.gfx:30815`、`interface/PB_Goals_shine.gfx:30818`、`interface/PB_Goals_shine.gfx:30830` |
| `gfx/interface/goals/pb_goals/pb_jap_empower_red_guards.dds` | `interface/PB_Goals.gfx:4954`、`interface/PB_Goals_shine.gfx:31025`、`interface/PB_Goals_shine.gfx:31028`、`interface/PB_Goals_shine.gfx:31040` |
| `gfx/interface/goals/pb_goals/pb_jap_future_of_republic.dds` | `interface/PB_Goals.gfx:4922`、`interface/PB_Goals_shine.gfx:30785`、`interface/PB_Goals_shine.gfx:30788`、`interface/PB_Goals_shine.gfx:30800` |
| `gfx/interface/goals/pb_goals/pb_jap_future_of_republic_hashimoto.dds` | `interface/PB_Goals.gfx:5038`、`interface/PB_Goals_shine.gfx:31655`、`interface/PB_Goals_shine.gfx:31658`、`interface/PB_Goals_shine.gfx:31670` |
| `gfx/interface/goals/pb_goals/pb_jap_hashimoto_breakneck_industrialization.dds` | `interface/PB_Goals.gfx:5050`、`interface/PB_Goals_shine.gfx:31745`、`interface/PB_Goals_shine.gfx:31748`、`interface/PB_Goals_shine.gfx:31760` |
| `gfx/interface/goals/pb_goals/pb_jap_hashimoto_denounce_democracy.dds` | `interface/PB_Goals.gfx:5042`、`interface/PB_Goals_shine.gfx:31685`、`interface/PB_Goals_shine.gfx:31688`、`interface/PB_Goals_shine.gfx:31700` |
| `gfx/interface/goals/pb_goals/pb_jap_hashimoto_embrace_ishii.dds` | `interface/PB_Goals.gfx:5062`、`interface/PB_Goals_shine.gfx:31835`、`interface/PB_Goals_shine.gfx:31838`、`interface/PB_Goals_shine.gfx:31850` |
| `gfx/interface/goals/pb_goals/pb_jap_hashimoto_red_bushido.dds` | `interface/PB_Goals.gfx:5046`、`interface/PB_Goals_shine.gfx:31715`、`interface/PB_Goals_shine.gfx:31718`、`interface/PB_Goals_shine.gfx:31730` |
| `gfx/interface/goals/pb_goals/pb_jap_hashimoto_red_bushido_new_tenant.dds` | `interface/PB_Goals.gfx:5066`、`interface/PB_Goals_shine.gfx:31865`、`interface/PB_Goals_shine.gfx:31868`、`interface/PB_Goals_shine.gfx:31880` |
| `gfx/interface/goals/pb_goals/pb_jap_hashimoto_womens_rights_reform.dds` | `interface/PB_Goals.gfx:5054`、`interface/PB_Goals_shine.gfx:31775`、`interface/PB_Goals_shine.gfx:31778`、`interface/PB_Goals_shine.gfx:31790` |
| `gfx/interface/goals/pb_goals/pb_jap_intensify_paranoia.dds` | `interface/PB_Goals.gfx:4966`、`interface/PB_Goals_shine.gfx:31115`、`interface/PB_Goals_shine.gfx:31118`、`interface/PB_Goals_shine.gfx:31130` |
| `gfx/interface/goals/pb_goals/pb_jap_ishii_coup.dds` | `interface/PB_Goals.gfx:5070`、`interface/PB_Goals_shine.gfx:31895`、`interface/PB_Goals_shine.gfx:31898`、`interface/PB_Goals_shine.gfx:31910` |
| `gfx/interface/goals/pb_goals/pb_jap_loyalty_oaths.dds` | `interface/PB_Goals.gfx:4962`、`interface/PB_Goals_shine.gfx:31085`、`interface/PB_Goals_shine.gfx:31088`、`interface/PB_Goals_shine.gfx:31100` |
| `gfx/interface/goals/pb_goals/pb_jap_make_shit_up.dds` | `interface/PB_Goals.gfx:4958`、`interface/PB_Goals_shine.gfx:31055`、`interface/PB_Goals_shine.gfx:31058`、`interface/PB_Goals_shine.gfx:31070` |
| `gfx/interface/goals/pb_goals/pb_jap_party_congress_conclusion.dds` | `interface/PB_Goals.gfx:4938`、`interface/PB_Goals_shine.gfx:30905`、`interface/PB_Goals_shine.gfx:30908`、`interface/PB_Goals_shine.gfx:30920` |
| `gfx/interface/goals/pb_goals/pb_jap_promise_autonomy.dds` | `interface/PB_Goals.gfx:4990`、`interface/PB_Goals_shine.gfx:31295`、`interface/PB_Goals_shine.gfx:31298`、`interface/PB_Goals_shine.gfx:31310` |
| `gfx/interface/goals/pb_goals/pb_jap_promise_reforms.dds` | `interface/PB_Goals.gfx:4986`、`interface/PB_Goals_shine.gfx:31265`、`interface/PB_Goals_shine.gfx:31268`、`interface/PB_Goals_shine.gfx:31280` |
| `gfx/interface/goals/pb_goals/pb_jap_purge_army.dds` | `interface/PB_Goals.gfx:4946`、`interface/PB_Goals_shine.gfx:30965`、`interface/PB_Goals_shine.gfx:30968`、`interface/PB_Goals_shine.gfx:30980` |
| `gfx/interface/goals/pb_goals/pb_jap_purge_bureaucrats.dds` | `interface/PB_Goals.gfx:4950`、`interface/PB_Goals_shine.gfx:30995`、`interface/PB_Goals_shine.gfx:30998`、`interface/PB_Goals_shine.gfx:31010` |
| `gfx/interface/goals/pb_goals/pb_jap_purge_navy.dds` | `interface/PB_Goals.gfx:4942`、`interface/PB_Goals_shine.gfx:30935`、`interface/PB_Goals_shine.gfx:30938`、`interface/PB_Goals_shine.gfx:30950` |
| `gfx/interface/goals/pb_goals/pb_jap_tea_with_anarchists.dds` | `interface/PB_Goals.gfx:4982`、`interface/PB_Goals_shine.gfx:31235`、`interface/PB_Goals_shine.gfx:31238`、`interface/PB_Goals_shine.gfx:31250` |
| `gfx/interface/goals/pb_goals/pb_jap_wild_promises.dds` | `interface/PB_Goals.gfx:4994`、`interface/PB_Goals_shine.gfx:31325`、`interface/PB_Goals_shine.gfx:31328`、`interface/PB_Goals_shine.gfx:31340` |
| `gfx/interface/goals/rework_jap/kr_ideology_national_populist.png` |  |
| `gfx/interface/goals/rework_jap/kr_ideology_paternal_autocrat.png` |  |
| `gfx/interface/goals/rework_jap/kr_ideology_syndicalist.png` |  |
| `gfx/interface/goals/rework_jap/kr_ideology_totalist.png` |  |
| `gfx/interface/goals/rotg_goals/goal_japanese_instructors.dds` | `interface/ROTGgoals.gfx:129`、`interface/ROTGgoals_shine.gfx:665`、`interface/ROTGgoals_shine.gfx:668`、`interface/ROTGgoals_shine.gfx:681` |
| `gfx/interface/goals/rotg_goals/goal_japanese_officer.tga` | `interface/ROTGgoals.gfx:42`、`interface/ROTGgoals_shine.gfx:133`、`interface/ROTGgoals_shine.gfx:136`、`interface/ROTGgoals_shine.gfx:149` |
| `gfx/interface/goals/rotg_goals/japanification_of_foreign_subsidification.dds` | `interface/ROTGgoals.gfx:46`、`interface/ROTGgoals_shine.gfx:165`、`interface/ROTGgoals_shine.gfx:168`、`interface/ROTGgoals_shine.gfx:181` |
| `gfx/interface/goals/rotg_goals/taiyuan_arsenal.tga` | `interface/ROTGgoals.gfx:1558`、`interface/ROTGgoals_shine.gfx:11883`、`interface/ROTGgoals_shine.gfx:11886`、`interface/ROTGgoals_shine.gfx:11899` |
| `gfx/interface/goals/rus_dominate_japan.png` | `interface/kxx_china_goals.gfx:723`、`interface/kxx_china_goals.gfx:791`、`interface/kxx_china_goals.gfx:794`、`interface/kxx_china_goals.gfx:807` |
| `gfx/interface/goals/tai/2ndsingapore.dds` | `interface/RF_goals.gfx:15706`、`interface/RF_goals_shine.gfx:124267`、`interface/RF_goals_shine.gfx:124270`、`interface/RF_goals_shine.gfx:124283` |
| `gfx/interface/goals/tai/5nationvanguard.dds` | `interface/RF_goals.gfx:15794`、`interface/RF_goals_shine.gfx:124971`、`interface/RF_goals_shine.gfx:124974`、`interface/RF_goals_shine.gfx:124987` |
| `gfx/interface/goals/tai/agriculturalsupport.dds` | `interface/RF_goals.gfx:15658`、`interface/RF_goals_shine.gfx:123883`、`interface/RF_goals_shine.gfx:123886`、`interface/RF_goals_shine.gfx:123899` |
| `gfx/interface/goals/tai/anewmandate.dds` | `interface/RF_goals.gfx:15538`、`interface/RF_goals_shine.gfx:122923`、`interface/RF_goals_shine.gfx:122926`、`interface/RF_goals_shine.gfx:122939` |
| `gfx/interface/goals/tai/beaconofliberty.dds` | `interface/RF_goals.gfx:15642`、`interface/RF_goals_shine.gfx:123755`、`interface/RF_goals_shine.gfx:123758`、`interface/RF_goals_shine.gfx:123771` |
| `gfx/interface/goals/tai/breakingfree.dds` | `interface/RF_goals.gfx:15750`、`interface/RF_goals_shine.gfx:124619`、`interface/RF_goals_shine.gfx:124622`、`interface/RF_goals_shine.gfx:124635` |
| `gfx/interface/goals/tai/chihsingtaiwan.dds` | `interface/RF_goals.gfx:15542`、`interface/RF_goals_shine.gfx:122955`、`interface/RF_goals_shine.gfx:122958`、`interface/RF_goals_shine.gfx:122971` |
| `gfx/interface/goals/tai/chinesefiume.dds` | `interface/RF_goals.gfx:15622`、`interface/RF_goals_shine.gfx:123595`、`interface/RF_goals_shine.gfx:123598`、`interface/RF_goals_shine.gfx:123611` |
| `gfx/interface/goals/tai/chinesesocialism.dds` | `interface/RF_goals.gfx:15630`、`interface/RF_goals_shine.gfx:123659`、`interface/RF_goals_shine.gfx:123662`、`interface/RF_goals_shine.gfx:123675` |
| `gfx/interface/goals/tai/civilliberties.dds` | `interface/RF_goals.gfx:15702`、`interface/RF_goals_shine.gfx:124235`、`interface/RF_goals_shine.gfx:124238`、`interface/RF_goals_shine.gfx:124251` |
| `gfx/interface/goals/tai/corporatestate.dds` | `interface/RF_goals.gfx:15722`、`interface/RF_goals_shine.gfx:124395`、`interface/RF_goals_shine.gfx:124398`、`interface/RF_goals_shine.gfx:124411` |
| `gfx/interface/goals/tai/culturalrevolution.dds` | `interface/RF_goals.gfx:15546`、`interface/RF_goals_shine.gfx:122987`、`interface/RF_goals_shine.gfx:122990`、`interface/RF_goals_shine.gfx:123003` |
| `gfx/interface/goals/tai/curtailcorporate.dds` | `interface/RF_goals.gfx:15698`、`interface/RF_goals_shine.gfx:124203`、`interface/RF_goals_shine.gfx:124206`、`interface/RF_goals_shine.gfx:124219` |
| `gfx/interface/goals/tai/dealwithaustralia.dds` | `interface/RF_goals.gfx:15710`、`interface/RF_goals_shine.gfx:124299`、`interface/RF_goals_shine.gfx:124302`、`interface/RF_goals_shine.gfx:124315` |
| `gfx/interface/goals/tai/dealwiththeanglos.dds` | `interface/RF_goals.gfx:15726`、`interface/RF_goals_shine.gfx:124427`、`interface/RF_goals_shine.gfx:124430`、`interface/RF_goals_shine.gfx:124443` |
| `gfx/interface/goals/tai/dealwiththedutch.dds` | `interface/RF_goals.gfx:15758`、`interface/RF_goals_shine.gfx:124683`、`interface/RF_goals_shine.gfx:124686`、`interface/RF_goals_shine.gfx:124699` |
| `gfx/interface/goals/tai/dealwiththeusa.dds` | `interface/RF_goals.gfx:15730`、`interface/RF_goals_shine.gfx:124459`、`interface/RF_goals_shine.gfx:124462`、`interface/RF_goals_shine.gfx:124475` |
| `gfx/interface/goals/tai/denouncethereactionaries.dds` | `interface/RF_goals.gfx:15550`、`interface/RF_goals_shine.gfx:123019`、`interface/RF_goals_shine.gfx:123022`、`interface/RF_goals_shine.gfx:123035` |
| `gfx/interface/goals/tai/denouncethesocialists.dds` | `interface/RF_goals.gfx:15554`、`interface/RF_goals_shine.gfx:123051`、`interface/RF_goals_shine.gfx:123054`、`interface/RF_goals_shine.gfx:123067` |
| `gfx/interface/goals/tai/economicequality.dds` | `interface/RF_goals.gfx:15674`、`interface/RF_goals_shine.gfx:124011`、`interface/RF_goals_shine.gfx:124014`、`interface/RF_goals_shine.gfx:124027` |
| `gfx/interface/goals/tai/formosapact.dds` | `interface/RF_goals.gfx:15714`、`interface/RF_goals_shine.gfx:124331`、`interface/RF_goals_shine.gfx:124334`、`interface/RF_goals_shine.gfx:124347` |
| `gfx/interface/goals/tai/freeelections.dds` | `interface/RF_goals.gfx:15742`、`interface/RF_goals_shine.gfx:124555`、`interface/RF_goals_shine.gfx:124558`、`interface/RF_goals_shine.gfx:124571` |
| `gfx/interface/goals/tai/frenchconnections.dds` | `interface/RF_goals.gfx:15626`、`interface/RF_goals_shine.gfx:123627`、`interface/RF_goals_shine.gfx:123630`、`interface/RF_goals_shine.gfx:123643` |
| `gfx/interface/goals/tai/friendsinhanoi.dds` | `interface/RF_goals.gfx:15558`、`interface/RF_goals_shine.gfx:123083`、`interface/RF_goals_shine.gfx:123086`、`interface/RF_goals_shine.gfx:123099` |
| `gfx/interface/goals/tai/future.dds` | `interface/RF_goals.gfx:15562`、`interface/RF_goals_shine.gfx:123115`、`interface/RF_goals_shine.gfx:123118`、`interface/RF_goals_shine.gfx:123131` |
| `gfx/interface/goals/tai/huajiachengpo.dds` | `interface/RF_goals.gfx:15566`、`interface/RF_goals_shine.gfx:123147`、`interface/RF_goals_shine.gfx:123150`、`interface/RF_goals_shine.gfx:123163` |
| `gfx/interface/goals/tai/infiltratethecities.dds` | `interface/RF_goals.gfx:15650`、`interface/RF_goals_shine.gfx:123819`、`interface/RF_goals_shine.gfx:123822`、`interface/RF_goals_shine.gfx:123835` |
| `gfx/interface/goals/tai/infiltratethecountryside.dds` | `interface/RF_goals.gfx:15782`、`interface/RF_goals_shine.gfx:124875`、`interface/RF_goals_shine.gfx:124878`、`interface/RF_goals_shine.gfx:124891` |
| `gfx/interface/goals/tai/internationalecontacts.dds` | `interface/RF_goals.gfx:15790`、`interface/RF_goals_shine.gfx:124939`、`interface/RF_goals_shine.gfx:124942`、`interface/RF_goals_shine.gfx:124955` |
| `gfx/interface/goals/tai/jewelofasia.dds` | `interface/RF_goals.gfx:15806`、`interface/RF_goals_shine.gfx:125067`、`interface/RF_goals_shine.gfx:125070`、`interface/RF_goals_shine.gfx:125083` |
| `gfx/interface/goals/tai/jointhecommunes.dds` | `interface/RF_goals.gfx:15686`、`interface/RF_goals_shine.gfx:124107`、`interface/RF_goals_shine.gfx:124110`、`interface/RF_goals_shine.gfx:124123` |
| `gfx/interface/goals/tai/jointhepwl.dds` | `interface/RF_goals.gfx:15762`、`interface/RF_goals_shine.gfx:124715`、`interface/RF_goals_shine.gfx:124718`、`interface/RF_goals_shine.gfx:124731` |
| `gfx/interface/goals/tai/liaosrepublicans.dds` | `interface/RF_goals.gfx:15738`、`interface/RF_goals_shine.gfx:124523`、`interface/RF_goals_shine.gfx:124526`、`interface/RF_goals_shine.gfx:124539` |
| `gfx/interface/goals/tai/linscoalition.dds` | `interface/RF_goals.gfx:15690`、`interface/RF_goals_shine.gfx:124139`、`interface/RF_goals_shine.gfx:124142`、`interface/RF_goals_shine.gfx:124155` |
| `gfx/interface/goals/tai/localchairmen.dds` | `interface/RF_goals.gfx:15682`、`interface/RF_goals_shine.gfx:124075`、`interface/RF_goals_shine.gfx:124078`、`interface/RF_goals_shine.gfx:124091` |
| `gfx/interface/goals/tai/marchnorthoncemore.dds` | `interface/RF_goals.gfx:15786`、`interface/RF_goals_shine.gfx:124907`、`interface/RF_goals_shine.gfx:124910`、`interface/RF_goals_shine.gfx:124923` |
| `gfx/interface/goals/tai/marketeconomy.dds` | `interface/RF_goals.gfx:15694`、`interface/RF_goals_shine.gfx:124171`、`interface/RF_goals_shine.gfx:124174`、`interface/RF_goals_shine.gfx:124187` |
| `gfx/interface/goals/tai/miningcontracts.dds` | `interface/RF_goals.gfx:15802`、`interface/RF_goals_shine.gfx:125035`、`interface/RF_goals_shine.gfx:125038`、`interface/RF_goals_shine.gfx:125051` |
| `gfx/interface/goals/tai/modernchineseideal.dds` | `interface/RF_goals.gfx:15646`、`interface/RF_goals_shine.gfx:123787`、`interface/RF_goals_shine.gfx:123790`、`interface/RF_goals_shine.gfx:123803` |
| `gfx/interface/goals/tai/natureisthesculptorandchinaisthestatue.dds` | `interface/RF_goals.gfx:15570`、`interface/RF_goals_shine.gfx:123179`、`interface/RF_goals_shine.gfx:123182`、`interface/RF_goals_shine.gfx:123195` |
| `gfx/interface/goals/tai/newchinesepopulism.dds` | `interface/RF_goals.gfx:15666`、`interface/RF_goals_shine.gfx:123947`、`interface/RF_goals_shine.gfx:123950`、`interface/RF_goals_shine.gfx:123963` |
| `gfx/interface/goals/tai/newreligiouslaws.dds` | `interface/RF_goals.gfx:15634`、`interface/RF_goals_shine.gfx:123691`、`interface/RF_goals_shine.gfx:123694`、`interface/RF_goals_shine.gfx:123707` |
| `gfx/interface/goals/tai/nodictators.dds` | `interface/RF_goals.gfx:15678`、`interface/RF_goals_shine.gfx:124043`、`interface/RF_goals_shine.gfx:124046`、`interface/RF_goals_shine.gfx:124059` |
| `gfx/interface/goals/tai/noeastorwest.dds` | `interface/RF_goals.gfx:15618`、`interface/RF_goals_shine.gfx:123563`、`interface/RF_goals_shine.gfx:123566`、`interface/RF_goals_shine.gfx:123579` |
| `gfx/interface/goals/tai/nonorthorsouth.dds` | `interface/RF_goals.gfx:15614`、`interface/RF_goals_shine.gfx:123531`、`interface/RF_goals_shine.gfx:123534`、`interface/RF_goals_shine.gfx:123547` |
| `gfx/interface/goals/tai/noracialboundaries.dds` | `interface/RF_goals.gfx:15774`、`interface/RF_goals_shine.gfx:124811`、`interface/RF_goals_shine.gfx:124814`、`interface/RF_goals_shine.gfx:124827` |
| `gfx/interface/goals/tai/occidentalistchina.dds` | `interface/RF_goals.gfx:15574`、`interface/RF_goals_shine.gfx:123211`、`interface/RF_goals_shine.gfx:123214`、`interface/RF_goals_shine.gfx:123227` |
| `gfx/interface/goals/tai/outofonemany.dds` | `interface/RF_goals.gfx:15578`、`interface/RF_goals_shine.gfx:123243`、`interface/RF_goals_shine.gfx:123246`、`interface/RF_goals_shine.gfx:123259` |
| `gfx/interface/goals/tai/pacifictradeorganisation.dds` | `interface/RF_goals.gfx:15718`、`interface/RF_goals_shine.gfx:124363`、`interface/RF_goals_shine.gfx:124366`、`interface/RF_goals_shine.gfx:124379` |
| `gfx/interface/goals/tai/panasianism.dds` | `interface/RF_goals.gfx:15798`、`interface/RF_goals_shine.gfx:125003`、`interface/RF_goals_shine.gfx:125006`、`interface/RF_goals_shine.gfx:125019` |
| `gfx/interface/goals/tai/past.dds` | `interface/RF_goals.gfx:15582`、`interface/RF_goals_shine.gfx:123275`、`interface/RF_goals_shine.gfx:123278`、`interface/RF_goals_shine.gfx:123291` |
| `gfx/interface/goals/tai/pensandpencilstreatise.dds` | `interface/RF_goals.gfx:15586`、`interface/RF_goals_shine.gfx:123307`、`interface/RF_goals_shine.gfx:123310`、`interface/RF_goals_shine.gfx:123323` |
| `gfx/interface/goals/tai/present.dds` | `interface/RF_goals.gfx:15590`、`interface/RF_goals_shine.gfx:123339`、`interface/RF_goals_shine.gfx:123342`、`interface/RF_goals_shine.gfx:123355` |
| `gfx/interface/goals/tai/purgethetechnocrats.dds` | `interface/RF_goals.gfx:15594`、`interface/RF_goals_shine.gfx:123371`、`interface/RF_goals_shine.gfx:123374`、`interface/RF_goals_shine.gfx:123387` |
| `gfx/interface/goals/tai/rallythemoderates.dds` | `interface/RF_goals.gfx:15662`、`interface/RF_goals_shine.gfx:123915`、`interface/RF_goals_shine.gfx:123918`、`interface/RF_goals_shine.gfx:123931` |
| `gfx/interface/goals/tai/serenerepublicofchina.dds` | `interface/RF_goals.gfx:15810`、`interface/RF_goals_shine.gfx:125099`、`interface/RF_goals_shine.gfx:125102`、`interface/RF_goals_shine.gfx:125115` |
| `gfx/interface/goals/tai/shippingcontracts.dds` | `interface/RF_goals.gfx:15638`、`interface/RF_goals_shine.gfx:123723`、`interface/RF_goals_shine.gfx:123726`、`interface/RF_goals_shine.gfx:123739` |
| `gfx/interface/goals/tai/socialistprograms.dds` | `interface/RF_goals.gfx:15766`、`interface/RF_goals_shine.gfx:124747`、`interface/RF_goals_shine.gfx:124750`、`interface/RF_goals_shine.gfx:124763` |
| `gfx/interface/goals/tai/supportshumei.dds` | `interface/RF_goals.gfx:15670`、`interface/RF_goals_shine.gfx:123979`、`interface/RF_goals_shine.gfx:123982`、`interface/RF_goals_shine.gfx:123995` |
| `gfx/interface/goals/tai/surrealarchitecture.dds` | `interface/RF_goals.gfx:15598`、`interface/RF_goals_shine.gfx:123403`、`interface/RF_goals_shine.gfx:123406`、`interface/RF_goals_shine.gfx:123419` |
| `gfx/interface/goals/tai/taiwanesesunyatsen.dds` | `interface/RF_goals.gfx:15778`、`interface/RF_goals_shine.gfx:124843`、`interface/RF_goals_shine.gfx:124846`、`interface/RF_goals_shine.gfx:124859` |
| `gfx/interface/goals/tai/tansclub.dds` | `interface/RF_goals.gfx:15602`、`interface/RF_goals_shine.gfx:123435`、`interface/RF_goals_shine.gfx:123438`、`interface/RF_goals_shine.gfx:123451` |
| `gfx/interface/goals/tai/thechaos.dds` | `interface/RF_goals.gfx:15746`、`interface/RF_goals_shine.gfx:124587`、`interface/RF_goals_shine.gfx:124590`、`interface/RF_goals_shine.gfx:124603` |
| `gfx/interface/goals/tai/thedreamscape.dds` | `interface/RF_goals.gfx:15606`、`interface/RF_goals_shine.gfx:123467`、`interface/RF_goals_shine.gfx:123470`、`interface/RF_goals_shine.gfx:123483` |
| `gfx/interface/goals/tai/thepeoplesparty.dds` | `interface/RF_goals.gfx:15734`、`interface/RF_goals_shine.gfx:124491`、`interface/RF_goals_shine.gfx:124494`、`interface/RF_goals_shine.gfx:124507` |
| `gfx/interface/goals/tai/thetcptakespower.dds` | `interface/RF_goals.gfx:15754`、`interface/RF_goals_shine.gfx:124651`、`interface/RF_goals_shine.gfx:124654`、`interface/RF_goals_shine.gfx:124667` |
| `gfx/interface/goals/tai/theyellowriver.dds` | `interface/RF_goals.gfx:15610`、`interface/RF_goals_shine.gfx:123499`、`interface/RF_goals_shine.gfx:123502`、`interface/RF_goals_shine.gfx:123515` |
| `gfx/interface/goals/tai/urbansupport.dds` | `interface/RF_goals.gfx:15654`、`interface/RF_goals_shine.gfx:123851`、`interface/RF_goals_shine.gfx:123854`、`interface/RF_goals_shine.gfx:123867` |
| `gfx/interface/goals/tai/womensrights.dds` | `interface/RF_goals.gfx:15770`、`interface/RF_goals_shine.gfx:124779`、`interface/RF_goals_shine.gfx:124782`、`interface/RF_goals_shine.gfx:124795` |
| `gfx/interface/goals/taiwan/taiwan_colony.png` |  |
| `gfx/interface/goals/the new order/jap_cabinet_reshuffle.dds` | `interface/old_world_blues.gfx:1679`、`interface/old_world_blues_shine.gfx:10433`、`interface/old_world_blues_shine.gfx:10436`、`interface/old_world_blues_shine.gfx:10448` |
| `gfx/interface/goals/the new order/jap_denounce_the_reformists.dds` | `interface/old_world_blues.gfx:1835`、`interface/old_world_blues_shine.gfx:11635`、`interface/old_world_blues_shine.gfx:11638`、`interface/old_world_blues_shine.gfx:11650` |
| `gfx/interface/goals/the new order/jap_rebuilding_the_cities.dds` | `interface/old_world_blues.gfx:1743`、`interface/old_world_blues_shine.gfx:10945`、`interface/old_world_blues_shine.gfx:10948`、`interface/old_world_blues_shine.gfx:10960` |
| `gfx/interface/goals/the new order/jap_red_alert.dds` | `interface/old_world_blues.gfx:1675`、`interface/old_world_blues_shine.gfx:10402`、`interface/old_world_blues_shine.gfx:10405`、`interface/old_world_blues_shine.gfx:10417` |
| `gfx/interface/goals/ytg_contact_comjap.png` | `interface/YDBJ_main_goals_shine.gfx:9064`、`interface/YDBJ_main_goals_shine.gfx:9067`、`interface/YDBJ_main_goals_shine.gfx:9080`、`interface/YTG_goals.gfx:40`、`interface/YTG_goals_shine.gfx:274` …共 7 处 |
| `gfx/interface/goals/ytg_poisoning_japanese.png` | `interface/YDBJ_main_goals_shine.gfx:10324`、`interface/YDBJ_main_goals_shine.gfx:10327`、`interface/YDBJ_main_goals_shine.gfx:10340`、`interface/YTG_goals.gfx:208`、`interface/YTG_goals_shine.gfx:1534` …共 7 处 |
| `gfx/interface/ideas/cal/cal_japanese_architectural_style.png` | `interface/CAL_ideas.gfx:80` |
| `gfx/interface/ideas/gea/gea_attack_jap.png` | `interface/GEA_ideas.gfx:201` |
| `gfx/interface/ideas/ideas/idea_japanese_monopolies.png` | `interface/FX_ideas.gfx:1416` |
| `gfx/interface/ideas/ideas/jap_gunbatsu.png` | `interface/FX_ideas.gfx:1316` |
| `gfx/interface/ideas/jap/1984.png` | `interface/KXX_JAP_ideas.gfx:4` |
| `gfx/interface/ideas/jap/generic_agrarian_reform.png` |  |
| `gfx/interface/ideas/jap/jap_administration_office.png` | `interface/FX_ideas.gfx:1276` |
| `gfx/interface/ideas/jap/jap_bodhisattva_spirit.png` | `interface/FX_ideas.gfx:1376` |
| `gfx/interface/ideas/jap/jap_co_prosper.png` | `interface/FX_ideas.gfx:1284` |
| `gfx/interface/ideas/jap/jap_controlling_zaibatsu.png` | `interface/FX_ideas.gfx:1288` |
| `gfx/interface/ideas/jap/jap_democracy.png` | `interface/FX_ideas.gfx:1296` |
| `gfx/interface/ideas/jap/jap_faith_inquisition.png` | `interface/FX_ideas.gfx:1280` |
| `gfx/interface/ideas/jap/jap_fallen_zaibatsu.png` | `interface/FX_ideas.gfx:1300` |
| `gfx/interface/ideas/jap/jap_fengtian_exploitation.png` | `interface/FX_ideas.gfx:1304` |
| `gfx/interface/ideas/jap/jap_golden_age.png` | `interface/FX_ideas.gfx:1312` |
| `gfx/interface/ideas/jap/jap_hull_breaking.png` | `interface/RF_ideas.gfx:2354` |
| `gfx/interface/ideas/jap/jap_izumo_league.png` | `interface/FX_ideas.gfx:1320` |
| `gfx/interface/ideas/jap/jap_kohoda.png` | `interface/FX_ideas.gfx:1324` |
| `gfx/interface/ideas/jap/jap_kuniyuki_regime.png` | `interface/FX_ideas.gfx:1328` |
| `gfx/interface/ideas/jap/jap_kyujidai.png` | `interface/FX_ideas.gfx:1332` |
| `gfx/interface/ideas/jap/jap_man_of_his_men.png` | `interface/FX_ideas.gfx:1548` |
| `gfx/interface/ideas/jap/jap_mantetsu.png` | `interface/FX_ideas.gfx:852` |
| `gfx/interface/ideas/jap/jap_nagasaki_protocol.png` | `interface/FX_ideas.gfx:1340` |
| `gfx/interface/ideas/jap/jap_nostalgic_period.png` | `interface/FX_ideas.gfx:1344` |
| `gfx/interface/ideas/jap/jap_raise_flag.png` | `interface/FX_ideas.gfx:1348` |
| `gfx/interface/ideas/jap/jap_separation_of_command.png` | `interface/FX_ideas.gfx:1356` |
| `gfx/interface/ideas/jap/jap_shinjidai.png` | `interface/FX_ideas.gfx:1360` |
| `gfx/interface/ideas/jap/jap_shitty_tracks.png` | `interface/FX_ideas.gfx:1364` |
| `gfx/interface/ideas/jap/jap_shogun_loyalty.png` | `interface/FX_ideas.gfx:1368` |
| `gfx/interface/ideas/jap/jap_shuumatsuin.png` | `interface/FX_ideas.gfx:1372` |
| `gfx/interface/ideas/jap/jap_tanegashima_league.png` | `interface/FX_ideas.gfx:1380` |
| `gfx/interface/ideas/jap/jap_tokugawa_full_auth.png` | `interface/FX_ideas.gfx:1308` |
| `gfx/interface/ideas/jap/jap_tokugawa_restored_auth.png` | `interface/FX_ideas.gfx:1352` |
| `gfx/interface/ideas/jap/jap_tokugawa_wek_auth.png` | `interface/FX_ideas.gfx:1396` |
| `gfx/interface/ideas/jap/jap_toseiha.png` | `interface/FX_ideas.gfx:1384` |
| `gfx/interface/ideas/jap/jap_true_faith_ministry.png` | `interface/FX_ideas.gfx:1388` |
| `gfx/interface/ideas/jap/jap_tuned_blessed_sound.png` | `interface/FX_ideas.gfx:1392` |
| `gfx/interface/ideas/jap/jap_women.png` | `interface/FX_ideas.gfx:1400` |
| `gfx/interface/ideas/jap/jap_yen.png` | `interface/FX_ideas.gfx:1404` |
| `gfx/interface/ideas/japan/idea_jap_reactionary_plot.dds` | `interface/PB_ideas.gfx:1654` |
| `gfx/interface/ideas/japan/idea_jap_republican_terror_legacy.dds` | `interface/PB_ideas.gfx:90` |
| `gfx/interface/ideas/japan/idea_jap_sakurakai.dds` | `interface/PB_ideas.gfx:94` |
| `gfx/interface/ideas/pb_sng_japanese_threat.dds` | `interface/PB_ideas.gfx:1022` |
| `gfx/interface/ideas/sca/sca_tokyo_steel_works.dds` | `interface/PB_ideas.gfx:1790` |
| `gfx/interface/ideas/tai/free_nation.dds` | `interface/RF_ideas.gfx:3508` |
| `gfx/interface/ideas/tai/jewel_of_asia.dds` | `interface/RF_ideas.gfx:3512` |
| `gfx/interface/ideas/tai/native_influence.dds` | `interface/RF_ideas.gfx:3516` |
| `gfx/interface/ideas/tai/native_insur.dds` | `interface/RF_ideas.gfx:3520` |
| `gfx/interface/ideas/tai/native_rebellion.dds` | `interface/RF_ideas.gfx:3524` |
| `gfx/interface/ideas/zhr/zhr_japanese_influence.png` | `interface/RF_ideas.gfx:1306` |
| `gfx/interface/ideologies/ideology_bars/antijapan.png` | `interface/yun_ideologies_picture.gfx:135` |
| `gfx/interface/ideologies/ideology_bars/rd/japanese_militarism.png` |  |
| `gfx/interface/ideologies/subideologies/anti_japaneseism.png` | `interface/kxx_ideology.gfx:807` |
| `gfx/interface/ideologies/subideologies/little_japan_group.png` | `interface/KXX_JAP_ideologies.gfx:175` |
| `gfx/interface/ideologies/subideologies/natpop_nihon_socialism_2.png` | `interface/kxx_ideology.gfx:883` |
| `gfx/interface/ideologies/subideologies/npo_japanese_militarism.png` | `interface/kxx_ideology.gfx:1010` |
| `gfx/interface/ideologies/subideologies/pataut_japanese_militarism.png` | `interface/kxx_ideology.gfx:1014` |
| `gfx/interface/ideologies/subideologies/tot_japanese_militarism.png` | `interface/kxx_ideology.gfx:1018` |
| `gfx/interface/ideologies/subideologies/tot_nihon_socialism_2.png` | `interface/kxx_ideology.gfx:879` |
| `gfx/leaders/brg/portrait_oman_said_ibn_taimur.png` | `common/decisions/Counterrev_Britian_decisions.txt:12733`、`common/decisions/Counterrev_Britian_decisions.txt:12740`、`common/decisions/Counterrev_Britian_decisions.txt:12747`、`common/decisions/Counterrev_Britian_decisions.txt:12754`、`common/decisions/Counterrev_Britian_decisions.txt:12761` …共 6 处 |
| `gfx/leaders/chl/portrait_jap_tarou_yoshihara.png` | `common/decisions/Chile_decisions.txt:1099` |
| `gfx/leaders/gxca/portrait_gxc_taixu.png` | `events/china_anarchists.txt:388` |
| `gfx/leaders/jap/portrait_jap_abe_genki.png` | `events/SCB_JAP_Redux.txt:2878` |
| `gfx/leaders/jap/portrait_jap_adachi_kenzo_kx.png` | `events/KXX_JAP_Expand.txt:2079`、`events/SCB_JAP_Redux.txt:1031`、`history/countries/JAP - Japan.txt:414` |
| `gfx/leaders/jap/portrait_jap_aikoku_kyoto.png` | `events/test_picker.txt:76`、`events/test_picker.txt:82`、`events/test_picker.txt:88` |
| `gfx/leaders/jap/portrait_jap_akihito.png` | `interface/KXX_Ridin_With_Biden_Leaders.gfx:622` |
| `gfx/leaders/jap/portrait_jap_akira_kazami_suit.png` | `events/KXX_JAP_Expand.txt:4004` |
| `gfx/leaders/jap/portrait_jap_aso_hisashi.png` | `events/KXX_JAP_Expand.txt:2299` |
| `gfx/leaders/jap/portrait_jap_atsushi_akaike.png` | `events/KXX_JAP_Expand.txt:5590` |
| `gfx/leaders/jap/portrait_jap_bin_akao.png` | `events/SCB_JAP_Redux.txt:1586` |
| `gfx/leaders/jap/portrait_jap_chiba_saburo.png` | `events/KXX_JAP_Expand.txt:4852`、`events/SCB_JAP_Redux.txt:2829` |
| `gfx/leaders/jap/portrait_jap_chikuhei_nakajima.png` | `events/KXX_JAP_Expand.txt:2423`、`events/KXX_JAP_Expand.txt:4556` |
| `gfx/leaders/jap/portrait_jap_chozaburo_mizutani.png` | `events/KXX_JAP_Expand.txt:2130`、`events/KXX_JAP_Expand.txt:4913` |
| `gfx/leaders/jap/portrait_jap_egawa_sakurado.png` | `events/SCB_JAP_Redux.txt:1771` |
| `gfx/leaders/jap/portrait_jap_gempo_yamamoto.png` | `events/KXX_JAP_Expand.txt:2990` |
| `gfx/leaders/jap/portrait_jap_giro_senoo_kx.png` | `events/KXX_JAP_Expand.txt:3237`、`events/SCB_JAP_Redux.txt:1646`、`events/SCB_JAP_Redux.txt:1712`、`events/SCB_JAP_Redux.txt:1777` |
| `gfx/leaders/jap/portrait_jap_gondou_seikyou.png` | `events/KXX_JAP_Expand.txt:3055` |
| `gfx/leaders/jap/portrait_jap_goto_fumio.png` | `events/KXX_JAP_Expand.txt:2707`、`events/SCB_JAP_Redux.txt:780` |
| `gfx/leaders/jap/portrait_jap_hachiro_arita.png` | `events/KXX_JAP_Expand.txt:5507` |
| `gfx/leaders/jap/portrait_jap_hatoyama_ichiro.png` | `events/KXX_JAP_Expand.txt:4511` |
| `gfx/leaders/jap/portrait_jap_hidetsugu_yagi.png` | `events/KXX_JAP_Expand.txt:4939` |
| `gfx/leaders/jap/portrait_jap_hitoshi_yamakawa_kx.png` | `events/KXX_JAP_RED_Expand.txt:93`、`events/KXX_JAP_RED_Expand.txt:340`、`events/test_picker.txt:100`、`history/countries/JAP - Japan.txt:378` |
| `gfx/leaders/jap/portrait_jap_hotsumi_ozaki.png` | `events/KXX_JAP_Expand.txt:4017` |
| `gfx/leaders/jap/portrait_jap_ikeda_shigeaki.png` | `events/KXX_JAP_Expand.txt:170`、`events/KXX_JAP_Expand.txt:2584` |
| `gfx/leaders/jap/portrait_jap_ikuo_oyama.png` | `events/KXX_JAP_RED_Expand.txt:378` |
| `gfx/leaders/jap/portrait_jap_imao_hirano.png` | `events/test_picker.txt:38`、`events/test_picker.txt:44` |
| `gfx/leaders/jap/portrait_jap_inejiro_asanuma.png` | `events/KXX_JAP_Expand.txt:2315`、`events/KXX_JAP_RED_Expand.txt:785` |
| `gfx/leaders/jap/portrait_jap_inukai_tsuyoshi.png` | `events/KXX_JAP_Expand.txt:38` |
| `gfx/leaders/jap/portrait_jap_ishiguro_tadaatsu.png` | `events/SCB_JAP_Redux.txt:2858` |
| `gfx/leaders/jap/portrait_jap_ishikawa_sanshiro.png` | `events/KXX_JAP_RED_Expand.txt:143`、`events/KXX_JAP_RED_Expand.txt:579` |
| `gfx/leaders/jap/portrait_jap_iwasaki_koyata.png` | `events/KXX_JAP_Expand.txt:151` |
| `gfx/leaders/jap/portrait_jap_izawa_takio.png` | `events/SCB_JAP_Redux.txt:2898` |
| `gfx/leaders/jap/portrait_jap_jcp_central_committee.png` | `events/KXX_JAP_RED_Expand.txt:1060` |
| `gfx/leaders/jap/portrait_jap_jiichiro_matumoto.png` | `events/KXX_JAP_RED_Expand.txt:169`、`events/KXX_JAP_RED_Expand.txt:697` |
| `gfx/leaders/jap/portrait_jap_joichi_yamaji.png` | `events/KXX_JAP_Expand.txt:2092`、`events/KXX_JAP_Expand.txt:4988`、`events/SCB_JAP_Redux.txt:2932` |
| `gfx/leaders/jap/portrait_jap_jun_tsuji.png` | `events/KXX_JAP_RED_Expand.txt:641` |
| `gfx/leaders/jap/portrait_jap_kanemitsu_tsuneo.png` | `events/KXX_JAP_Expand.txt:4639` |
| `gfx/leaders/jap/portrait_jap_karasawa_toshiki.png` | `events/SCB_JAP_Redux.txt:2868` |
| `gfx/leaders/jap/portrait_jap_katou_kanji.png` | `events/KXX_JAP_Expand.txt:3344` |
| `gfx/leaders/jap/portrait_jap_katsumaro_akamatsu.png` | `events/KXX_JAP_Expand.txt:2283` |
| `gfx/leaders/jap/portrait_jap_kazuo_fukumoto.png` | `events/KXX_JAP_RED_Expand.txt:244`、`events/test_picker.txt:94`、`history/countries/JAP - Japan.txt:372` |
| `gfx/leaders/jap/portrait_jap_kazushige_ugaki_kx.png` | `events/KXX_JAP_Expand.txt:2459`、`events/KXX_JAP_Expand.txt:2554`、`events/KXX_JAP_Expand.txt:2656`、`events/KXX_JAP_Expand.txt:2726`、`events/KXX_JAP_Expand.txt:2822` …共 12 处 |
| `gfx/leaders/jap/portrait_jap_kenichiro_honma.png` | `events/KXX_JAP_Expand.txt:3404` |
| `gfx/leaders/jap/portrait_jap_kenji_miyamoto.png` | `events/KXX_JAP_RED_Expand.txt:893` |
| `gfx/leaders/jap/portrait_jap_kiichiro_higuchi.png` | `history/countries/JAP - Japan.txt:832` |
| `gfx/leaders/jap/portrait_jap_kijyuro_shidehara.png` | `events/KXX_JAP_Expand.txt:5045` |
| `gfx/leaders/jap/portrait_jap_kikue_yamakawa.png` | `events/KXX_JAP_RED_Expand.txt:435` |
| `gfx/leaders/jap/portrait_jap_kishida_masaki.png` | `events/SCB_JAP_Redux.txt:2942` |
| `gfx/leaders/jap/portrait_jap_kishio_satomi.png` | `events/KXX_JAP_Expand.txt:2996`、`events/SCB_JAP_Redux.txt:1653`、`events/SCB_JAP_Redux.txt:1719`、`events/SCB_JAP_Redux.txt:1784` |
| `gfx/leaders/jap/portrait_jap_kita_ikki.png` | `events/KXX_JAP_Expand.txt:3495`、`events/KXX_JAP_Expand.txt:3585`、`events/KXX_JAP_Expand.txt:3732`、`events/SCB_JAP_Redux.txt:1835` |
| `gfx/leaders/jap/portrait_jap_kita_mosley.png` | `events/KXX_JAP_Expand.txt:6348` |
| `gfx/leaders/jap/portrait_jap_kiyoteru_hanada.png` | `events/KXX_JAP_Expand.txt:2248`、`events/KXX_JAP_Expand.txt:2254` |
| `gfx/leaders/jap/portrait_jap_kobayashi_ichizo.png` | `events/KXX_JAP_Expand.txt:189` |
| `gfx/leaders/jap/portrait_jap_kodoha.png` | `events/KXX_JAP_Expand.txt:1394` |
| `gfx/leaders/jap/portrait_jap_kojiro_fukushi.png` | `events/KXX_JAP_Expand.txt:2210`、`events/KXX_JAP_Expand.txt:2216` |
| `gfx/leaders/jap/portrait_jap_konoe_fumimaro.png` | `events/KXX_JAP_Expand.txt:1548`、`events/KXX_JAP_Expand.txt:3905`、`events/KXX_JAP_Expand.txt:4045`、`events/SCB_JAP_Redux.txt:807`、`history/countries/JSR - Kodoha Revolt.txt:41` |
| `gfx/leaders/jap/portrait_jap_kumazawa_hiromichi.png` | `interface/KXX_Ridin_With_Biden_Leaders.gfx:610` |
| `gfx/leaders/jap/portrait_jap_masamichi_royama.png` | `events/KXX_JAP_Expand.txt:4030` |
| `gfx/leaders/jap/portrait_jap_matsutani_makoto.png` | `events/KXX_JAP_Expand.txt:5308`、`events/KXX_JAP_Expand.txt:5339`、`events/KXX_JAP_Expand.txt:5365` |
| `gfx/leaders/jap/portrait_jap_minami_jiro.png` | `events/SCB_JAP_Redux.txt:639` |
| `gfx/leaders/jap/portrait_jap_miyazaki_ryusuke.png` | `common/decisions/Left_Kuomintang_decisions.txt:6501`、`events/KXX_JAP_Expand.txt:2229`、`events/KXX_JAP_Expand.txt:2235`、`events/KXX_JAP_RED_Expand.txt:842` |
| `gfx/leaders/jap/portrait_jap_mori_tsutomu.png` | `events/KXX_JAP_Expand.txt:1946`、`events/SCB_JAP_Redux.txt:955` |
| `gfx/leaders/jap/portrait_jap_morinosuke_kajima.png` | `events/KXX_JAP_Expand.txt:4878`、`events/SCB_JAP_Redux.txt:2839` |
| `gfx/leaders/jap/portrait_jap_mosaburo_suzuki.png` | `events/KXX_JAP_Expand.txt:1612`、`events/KXX_JAP_Expand.txt:1618`、`events/KXX_JAP_Expand.txt:4952`、`events/KXX_JAP_RED_Expand.txt:466`、`events/test_picker.txt:106` |
| `gfx/leaders/jap/portrait_jap_nakano_seigo.png` | `events/KXX_JAP_Expand.txt:1807`、`events/KXX_JAP_Expand.txt:1813`、`events/KXX_JAP_Expand.txt:2172`、`events/KXX_JAP_Expand.txt:2178`、`events/KXX_JAP_RED_Expand.txt:804` |
| `gfx/leaders/jap/portrait_jap_nishida_mitsugi.png` | `events/KXX_JAP_Expand.txt:3501`、`events/SCB_JAP_Redux.txt:1841`、`events/test_picker.txt:118` |
| `gfx/leaders/jap/portrait_jap_nissho_inoue.png` | `events/KXX_JAP_Expand.txt:2984`、`events/SCB_JAP_Redux.txt:1640`、`events/SCB_JAP_Redux.txt:1706` |
| `gfx/leaders/jap/portrait_jap_nobusuke_kishi.png` | `events/KXX_JAP_Expand.txt:4121` |
| `gfx/leaders/jap/portrait_jap_nobutaka_shioden.png` | `events/KXX_JAP_Expand.txt:6092`、`events/test_picker.txt:66` |
| `gfx/leaders/jap/portrait_jap_nobuyuki_abe.png` | `events/KXX_JAP_Expand.txt:6264` |
| `gfx/leaders/jap/portrait_jap_norihiro_yasue.png` | `events/KXX_JAP_Expand.txt:6123` |
| `gfx/leaders/jap/portrait_jap_oasa_tadao.png` | `events/KXX_JAP_Expand.txt:4805` |
| `gfx/leaders/jap/portrait_jap_obata_toshiro.png` | `events/KXX_JAP_Expand.txt:689` |
| `gfx/leaders/jap/portrait_jap_ohara_naoshi.png` | `events/SCB_JAP_Redux.txt:2888` |
| `gfx/leaders/jap/portrait_jap_okawa_shumei_2.png` | `events/KXX_JAP_Expand.txt:2935`、`events/SCB_JAP_Redux.txt:1452` |
| `gfx/leaders/jap/portrait_jap_onisburo_deguchi.png` | `events/KXX_JAP_Expand.txt:3162`、`events/SCB_JAP_Redux.txt:1383` |
| `gfx/leaders/jap/portrait_jap_rikichi_okamoto.png` | `events/KXX_JAP_Expand.txt:3061` |
| `gfx/leaders/jap/portrait_jap_rikizo_hirano.png` | `events/KXX_JAP_Expand.txt:2328` |
| `gfx/leaders/jap/portrait_jap_roichi_hayashi.png` | `events/KXX_JAP_Expand.txt:5001`、`events/SCB_JAP_Redux.txt:2952` |
| `gfx/leaders/jap/portrait_jap_ryohei_uchida.png` | `events/KXX_JAP_Expand.txt:3109`、`events/SCB_JAP_Redux.txt:1333` |
| `gfx/leaders/jap/portrait_jap_ryutaro_nagai.png` | `events/KXX_JAP_Expand.txt:2049`、`events/KXX_JAP_Expand.txt:4731`、`events/SCB_JAP_Redux.txt:1002` |
| `gfx/leaders/jap/portrait_jap_saito_takao.png` | `events/KXX_JAP_Expand.txt:4768` |
| `gfx/leaders/jap/portrait_jap_saneatsu_mushanokoji.png` | `events/KXX_JAP_Expand.txt:3365`、`events/SCB_JAP_Redux.txt:1566` |
| `gfx/leaders/jap/portrait_jap_sanji_muto.png` | `events/KXX_JAP_Expand.txt:2364`、`events/SCB_JAP_Redux.txt:1096` |
| `gfx/leaders/jap/portrait_jap_satokata_takahashi.png` | `events/KXX_JAP_Expand.txt:3424` |
| `gfx/leaders/jap/portrait_jap_shigeko_prince_fushimi_hiroyasu.png` | `events/KXX_JAP_Expand.txt:2849` |
| `gfx/leaders/jap/portrait_jap_shumpachi_hojo.png` | `events/KXX_JAP_Expand.txt:5559` |
| `gfx/leaders/jap/portrait_jap_suehiko_shiono.png` | `events/SCB_JAP_Redux.txt:712` |
| `gfx/leaders/jap/portrait_jap_sumihisa_ikeda.png` | `events/KXX_JAP_Expand.txt:405` |
| `gfx/leaders/jap/portrait_jap_suzuki_kisaburo.png` | `events/KXX_JAP_Expand.txt:1921`、`events/SCB_JAP_Redux.txt:937`、`history/countries/JAP - Japan.txt:408` |
| `gfx/leaders/jap/portrait_jap_tadamasa_sakai.png` | `events/KXX_JAP_Expand.txt:5533` |
| `gfx/leaders/jap/portrait_jap_tanzan_ishibashi.png` | `events/KXX_JAP_Expand.txt:4865`、`events/SCB_JAP_Redux.txt:2809` |
| `gfx/leaders/jap/portrait_jap_taoka_kazuo.png` | `events/KXX_JAP_RED_Expand.txt:554` |
| `gfx/leaders/jap/portrait_jap_tempu_nakamura.png` | `events/KXX_JAP_Expand.txt:3414` |
| `gfx/leaders/jap/portrait_jap_tokugawa_iesato_kx.png` | `events/KXX_JAP_Expand.txt:5964` |
| `gfx/leaders/jap/portrait_jap_tokutomi_soho.png` | `events/KXX_JAP_Expand.txt:4147` |
| `gfx/leaders/jap/portrait_jap_tomito_izu.png` | `events/KXX_JAP_Expand.txt:4975`、`events/SCB_JAP_Redux.txt:2982` |
| `gfx/leaders/jap/portrait_jap_tomozo_ogawa.png` | `events/KXX_JAP_Expand.txt:5014`、`events/SCB_JAP_Redux.txt:2972` |
| `gfx/leaders/jap/portrait_jap_tsurumi_yusuke.png` | `events/SCB_JAP_Redux.txt:2819` |
| `gfx/leaders/jap/portrait_jap_yamaguchi_einosuke.png` | `events/KXX_JAP_Expand.txt:5621` |
| `gfx/leaders/jap/portrait_jap_yamamoto_senji.png` | `events/KXX_JAP_Expand.txt:2144`、`history/countries/JAP - Japan.txt:384` |
| `gfx/leaders/jap/portrait_jap_yamazaki_tatsunosuke.png` | `events/SCB_JAP_Redux.txt:1049` |
| `gfx/leaders/jap/portrait_jap_yasaburo_shimonaka.png` | `events/KXX_JAP_Expand.txt:2341` |
| `gfx/leaders/jap/portrait_jap_yojiro_matsutani.png` | `events/SCB_JAP_Redux.txt:2962` |
| `gfx/leaders/jap/portrait_jap_yoshimichi_hara.png` | `events/SCB_JAP_Redux.txt:739` |
| `gfx/leaders/jap/portrait_jap_yoshisuke_aikawa.png` | `events/KXX_JAP_Expand.txt:132` |
| `gfx/leaders/jap/portrait_jap_yosuke_matsuoka.png` | `events/KXX_JAP_Expand.txt:4134` |
| `gfx/leaders/jap/portrait_jap_yukio_ozaki.png` | `events/KXX_JAP_Expand.txt:2377`、`events/SCB_JAP_Redux.txt:1078`、`history/countries/JAP - Japan.txt:396` |
| `gfx/leaders/jap/portrait_jap_zaibatsu_council.png` | `events/KXX_JAP_Expand.txt:209` |
| `gfx/leaders/jap/portrait_two_kozaburo_tachibana.png` | `events/KXX_JAP_Expand.txt:3049`、`events/SCB_JAP_Redux.txt:1546` |
| `gfx/leaders/jap/portriat_jap_suehiro_nishio.png` | `events/KXX_JAP_Expand.txt:4926`、`events/KXX_JAP_RED_Expand.txt:823` |
| `gfx/leaders/jsr/portrait_jsr_taisaku_kitahara.png` | `events/KXX_JAP_RED_Expand.txt:735`、`history/countries/JSR - Kodoha Revolt.txt:48` |
| `gfx/leaders/twi/portrait_jap_rikichi_ando.png` | `history/countries/JST - South Seas Territory.txt:50` |
| `gfx/leaders/yun/portrait_kor_kim_il_sung.png` | `common/national_focus/jucheyunnan.txt:399` |
| `gfx/super_events/gfx_spevnt_japan_cw_army.png` | `interface/KXX_Super_Events.gfx:133`、`interface/PB_RD_Super_Events.gfx:16` |
| `gfx/super_events/gfx_spevnt_japan_cw_commie.png` | `interface/KXX_Super_Events.gfx:127`、`interface/PB_RD_Super_Events.gfx:10` |
| `gfx/super_events/gfx_spevnt_taiwan_commie_unite_china.png` | `interface/KXX_Super_Events.gfx:169`、`interface/PB_RD_Super_Events.gfx:52` |
| `gfx/super_events/gfx_spevnt_taiwan_tpp_unite_china.png` | `interface/KXX_Super_Events.gfx:163`、`interface/PB_RD_Super_Events.gfx:46` |
| `gfx/super_events/gfx_spevnt_taiwan_xiongzheng_unite_china.png` | `interface/KXX_Super_Events.gfx:157`、`interface/PB_RD_Super_Events.gfx:40` |
| `gfx/super_events/super_event_image_spevnt_japan_cw.png` | `interface/KXX_Super_Events.gfx:121`、`interface/PB_RD_Super_Events.gfx:4` |

## 可整体删除的 .gfx（无被引用的块）

```
interface/JAP_parliament_gui.gfx
interface/RD_Japan_Ministers.gfx
interface/RD_Japan_event_pictures.gfx
interface/RD_Lu_xun_ministers.gfx
interface/RD_PHI_ideas.gfx
interface/RD_Philippines_Focus_Icons.gfx
interface/RD_Southern_Warlords_ideas.gfx
interface/RD_TWI_event_pictures.gfx
interface/RD_TWI_ideas.gfx
interface/RD_Taiwan_Ministers.gfx
interface/RD_Taiwan_ideas.gfx
interface/RD_VNQ_ideas.gfx
interface/RD_decisions.gfx
interface/RD_traits.gfx
interface/TAI_goals_shine.gfx
interface/TAI_ministers.gfx
interface/focus-AJPSEIYUKAITWO_customicons.gfx
interface/focus-CAMCOMUNIE_customicons.gfx
interface/focus-CAMJAP_customicons.gfx
interface/focus-CAMMIL_customicons.gfx
interface/focus-CAMMON_customicons.gfx
interface/focus-CHI_customicons.gfx
interface/focus-CMC_customicons.gfx
interface/focus-CNHBOL_customicons.gfx
interface/focus-CNH_GUOMON_customicons.gfx
interface/focus-CNH_customicons.gfx
interface/focus-CYU_customicons.gfx
interface/focus-DSY_customicons.gfx
interface/focus-DUX_customicons.gfx
interface/focus-GXC_customicons.gfx
interface/focus-HEL_customicons.gfx
interface/focus-HKP_customicons.gfx
interface/focus-ICONONE_customicons.gfx
interface/focus-JAPAKAO_customicons.gfx
interface/focus-JAPDOMEITWO_customicons.gfx
interface/focus-JAPECON_customicons.gfx
interface/focus-JAPIRAA_customicons.gfx
interface/focus-JAPKONOE_customicons.gfx
interface/focus-JAPKOZA_customicons.gfx
interface/focus-JAPLEFTIRAA_customicons.gfx
interface/focus-JAPLIB_customicons.gfx
interface/focus-JAPMILICIVIL_customicons.gfx
interface/focus-JAPMINSEITOTWO_customicons.gfx
interface/focus-JAPNAK_customicons.gfx
interface/focus-JAPNICH_customicons.gfx
interface/focus-JAPPAN_customicons.gfx
interface/focus-JAPSEI_customicons.gfx
interface/focus-JAPTAISHUTOTWO_customicons.gfx
interface/focus-JAPVINJAP_customicons.gfx
interface/focus-JAP_ELECTION_customicons.gfx
interface/focus-JAP_YAKUZA_customicons.gfx
interface/focus-KORJUCHE_customicons.gfx
interface/focus-LAOCOM_customicons.gfx
interface/focus-LAOREB_customicons.gfx
interface/focus-LECFOR_customicons.gfx
interface/focus-LECQUIBAI_customicons.gfx
interface/focus-LUXUN_customicons.gfx
interface/focus-RDHNNICONTWO_customicons.gfx
interface/focus-RDSOCJAP_customicons.gfx
interface/focus-SHX_customicons.gfx
interface/focus-SZC_customicons.gfx
interface/focus-TAIMON_customicons.gfx
interface/focus-TAISOC_customicons.gfx
interface/focus-TAI_customicons.gfx
interface/focus-TECHAUTHCNH_customicons.gfx
interface/focus-TECHNATECHINA_customicons.gfx
interface/focus-TEH_customicons.gfx
interface/focus-TIA_customicons.gfx
interface/focus-TIB_customicons.gfx
interface/focus-TRMKOR_customicons.gfx
interface/focus-TWI_customicons.gfx
interface/focus-VIETJAP_customicons.gfx
interface/focus-VININC_GIAP_customicons.gfx
interface/focus-WANGHONGWEN_customicons.gfx
interface/focus-XSM_customicons.gfx
interface/focus-ZAIJAP_customicons.gfx
interface/japan_china_influence_scripted_gui_graphics.gfx
interface/japan_popularity_scripted_gui_graphics.gfx
interface/rework_JAP_goal_shine.gfx
interface/rework_JAP_ideas.gfx
interface/tai_event.gfx
```

## 需保留/编辑的 .gfx

```
interface/RD_Japan_Rework_decisions.gfx  (1 块需保留)
interface/RD_Japan_Rework_ideas.gfx  (1 块需保留)
interface/RD_Philippines_ideas.gfx  (2 块需保留)
interface/RD_Shanxi_ministers.gfx  (2 块需保留)
interface/RD_event_pictures.gfx  (4 块需保留)
interface/RD_game_rules.gfx  (9 块需保留)
interface/RD_game_rules_flags.gfx  (1 块需保留)
interface/RD_ideas.gfx  (9 块需保留)
interface/RD_ideology_picture.gfx  (38 块需保留)
interface/RD_lu_xun_decisions.gfx  (7 块需保留)
interface/RD_lu_xun_ideas.gfx  (1 块需保留)
interface/RD_ministers.gfx  (21 块需保留)
interface/TAI_goals.gfx  (1 块需保留)
interface/focus-CAMDEMSOC_customicons.gfx  (1 块需保留)
interface/focus-CHINA_FOREIGN_POLICY_customicons.gfx  (17 块需保留)
interface/focus-GXCECON_customicons.gfx  (2 块需保留)
interface/focus-JAPANA_customicons.gfx  (56 块需保留)
interface/focus-JAPARAKI_customicons.gfx  (18 块需保留)
interface/focus-JAPARMY_customicons.gfx  (2 块需保留)
interface/focus-JAPCOMMUNIST_customicons.gfx  (92 块需保留)
interface/focus-JAPFOR_customicons.gfx  (1 块需保留)
interface/focus-JAPIRAARIGHTIST_customicons.gfx  (1 块需保留)
interface/focus-JAPKOKUMIN_customicons.gfx  (2 块需保留)
interface/focus-JAPRECOVERY_customicons.gfx  (42 块需保留)
interface/focus-JAPSOCDEM_customicons.gfx  (1 块需保留)
interface/focus-JAPSOCIALISM_customicons.gfx  (10 块需保留)
interface/focus-JAPTOSEIHA_customicons.gfx  (2 块需保留)
interface/focus-JAP_BLACKDRAG_customicons.gfx  (4 块需保留)
interface/focus-JAP_SOCFOR_customicons.gfx  (13 块需保留)
interface/focus-JAP_customicons.gfx  (1 块需保留)
interface/focus-PHI_customicons.gfx  (1 块需保留)
interface/focus-QIE_customicons.gfx  (16 块需保留)
interface/focus-RDHNNKMTUNI_customicons.gfx  (1 块需保留)
interface/focus-SQITWO_customicons.gfx  (38 块需保留)
interface/focus-SQI_customicons.gfx  (58 块需保留)
interface/focus-TAIECONO_customicons.gfx  (1 块需保留)
interface/focus-VNQ_2_customicons.gfx  (95 块需保留)
interface/focus-VNQ_customicons.gfx  (17 块需保留)
interface/focus-YUNJUCHE_customicons.gfx  (18 块需保留)
interface/focus-ZHA_customicons.gfx  (5 块需保留)
interface/focus-ZHU_customicons.gfx  (49 块需保留)
interface/rework_JAP_goal.gfx  (4 块需保留)
```
