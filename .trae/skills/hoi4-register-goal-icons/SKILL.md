---
name: "hoi4-register-goal-icons"
description: "Registers goal icons for HOI4 national focuses. Invoke when user needs to register new goal icons to .gfx files and update focus files with new icon references."
---

# HOI4 国策图标注册

此skill用于将新的国策图标注册到gfx文件中，并更新国策文件中的图标引用。

## 触发条件

当用户需要：
- 将新图标文件注册到gfx文件
- 为国策更换新图标
- 批量更新国策图标引用

## 执行步骤

### 1. 确认图标文件位置

首先确认图标文件已放置在正确的目录，通常是：
- `gfx/interface/goals/<子目录>/`

### 2. 在gfx文件中注册图标

在对应的gfx文件中（如`interface/xxx.gfx`）添加图标注册：

**格式要求**：
- 每个普通图标后**紧跟**其shine版本
- shine版本包含完整的动画效果定义

**标准模板**：
```
SpriteType = {
    name = "GFX_goal_<标签>_<名称>"
    texturefile = "gfx/interface/goals/<目录>/<文件名>.png"
}
SpriteType = {
    name = "GFX_goal_<标签>_<名称>_shine"
    texturefile = "gfx/interface/goals/<目录>/<文件名>.png"
    effectFile = "gfx/FX/buttonstate.lua"
    animation = {
        animationmaskfile = "gfx/interface/goals/<目录>/<文件名>.png"
        animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
        animationrotation = -90.0
        animationlooping = no
        animationtime = 0.75
        animationdelay = 0
        animationblendmode = "add"
        animationtype = "scrolling"
        animationrotationoffset = { x = 0.0 y = 0.0 }
        animationtexturescale = { x = 1.0 y = 1.0 }
    }
    animation = {
        animationmaskfile = "gfx/interface/goals/<目录>/<文件名>.png"
        animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
        animationrotation = 90.0
        animationlooping = no
        animationtime = 0.75
        animationdelay = 0
        animationblendmode = "add"
        animationtype = "scrolling"
        animationrotationoffset = { x = 0.0 y = 0.0 }
        animationtexturescale = { x = 1.0 y = 1.0 }
    }
    legacy_lazy_load = no
}
```

### 3. 更新国策文件中的图标引用

**重要**：不要只替换`GFX_goal_unknown`！

需要替换所有不符合新命名规范的图标引用：
- 外部图标引用（如`GFX_goal_USA_xxx`、`GFX_goal_AUS_xxx`等）
- 通用图标引用（如`GFX_goal_unknown`、`GFX_raisethearmies`等）
- 其他模组的图标引用

**正确做法**：
1. 读取国策文件，找出所有`icon =`行
2. 识别哪些国策需要更新（根据图标文件名与国策ID的对应关系）
3. 将旧图标引用替换为新注册的图标名

### 4. 命名规范

- 图标文件名：`<标签>_<描述>.png`（如`JAP_iron_fist.png`）
- 图标注册名：`GFX_goal_<标签>_<描述>`（如`GFX_goal_JAP_iron_fist`）
- shine版本：`GFX_goal_<标签>_<描述>_shine`

## 常见错误

1. **只替换unknown**：不要只查找`GFX_goal_unknown`，要查找所有需要替换的图标引用
2. **shine不紧跟**：shine版本必须紧跟在对应普通图标后面
3. **破坏gfx结构**：编辑时注意括号配对，避免结构混乱
4. **命名不一致**：图标名、注册名、国策引用名要保持一致

## 示例

假设有图标文件`JAP_new_focus.png`：

1. 注册到gfx：
```
SpriteType = {
    name = "GFX_goal_JAP_new_focus"
    texturefile = "gfx/interface/goals/KXX_JAP/JAP_new_focus.png"
}
SpriteType = {
    name = "GFX_goal_JAP_new_focus_shine"
    ...动画配置...
}
```

2. 更新国策：
```
# 原来
icon = GFX_goal_USA_some_icon

# 改为
icon = GFX_goal_JAP_new_focus
```
