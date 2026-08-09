# Hearts of Iron IV - Effects 完整参考文档

基于官方 documentation/effects_documentation.md 整理

---

## 目录

1. [CHARACTER 范围](#一-character-范围)
2. [COUNTRY 范围](#二-country-范围)
3. [INDUSTRIAL_ORG 范围](#三-industrial_org-范围)
4. [OPERATION 范围](#四-operation-范围)
5. [PURCHASE_CONTRACT 范围](#五-purchase_contract-范围)
6. [RAID_INSTANCE 范围](#六-raid_instance-范围)
7. [SPECIAL_PROJECT 范围](#七-special_project-范围)
8. [STATE 范围](#八-state-范围)
9. [STRATEGIC_REGION 范围](#九-strategic_region-范围)
10. [any 范围](#十-any-范围)

---

## 一、CHARACTER 范围

### 1.1 角色技能与属性

| Effect | 说明 | 示例 |
|--------|------|------|
| `add_attack` | 增加进攻技能 | `add_attack = 1` |
| `add_defense` | 增加防御技能 | `add_defense = 1` |
| `add_planning` | 增加规划技能 | `add_planning = 1` |
| `add_logistics` | 增加后勤技能 | `add_logistics = 1` |
| `add_maneuver` | 增加机动技能 | `add_maneuver = 1` |
| `add_coordination` | 增加协同技能 | `add_coordination = 1` |
| `add_skill_level` | 增加技能等级 | `add_skill_level = 1` |
| `add_max_trait` | 增加最大特征数 | `add_max_trait = 1` |
| `add_scientist_level` | 增加科学家等级 | `add_scientist_level = { character = THIS level = 1 }` |
| `add_scientist_xp` | 增加科学家经验 | `add_scientist_xp = { character = THIS xp = 100 }` |
| `gain_xp` | 获得经验 | `gain_xp = { character = THIS xp = 100 }` |
| `boost_planning` | 提升规划值 | `boost_planning = 10` |
| `injure_scientist_for_days` | 使科学家受伤 | `injure_scientist_for_days = { character = THIS days = 30 }` |
| `supply_units` | 补给部队 | `supply_units = { character = THIS }` |

### 1.2 角色职位

| Effect | 说明 | 示例 |
|--------|------|------|
| `add_advisor_role` | 任命为顾问 | `add_advisor_role = { advisor = political_advisor }` |
| `add_field_marshal_role` | 任命为元帅 | `add_field_marshal_role = { character = THIS }` |
| `add_corps_commander_role` | 任命为军长 | `add_corps_commander_role = { character = THIS }` |
| `add_naval_commander_role` | 任命为海军指挥官 | `add_naval_commander_role = { character = THIS }` |
| `add_country_leader_role` | 任命为国家领导人 | `add_country_leader_role = { character = THIS }` |
| `add_scientist_role` | 任命为科学家 | `add_scientist_role = { character = THIS }` |
| `remove_advisor_role` | 移除顾问职位 | `remove_advisor_role = { advisor = political_advisor }` |
| `remove_country_leader_role` | 移除国家领导人职位 | `remove_country_leader_role = { character = THIS }` |
| `remove_scientist_role` | 移除科学家职位 | `remove_scientist_role = { character = THIS }` |
| `remove_unit_leader` | 移除部队指挥官 | `remove_unit_leader = { character = THIS }` |
| `remove_unit_leader_role` | 移除部队指挥官职位 | `remove_unit_leader_role = { character = THIS }` |
| `set_can_be_fired_in_advisor_role` | 设置顾问是否可解雇 | `set_can_be_fired_in_advisor_role = { advisor = political_advisor value = yes }` |

### 1.3 角色特征

| Effect | 说明 | 示例 |
|--------|------|------|
| `add_trait` | 添加特征 | `add_trait = { character = THIS trait = aggressive }` |
| `remove_trait` | 移除特征 | `remove_trait = { character = THIS trait = aggressive }` |
| `add_random_trait` | 添加随机特征 | `add_random_trait = { character = THIS max_traits = 1 }` |
| `add_country_leader_trait` | 添加国家领导人特征 | `add_country_leader_trait = { trait = charismatic }` |
| `remove_country_leader_trait` | 移除国家领导人特征 | `remove_country_leader_trait = { trait = charismatic }` |
| `add_scientist_trait` | 添加科学家特征 | `add_scientist_trait = { trait = brilliant_theoretician }` |
| `add_unit_leader_trait` | 添加部队指挥官特征 | `add_unit_leader_trait = { character = THIS trait = aggressive }` |
| `remove_unit_leader_trait` | 移除部队指挥官特征 | `remove_unit_leader_trait = { character = THIS trait = aggressive }` |
| `replace_unit_leader_trait` | 替换部队指挥官特征 | `replace_unit_leader_trait = { character = THIS old_trait = defensive new_trait = aggressive }` |
| `add_timed_unit_leader_trait` | 添加限时部队指挥官特征 | `add_timed_unit_leader_trait = { character = THIS trait = aggressive duration = 365 }` |
| `add_temporary_buff_to_units` | 为部队添加临时增益 | `add_temporary_buff_to_units = { character = THIS buff = attack_buff duration = 30 }` |
| `swap_country_leader_traits` | 交换国家领导人特征 | `swap_country_leader_traits = { trait1 = charismatic trait2 = industrious }` |

### 1.4 间谍操作

| Effect | 说明 | 示例 |
|--------|------|------|
| `capture_operative` | 抓捕间谍 | `capture_operative = { character = THIS }` |
| `free_operative` | 释放间谍 | `free_operative = { character = THIS }` |
| `kill_operative` | 杀死间谍 | `kill_operative = { character = THIS }` |
| `turn_operative` | 策反间谍 | `turn_operative = { character = THIS }` |
| `harm_operative_leader` | 伤害间谍领袖 | `harm_operative_leader = { character = THIS }` |
| `force_operative_leader_into_hiding` | 迫使间谍躲藏 | `force_operative_leader_into_hiding = { character = THIS }` |

### 1.5 角色管理

| Effect | 说明 | 示例 |
|--------|------|------|
| `promote_leader` | 晋升将领 | `promote_leader = { character = THIS }` |
| `demote_leader` | 降职将领 | `demote_leader = { character = THIS }` |
| `promote_character` | 晋升角色 | `promote_character = { character = THIS }` |
| `retire` | 退役 | `retire = { character = THIS }` |
| `retire_character` | 使角色退役 | `retire_character = { character = THIS }` |

### 1.6 角色信息

| Effect | 说明 | 示例 |
|--------|------|------|
| `set_leader_portrait` | 设置头像 | `set_leader_portrait = { character = THIS portrait = GFX_portrait_xxx }` |
| `set_leader_name` | 设置领袖名称 | `set_leader_name = { character = THIS name = "New Leader" }` |
| `set_leader_description` | 设置领袖描述 | `set_leader_description = { character = THIS description = "description_key" }` |
| `set_character_name` | 设置角色名称 | `set_character_name = { character = THIS name = "New Name" }` |
| `set_nationality` | 设置国籍 | `set_nationality = { character = THIS nationality = GER }` |
| `add_nationality` | 添加国籍 | `add_nationality = { character = THIS nationality = GER }` |
| `set_portraits` | 设置头像组 | `set_portraits = { character = THIS portraits = { GFX_portrait_1 GFX_portrait_2 } }` |

### 1.7 标志与事件

| Effect | 说明 | 示例 |
|--------|------|------|
| `set_character_flag` | 设置角色标志 | `set_character_flag = { character = THIS flag = my_flag }` |
| `clr_character_flag` | 清除角色标志 | `clr_character_flag = { character = THIS flag = my_flag }` |
| `modify_character_flag` | 修改角色标志 | `modify_character_flag = { character = THIS flag = my_flag value = 1 }` |
| `set_unit_leader_flag` | 设置部队指挥官标志 | `set_unit_leader_flag = { character = THIS flag = my_flag }` |
| `clr_unit_leader_flag` | 清除部队指挥官标志 | `clr_unit_leader_flag = { character = THIS flag = my_flag }` |
| `modify_unit_leader_flag` | 修改部队指挥官标志 | `modify_unit_leader_flag = { character = THIS flag = my_flag value = 1 }` |
| `operative_leader_event` | 间谍领袖事件 | `operative_leader_event = { character = THIS event = event_id }` |
| `unit_leader_event` | 部队指挥官事件 | `unit_leader_event = { character = THIS event = event_id }` |
| `remove_exile_tag` | 移除流亡标签 | `remove_exile_tag = { character = THIS }` |
| `force_update_dynamic_modifier` | 强制更新动态修正 | `force_update_dynamic_modifier = { character = THIS modifier = my_modifier }` |
| `print_variables` | 打印变量 | `print_variables = { var1 var2 }` |
| `add_dynamic_modifier` | 添加动态修正 | `add_dynamic_modifier = { name = custom_modifier }` |
| `remove_dynamic_modifier` | 移除动态修正 | `remove_dynamic_modifier = { name = custom_modifier }` |

---

## 二、COUNTRY 范围

### 2.1 资源与生产

| Effect | 说明 | 示例 |
|--------|------|------|
| `add_manpower` | 增加人力 | `add_manpower = 100000` |
| `add_political_power` | 增加政治点数 | `add_political_power = 100` |
| `add_command_power` | 增加指挥点数 | `add_command_power = 10` |
| `add_fuel` | 增加燃料 | `add_fuel = 1000` |
| `add_resource` | 增加资源 | `add_resource = { steel = 1000 oil = 500 }` |
| `add_cic` | 增加民用工厂 | `add_cic = 5` |
| `set_political_power` | 设置政治点数 | `set_political_power = 500` |
| `set_fuel` | 设置燃料 | `set_fuel = 10000` |
| `set_fuel_ratio` | 设置燃料比例 | `set_fuel_ratio = 0.8` |
| `modify_building_resources` | 修改建筑资源 | `modify_building_resources = { type = arms_factory resource = steel amount = 100 }` |
| `add_factory_level` | 增加工厂等级 | `add_factory_level = { type = arms_factory level = 5 }` |
| `add_building_construction` | 添加建筑建设 | `add_building_construction = { type = infrastructure level = 1 }` |
| `damage_building` | 损坏建筑 | `damage_building = { type = arms_factory level = 1 }` |
| `remove_building` | 移除建筑 | `remove_building = { type = arms_factory level = 1 }` |
| `add_offsite_building` | 添加异地建筑 | `add_offsite_building = { type = naval_base level = 1 }` |

### 2.2 稳定度与战争支持度

| Effect | 说明 | 示例 |
|--------|------|------|
| `add_stability` | 增加稳定度 | `add_stability = 0.1` |
| `add_war_support` | 增加战争支持度 | `add_war_support = 0.1` |
| `add_legitimacy` | 增加正统性 | `add_legitimacy = 0.1` |
| `set_stability` | 设置稳定度 | `set_stability = 0.8` |
| `set_war_support` | 设置战争支持度 | `set_war_support = 0.8` |
| `set_legitimacy` | 设置正统性 | `set_legitimacy = 0.8` |

### 2.3 国家精神与理念

| Effect | 说明 | 示例 |
|--------|------|------|
| `add_ideas` | 添加理念 | `add_ideas = { custom_idea_1 custom_idea_2 }` |
| `remove_ideas` | 移除理念 | `remove_ideas = { custom_idea_1 }` |
| `remove_ideas_with_trait` | 移除带特定特征的理念 | `remove_ideas_with_trait = { trait = war_economy }` |
| `add_timed_idea` | 添加限时理念 | `add_timed_idea = { idea = temp_bonus duration = 365 }` |
| `modify_timed_idea` | 修改限时理念 | `modify_timed_idea = { idea = temp_bonus duration = 180 }` |
| `add_dynamic_modifier` | 添加动态修正 | `add_dynamic_modifier = { name = custom_modifier duration = 365 }` |
| `remove_dynamic_modifier` | 移除动态修正 | `remove_dynamic_modifier = { name = custom_modifier }` |
| `force_update_dynamic_modifier` | 强制更新动态修正 | `force_update_dynamic_modifier = { name = custom_modifier }` |
| `swap_ideas` | 交换理念 | `swap_ideas = { idea1 = old_idea idea2 = new_idea }` |
| `show_ideas_tooltip` | 显示理念提示 | `show_ideas_tooltip = { idea = custom_idea }` |

### 2.4 装备相关

| Effect | 说明 | 示例 |
|--------|------|------|
| `add_equipment_bonus` | 添加装备加成 | `add_equipment_bonus = { bonus = { infantry_equipment = { soft_attack = 0.1 } } }` |
| `add_equipment_production` | 添加装备生产 | `add_equipment_production = { type = infantry_equipment amount = 100 }` |
| `add_equipment_to_stockpile` | 添加装备到库存 | `add_equipment_to_stockpile = { type = medium_tank_equipment amount = 50 }` |
| `add_equipment_subsidy` | 添加装备补贴 | `add_equipment_subsidy = { type = aircraft_equipment amount = 10 }` |
| `send_equipment` | 发送装备 | `send_equipment = { target = GER type = infantry_equipment amount = 100 }` |
| `send_equipment_fraction` | 发送装备比例 | `send_equipment_fraction = { target = GER type = infantry_equipment fraction = 0.5 }` |
| `set_equipment_fraction` | 设置装备比例 | `set_equipment_fraction = { type = infantry_equipment fraction = 0.8 }` |
| `set_equipment_version_number` | 设置装备版本号 | `set_equipment_version_number = { type = infantry_equipment version = 2 }` |
| `create_equipment_variant` | 创建装备变体 | `create_equipment_variant = { type = infantry_equipment name = "Improved Infantry" }` |
| `get_supply_vehicles` | 获取补给车辆 | `get_supply_vehicles = { amount = 100 }` |
| `get_supply_vehicles_temp` | 临时获取补给车辆 | `get_supply_vehicles_temp = { amount = 100 }` |

### 2.5 军事经验与王牌

| Effect | 说明 | 示例 |
|--------|------|------|
| `army_experience` | 增加陆军经验 | `army_experience = 100` |
| `navy_experience` | 增加海军经验 | `navy_experience = 100` |
| `air_experience` | 增加空军经验 | `air_experience = 100` |
| `add_ace` | 添加王牌飞行员 | `add_ace = { type = fighter }` |

### 2.6 研究相关

| Effect | 说明 | 示例 |
|--------|------|------|
| `add_research_slot` | 增加研究槽位 | `add_research_slot = 1` |
| `set_research_slots` | 设置研究槽位 | `set_research_slots = 4` |
| `add_tech_bonus` | 增加研究加成 | `add_tech_bonus = { type = infantry_equipment bonus = 0.2 }` |
| `complete_research` | 完成研究 | `complete_research = { tech = tech_infantry_equipment_1 }` |
| `inherit_technology` | 继承科技 | `inherit_technology = { target = GER }` |
| `steal_random_tech_bonus` | 窃取随机科技加成 | `steal_random_tech_bonus = { target = GER }` |
| `set_technology` | 设置科技 | `set_technology = { tech = tech_infantry_equipment_1 }` |
| `modify_tech_sharing_bonus` | 修改科技共享加成 | `modify_tech_sharing_bonus = { bonus = 0.1 }` |
| `select_tech_tree_icon_origin` | 选择科技树图标来源 | `select_tech_tree_icon_origin = { country = GER }` |
| `mark_technology_tree_layout_dirty` | 标记科技树布局需要更新 | `mark_technology_tree_layout_dirty = yes` |

### 2.7 战争与外交

| Effect | 说明 | 示例 |
|--------|------|------|
| `declare_war_on` | 宣战 | `declare_war_on = { target = GER casus_belli = cb_conquest }` |
| `add_to_war` | 加入战争 | `add_to_war = { target = GER side = attacker }` |
| `add_war_score` | 增加战争分数 | `add_war_score = { target = GER amount = 10 }` |
| `white_peace` | 白和平 | `white_peace = { target = GER }` |
| `start_peace_conference` | 开始和平会议 | `start_peace_conference = { target = GER }` |
| `add_to_faction` | 加入阵营 | `add_to_faction = { target = faction_name }` |
| `create_faction` | 创建阵营 | `create_faction = { name = "New Faction" }` |
| `create_faction_from_template` | 从模板创建阵营 | `create_faction_from_template = { template = faction_template }` |
| `leave_faction` | 离开阵营 | `leave_faction = yes` |
| `remove_from_faction` | 从阵营移除 | `remove_from_faction = { target = GER }` |
| `dismantle_faction` | 解散阵营 | `dismantle_faction = yes` |
| `set_faction_leader` | 设置阵营领袖 | `set_faction_leader = { country = GER }` |
| `set_faction_name` | 设置阵营名称 | `set_faction_name = { name = "New Faction Name" }` |
| `set_faction_manifest` | 设置阵营宣言 | `set_faction_manifest = { manifest = manifest_key }` |
| `set_faction_rule` | 设置阵营规则 | `set_faction_rule = { rule = rule_name value = yes }` |
| `set_faction_spymaster` | 设置阵营间谍大师 | `set_faction_spymaster = { country = GER }` |
| `set_faction_upgrade` | 设置阵营升级 | `set_faction_upgrade = { upgrade = upgrade_name }` |
| `set_faction_member_upgrade_min` | 设置阵营成员最低升级 | `set_faction_member_upgrade_min = { upgrade = upgrade_name level = 1 }` |
| `add_faction_goal` | 添加阵营目标 | `add_faction_goal = { goal = goal_name }` |
| `remove_faction_goal` | 移除阵营目标 | `remove_faction_goal = { goal = goal_name }` |
| `add_faction_goal_slot` | 添加阵营目标槽位 | `add_faction_goal_slot = 1` |
| `add_faction_influence_ratio` | 添加阵营影响力比例 | `add_faction_influence_ratio = 0.1` |
| `add_faction_influence_score` | 添加阵营影响力分数 | `add_faction_influence_score = 100` |
| `add_faction_initiative` | 添加阵营主动性 | `add_faction_initiative = 10` |
| `add_faction_power_projection` | 添加阵营力量投射 | `add_faction_power_projection = 10` |
| `add_opinion_modifier` | 添加好感度修正 | `add_opinion_modifier = { target = USA modifier = friendly }` |
| `remove_opinion_modifier` | 移除好感度修正 | `remove_opinion_modifier = { target = USA modifier = friendly }` |
| `reverse_add_opinion_modifier` | 反向添加好感度修正 | `reverse_add_opinion_modifier = { target = USA modifier = friendly }` |
| `add_relation_modifier` | 添加关系修正 | `add_relation_modifier = { target = GER modifier = rival }` |
| `remove_relation_modifier` | 移除关系修正 | `remove_relation_modifier = { target = GER modifier = rival }` |
| `add_relation_rule_override` | 添加关系规则覆盖 | `add_relation_rule_override = { target = GER rule = can_declare_war value = no }` |
| `remove_relation_rule_override` | 移除关系规则覆盖 | `remove_relation_rule_override = { target = GER rule = can_declare_war }` |
| `set_relation_rule` | 设置关系规则 | `set_relation_rule = { target = GER rule = can_declare_war value = no }` |
| `clear_rule` | 清除规则 | `clear_rule = { rule = rule_name }` |
| `set_rule` | 设置规则 | `set_rule = { rule = rule_name value = yes }` |
| `give_guarantee` | 给予保障 | `give_guarantee = { target = POL }` |
| `give_market_access` | 给予市场准入 | `give_market_access = { target = GER }` |
| `give_military_access` | 给予军事通行权 | `give_military_access = { target = GER }` |
| `give_resource_rights` | 给予资源权利 | `give_resource_rights = { target = GER resource = oil }` |
| `remove_resource_rights` | 移除资源权利 | `remove_resource_rights = { target = GER resource = oil }` |
| `send_embargo` | 实施禁运 | `send_embargo = { target = GER }` |
| `break_embargo` | 解除禁运 | `break_embargo = { target = GER }` |
| `diplomatic_relation` | 外交关系 | `diplomatic_relation = { target = GER relation = ally }` |

### 2.8 情报与间谍

| Effect | 说明 | 示例 |
|--------|------|------|
| `add_intel` | 增加情报 | `add_intel = { target = GER amount = 10 }` |
| `add_decryption` | 增加解密 | `add_decryption = 10` |
| `create_intelligence_agency` | 创建情报机构 | `create_intelligence_agency = { agency = intelligence_agency }` |
| `upgrade_intelligence_agency` | 升级情报机构 | `upgrade_intelligence_agency = { level = 2 }` |
| `add_operation_token` | 添加行动令牌 | `add_operation_token = 1` |
| `remove_operation_token` | 移除行动令牌 | `remove_operation_token = 1` |
| `capture_operative` | 抓捕间谍 | `capture_operative = { character = OPERATIVE_ID }` |
| `free_operative` | 释放间谍 | `free_operative = { character = OPERATIVE_ID }` |
| `free_random_operative` | 随机释放间谍 | `free_random_operative = yes` |
| `kill_operative` | 杀死间谍 | `kill_operative = { character = OPERATIVE_ID }` |
| `turn_operative` | 策反间谍 | `turn_operative = { character = OPERATIVE_ID }` |
| `add_threat` | 增加威胁度 | `add_threat = 10` |

### 2.9 核武器与战争机器

| Effect | 说明 | 示例 |
|--------|------|------|
| `add_nuclear_bombs` | 增加核弹 | `add_nuclear_bombs = 1` |
| `launch_nuke` | 发射核弹 | `launch_nuke = { target_province = PROVINCE_ID }` |
| `add_mines` | 增加水雷 | `add_mines = 100` |
| `create_railway_gun` | 创建列车炮 | `create_railway_gun = { province = PROVINCE_ID }` |
| `teleport_railway_guns_to_deploy_province` | 传送列车炮到部署省份 | `teleport_railway_guns_to_deploy_province = yes` |

### 2.10 国家领导人与顾问

| Effect | 说明 | 示例 |
|--------|------|------|
| `create_country_leader` | 创建国家领导人 | `create_country_leader = { name = "Leader" portrait = GFX_portrait_xxx }` |
| `set_country_leader_portrait` | 设置国家领导人头像 | `set_country_leader_portrait = { portrait = GFX_portrait_xxx }` |
| `set_country_leader_name` | 设置国家领导人名称 | `set_country_leader_name = { name = "New Leader" }` |
| `set_country_leader_description` | 设置国家领导人描述 | `set_country_leader_description = { description = "description_key" }` |
| `set_country_leader_ideology` | 设置国家领导人意识形态 | `set_country_leader_ideology = { ideology = fascist }` |
| `kill_country_leader` | 杀死国家领导人 | `kill_country_leader = yes` |
| `kill_ideology_leader` | 杀死意识形态领袖 | `kill_ideology_leader = { ideology = fascist }` |
| `retire_country_leader` | 使国家领导人退休 | `retire_country_leader = yes` |
| `retire_ideology_leader` | 使意识形态领袖退休 | `retire_ideology_leader = { ideology = fascist }` |
| `swap_ruler_traits` | 交换统治者特征 | `swap_ruler_traits = { trait1 = charismatic trait2 = industrious }` |
| `activate_advisor` | 激活顾问 | `activate_advisor = { advisor = political_advisor }` |
| `deactivate_advisor` | 停用顾问 | `deactivate_advisor = { advisor = political_advisor }` |
| `create_field_marshal` | 创建元帅 | `create_field_marshal = { name = "Marshal" }` |
| `create_corps_commander` | 创建军长 | `create_corps_commander = { name = "Commander" }` |
| `create_navy_leader` | 创建海军将领 | `create_navy_leader = { name = "Admiral" }` |
| `create_operative_leader` | 创建间谍领袖 | `create_operative_leader = { name = "Spy" }` |
| `generate_character` | 生成角色 | `generate_character = { template = character_template }` |
| `generate_scientist_character` | 生成科学家角色 | `generate_scientist_character = { level = 3 }` |
| `recruit_character` | 招募角色 | `recruit_character = { character = CHARACTER_ID }` |
| `recall_attache` | 召回武官 | `recall_attache = { target = GER }` |
| `recall_volunteers_from` | 从他国召回志愿军 | `recall_volunteers_from = { target = GER }` |

### 2.11 国策与决议

| Effect | 说明 | 示例 |
|--------|------|------|
| `complete_national_focus` | 完成国策 | `complete_national_focus = { focus = focus_name }` |
| `uncomplete_national_focus` | 取消完成国策 | `uncomplete_national_focus = { focus = focus_name }` |
| `unlock_national_focus` | 解锁国策 | `unlock_national_focus = { focus = focus_name }` |
| `reduce_focus_completion_cost` | 减少国策完成花费 | `reduce_focus_completion_cost = { focus = focus_name cost = 0.5 }` |
| `activate_decision` | 激活决议 | `activate_decision = { decision = decision_name }` |
| `remove_decision` | 移除决议 | `remove_decision = { decision = decision_name }` |
| `remove_decision_on_cooldown` | 移除冷却中的决议 | `remove_decision_on_cooldown = { decision = decision_name }` |
| `activate_targeted_decision` | 激活定向决议 | `activate_targeted_decision = { decision = decision_name target = STATE_ID }` |
| `remove_targeted_decision` | 移除定向决议 | `remove_targeted_decision = { decision = decision_name target = STATE_ID }` |
| `activate_mission` | 激活任务 | `activate_mission = { mission = mission_name }` |
| `remove_mission` | 移除任务 | `remove_mission = { mission = mission_name }` |
| `activate_mission_tooltip` | 激活任务提示 | `activate_mission_tooltip = { mission = mission_name }` |
| `activate_shine_on_focus` | 激活国策高亮 | `activate_shine_on_focus = { focus = focus_name }` |
| `deactivate_shine_on_focus` | 停用国策高亮 | `deactivate_shine_on_focus = { focus = focus_name }` |
| `load_focus_tree` | 加载国策树 | `load_focus_tree = { tree = focus_tree_name }` |
| `mark_focus_tree_layout_dirty` | 标记国策树布局需要更新 | `mark_focus_tree_layout_dirty = yes` |

### 2.12 领土与宣称

| Effect | 说明 | 示例 |
|--------|------|------|
| `add_state_claim` | 添加宣称 | `add_state_claim = { state = STATE_ID }` |
| `remove_state_claim` | 移除宣称 | `remove_state_claim = { state = STATE_ID }` |
| `add_state_core` | 添加核心 | `add_state_core = { state = STATE_ID }` |
| `remove_state_core` | 移除核心 | `remove_state_core = { state = STATE_ID }` |
| `annex_country` | 吞并国家 | `annex_country = { target = TAG }` |
| `release` | 释放国家 | `release = { target = TAG }` |
| `release_puppet` | 释放傀儡 | `release_puppet = { target = TAG }` |
| `release_autonomy` | 释放自治 | `release_autonomy = { target = TAG }` |
| `release_on_controlled` | 在控制领土上释放 | `release_on_controlled = { target = TAG }` |
| `release_puppet_on_controlled` | 在控制领土上释放傀儡 | `release_puppet_on_controlled = { target = TAG }` |
| `transfer_state` | 转移领土 | `transfer_state = { state = STATE_ID target = TAG }` |
| `transfer_state_to` | 转移领土给 | `transfer_state_to = { country = TAG }` |
| `set_state_controller` | 设置地区控制者 | `set_state_controller = { state = STATE_ID country = TAG }` |
| `set_state_owner` | 设置地区所有者 | `set_state_owner = { state = STATE_ID country = TAG }` |
| `set_province_controller` | 设置省份控制者 | `set_province_controller = { province = PROVINCE_ID country = TAG }` |
| `add_contested_owner` | 添加争议所有者 | `add_contested_owner = { state = STATE_ID country = TAG }` |
| `remove_contested_owner` | 移除争议所有者 | `remove_contested_owner = { state = STATE_ID country = TAG }` |
| `end_puppet` | 结束傀儡关系 | `end_puppet = { target = TAG }` |
| `end_exile` | 结束流亡 | `end_exile = yes` |
| `become_exiled_in` | 在他国流亡 | `become_exiled_in = { target = TAG }` |
| `add_autonomy_ratio` | 添加自治比例 | `add_autonomy_ratio = 0.1` |
| `add_autonomy_score` | 添加自治分数 | `add_autonomy_score = 10` |
| `set_autonomy` | 设置自治 | `set_autonomy = { target = TAG autonomy = autonomy_level }` |

### 2.13 政治与政党

| Effect | 说明 | 示例 |
|--------|------|------|
| `set_political_party` | 设置执政党 | `set_political_party = { party = fascist_party }` |
| `set_party_rule` | 设置政党统治 | `set_party_rule = { party = fascist_party }` |
| `set_party_name` | 设置政党名称 | `set_party_name = { party = fascist_party name = "New Party" }` |
| `party_leader` | 政党领袖 | `party_leader = { party = fascist_party character = CHARACTER_ID }` |
| `set_popularities` | 设置政党支持率 | `set_popularities = { fascist = 0.5 democratic = 0.3 communist = 0.2 }` |
| `add_popularity` | 增加政党支持率 | `add_popularity = { fascist = 0.1 }` |
| `set_politics` | 设置政治 | `set_politics = { ruling_party = fascist_party }` |
| `add_breakthrough_points` | 添加突破点 | `add_breakthrough_points = 10` |
| `add_breakthrough_progress` | 添加突破进度 | `add_breakthrough_progress = 0.1` |
| `set_power_balance` | 设置权力平衡 | `set_power_balance = { ideology = fascist value = 0.8 }` |
| `remove_power_balance` | 移除权力平衡 | `remove_power_balance = { ideology = fascist }` |
| `start_civil_war` | 开始内战 | `start_civil_war = { target = TAG }` |
| `add_civil_war_target` | 添加内战目标 | `add_civil_war_target = { target = TAG }` |
| `remove_civil_war_target` | 移除内战目标 | `remove_civil_war_target = { target = TAG }` |
| `hold_election` | 举行选举 | `hold_election = yes` |

### 2.14 军事组织与编制

| Effect | 说明 | 示例 |
|--------|------|------|
| `set_oob` | 设置编制 | `set_oob = { oob = oob_name }` |
| `set_keyed_oob` | 设置键控编制 | `set_keyed_oob = { key = oob_key }` |
| `set_air_oob` | 设置空军编制 | `set_air_oob = { oob = air_oob_name }` |
| `set_naval_oob` | 设置海军编制 | `set_naval_oob = { oob = naval_oob_name }` |
| `load_oob` | 加载编制 | `load_oob = { oob = oob_name }` |
| `division_template` | 师编制 | `division_template = { template = template_name }` |
| `create_colonial_division_template` | 创建殖民地师编制 | `create_colonial_division_template = { name = "Colonial Division" }` |
| `add_units_to_division_template` | 向师编制添加部队 | `add_units_to_division_template = { template = template_name unit = infantry amount = 1 }` |
| `set_division_template_cap` | 设置师编制上限 | `set_division_template_cap = { cap = 50 }` |
| `clear_division_template_cap` | 清除师编制上限 | `clear_division_template_cap = yes` |
| `set_division_template_lock` | 设置师编制锁定 | `set_division_template_lock = { template = template_name lock = yes }` |
| `country_lock_all_division_template` | 国家锁定所有师编制 | `country_lock_all_division_template = yes` |
| `set_division_force_allow_recruiting` | 设置师强制允许招募 | `set_division_force_allow_recruiting = { template = template_name value = yes }` |
| `create_unit` | 创建部队 | `create_unit = { type = infantry_division template = template_name }` |
| `delete_unit` | 删除部队 | `delete_unit = { unit = UNIT_ID }` |
| `delete_units` | 删除多个部队 | `delete_units = { type = infantry_division amount = 10 }` |
| `delete_unit_template_and_units` | 删除师编制和部队 | `delete_unit_template_and_units = { template = template_name }` |
| `transfer_units_fraction` | 转移部队比例 | `transfer_units_fraction = { target = GER fraction = 0.5 }` |
| `transfer_navy` | 转移海军 | `transfer_navy = { target = GER }` |
| `transfer_ship` | 转移船只 | `transfer_ship = { ship = SHIP_ID target = GER }` |
| `create_ship` | 创建船只 | `create_ship = { type = destroyer name = "Destroyer" }` |
| `destroy_ships` | 销毁船只 | `destroy_ships = { type = destroyer amount = 5 }` |
| `damage_units` | 损坏部队 | `damage_units = { amount = 10 }` |

### 2.15 军事学说

| Effect | 说明 | 示例 |
|--------|------|------|
| `set_grand_doctrine` | 设置主战学说 | `set_grand_doctrine = { doctrine = mobile_warfare }` |
| `set_sub_doctrine` | 设置子学说 | `set_sub_doctrine = { doctrine = blitzkrieg }` |
| `add_doctrine_cost_reduction` | 减少学说花费 | `add_doctrine_cost_reduction = 0.1` |
| `unlock_tactic` | 解锁战术 | `unlock_tactic = { tactic = tactic_name }` |

### 2.16 标志与事件

| Effect | 说明 | 示例 |
|--------|------|------|
| `set_country_flag` | 设置国家标志 | `set_country_flag = my_flag` |
| `clr_country_flag` | 清除国家标志 | `clr_country_flag = my_flag` |
| `modify_country_flag` | 修改国家标志 | `modify_country_flag = { flag = my_flag value = 1 }` |
| `country_event` | 国家事件 | `country_event = { id = event_id }` |
| `state_event` | 地区事件 | `state_event = { id = event_id }` |
| `news_event` | 新闻事件 | `news_event = { id = event_id }` |
| `ai_message` | AI消息 | `ai_message = "Message text"` |
| `scoped_play_song` | 播放音乐 | `scoped_play_song = { song = song_name }` |
| `scoped_sound_effect` | 播放音效 | `scoped_sound_effect = { effect = effect_name }` |
| `play_song` | 播放音乐（全局） | `play_song = { song = song_name }` |
| `print_variables` | 打印变量 | `print_variables = { var1 var2 }` |
| `career_profile_step_missiolini` | 墨索里尼职业档案步骤 | `career_profile_step_missiolini = yes` |
| `character_list_tooltip` | 角色列表提示 | `character_list_tooltip = yes` |

### 2.17 杂项

| Effect | 说明 | 示例 |
|--------|------|------|
| `set_capital` | 设置首都 | `set_capital = { state = STATE_ID }` |
| `set_cosmetic_tag` | 设置美化标签 | `set_cosmetic_tag = { tag = cosmetic_tag }` |
| `drop_cosmetic_tag` | 移除美化标签 | `drop_cosmetic_tag = { tag = cosmetic_tag }` |
| `set_major` | 设置为大国 | `set_major = yes` |
| `set_occupation_law` | 设置占领法 | `set_occupation_law = { law = occupation_law_name }` |
| `set_occupation_law_where_available` | 在可用地区设置占领法 | `set_occupation_law_where_available = { law = occupation_law_name }` |
| `set_truce` | 设置停战 | `set_truce = { target = GER duration = 365 }` |
| `add_collaboration` | 添加协作度 | `add_collaboration = 0.1` |
| `set_collaboration` | 设置协作度 | `set_collaboration = 0.8` |
| `reserve_dynamic_country` | 保留动态国家 | `reserve_dynamic_country = { tag = DYN_TAG }` |
| `create_import` | 创建进口 | `create_import = { resource = steel amount = 100 }` |
| `create_production_license` | 创建生产许可证 | `create_production_license = { target = GER type = infantry_equipment }` |
| `add_ai_strategy` | 添加AI策略 | `add_ai_strategy = { strategy = ai_strategy_name }` |

### 2.18 遍历效果

| Effect | 说明 | 示例 |
|--------|------|------|
| `every_allied_country` | 遍历所有同盟国 | `every_allied_country = { add_opinion_modifier = { target = THIS modifier = friendly } }` |
| `every_army_leader` | 遍历所有陆军将领 | `every_army_leader = { add_attack = 1 }` |
| `every_character` | 遍历所有角色 | `every_character = { add_skill_level = 1 }` |
| `every_controlled_state` | 遍历所有控制地区 | `every_controlled_state = { add_compliance = 0.05 }` |
| `every_core_state` | 遍历所有核心地区 | `every_core_state = { add_manpower = 100 }` |
| `every_country_division` | 遍历所有国家部队 | `every_country_division = { gain_xp = 50 }` |
| `every_country_with_original_tag` | 遍历所有原始标签国家 | `every_country_with_original_tag = { add_opinion_modifier = { target = THIS modifier = friendly } }` |
| `every_enemy_country` | 遍历所有敌国 | `every_enemy_country = { add_intel = { target = THIS civilian_intel = 1 } }` |
| `every_faction_member` | 遍历所有阵营成员 | `every_faction_member = { add_faction_influence_score = 10 }` |
| `every_military_industrial_organization` | 遍历所有军工组织 | `every_military_industrial_organization = { add_mio_funds = 100 }` |
| `every_navy_leader` | 遍历所有海军将领 | `every_navy_leader = { add_attack = 1 }` |
| `every_neighbor_country` | 遍历所有邻国 | `every_neighbor_country = { add_opinion_modifier = { target = THIS modifier = neighbor } }` |
| `every_occupied_country` | 遍历所有被占领国家 | `every_occupied_country = { add_collaboration = 0.1 }` |
| `every_operative` | 遍历所有间谍 | `every_operative = { add_intel = 1 }` |
| `every_other_country` | 遍历所有其他国家 | `every_other_country = { add_opinion_modifier = { target = THIS modifier = friendly } }` |
| `every_owned_state` | 遍历所有拥有地区 | `every_owned_state = { add_manpower = 50 }` |
| `every_subject_country` | 遍历所有附庸国 | `every_subject_country = { add_opinion_modifier = { target = THIS modifier = subject } }` |
| `every_unit_leader` | 遍历所有部队指挥官 | `every_unit_leader = { add_skill_level = 1 }` |
| `global_every_army_leader` | 全局遍历所有陆军将领 | `global_every_army_leader = { add_attack = 1 }` |

### 2.19 随机选择效果

| Effect | 说明 | 示例 |
|--------|------|------|
| `random_allied_country` | 随机同盟国 | `random_allied_country = { add_opinion_modifier = { target = THIS modifier = friendly } }` |
| `random_army_leader` | 随机陆军将领 | `random_army_leader = { add_attack = 1 }` |
| `random_character` | 随机角色 | `random_character = { add_skill_level = 1 }` |
| `random_controlled_state` | 随机控制地区 | `random_controlled_state = { add_building_construction = { type = infrastructure level = 1 } }` |
| `random_core_state` | 随机核心地区 | `random_core_state = { add_manpower = 1000 }` |
| `random_country_division` | 随机国家部队 | `random_country_division = { gain_xp = 100 }` |
| `random_enemy_country` | 随机敌国 | `random_enemy_country = { add_intel = { target = THIS civilian_intel = 5 } }` |
| `random_military_industrial_organization` | 随机军工组织 | `random_military_industrial_organization = { add_mio_funds = 500 }` |
| `random_navy_leader` | 随机海军将领 | `random_navy_leader = { add_attack = 1 }` |
| `random_neighbor_country` | 随机邻国 | `random_neighbor_country = { add_opinion_modifier = { target = THIS modifier = friendly } }` |
| `random_occupied_country` | 随机被占领国家 | `random_occupied_country = { add_collaboration = 0.2 }` |
| `random_operative` | 随机间谍 | `random_operative = { free_operative = { character = THIS } }` |
| `random_owned_controlled_state` | 随机拥有/控制地区 | `random_owned_controlled_state = { add_building_construction = { type = arms_factory level = 1 } }` |
| `random_owned_state` | 随机拥有地区 | `random_owned_state = { add_manpower = 500 }` |
| `random_subject_country` | 随机附庸国 | `random_subject_country = { add_opinion_modifier = { target = THIS modifier = friendly } }` |
| `random_unit_leader` | 随机部队指挥官 | `random_unit_leader = { add_skill_level = 1 }` |

### 2.20 额外任务与决议

| Effect | 说明 | 示例 |
|--------|------|------|
| `add_days_mission_timeout` | 增加任务超时天数 | `add_days_mission_timeout = { mission = my_mission days = 30 }` |
| `add_days_remove` | 增加决议移除天数 | `add_days_remove = { decision = my_decision days = 30 }` |
| `unlock_decision_tooltip` | 解锁决议提示 | `unlock_decision_tooltip = { decision = decision_name }` |
| `unlock_decision_category_tooltip` | 解锁决议类别提示 | `unlock_decision_category_tooltip = { category = category_name }` |
| `unlock_military_industrial_organization_tooltip` | 解锁军工组织提示 | `unlock_military_industrial_organization_tooltip = { mio = mio_name }` |

### 2.21 设计与生产扩展

| Effect | 说明 | 示例 |
|--------|------|------|
| `add_design_template_bonus` | 添加设计模板加成 | `add_design_template_bonus = { uses = 1 cost_factor = 0.4 equipment = infantry_equipment_0 }` |
| `add_unit_bonus` | 添加部队加成 | `add_unit_bonus = { bonus = { soft_attack = 0.1 } }` |
| `add_to_tech_sharing_group` | 添加到科技共享组 | `add_to_tech_sharing_group = { group = tech_group_name }` |
| `remove_from_tech_sharing_group` | 从科技共享组移除 | `remove_from_tech_sharing_group = { group = tech_group_name }` |

### 2.22 战争目标与傀儡

| Effect | 说明 | 示例 |
|--------|------|------|
| `create_wargoal` | 创建战争目标 | `create_wargoal = { target = TAG type = cb_conquest }` |
| `remove_wargoal` | 移除战争目标 | `remove_wargoal = { target = TAG type = cb_conquest }` |
| `puppet` | 傀儡化国家 | `puppet = { target = TAG }` |

### 2.23 威胁与政治扩展

| Effect | 说明 | 示例 |
|--------|------|------|
| `add_named_threat` | 添加命名威胁 | `add_named_threat = { name = threat_name value = 10 }` |
| `add_scaled_political_power` | 增加缩放政治点数 | `add_scaled_political_power = { value = 100 }` |
| `retire_character` | 使角色退役 | `retire_character = { character = CHARACTER_ID }` |
| `show_unit_leaders_tooltip` | 显示部队指挥官提示 | `show_unit_leaders_tooltip = yes` |
| `goto_province` | 跳转到省份 | `goto_province = { province = PROVINCE_ID }` |

### 2.24 分数获取

| Effect | 说明 | 示例 |
|--------|------|------|
| `get_highest_scored_country` | 获取最高分数国家 | `get_highest_scored_country = { score = my_score_var }` |
| `get_highest_scored_country_temp` | 获取最高分数国家(临时) | `get_highest_scored_country_temp = { score = my_temp_score_var }` |
| `get_sorted_scored_countries` | 获取排序分数国家 | `get_sorted_scored_countries = { array = my_country_array }` |
| `get_sorted_scored_countries_temp` | 获取排序分数国家(临时) | `get_sorted_scored_countries_temp = { array = my_temp_country_array }` |

---

## 三、INDUSTRIAL_ORG 范围

### 3.1 MIO资金与研究

| Effect | 说明 | 示例 |
|--------|------|------|
| `add_mio_funds` | 增加MIO资金 | `add_mio_funds = 1000` |
| `set_mio_funds` | 设置MIO资金 | `set_mio_funds = 5000` |
| `add_mio_funds_gain_factor` | 增加MIO资金获取因子 | `add_mio_funds_gain_factor = 0.1` |
| `set_mio_funds_gain_factor` | 设置MIO资金获取因子 | `set_mio_funds_gain_factor = 1.5` |
| `add_mio_research_bonus` | 增加MIO研究加成 | `add_mio_research_bonus = 0.1` |
| `set_mio_research_bonus` | 设置MIO研究加成 | `set_mio_research_bonus = 0.2` |

### 3.2 MIO设计团队

| Effect | 说明 | 示例 |
|--------|------|------|
| `add_mio_design_team_assign_cost` | 增加设计团队指派花费 | `add_mio_design_team_assign_cost = 100` |
| `set_mio_design_team_assign_cost` | 设置设计团队指派花费 | `set_mio_design_team_assign_cost = 200` |
| `add_mio_design_team_change_cost` | 增加设计团队变更花费 | `add_mio_design_team_change_cost = 50` |
| `set_mio_design_team_change_cost` | 设置设计团队变更花费 | `set_mio_design_team_change_cost = 100` |
| `add_mio_industrial_manufacturer_assign_cost` | 增加工业制造商指派花费 | `add_mio_industrial_manufacturer_assign_cost = 100` |
| `set_mio_industrial_manufacturer_assign_cost` | 设置工业制造商指派花费 | `set_mio_industrial_manufacturer_assign_cost = 200` |

### 3.3 MIO规模与容量

| Effect | 说明 | 示例 |
|--------|------|------|
| `add_mio_size` | 增加MIO规模 | `add_mio_size = 1` |
| `add_mio_size_up_requirement_factor` | 增加MIO升级需求因子 | `add_mio_size_up_requirement_factor = 0.1` |
| `set_mio_size_up_requirement_factor` | 设置MIO升级需求因子 | `set_mio_size_up_requirement_factor = 1.0` |
| `add_mio_task_capacity` | 增加MIO任务容量 | `add_mio_task_capacity = 1` |
| `set_mio_task_capacity` | 设置MIO任务容量 | `set_mio_task_capacity = 5` |

### 3.4 MIO政策与特征

| Effect | 说明 | 示例 |
|--------|------|------|
| `add_mio_policy_cooldown` | 增加MIO政策冷却 | `add_mio_policy_cooldown = { policy = policy_name days = 30 }` |
| `set_mio_policy_cooldown` | 设置MIO政策冷却 | `set_mio_policy_cooldown = { policy = policy_name days = 30 }` |
| `add_mio_policy_cost` | 增加MIO政策花费 | `add_mio_policy_cost = { policy = policy_name cost = 100 }` |
| `set_mio_policy_cost` | 设置MIO政策花费 | `set_mio_policy_cost = { policy = policy_name cost = 100 }` |
| `complete_mio_trait` | 完成MIO特征 | `complete_mio_trait = { trait = trait_name }` |
| `unlock_mio_trait_tooltip` | 解锁MIO特征提示 | `unlock_mio_trait_tooltip = { trait = trait_name }` |
| `show_mio_tooltip` | 显示MIO提示 | `show_mio_tooltip = { mio = mio_name }` |

### 3.5 MIO标志与信息

| Effect | 说明 | 示例 |
|--------|------|------|
| `set_mio_flag` | 设置MIO标志 | `set_mio_flag = my_flag` |
| `clr_mio_flag` | 清除MIO标志 | `clr_mio_flag = my_flag` |
| `modify_mio_flag` | 修改MIO标志 | `modify_mio_flag = { flag = my_flag value = 1 }` |
| `set_mio_name_key` | 设置MIO名称键 | `set_mio_name_key = { name = "name_key" }` |
| `set_mio_icon` | 设置MIO图标 | `set_mio_icon = { icon = GFX_mio_icon }` |

---

## 四、OPERATION 范围

| Effect | 说明 | 示例 |
|--------|------|------|
| `every_operative` | 遍历所有间谍 | `every_operative = { add_intel = 1 }` |
| `random_operative` | 随机间谍 | `random_operative = { free_operative = { character = THIS } }` |
| `execute_operation_coordinated_strike` | 执行协调打击行动 | `execute_operation_coordinated_strike = { target = TAG }` |

---

## 五、PURCHASE_CONTRACT 范围

| Effect | 说明 | 示例 |
|--------|------|------|
| `cancel_purchase_contract` | 取消采购合同 | `cancel_purchase_contract = { contract = THIS }` |
| `random_purchase_contract` | 随机采购合同 | `random_purchase_contract = { cancel_purchase_contract = { contract = THIS } }` |
| `every_purchase_contract` | 遍历所有采购合同 | `every_purchase_contract = { cancel_purchase_contract = { contract = THIS } }` |

---

## 六、RAID_INSTANCE 范围

| Effect | 说明 | 示例 |
|--------|------|------|
| `add_raid_history_entry` | 添加突袭历史记录 | `add_raid_history_entry = { text = "Raid successful" }` |
| `raid_add_unit_experience` | 突袭增加部队经验 | `raid_add_unit_experience = 50` |
| `raid_damage_units` | 突袭损坏部队 | `raid_damage_units = 10` |

---

## 七、SPECIAL_PROJECT 范围

### 7.1 项目进度与精通度

| Effect | 说明 | 示例 |
|--------|------|------|
| `complete_special_project` | 完成特殊项目 | `complete_special_project = { project = project_name }` |
| `add_project_progress_ratio` | 增加项目进度比例 | `add_project_progress_ratio = 0.1` |
| `add_mastery` | 增加精通度 | `add_mastery = { type = air_mastery amount = 10 }` |
| `add_daily_mastery` | 增加每日精通度 | `add_daily_mastery = { type = land_mastery amount = 0.1 }` |
| `add_mastery_bonus` | 增加精通度加成 | `add_mastery_bonus = { type = sea_mastery bonus = 0.1 }` |

### 7.2 项目标志与修正

| Effect | 说明 | 示例 |
|--------|------|------|
| `set_project_flag` | 设置项目标志 | `set_project_flag = my_flag` |
| `clr_project_flag` | 清除项目标志 | `clr_project_flag = my_flag` |
| `modify_project_flag` | 修改项目标志 | `modify_project_flag = { flag = my_flag value = 1 }` |
| `add_dynamic_modifier` | 添加动态修正 | `add_dynamic_modifier = { name = custom_modifier }` |
| `remove_dynamic_modifier` | 移除动态修正 | `remove_dynamic_modifier = { name = custom_modifier }` |
| `force_update_dynamic_modifier` | 强制更新动态修正 | `force_update_dynamic_modifier = { name = custom_modifier }` |
| `complete_prototype_reward_option` | 完成原型奖励选项 | `complete_prototype_reward_option = { option = option_name }` |

---

## 八、STATE 范围

### 8.1 地区基础属性

| Effect | 说明 | 示例 |
|--------|------|------|
| `add_manpower` | 增加人力 | `add_manpower = 10000` |
| `add_resource` | 增加资源 | `add_resource = { steel = 100 }` |
| `add_building_construction` | 添加建筑建设 | `add_building_construction = { type = infrastructure level = 1 }` |
| `damage_building` | 损坏建筑 | `damage_building = { type = arms_factory level = 1 }` |
| `remove_building` | 移除建筑 | `remove_building = { type = arms_factory level = 1 }` |
| `set_building_level` | 设置建筑等级 | `set_building_level = { type = arms_factory level = 5 }` |

### 8.2 地区控制与归属

| Effect | 说明 | 示例 |
|--------|------|------|
| `add_core_of` | 添加核心归属 | `add_core_of = { country = TAG }` |
| `remove_core_of` | 移除核心归属 | `remove_core_of = { country = TAG }` |
| `add_claim_by` | 添加宣称归属 | `add_claim_by = { country = TAG }` |
| `remove_claim_by` | 移除宣称归属 | `remove_claim_by = { country = TAG }` |
| `add_contested_owner` | 添加争议所有者 | `add_contested_owner = { country = TAG }` |
| `remove_contested_owner` | 移除争议所有者 | `remove_contested_owner = { country = TAG }` |
| `set_state_controller_to` | 设置地区控制者 | `set_state_controller_to = { country = TAG }` |
| `set_state_owner_to` | 设置地区所有者 | `set_state_owner_to = { country = TAG }` |
| `set_state_province_controller` | 设置地区省份控制者 | `set_state_province_controller = { country = TAG }` |
| `transfer_state_to` | 转移地区给 | `transfer_state_to = { country = TAG }` |

### 8.3 占领与顺从度

| Effect | 说明 | 示例 |
|--------|------|------|
| `set_occupation_law` | 设置占领法 | `set_occupation_law = { law = occupation_law_name }` |
| `set_occupation_law_where_available` | 在可用地区设置占领法 | `set_occupation_law_where_available = { law = occupation_law_name }` |
| `add_compliance` | 增加顺从度 | `add_compliance = 0.1` |
| `set_compliance` | 设置顺从度 | `set_compliance = 0.8` |

### 8.4 抵抗运动

| Effect | 说明 | 示例 |
|--------|------|------|
| `add_resistance` | 增加抵抗度 | `add_resistance = 0.1` |
| `set_resistance` | 设置抵抗度 | `set_resistance = 0.5` |
| `add_resistance_target` | 增加抵抗目标 | `add_resistance_target = 0.1` |
| `remove_resistance_target` | 移除抵抗目标 | `remove_resistance_target = yes` |
| `start_resistance` | 开始抵抗 | `start_resistance = { intensity = 1 }` |
| `cancel_resistance` | 取消抵抗 | `cancel_resistance = yes` |
| `force_enable_resistance` | 强制启用抵抗 | `force_enable_resistance = yes` |
| `force_disable_resistance` | 强制禁用抵抗 | `force_disable_resistance = yes` |

### 8.5 地区修正与建筑

| Effect | 说明 | 示例 |
|--------|------|------|
| `add_state_modifier` | 添加地区修正 | `add_state_modifier = { modifier = state_modifier_name }` |
| `add_province_modifier` | 添加省份修正 | `add_province_modifier = { modifier = province_modifier_name }` |
| `remove_province_modifier` | 移除省份修正 | `remove_province_modifier = { modifier = province_modifier_name }` |
| `add_dynamic_modifier` | 添加动态修正 | `add_dynamic_modifier = { name = custom_modifier }` |
| `remove_dynamic_modifier` | 移除动态修正 | `remove_dynamic_modifier = { name = custom_modifier }` |
| `force_update_dynamic_modifier` | 强制更新动态修正 | `force_update_dynamic_modifier = { name = custom_modifier }` |
| `add_extra_state_shared_building_slots` | 增加额外共享建筑槽位 | `add_extra_state_shared_building_slots = 1` |
| `construct_building_in_random_province` | 在随机省份建造建筑 | `construct_building_in_random_province = { type = infrastructure }` |

### 8.6 地区信息与标志

| Effect | 说明 | 示例 |
|--------|------|------|
| `set_state_name` | 设置地区名称 | `set_state_name = { name = "New Name" }` |
| `reset_state_name` | 重置地区名称 | `reset_state_name = yes` |
| `set_state_category` | 设置地区类别 | `set_state_category = { category = urban }` |
| `set_state_flag` | 设置地区标志 | `set_state_flag = my_flag` |
| `clr_state_flag` | 清除地区标志 | `clr_state_flag = my_flag` |
| `modify_state_flag` | 修改地区标志 | `modify_state_flag = { flag = my_flag value = 1 }` |

### 8.7 地区事件与战争

| Effect | 说明 | 示例 |
|--------|------|------|
| `state_event` | 地区事件 | `state_event = { id = event_id }` |
| `activate_targeted_decision` | 激活定向决议 | `activate_targeted_decision = { decision = decision_name }` |
| `remove_targeted_decision` | 移除定向决议 | `remove_targeted_decision = { decision = decision_name }` |
| `set_border_war` | 设置边境战争 | `set_border_war = { target = TAG }` |
| `set_garrison_strength` | 设置驻军强度 | `set_garrison_strength = 10` |
| `set_demilitarized_zone` | 设置非军事区 | `set_demilitarized_zone = yes` |
| `teleport_armies` | 传送军队 | `teleport_armies = { target_state = STATE_ID }` |

### 8.8 遍历与随机

| Effect | 说明 | 示例 |
|--------|------|------|
| `every_neighbor_state` | 遍历所有相邻地区 | `every_neighbor_state = { add_manpower = 100 }` |
| `every_state_division` | 遍历所有地区部队 | `every_state_division = { gain_xp = 50 }` |
| `random_neighbor_state` | 随机相邻地区 | `random_neighbor_state = { add_building_construction = { type = infrastructure level = 1 } }` |
| `random_state_division` | 随机地区部队 | `random_state_division = { gain_xp = 50 }` |

### 8.9 战略位置

| Effect | 说明 | 示例 |
|--------|------|------|
| `strategic_province_location` | 战略省份位置 | `strategic_province_location = { province = PROVINCE_ID }` |
| `strategic_state_location` | 战略地区位置 | `strategic_state_location = { state = STATE_ID }` |
| `raid_reduce_project_progress_ratio` | 突袭减少项目进度比例 | `raid_reduce_project_progress_ratio = 0.1` |
| `print_variables` | 打印变量 | `print_variables = { var1 var2 }` |

---

## 九、STRATEGIC_REGION 范围

| Effect | 说明 | 示例 |
|--------|------|------|
| `add_region_efficiency` | 增加区域效率 | `add_region_efficiency = 0.1` |

---

## 十、any 范围

### 10.1 变量操作

| Effect | 说明 | 示例 |
|--------|------|------|
| `add_to_variable` | 添加到变量 | `add_to_variable = { var = my_var value = 10 }` |
| `add_to_temp_variable` | 添加到临时变量 | `add_to_temp_variable = { var = my_temp_var value = 10 }` |
| `multiply_variable` | 乘法变量 | `multiply_variable = { var = my_var value = 2 }` |
| `multiply_temp_variable` | 乘法临时变量 | `multiply_temp_variable = { var = my_temp_var value = 2 }` |
| `divide_variable` | 除法变量 | `divide_variable = { var = my_var value = 2 }` |
| `divide_temp_variable` | 除法临时变量 | `divide_temp_variable = { var = my_temp_var value = 2 }` |
| `modulo_variable` | 取模变量 | `modulo_variable = { var = my_var value = 2 }` |
| `modulo_temp_variable` | 取模临时变量 | `modulo_temp_variable = { var = my_temp_var value = 2 }` |
| `clamp_variable` | 限制变量范围 | `clamp_variable = { var = my_var min = 0 max = 100 }` |
| `clamp_temp_variable` | 限制临时变量范围 | `clamp_temp_variable = { var = my_temp_var min = 0 max = 100 }` |
| `clear_variable` | 清除变量 | `clear_variable = { var = my_var }` |
| `randomize_variable` | 随机化变量 | `randomize_variable = { var = my_var min = 1 max = 10 }` |
| `randomize_temp_variable` | 随机化临时变量 | `randomize_temp_variable = { var = my_temp_var min = 1 max = 10 }` |
| `set_variable` | 设置变量 | `set_variable = { var = my_var value = 10 }` |
| `set_temp_variable` | 设置临时变量 | `set_temp_variable = { var = my_temp_var value = 10 }` |
| `subtract_from_variable` | 从变量减去 | `subtract_from_variable = { var = my_var value = 5 }` |
| `subtract_from_temp_variable` | 从临时变量减去 | `subtract_from_temp_variable = { var = my_temp_var value = 5 }` |
| `round_variable` | 四舍五入变量 | `round_variable = { var = my_var }` |
| `round_temp_variable` | 四舍五入临时变量 | `round_temp_variable = { var = my_temp_var }` |
| `set_variable_to_random` | 设置变量为随机值 | `set_variable_to_random = { var = my_var min = 1 max = 10 }` |
| `set_temp_variable_to_random` | 设置临时变量为随机值 | `set_temp_variable_to_random = { var = my_temp_var min = 1 max = 10 }` |

### 10.2 数组操作

| Effect | 说明 | 示例 |
|--------|------|------|
| `add_to_array` | 添加到数组 | `add_to_array = { array = my_array value = 1 }` |
| `add_to_temp_array` | 添加到临时数组 | `add_to_temp_array = { array = my_temp_array value = 1 }` |
| `clear_array` | 清除数组 | `clear_array = { array = my_array }` |
| `clear_temp_array` | 清除临时数组 | `clear_temp_array = { array = my_temp_array }` |
| `find_highest_in_array` | 查找数组最大值 | `find_highest_in_array = { array = my_array }` |
| `find_lowest_in_array` | 查找数组最小值 | `find_lowest_in_array = { array = my_array }` |
| `random_scope_in_array` | 随机数组范围 | `random_scope_in_array = { array = my_array }` |

### 10.3 循环与条件

| Effect | 说明 | 示例 |
|--------|------|------|
| `if` | 条件判断 | `if = { limit = { has_idea = custom_idea } effect = { add_manpower = 1000 } }` |
| `random` | 随机判断 | `random = { chance = 50 effect = { add_political_power = 10 } }` |
| `random_list` | 随机列表 | `random_list = { 50 = { add_manpower = 100 } 50 = { add_political_power = 10 } }` |
| `for_loop_effect` | 循环效果 | `for_loop_effect = { times = 10 effect = { add_manpower = 100 } }` |
| `for_each_loop` | 遍历循环 | `for_each_loop = { array = my_array effect = { add_manpower = 100 } }` |
| `for_each_scope_loop` | 遍历范围循环 | `for_each_scope_loop = { scope = country effect = { add_opinion_modifier = { target = THIS modifier = friendly } } }` |

### 10.4 全局遍历

| Effect | 说明 | 示例 |
|--------|------|------|
| `every_country` | 遍历所有国家 | `every_country = { add_opinion_modifier = { target = THIS modifier = friendly } }` |
| `every_possible_country` | 遍历所有可能国家 | `every_possible_country = { add_opinion_modifier = { target = THIS modifier = friendly } }` |
| `every_state` | 遍历所有地区 | `every_state = { add_manpower = 100 }` |
| `every_scientist` | 遍历所有科学家 | `every_scientist = { add_scientist_xp = { character = THIS xp = 50 } }` |
| `every_active_scientist` | 遍历所有活跃科学家 | `every_active_scientist = { add_scientist_xp = { character = THIS xp = 50 } }` |
| `every_collection_element` | 遍历所有集合元素 | `every_collection_element = { collection = my_collection effect = { add_manpower = 100 } }` |

### 10.5 随机选择

| Effect | 说明 | 示例 |
|--------|------|------|
| `random_country` | 随机国家 | `random_country = { add_opinion_modifier = { target = THIS modifier = friendly } }` |
| `random_country_with_original_tag` | 随机原始标签国家 | `random_country_with_original_tag = { add_opinion_modifier = { target = THIS modifier = friendly } }` |
| `random_other_country` | 随机其他国家 | `random_other_country = { add_opinion_modifier = { target = THIS modifier = friendly } }` |
| `random_state` | 随机地区 | `random_state = { add_building_construction = { type = infrastructure level = 1 } }` |
| `random_scientist` | 随机科学家 | `random_scientist = { add_scientist_xp = { character = THIS xp = 50 } }` |
| `random_active_scientist` | 随机活跃科学家 | `random_active_scientist = { add_scientist_xp = { character = THIS xp = 50 } }` |

### 10.6 全局标志

| Effect | 说明 | 示例 |
|--------|------|------|
| `set_global_flag` | 设置全局标志 | `set_global_flag = my_flag` |
| `clr_global_flag` | 清除全局标志 | `clr_global_flag = my_flag` |
| `modify_global_flag` | 修改全局标志 | `modify_global_flag = { flag = my_flag value = 1 }` |
| `clear_global_event_target` | 清除全局事件目标 | `clear_global_event_target = { event = event_id }` |
| `clear_global_event_targets` | 清除所有全局事件目标 | `clear_global_event_targets = yes` |

### 10.7 动态国家与实体

| Effect | 说明 | 示例 |
|--------|------|------|
| `create_dynamic_country` | 创建动态国家 | `create_dynamic_country = { tag = DYN_TAG name = "New Country" }` |
| `change_tag_from` | 变更标签来源 | `change_tag_from = { old_tag = OLD_TAG new_tag = NEW_TAG }` |
| `create_entity` | 创建实体 | `create_entity = { entity = entity_name }` |
| `destroy_entity` | 销毁实体 | `destroy_entity = { entity = entity_name }` |

### 10.8 铁路与运输

| Effect | 说明 | 示例 |
|--------|------|------|
| `build_railway` | 建造铁路 | `build_railway = { province = PROVINCE_ID }` |

### 10.9 边境战争

| Effect | 说明 | 示例 |
|--------|------|------|
| `cancel_border_war` | 取消边境战争 | `cancel_border_war = { target = TAG }` |
| `finalize_border_war` | 完成边境战争 | `finalize_border_war = { target = TAG }` |

### 10.10 分数与胜利点

| Effect | 说明 | 示例 |
|--------|------|------|
| `add_victory_points` | 增加胜利点 | `add_victory_points = 100` |
| `add_power_balance_modifier` | 增加权力平衡修正 | `add_power_balance_modifier = { modifier = power_balance_modifier }` |
| `add_power_balance_value` | 增加权力平衡值 | `add_power_balance_value = { ideology = fascist value = 0.1 }` |
| `set_victory_points` | 设置胜利点 | `set_victory_points = 1000` |

### 10.11 地区抵抗与顺从度修正

| Effect | 说明 | 示例 |
|--------|------|------|
| `add_state_resistance_compliance_modifier` | 增加地区抵抗顺从度修正 | `add_state_resistance_compliance_modifier = { modifier = my_modifier }` |
| `remove_state_resistance_compliance_modifier` | 移除地区抵抗顺从度修正 | `remove_state_resistance_compliance_modifier = { modifier = my_modifier }` |

### 10.12 实体与事件

| Effect | 说明 | 示例 |
|--------|------|------|
| `save_event_target_as` | 保存事件目标 | `save_event_target_as = { target = event_target_name }` |
| `save_global_event_target_as` | 保存全局事件目标 | `save_global_event_target_as = { target = global_target_name }` |
| `custom_effect_tooltip` | 自定义效果提示 | `custom_effect_tooltip = { text = "Custom Tooltip" }` |
| `custom_override_tooltip` | 自定义覆盖提示 | `custom_override_tooltip = { text = "Override Text" }` |
| `effect_tooltip` | 效果提示 | `effect_tooltip = { effect = { add_manpower = 100 } }` |
| `event_option_tooltip` | 事件选项提示 | `event_option_tooltip = { text = "Option Text" }` |
| `hidden_effect` | 隐藏效果 | `hidden_effect = { add_manpower = 100 }` |
| `meta_effect` | 元效果 | `meta_effect = { effect = { add_manpower = 100 } }` |
| `log` | 日志 | `log = "Debug message"` |

### 10.13 地图与界面

| Effect | 说明 | 示例 |
|--------|------|------|
| `goto_state` | 跳转到地区 | `goto_state = { state = STATE_ID }` |
| `force_update_map_mode` | 强制更新地图模式 | `force_update_map_mode = yes` |

### 10.14 阵营与科研

| Effect | 说明 | 示例 |
|--------|------|------|
| `set_faction_military_unlocked` | 设置阵营军事解锁 | `set_faction_military_unlocked = yes` |
| `set_faction_research_unlocked` | 设置阵营科研解锁 | `set_faction_research_unlocked = yes` |

### 10.15 天气与音效

| Effect | 说明 | 示例 |
|--------|------|------|
| `randomize_weather` | 随机化天气 | `randomize_weather = yes` |
| `sound_effect` | 播放音效 | `sound_effect = { effect = sound_name }` |

### 10.16 省份名称

| Effect | 说明 | 示例 |
|--------|------|------|
| `set_province_name` | 设置省份名称 | `set_province_name = { province = PROVINCE_ID name = "New Name" }` |
| `reset_province_name` | 重置省份名称 | `reset_province_name = { province = PROVINCE_ID }` |

### 10.17 采购合同

| Effect | 说明 | 示例 |
|--------|------|------|
| `create_purchase_contract` | 创建采购合同 | `create_purchase_contract = { target = GER type = infantry_equipment amount = 100 }` |

### 10.18 MIO提示

| Effect | 说明 | 示例 |
|--------|------|------|
| `unlock_mio_policy_tooltip` | 解锁MIO政策提示 | `unlock_mio_policy_tooltip = { policy = policy_name }` |

### 10.19 单位创建与伤害

| Effect | 说明 | 示例 |
|--------|------|------|
| `create_unit` | 创建部队 | `create_unit = { type = infantry_division template = template_name }` |
| `damage_units` | 损坏部队 | `damage_units = { amount = 10 }` |