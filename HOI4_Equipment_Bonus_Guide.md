# Hearts of Iron IV - 国家精神 equipment_bonus 装备加成指南

这是一个完整的 Hearts of Iron IV 国家精神（National Spirit）中 equipment_bonus 的参考文档。

---

## 目录

1. [装备类型名称列表](#一-装备类型名称列表)
2. [可用加成属性表](#二-可用加成属性表)
3. [使用示例](#三-使用示例)
4. [完整国家精神模板](#四-完整国家精神模板)

---

## 一、装备类型名称列表

### 1.1 陆军装备

```yaml
infantry_equipment          # 步兵装备
militia_equipment           # 民兵装备
artillery_equipment         # 火炮装备
anti_tank_equipment         # 反坦克装备
anti_air_equipment         # 防空装备
armored_car_equipment      # 装甲车装备
motorized_equipment        # 摩托化装备
mechanized_equipment       # 机械化装备
light_tank_equipment        # 轻型坦克装备
medium_tank_equipment       # 中型坦克装备
heavy_tank_equipment        # 重型坦克装备
super_heavy_tank_equipment  # 超重型坦克装备
modern_tank_equipment       # 现代坦克装备
mountaineer_equipment       # 山地步兵装备
paratrooper_equipment       # 伞兵装备
marine_equipment            # 海军陆战队装备
cavalry_equipment           # 骑兵装备
```

---

### 1.2 海军装备

```yaml
destroyer_equipment         # 驱逐舰装备
cruiser_equipment           # 巡洋舰装备
battleship_equipment        # 战列舰装备
carrier_equipment           # 航母装备
submarine_equipment         # 潜艇装备
convoy_equipment            # 运输船装备
```

---

### 1.3 空军装备（机身类型）

```yaml
small_plane_airframe        # 小飞机机身（战斗机）
small_plane_cas_airframe    # 小飞机CAS机身
small_plane_naval_airframe  # 小飞机海军机身
medium_plane_airframe       # 中型飞机机身（战术轰炸机）
medium_plane_fighter_airframe # 中型战斗机机身
large_plane_airframe        # 大型飞机机身（战略轰炸机）
large_plane_transport_airframe # 大型运输机机身
helicopter_airframe         # 直升机机身
```

---

### 1.4 空军装备（装备类型）

```yaml
fighter_equipment           # 战斗机装备
heavy_fighter_equipment     # 重型战斗机装备
close_air_support_equipment # 近距支援机装备
tactical_bomber_equipment   # 战术轰炸机装备
strategic_bomber_equipment  # 战略轰炸机装备
naval_bomber_equipment      # 海军轰炸机装备
transport_plane_equipment   # 运输机装备
recon_plane_equipment       # 侦察机装备
helicopter_equipment        # 直升机装备
```

---

### 1.5 导弹与特种武器

```yaml
ballistic_missile_equipment   # 弹道导弹装备
nuclear_missile_equipment     # 核导弹装备
guided_missile_equipment      # 制导导弹装备
sam_missile_equipment         # 防空导弹装备
railway_gun_equipment         # 列车炮装备
```

---

## 二、可用加成属性表

| 属性名称 | 中文名称 | 适用装备类型 | 说明 | 示例值 |
|---------|---------|-------------|------|--------|
| `build_cost_ic` | 建造成本 | 所有装备 | 减少/增加装备的IC建造成本 | `-0.10` = -10% |
| `soft_attack` | 软攻击 | 陆军装备 | 提高/降低软攻击值 | `0.10` = +10% |
| `hard_attack` | 硬攻击 | 陆军装备 | 提高/降低硬攻击值 | `0.10` = +10% |
| `ap_attack` | 穿甲攻击 | 坦克/反坦克装备 | 提高/降低穿甲攻击 | `0.10` = +10% |
| `defense` | 防御 | 陆军装备 | 提高/降低防御值 | `0.10` = +10% |
| `breakthrough` | 突破 | 陆军装备 | 提高/降低突破值 | `0.10` = +10% |
| `armor_value` | 装甲值 | 坦克/装甲车辆 | 提高/降低装甲值 | `0.10` = +10% |
| `maximum_speed` | 最大速度 | 陆军/海军装备 | 提高/降低移动速度 | `0.10` = +10% |
| `reliability` | 可靠性 | 所有装备 | 提高/降低装备可靠性 | `0.10` = +10% |
| `air_attack` | 对空攻击 | 飞机装备 | 提高/降低对空攻击 | `0.10` = +10% |
| `air_defence` | 对空防御 | 飞机装备 | 提高/降低对空防御 | `0.10` = +10% |
| `air_agility` | 空中机动性 | 飞机装备 | 提高/降低空中机动性 | `0.10` = +10% |
| `air_range` | 空中航程 | 飞机装备 | 提高/降低航程 | `0.10` = +10% |
| `air_ground_attack` | 对地攻击 | 飞机装备 | 提高/降低对地攻击 | `0.10` = +10% |
| `surface_detection` | 水面探测 | 飞机/海军装备 | 提高水面探测范围 | `0.15` = +15% |
| `sub_detection` | 潜艇探测 | 飞机/海军装备 | 提高潜艇探测能力 | `0.15` = +15% |
| `instant` | 立即生效 | 所有装备 | 加成是否立即生效 | `yes` |

---

## 三、使用示例

### 3.1 飞机机身加成

```yaml
equipment_bonus = {
    small_plane_airframe = {
        build_cost_ic = -0.1
        air_attack = 0.1
        air_defence = 0.1
        air_agility = 0.1
        instant = yes
    }
    small_plane_cas_airframe = {
        build_cost_ic = -0.1
        air_ground_attack = 0.1
        air_agility = 0.1
        air_range = 0.1
        instant = yes
    }
}
```

### 3.2 步兵装备加成

```yaml
equipment_bonus = {
    infantry_equipment = {
        build_cost_ic = -0.1
        soft_attack = 0.1
        defense = 0.05
        instant = yes
    }
}
```

### 3.3 坦克装备加成

```yaml
equipment_bonus = {
    medium_tank_equipment = {
        build_cost_ic = -0.1
        armor_value = 0.1
        hard_attack = 0.1
        breakthrough = 0.1
        instant = yes
    }
}
```

### 3.4 多装备类型加成

```yaml
equipment_bonus = {
    infantry_equipment = {
        build_cost_ic = -0.1
        soft_attack = 0.1
        instant = yes
    }
    artillery_equipment = {
        build_cost_ic = -0.1
        hard_attack = 0.15
        instant = yes
    }
    anti_tank_equipment = {
        build_cost_ic = -0.1
        ap_attack = 0.15
        instant = yes
    }
}
```

---

## 四、完整国家精神模板

```yaml
custom_national_spirit = {
    id = custom_war_economy
    name = "custom_war_economy"
    description = "custom_war_economy_desc"
    picture = GFX_idea_war_economy
    
    # 普通国家修正
    modifier = {
        army_attack_factor = 0.1
        production_speed_buildings_factor = 0.1
        war_support_factor = 0.05
    }
    
    # 装备特定修正
    equipment_bonus = {
        # 步兵装备
        infantry_equipment = {
            build_cost_ic = -0.1
            soft_attack = 0.1
            defense = 0.05
            instant = yes
        }
        
        # 火炮装备
        artillery_equipment = {
            build_cost_ic = -0.1
            hard_attack = 0.15
            instant = yes
        }
        
        # 战斗机机身
        small_plane_airframe = {
            build_cost_ic = -0.1
            air_attack = 0.1
            air_defence = 0.1
            air_agility = 0.1
            instant = yes
        }
        
        # CAS机身
        small_plane_cas_airframe = {
            build_cost_ic = -0.1
            air_ground_attack = 0.1
            air_agility = 0.1
            air_range = 0.1
            instant = yes
        }
        
        # 中型坦克
        medium_tank_equipment = {
            build_cost_ic = -0.1
            armor_value = 0.1
            hard_attack = 0.1
            breakthrough = 0.1
            instant = yes
        }
    }
}
```

---

## 使用说明

### 数值格式
- **负数表示减少**：`-0.10` = -10% 建造成本
- **正数表示增加**：`0.10` = +10% 属性值
- 通常取值范围：-0.10 到 0.10

### 关键属性
- **`instant = yes`**：必须添加，否则加成不会立即生效

### 文件位置
将国家精神添加到以下文件：
- `common/national_focus/` - 国策解锁的国家精神
- `common/ideas/` - 国家理念中的精神
- `common/decisions/` - 决议解锁的国家精神

---

**文档版本**: Hearts of Iron IV 1.14.x  
**生成日期**: 2026年5月