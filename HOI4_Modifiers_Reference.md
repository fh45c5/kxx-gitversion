# Hearts of Iron IV Modifiers 参考手册

这是一个完整的 Hearts of Iron IV 游戏中所有军事相关 modifiers 的参考文档。

---

## 目录

1. [陆军基础战斗修正](#一-陆军基础战斗修正)
2. [陆军子单位修正](#二-陆军子单位修正)
3. [战斗辅助修正](#三-战斗辅助修正)
4. [补给与损耗](#四-补给与损耗)
5. [训练与经验](#五-训练与经验)
6. [海军战斗修正](#六-海军战斗修正)
7. [空军战斗修正](#七-空军战斗修正)
8. [将领相关修正](#八-将领相关修正)
9. [情报与间谍](#九-情报与间谍)
10. [生产与工业](#十-生产与工业)
11. [人力与动员](#十一-人力与动员)
12. [学说与设计](#十二-学说与设计)
13. [特种项目](#十三-特种项目)
14. [稳定度与战争支持度](#十四-稳定度与战争支持度)
15. [阵营与外交](#十五-阵营与外交)
16. [抵抗与顺从度](#十六-抵抗与顺从度)
17. [贸易与资源](#十七-贸易与资源)
18. [建筑与修复](#十八-建筑与修复)
19. [其他杂项修正](#十九-其他杂项修正)
20. [天气与环境修正](#二十-天气与环境修正)
21. [军工机构（MIO）](#二十一-军工机构mio)
22. [海军入侵与空降](#二十二-海军入侵与空降)
23. [封锁与护航](#二十三-封锁与护航)

---

## 一、陆军基础战斗修正

### 1.1 基础战斗属性

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `army_attack_factor` | 陆军师攻击 | 全局攻击加成 |
| `army_defence_factor` | 陆军师防御 | 全局防御加成 |
| `army_morale_factor` | 陆军师组织度恢复速率 | 士气恢复 |
| `army_org_factor` | 陆军师组织度 | 最大组织度 |
| `army_speed_factor` | 陆军师速度 | 移动速度 |
| `army_attack_speed_factor` | 陆军师进攻速度 | 进入敌方领土速度 |
| `army_armor_speed_factor` | 装甲速度 | 装甲单位移动速度 |
| `army_retreat_speed_factor` | 陆军师撤退速度 | 撤退时速度 |

### 1.2 领土相关战斗修正

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `army_core_attack_factor` | 陆军师核心领土攻击 | 在核心领土攻击加成 |
| `army_core_defence_factor` | 陆军师核心领土防御 | 在核心领土防御加成 |
| `army_claim_attack_factor` | 陆军师已宣称领土攻击 | 在已宣称领土攻击加成 |
| `army_claim_defence_factor` | 陆军师已宣称领土防御 | 在已宣称领土防御加成 |

### 1.3 针对国家规模修正

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `army_attack_against_major_factor` | 对主要国家的攻击 | 攻击主要国家时加成 |
| `army_defence_against_major_factor` | 对主要国家的防御 | 防御主要国家时加成 |
| `army_breakthrough_against_major_factor` | 对主要国家的突破 | 突破主要国家防御加成 |
| `army_attack_against_minor_factor` | 对次要国家的攻击 | 攻击次要国家时加成 |
| `army_defence_against_minor_factor` | 对次要国家的防御 | 防御次要国家时加成 |
| `army_breakthrough_against_minor_factor` | 对次要国家的突破 | 突破次要国家防御加成 |

### 1.4 兵种特定修正

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `army_infantry_attack_factor` | 步兵攻击 | 步兵单位攻击 |
| `army_infantry_defence_factor` | 步兵防御 | 步兵单位防御 |
| `army_armor_attack_factor` | 装甲攻击 | 装甲单位攻击 |
| `army_armor_defence_factor` | 装甲防御 | 装甲单位防御 |
| `army_artillery_attack_factor` | 炮兵攻击 | 炮兵单位攻击 |
| `army_artillery_defence_factor` | 炮兵防御 | 炮兵单位防御 |
| `motorized_attack_factor` | 摩托化攻击 | 摩托化单位攻击 |
| `motorized_defence_factor` | 摩托化防御 | 摩托化单位防御 |
| `mechanized_attack_factor` | 机械化攻击 | 机械化单位攻击 |
| `mechanized_defence_factor` | 机械化防御 | 机械化单位防御 |
| `cavalry_attack_factor` | 骑兵攻击 | 骑兵单位攻击 |
| `cavalry_defence_factor` | 骑兵防御 | 骑兵单位防御 |
| `special_forces_attack_factor` | 特种攻击 | 特种部队攻击 |
| `special_forces_defence_factor` | 特种防御 | 特种部队防御 |

---

## 二、陆军子单位修正

### 2.1 基础步兵类

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `modifier_army_sub_unit_infantry_attack_factor` | 步兵攻击 | 基础步兵攻击 |
| `modifier_army_sub_unit_infantry_defence_factor` | 步兵防御 | 基础步兵防御 |
| `modifier_army_sub_unit_infantry_speed_factor` | 步兵速度 | 基础步兵速度 |
| `modifier_army_sub_unit_militia_attack_factor` | 民兵攻击 | 民兵攻击 |
| `modifier_army_sub_unit_militia_defence_factor` | 民兵防御 | 民兵防御 |
| `modifier_army_sub_unit_militia_speed_factor` | 民兵速度 | 民兵速度 |
| `modifier_army_sub_unit_militia_max_org_factor` | 民兵组织度 | 民兵最大组织度 |

### 2.2 骑兵类

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `modifier_army_sub_unit_cavalry_attack_factor` | 骑兵攻击 | 骑兵攻击 |
| `modifier_army_sub_unit_cavalry_defence_factor` | 骑兵防御 | 骑兵防御 |
| `modifier_army_sub_unit_cavalry_speed_factor` | 骑兵速度 | 骑兵速度 |
| `modifier_army_sub_unit_camelry_attack_factor` | 骆驼骑兵攻击 | 骆驼骑兵攻击 |
| `modifier_army_sub_unit_camelry_defence_factor` | 骆驼骑兵防御 | 骆驼骑兵防御 |
| `modifier_army_sub_unit_camelry_speed_factor` | 骆驼骑兵速度 | 骆驼骑兵速度 |

### 2.3 装甲车辆类

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `modifier_army_sub_unit_armored_car_attack_factor` | 装甲车攻击 | 装甲车攻击 |
| `modifier_army_sub_unit_armored_car_defence_factor` | 装甲车防御 | 装甲车防御 |
| `modifier_army_sub_unit_armored_car_speed_factor` | 装甲车速度 | 装甲车速度 |
| `modifier_army_sub_unit_armored_car_max_org_factor` | 装甲车组织度 | 装甲车组织度 |

### 2.4 特种部队类

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `modifier_army_sub_unit_marine_attack_factor` | 海军陆战队攻击 | 海军陆战队攻击 |
| `modifier_army_sub_unit_marine_defence_factor` | 海军陆战队防御 | 海军陆战队防御 |
| `modifier_army_sub_unit_marine_speed_factor` | 海军陆战队速度 | 海军陆战队速度 |
| `modifier_army_sub_unit_marine_max_org_factor` | 海军陆战队组织度 | 海军陆战队组织度 |
| `modifier_army_sub_unit_mountaineers_attack_factor` | 山地步兵攻击 | 山地步兵攻击 |
| `modifier_army_sub_unit_mountaineers_defence_factor` | 山地步兵防御 | 山地步兵防御 |
| `modifier_army_sub_unit_mountaineers_speed_factor` | 山地步兵速度 | 山地步兵速度 |
| `modifier_army_sub_unit_mountaineers_max_org_factor` | 山地步兵组织度 | 山地步兵组织度 |
| `modifier_army_sub_unit_paratrooper_attack_factor` | 空降伞兵攻击 | 伞兵攻击 |
| `modifier_army_sub_unit_paratrooper_defence_factor` | 空降伞兵防御 | 伞兵防御 |
| `modifier_army_sub_unit_paratrooper_speed_factor` | 空降伞兵速度 | 伞兵速度 |
| `modifier_army_sub_unit_paratrooper_max_org_factor` | 空降伞兵组织度 | 伞兵组织度 |

---

## 三、战斗辅助修正

### 3.1 计划与主动性

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `planning_speed` | 计划速度 | 积累计划加成速度 |
| `max_planning_factor` | 计划加成上限 | 最大计划加成 |
| `initiative_factor` | 主动性 | 主动进攻能力 |
| `planning_decay_rate_factor` | 作战准备下降率 | 计划加成衰减速度 |

### 3.2 堑壕与防御工事

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `max_dig_in` | 堑壕上限 | 临时防御工事级别 |
| `dig_in_speed_factor` | 堑壕速度 | 建造防御工事速度 |
| `max_dig_in_factor` | 堑壕上限系数 | 堑壕最大等级修正 |
| `land_bunker_effectiveness_factor` | 陆上要塞效率 | 要塞防御效果 |
| `coastal_bunker_effectiveness_factor` | 海岸要塞效率 | 海岸要塞防御效果 |

### 3.3 协同与侦查

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `coordination_bonus` | 协同性 | 部队协同作战能力 |
| `recon_factor` | 侦查 | 侦查能力 |
| `recon_factor_while_entrenched` | 堑壕中侦查加成 | 堑壕状态下侦查 |

### 3.4 特殊战斗修正

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `land_night_attack` | 陆战夜战攻击 | 夜战攻击能力 |
| `river_crossing_penalty_factor` | 跨河速度惩罚 | 渡河惩罚 |
| `pocket_penalty` | 包围惩罚 | 被包围时的作战能力 |
| `shore_bombardment` | 对岸炮击加成 | 海军炮击支援 |
| `railway_gun_bombardment_factor` | 列车炮轰击 | 列车炮攻击加成 |
| `air_superiority_bonus_in_combat` | 战斗中空优加成 | 制空权加成 |
| `cas_damage_reduction` | 承受密接支援伤害减免 | CAS伤害减免 |

---

## 四、补给与损耗

### 4.1 补给系统

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `supply_consumption_factor` | 补给消耗 | 部队补给消耗 |
| `supply_factor` | 补给效率 | 补给效果 |
| `supply_node_range` | 补给范围 | 补给节点覆盖范围 |
| `out_of_supply_factor` | 非战斗补给耗尽惩罚 | 补给耗尽惩罚 |
| `no_supply_grace` | 携行补给 | 无补给坚持时间 |

### 4.2 损耗系统

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `attrition` | 陆军师损耗 | 非战斗损耗 |
| `attrition_factor` | 损耗系数 | 损耗比例 |
| `winter_attrition_factor` | 冬季损耗 | 冬季损耗惩罚 |
| `heat_attrition_factor` | 炎热损耗 | 炎热损耗惩罚 |
| `truck_attrition_factor` | 补给卡车损耗 | 卡车损耗 |
| `army_fuel_consumption_factor` | 陆军燃料消耗 | 燃料消耗 |

---

## 五、训练与经验

### 5.1 训练系统

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `training_time_factor` | 训练时间 | 训练部队时间 |
| `minimum_training_level` | 最低训练程度 | 部署所需最低训练等级 |
| `max_training_xp_factor` | 最大训练经验 | 训练可获得的最大经验 |

### 5.2 经验系统

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `experience_gain_army_factor` | 陆军经验增长 | 获取经验速度 |
| `experience_gain_army_unit_factor` | 陆军师经验增长 | 单位经验获取 |
| `experience_loss_factor` | 有经验士兵损失 | 经验损失比例 |
| `army_experience_from_volunteers` | 来自志愿军的陆军经验 | 志愿军经验加成 |

---

## 六、海军战斗修正

### 6.1 基础海军属性

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `navy_org_factor` | 海军组织度 | 海军最大组织度 |
| `naval_morale_factor` | 海军组织度恢复速率 | 海军士气恢复 |
| `navy_speed_factor` | 海军速度 | 舰队移动速度 |
| `naval_coordination` | 舰队协同性 | 舰队集结分散速度 |

### 6.2 舰艇类型修正

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `navy_capital_ship_attack_factor` | 主力舰攻击 | 主力舰攻击加成 |
| `navy_capital_ship_defence_factor` | 主力舰装甲 | 主力舰防御加成 |
| `navy_screen_attack_factor` | 屏卫舰攻击 | 屏卫舰攻击加成 |
| `navy_screen_defence_factor` | 屏卫舰防御 | 屏卫舰防御加成 |
| `navy_submarine_attack_factor` | 潜艇攻击 | 潜艇攻击加成 |
| `navy_submarine_defence_factor` | 潜艇防御 | 潜艇防御加成 |

### 6.3 海战特殊修正

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `naval_damage_factor` | 海军伤害 | 对敌方船只伤害 |
| `naval_defense_factor` | 海军防御 | 受到的伤害减免 |
| `naval_critical_score_chance_factor` | 打出致命一击的几率 | 致命一击概率 |
| `naval_critical_receive_chance_factor` | 遭受致命一击的几率 | 被致命一击概率 |
| `naval_torpedo_hit_chance_factor` | 鱼雷命中几率 | 鱼雷命中率 |
| `naval_torpedo_screen_penetration_factor` | 鱼雷穿透屏卫舰 | 鱼雷突破屏卫效率 |
| `naval_light_gun_hit_chance_factor` | 轻型火炮命中率 | 轻炮命中 |
| `naval_heavy_gun_hit_chance_factor` | 重型火炮命中率 | 重炮命中 |
| `screening_efficiency` | 屏卫效率 | 屏卫保护主力舰效率 |
| `positioning` | 阵位 | 战斗阵位效果 |

---

## 七、空军战斗修正

### 7.1 基础空军属性

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `air_org_factor` | 空军组织度 | 空军最大组织度 |
| `air_morale_factor` | 空军组织度恢复速率 | 空军士气恢复 |
| `air_max_speed_factor` | 空军最大速度 | 飞机速度 |
| `air_agility_factor` | 空军机动 | 飞机机动性 |

### 7.2 任务特定修正

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `air_attack_factor` | 对空攻击 | 空战攻击 |
| `air_defence_factor` | 空中防御 | 空战防御 |
| `air_bombing_factor` | 对地轰炸 | 轰炸能力 |
| `strategic_bomber_bombing_factor` | 战略轰炸 | 战略轰炸效率 |
| `naval_strike_attack_factor` | 对海轰炸 | 反舰攻击 |
| `naval_strike_targetting_factor` | 对海瞄准 | 反舰瞄准 |

### 7.3 王牌飞行员

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `air_ace_generation_chance_factor` | 王牌飞行员产生几率 | 产生王牌概率 |
| `ace_bonuses_factor` | 空军王牌加成 | 王牌效果加成 |
| `ace_effectiveness_factor` | 王牌效率 | 王牌效率提升 |

---

## 八、将领相关修正

### 8.1 将领花费

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `army_leader_cost_factor` | 陆军指挥官花费 | 雇佣陆军将领花费 |
| `navy_leader_cost_factor` | 海军指挥官花费 | 雇佣海军将领花费 |
| `military_leader_cost_factor` | 指挥官花费 | 所有指挥官花费 |

### 8.2 将领技能

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `army_leader_start_attack_level` | 新将领初始进攻技能 | 进攻等级 |
| `army_leader_start_defense_level` | 新将领初始防御技能 | 防御等级 |
| `army_leader_start_planning_level` | 新将领初始规划技能 | 规划等级 |
| `army_leader_start_logistics_level` | 新将领初始后勤技能 | 后勤等级 |

---

## 九、情报与间谍

### 9.1 情报能力

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `encryption_factor` | 加密 | 通信加密等级 |
| `decryption_factor` | 解密 | 破译敌方密码 |
| `decryption_power` | 破译能力 | 密码破译强度 |
| `crypto_strength` | 加密等级 | 加密强度 |

### 9.2 情报收集

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `civilian_intel_factor` | 民政情报 | 民政情报等级 |
| `army_intel_factor` | 陆军情报 | 陆军情报等级 |
| `navy_intel_factor` | 海军情报 | 海军情报等级 |
| `airforce_intel_factor` | 空军情报 | 空军情报等级 |

### 9.3 反间谍与特工

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `intelligence_agency_defense` | 反间谍 | 反间谍能力 |
| `operative_slot` | 特工位 | 可用特工数量 |

---

## 十、生产与工业

### 10.1 建设速度

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `production_speed_buildings_factor` | 建设速度 | 建筑建造速度 |
| `production_speed_facility_factor` | 设施建设速度 | 设施建造速度 |
| `production_speed_infrastructure_factor` | 基础设施建设速度 | 基建速度 |
| `production_speed_arms_factory_factor` | 军用工厂建设速度 | 军工厂速度 |

### 10.2 生产效率

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `production_factory_max_efficiency_factor` | 生产效率上限 | 最大生产效率 |
| `production_factory_start_efficiency_factor` | 基础生产效率 | 初始效率 |
| `production_factory_efficiency_gain_factor` | 生产效率增长 | 效率提升速度 |

---

## 十一、人力与动员

### 11.1 人力系统

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `weekly_manpower` | 每周人力 | 人力增长 |
| `conscription_factor` | 可征募人口 | 征兵比例 |
| `recruitable_population` | 额外可征募人口 | 额外人力 |
| `non_core_manpower` | 非核心人力 | 非核心地区人力 |

### 11.2 动员系统

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `mobilization_speed` | 动员速度 | 动员进度速度 |
| `training_time_factor` | 训练时间 | 部队训练时长 |

---

## 十二、学说与设计

### 12.1 学说花费

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `land_doctrine_cost_factor` | 陆军学说花费 | 陆军学说花费 |
| `naval_doctrine_cost_factor` | 海军学说花费 | 海军学说花费 |
| `air_doctrine_cost_factor` | 空军学说花费 | 空军学说花费 |

### 12.2 设计花费

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `tank_manufacturer_cost_factor` | 坦克设计商花费 | 坦克设计花费 |
| `naval_manufacturer_cost_factor` | 海军设计商花费 | 海军设计花费 |
| `aircraft_manufacturer_cost_factor` | 飞机设计商花费 | 飞机设计花费 |

---

## 十三、特种项目

### 13.1 研究速度

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `sp_air_helicopter_speed_factor` | 直升机研究速度 | 直升机研究 |
| `sp_air_jet_engine_speed_factor` | 喷气发动机研究速度 | 喷气引擎研究 |
| `sp_rockets_ballistic_missile_speed_factor` | 弹道导弹研究速度 | 弹道导弹研究 |
| `sp_nuclear_bomb_speed_factor` | 核弹计划研究速度 | 核弹研究 |
| `sp_nuclear_reactor_speed_factor` | 核反应堆研究速度 | 反应堆研究 |

---

## 十四、稳定度与战争支持度

### 14.1 稳定度

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `stability_factor` | 稳定度 | 国家稳定度 |
| `stability_weekly` | 每周稳定度 | 稳定度周增长 |
| `war_stability_factor` | 战争对稳定度修正 | 战争稳定度影响 |

### 14.2 战争支持度

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `war_support_factor` | 战争支持度 | 国家战争支持度 |
| `war_support_weekly` | 每周战争支持度 | 战争支持度周增长 |
| `surrender_limit` | 投降界限 | 投降阈值 |

---

## 十五、阵营与外交

### 15.1 阵营影响

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `faction_influence_war_score` | 战争分数影响增益 | 阵营战争分数 |
| `faction_influence_contribution` | 贡献影响增益 | 阵营贡献 |
| `faction_influence_power` | 力量影响力修正 | 阵营力量 |

### 15.2 外交行动

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `justify_war_goal_time` | 正当化战争目标所需时间 | 宣战准备时间 |
| `guarantee_cost` | 保障独立花费 | 保障花费 |
| `puppet_cost_factor` | 傀儡花费 | 傀儡国家花费 |
| `annex_cost_factor` | 吞并花费 | 吞并花费 |

---

## 十六、抵抗与顺从度

### 16.1 抵抗系统

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `resistance_target` | 抵抗目标 | 抵抗目标值 |
| `resistance_growth` | 抵抗增长速度 | 抵抗增长 |
| `resistance_decay` | 抵抗下降速度 | 抵抗下降 |
| `resistance_activity_factor` | 抵抗活动几率 | 抵抗活动频率 |

### 16.2 顺从度系统

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `compliance_starting_value` | 初始顺从度 | 占领初始顺从度 |
| `compliance_growth` | 顺从度增长速度 | 顺从度增长 |

---

## 十七、贸易与资源

### 17.1 贸易系统

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `trade_opinion_factor` | 贸易影响力系数 | 贸易影响力 |
| `faction_trade_opinion_factor` | 阵营贸易影响力系数 | 阵营贸易影响 |

### 17.2 资源系统

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `local_resources_factor` | 战略资源获取效率 | 资源获取 |
| `state_resources_factor` | 当地可用资源 | 地区资源 |
| `equipment_capture_factor` | 装备缴获比例系数 | 缴获装备 |

---

## 十八、建筑与修复

### 18.1 建筑速度修正

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `modifier_state_production_speed_infrastructure_factor` | 基础设施建设速度 | 地区基建速度 |
| `modifier_state_production_speed_bunker_factor` | 陆上要塞建设速度 | 地区要塞速度 |
| `modifier_state_production_speed_coastal_bunker_factor` | 海岸要塞建设速度 | 地区海岸要塞速度 |
| `modifier_state_production_speed_industrial_complex_factor` | 民用工厂建设速度 | 地区民工厂速度 |

### 18.2 修复速度修正

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `modifier_repair_speed_infrastructure_factor` | 基础设施修复速度 | 基建修复 |
| `modifier_repair_speed_industrial_complex_factor` | 民用工厂修复速度 | 民工厂修复 |
| `modifier_repair_speed_bunker_factor` | 陆上要塞修复速度 | 要塞修复 |

---

## 十九、其他杂项修正

### 19.1 指挥点数

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `command_power_gain` | 每日指挥点数增长 | 指挥点日增长 |
| `max_command_power` | 最大指挥点数提高 | 指挥点上限 |

### 19.2 特种部队

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `special_forces_cap` | 特种部队容量上限乘数 | 特种部队上限 |
| `special_forces_cap_flat` | 特种部队上限 | 特种部队数量上限 |

### 19.3 装备与勋章

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `equipment_upgrade_xp_cost` | 装备经验花费 | 装备升级经验 |
| `medal_effectiveness` | 单位勋章效率 | 勋章效果 |

---

## 二十、天气与环境修正

### 20.1 天气惩罚

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `air_weather_penalty` | 恶劣天气惩罚 | 空军天气惩罚 |
| `navy_weather_penalty` | 恶劣天气惩罚 | 海军天气惩罚 |
| `air_night_penalty` | 夜间行动惩罚 | 空军夜战惩罚 |

### 20.2 气候适应

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `acclimatization_cold_climate_gain_factor` | 寒冷适应度增长率 | 寒冷适应 |
| `acclimatization_hot_climate_gain_factor` | 炎热适应度增长率 | 炎热适应 |

---

## 二十一、军工机构（MIO）

### 21.1 MIO基础

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `mio_research_bonus` | 军工机构研究加成 | 研究加成 |
| `mio_task_capacity` | 任务容量 | MIO任务数 |
| `mio_funds_gain` | 经费获取 | MIO经费 |

---

## 二十二、海军入侵与空降

### 22.1 海军入侵

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `naval_invasion_preparation` | 登陆准备时间 | 登陆准备 |
| `naval_invasion_preparation_speed` | 入侵准备速度 | 准备速度 |
| `naval_invasion_plan_cap` | 登陆作战计划上限 | 计划上限 |

### 22.2 空降作战

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `air_invasion_preparation` | 空降登陆准备时间 | 空降准备 |
| `paratrooper_extra_supply_grace` | 伞兵携行补给 | 伞兵补给 |

---

## 二十三、封锁与护航

### 23.1 封锁

| 代码名称 | 中文名称 | 说明 |
|---------|---------|------|
| `convoy_raiding_efficiency_factor` | 袭击运输船任务效率 | 破交效率 |
| `convoy_escort_efficiency` | 运输护航效率 | 护航效率 |

---

## 使用说明

### 数值格式

- `_factor` 后缀表示百分比修正，如 `0.10` 表示 +10%
- 无前缀表示固定值修正

### 应用位置

这些 modifiers 可以在以下文件中使用：
- `common/ideas/` - 国家理念
- `common/national_focus/` - 国策树
- `common/decisions/` - 决议
- `common/dynamic_modifiers/` - 动态修正
- `common/events/` - 事件

---

**文档版本**: Hearts of Iron IV 1.14.x  
**生成日期**: 2026年5月