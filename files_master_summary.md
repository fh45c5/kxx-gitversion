# 文件总汇总（含被排除项）

范围：`E:\Games\kxx-gitversion`。合并上一步报告的三个来源：

- **§A**：文件名以 `RD_` / `focus-` 开头的全部文件
- **§B**：与日本 / 台湾 / 朝鲜 / 西藏相关的文件（路径任一段命中，不限前缀）
- **§C**：日本部分里被排除的项（KXX_/SCB_ 前缀、KXX_/SCB_ 目录、含 Socialist、`history/countries/JAP - Japan.txt`）

## 总览

| 项目 | 数量 |
|---|---|
| 去重后文件总数 | **3392** |
| §A | 142 |
| §B | 2938 |
| §C（被排除项） | 367 |
| §A ∩ §B | 53 |
| §A ∩ §C | 0 |
| §B ∩ §C | 2 |

三个来源相加为 3447 条记录，去重后 3392 个文件（重复计入见上表交集）。

地区分组（§B）：日本 2286、台湾 571、朝鲜 71、西藏 61

（同一文件可同时命中多个地区，地区计数之和为 2989，§B 去重后为 2938。）

§B ∩ §C 的文件：`gfx/interface/goals/GFX_TAISOC_ties_with_japanese_socialists-248360.dds`、`gfx/interface/goals/KXX_FX/JAP_taisho_lesson.png`

## §C 被排除项的构成

| 排除原因 | 文件数 |
|---|---|
| 目录 KXX_/SCB_ | 290 |
| 含 Socialist 字样 | 50 |
| 文件名 KXX_/SCB_ 前缀 | 26 |
| JAP - Japan.txt | 1 |

## 按扩展名

| 扩展名 | 合计（去重文件） |
|---|---|
| .dds | 1517 |
| .png | 1115 |
| .tga | 439 |
| .txt | 131 |
| .gfx | 126 |
| .yml | 58 |
| .gui | 3 |
| .wav | 3 |

## 按目录（前 20）

| 目录 | 文件数 |
|---|---|
| `gfx/interface` | 2322 |
| `gfx/flags` | 425 |
| `gfx/leaders` | 181 |
| `gfx/event_pictures` | 125 |
| `common/national_focus` | 36 |
| `common/decisions` | 23 |
| `common/ideas` | 22 |
| `gfx/super_events` | 10 |
| `gfx/event` | 7 |
| `history/units` | 5 |
| `common/scripted_effects` | 4 |
| `common/countries` | 3 |
| `common/scripted_guis` | 3 |
| `common/scripted_localisation` | 3 |
| `common/scripted_triggers` | 3 |
| `history/countries` | 3 |
| `sound/menu` | 3 |
| `common/on_actions` | 2 |
| `common/opinion_modifiers` | 2 |
| `localisation/english` | 2 |

## .gfx 与图标

- 去重 .gfx：**126 个**（§A 113 / 仅 §B 10 / §C 3），共注册 **8883 条** sprite。
- 图标明细见 `rd_focus_gfx_icons.md` / `.tsv`。

## 完整合并清单（3392）

每条格式：`[来源] 路径`；来源为 A/B/C 的组合，C 的条目后缀排除原因。

```
[B] common/bop/JAP.txt
[B] common/countries/Japan_Revolt.txt
[B] common/countries/Taiwan.txt
[B] common/countries/hokkaido_puppet.txt
[B] common/decisions/Fengtian_Japan_decisions.txt
[B] common/decisions/JAP_construction.txt
[B] common/decisions/Japan_Reworked_decisions.txt
[C | 含 Socialist 字样] common/decisions/Japan_Socialist_decisions.txt
[B] common/decisions/Japan_decisions.txt
[C | 文件名 KXX_/SCB_ 前缀] common/decisions/KXX_JAP_debug.txt
[B] common/decisions/Nippon_Taiheiyosenso.txt
[A] common/decisions/RD_China_decisions.txt
[A] common/decisions/RD_Guides_decisions.txt
[A] common/decisions/RD_Philippines_decisions.txt
[C | 文件名 KXX_/SCB_ 前缀] common/decisions/SCB_JAP_party_cabinet_decisions.txt
[B] common/decisions/Taiwan_decisions.txt
[B] common/decisions/categories/Fengtian_Japan_decision_categories.txt
[B] common/decisions/categories/JAP_decision_categories.txt
[B] common/decisions/categories/Japan_Reworked_decisions_categories.txt
[C | 含 Socialist 字样] common/decisions/categories/Japan_Socialist_decision_categoties.txt
[B] common/decisions/categories/Japan_decision_categories.txt
[A] common/decisions/categories/RD_Guides_decision_categories.txt
[A] common/decisions/categories/RD_philippines_decision_categories.txt
[B] common/decisions/categories/Taiwan_decision_categories.txt
[B] common/decisions/categories/korea-jap_decisions_category.txt
[B] common/decisions/categories/nippon_decisions.txt
[B] common/decisions/korea-jap_decisions.txt
[B] common/dynamic_modifiers/JAP_dynamic_modifier.txt
[B] common/ideas/FX_Japan_ideas.txt
[B] common/ideas/JAP_Ministers_ideas.txt
[B] common/ideas/Japan_Rework_ideas.txt
[B] common/ideas/Japanese_Korea_ideas.txt
[B] common/ideas/Japanese_Taiwan_ideas.txt
[B] common/ideas/KX_taiwan_Minister.txt
[A] common/ideas/RD_China_Unification_ideas.txt
[A] common/ideas/RD_Lu_xun_Ministers.txt
[A] common/ideas/RD_Shanxi_Ministers.txt
[A+B] common/ideas/RD_TAI_Ministers.txt
[A] common/ideas/RD_Viet_Ministers_ideas.txt
[A] common/ideas/RD_misc_Minister.txt
[B] common/ideas/RF_Korea.txt
[B] common/ideas/RF_Taiwan.txt
[C | 文件名 KXX_/SCB_ 前缀] common/ideas/SCB_JAP_Revolution_ideas.txt
[C | 文件名 KXX_/SCB_ 前缀] common/ideas/SCB_JAP_democracy_ideas.txt
[B] common/ideas/Socialist_Tibet_ideas.txt
[B] common/ideas/TAI ideas.txt
[B] common/ideas/Taiwan_ideas.txt
[C | 含 Socialist 字样] common/ideas/japansocialist_ideas.txt
[B] common/ideas/okinawa_ideas.txt
[B] common/ideas/viet_pro_jap_ideas.txt
[B] common/military_industrial_organization/organizations/JAP_organization.txt
[B] common/national_focus/JAP_CW_military.txt
[B] common/national_focus/JAP_CW_shongunate.txt
[B] common/national_focus/JAP_CW_southcourt.txt
[B] common/national_focus/JAP_democracy_authdem.txt
[B] common/national_focus/JAP_democracy_bin_akao.txt
[B] common/national_focus/JAP_democracy_election.txt
[B] common/national_focus/JAP_democracy_marlib.txt
[B] common/national_focus/JAP_democracy_soccon.txt
[B] common/national_focus/JAP_democracy_socdem.txt
[B] common/national_focus/JAP_democracy_tohokai.txt
[B] common/national_focus/JAP_generic_economy.txt
[B] common/national_focus/JAP_generic_foreign.txt
[B] common/national_focus/JAP_generic_military.txt
[B] common/national_focus/JAP_military_koudouha.txt
[B] common/national_focus/JAP_military_toseiha.txt
[B] common/national_focus/JAP_minkan_blackdragon.txt
[B] common/national_focus/JAP_minkan_nichiren.txt
[B] common/national_focus/JAP_minkan_panasiaism.txt
[B] common/national_focus/JAP_minkan_peasantism.txt
[B] common/national_focus/JAP_minkan_yakuza.txt
[B] common/national_focus/JAP_natunity_IRAA.txt
[B] common/national_focus/JAP_natunity_IRAA_A.txt
[B] common/national_focus/JAP_natunity_IRAA_PRE.txt
[B] common/national_focus/JAP_natunity_IRAA_left.txt
[B] common/national_focus/JAP_natunity_IRAA_right.txt
[B] common/national_focus/JAP_natunity_zaibatsu.txt
[C | 含 Socialist 字样] common/national_focus/JAP_socialist_revolution.txt
[B] common/national_focus/Japan_Postwar.txt
[B] common/national_focus/Japanese_Empire.txt
[B] common/national_focus/Korea.txt
[C | 文件名 KXX_/SCB_ 前缀] common/national_focus/SCB_JAP_Revolution.txt
[C | 文件名 KXX_/SCB_ 前缀] common/national_focus/SCB_JAP_democracy_soccon_marlib.txt
[C | 文件名 KXX_/SCB_ 前缀] common/national_focus/SCB_JAP_generic_economy-military.txt
[C | 文件名 KXX_/SCB_ 前缀] common/national_focus/SCB_JAP_natunity_bureaucracy_military.txt
[B] common/national_focus/Tibet.txt
[B] common/national_focus/taiwan-tree.txt
[B] common/on_actions/JAP_parliament_gui_on_actions.txt
[B] common/on_actions/on_actions_japan.txt
[A] common/opinion_modifiers/RD_opinion_modifiers.txt
[B] common/opinion_modifiers/TWN_opinion_modifiers.txt
[B] common/scripted_effects/FX_Japan_effects.txt
[B] common/scripted_effects/JAP_Rework_scripted_effects.txt
[B] common/scripted_effects/JAP_parliament_gui_scripted_effects.txt
[A] common/scripted_effects/RD_replace_kx_scripted_effects.txt
[B] common/scripted_guis/JAP_parliament_gui.txt
[B] common/scripted_guis/Japan_China_influence_gui.txt
[B] common/scripted_guis/japan_national_populairty_scripted_gui.txt
[B] common/scripted_localisation/JAP_parliament_gui_scripted_localisation.txt
[B] common/scripted_localisation/TIB_socialist_scripted_loc.txt
[B] common/scripted_localisation/rework_JAP.txt
[B] common/scripted_triggers/JAP_Rework_scripted_triggers.txt
[B] common/scripted_triggers/JAP_congress_scripted_triggers.txt
[B] common/scripted_triggers/Japan_scripted_triggers.txt
[A] common/unit_leader/RD_traits.txt
[A] common/units/names_ships/RD_chinese_ship_names.txt
[B] events/FX_Japan_Shogun.txt
[B] events/Japan.txt
[B] events/Japan_Foreign.txt
[B] events/Japan_events_new.txt
[C | 文件名 KXX_/SCB_ 前缀] events/KXX_JAP_Expand.txt
[C | 文件名 KXX_/SCB_ 前缀] events/KXX_JAP_RED_Expand.txt
[A] events/RD_Guides.txt
[A+B] events/RD_Japan_News_Events.txt
[A] events/RD_Shanghai_Commune.txt
[A] events/RD_Shanghai_Commune_Foreign.txt
[A] events/RD_Super_events.txt
[B] events/RF_Taiwan.txt
[C | 文件名 KXX_/SCB_ 前缀] events/SCB_JAP_Redux.txt
[B] events/Socialist_Tibet_Events.txt
[B] events/Taiwan.txt
[B] events/rework_JAP.txt
[B] gfx/EnhancedSuperEvents/SPEVNT_Japanese_America.png
[B] gfx/event/Taiwan_MING.png
[B] gfx/event/Taiwan_map.png
[B] gfx/event/Taiwan_rotscapital.png
[B] gfx/event/Taiwan_suger.png
[B] gfx/event/news_event_TAI_Independent.png
[B] gfx/event/news_event_TAI_buddha_nuke.png
[B] gfx/event/taiwan_anarchy_uprising.png
[B] gfx/event_pictures/CHL/rise_of_japan.png
[B] gfx/event_pictures/East Asia/GXC/GFX_report_event_GXC_taixu_world.png
[B] gfx/event_pictures/East Asia/Japan/GEACPS_image.png
[B] gfx/event_pictures/East Asia/Japan/Jap_coup.png
[B] gfx/event_pictures/East Asia/Japan/Katayama.png
[B] gfx/event_pictures/East Asia/Japan/Kikue_image.png
[B] gfx/event_pictures/East Asia/Japan/akahata_image.png
[B] gfx/event_pictures/East Asia/Japan/anarchist_conference.png
[B] gfx/event_pictures/East Asia/Japan/chaplin_visits_japan.png
[B] gfx/event_pictures/East Asia/Japan/genyosha_image.png
[B] gfx/event_pictures/East Asia/Japan/hashimoto_image.png
[B] gfx/event_pictures/East Asia/Japan/hirotio_uniform.png
[B] gfx/event_pictures/East Asia/Japan/ikeda_image.png
[B] gfx/event_pictures/East Asia/Japan/ikki_kita_1.png
[B] gfx/event_pictures/East Asia/Japan/ikki_kita_image.png
[B] gfx/event_pictures/East Asia/Japan/inoue_nissho.png
[B] gfx/event_pictures/East Asia/Japan/iraa_1.png
[B] gfx/event_pictures/East Asia/Japan/iraa_2.png
[B] gfx/event_pictures/East Asia/Japan/iraa_3.png
[B] gfx/event_pictures/East Asia/Japan/ishiwara_image.png
[B] gfx/event_pictures/East Asia/Japan/iwane_matsui_image.png
[B] gfx/event_pictures/East Asia/Japan/jap_manchu_exploit.png
[B] gfx/event_pictures/East Asia/Japan/jap_manchurian_exploitation.png
[B] gfx/event_pictures/East Asia/Japan/japan_akira.png
[B] gfx/event_pictures/East Asia/Japan/japan_ambassador_kisaburo.png
[B] gfx/event_pictures/East Asia/Japan/japan_announcement.png
[B] gfx/event_pictures/East Asia/Japan/japan_barricade.png
[B] gfx/event_pictures/East Asia/Japan/japan_battle_flag.png
[B] gfx/event_pictures/East Asia/Japan/japan_battleship_kongo.png
[B] gfx/event_pictures/East Asia/Japan/japan_conscription.png
[B] gfx/event_pictures/East Asia/Japan/japan_crowd.png
[B] gfx/event_pictures/East Asia/Japan/japan_diet.png
[B] gfx/event_pictures/East Asia/Japan/japan_diet_disollution.png
[B] gfx/event_pictures/East Asia/Japan/japan_drought_farmers.png
[B] gfx/event_pictures/East Asia/Japan/japan_economy_building.png
[B] gfx/event_pictures/East Asia/Japan/japan_election_1936.png
[B] gfx/event_pictures/East Asia/Japan/japan_foreign_minister.png
[B] gfx/event_pictures/East Asia/Japan/japan_foreign_minister_2.png
[B] gfx/event_pictures/East Asia/Japan/japan_hirohito_addressing.png
[B] gfx/event_pictures/East Asia/Japan/japan_infrastructure.png
[B] gfx/event_pictures/East Asia/Japan/japan_islam_association.png
[B] gfx/event_pictures/East Asia/Japan/japan_kodoha_coup.png
[B] gfx/event_pictures/East Asia/Japan/japan_kokumin_domei.png
[B] gfx/event_pictures/East Asia/Japan/japan_kwantung.png
[B] gfx/event_pictures/East Asia/Japan/japan_lost_decade.png
[B] gfx/event_pictures/East Asia/Japan/japan_meeting.png
[B] gfx/event_pictures/East Asia/Japan/japan_motorized.png
[B] gfx/event_pictures/East Asia/Japan/japan_mutsu.png
[B] gfx/event_pictures/East Asia/Japan/japan_news.png
[B] gfx/event_pictures/East Asia/Japan/japan_officers_observe.png
[B] gfx/event_pictures/East Asia/Japan/japan_parade_shanghai.png
[B] gfx/event_pictures/East Asia/Japan/japan_politician.png
[B] gfx/event_pictures/East Asia/Japan/japan_rentaro.png
[B] gfx/event_pictures/East Asia/Japan/japan_restorationist_centralist.png
[B] gfx/event_pictures/East Asia/Japan/japan_revolt.png
[B] gfx/event_pictures/East Asia/Japan/japan_rice_farmers.png
[B] gfx/event_pictures/East Asia/Japan/japan_rikken_seiyukai.png
[B] gfx/event_pictures/East Asia/Japan/japan_rising_sun.png
[B] gfx/event_pictures/East Asia/Japan/japan_science.png
[C | 含 Socialist 字样] gfx/event_pictures/East Asia/Japan/japan_socialist_victory.png
[B] gfx/event_pictures/East Asia/Japan/japan_stock_exchange_crisis.png
[B] gfx/event_pictures/East Asia/Japan/japan_troops_gas.png
[B] gfx/event_pictures/East Asia/Japan/japan_ultimatum.png
[B] gfx/event_pictures/East Asia/Japan/japan_voting.png
[B] gfx/event_pictures/East Asia/Japan/japan_zero.png
[B] gfx/event_pictures/East Asia/Japan/japanese_battleship.png
[B] gfx/event_pictures/East Asia/Japan/japanese_officer_phone.png
[B] gfx/event_pictures/East Asia/Japan/japanese_officer_saluting.png
[B] gfx/event_pictures/East Asia/Japan/japanese_officers.png
[B] gfx/event_pictures/East Asia/Japan/japanese_soldiers.png
[B] gfx/event_pictures/East Asia/Japan/japanese_troops_train.png
[B] gfx/event_pictures/East Asia/Japan/japanese_young_officers.png
[B] gfx/event_pictures/East Asia/Japan/jcp_congress.png
[B] gfx/event_pictures/East Asia/Japan/jcp_congress_2.png
[B] gfx/event_pictures/East Asia/Japan/jcp_tokuda.png
[B] gfx/event_pictures/East Asia/Japan/kenzi_image.png
[B] gfx/event_pictures/East Asia/Japan/kenzo_image.png
[B] gfx/event_pictures/East Asia/Japan/konoe_cosplay_image.png
[B] gfx/event_pictures/East Asia/Japan/league_of_blood_trial.png
[B] gfx/event_pictures/East Asia/Japan/minseito_image.png
[B] gfx/event_pictures/East Asia/Japan/nakano_image_2.png
[B] gfx/event_pictures/East Asia/Japan/news_event_communist_japan.png
[B] gfx/event_pictures/East Asia/Japan/news_event_japanese_civil_war.png
[B] gfx/event_pictures/East Asia/Japan/news_event_japanese_diet.png
[B] gfx/event_pictures/East Asia/Japan/news_event_kodoha_coup.png
[B] gfx/event_pictures/East Asia/Japan/news_event_league_of_blood.png
[B] gfx/event_pictures/East Asia/Japan/news_event_toseiha_coup.png
[B] gfx/event_pictures/East Asia/Japan/nichiren_army.png
[B] gfx/event_pictures/East Asia/Japan/nosaka_image.png
[B] gfx/event_pictures/East Asia/Japan/ozaki_image.png
[B] gfx/event_pictures/East Asia/Japan/red_flag_japan.png
[B] gfx/event_pictures/East Asia/Japan/sadao_araki_image.png
[B] gfx/event_pictures/East Asia/Japan/senoo_image.png
[B] gfx/event_pictures/East Asia/Japan/shakai_taishuto_1937.png
[B] gfx/event_pictures/East Asia/Japan/shakai_taishuto_vote_poster.png
[B] gfx/event_pictures/East Asia/Japan/shumei_image_2.png
[B] gfx/event_pictures/East Asia/Japan/smilling_communism.png
[C | 含 Socialist 字样] gfx/event_pictures/East Asia/Japan/socialist_japan_protest.png
[B] gfx/event_pictures/East Asia/Japan/sukarno_ajapan.png
[B] gfx/event_pictures/East Asia/Japan/tachibana_image.png
[B] gfx/event_pictures/East Asia/Japan/tohokai_image.png
[B] gfx/event_pictures/East Asia/Japan/tohokai_image_2.png
[B] gfx/event_pictures/East Asia/Japan/tokuda_image_3.png
[B] gfx/event_pictures/East Asia/Japan/tsuji_jun_image.png
[B] gfx/event_pictures/East Asia/Japan/yakuza.png
[B] gfx/event_pictures/East Asia/Japan/yaushito_smiling.png
[B] gfx/event_pictures/East Asia/Japan/zaibatsu_image.png
[B] gfx/event_pictures/East Asia/TWI/report_event_TWI_taiwan_info.png
[B] gfx/event_pictures/JAP/JAP_Tokugawa_Yoshinobu.png
[B] gfx/event_pictures/JAP/JAP_koiso_kuniaki_event.png
[B] gfx/event_pictures/JAP/JAP_seiyukai_all_leader.png
[C | 文件名 KXX_/SCB_ 前缀] gfx/event_pictures/JAP/SCB_report_event_1.png
[C | 文件名 KXX_/SCB_ 前缀] gfx/event_pictures/JAP/SCB_report_event_2.png
[C | 文件名 KXX_/SCB_ 前缀] gfx/event_pictures/JAP/SCB_report_event_3.png
[C | 文件名 KXX_/SCB_ 前缀] gfx/event_pictures/JAP/SCB_report_event_4.png
[C | 文件名 KXX_/SCB_ 前缀] gfx/event_pictures/JAP/SCB_report_event_5.png
[C | 文件名 KXX_/SCB_ 前缀] gfx/event_pictures/JAP/SCB_report_event_6.png
[C | 文件名 KXX_/SCB_ 前缀] gfx/event_pictures/JAP/SCB_report_event_7.png
[C | 文件名 KXX_/SCB_ 前缀] gfx/event_pictures/JAP/SCB_report_event_8.png
[C | 文件名 KXX_/SCB_ 前缀] gfx/event_pictures/JAP/SCB_report_event_9.png
[B] gfx/event_pictures/JAP/jap_daihonei_army.png
[B] gfx/event_pictures/JAP/jap_kinzokugen_event.png
[B] gfx/event_pictures/JAP/jap_shinseiryujinkai.png
[B] gfx/event_pictures/report_event_JAP_revolution_strike_1.png
[B] gfx/event_pictures/world_news/GFX_attack_japs.dds
[B] gfx/flags/BRG_ANGLO_JAPAN_JAP_totalist.tga
[B] gfx/flags/BRG_korea.tga
[B] gfx/flags/BRG_korea2.tga
[B] gfx/flags/CAL_JAP.tga
[B] gfx/flags/CAL_JAP_1.tga
[B] gfx/flags/CAL_JAP_2.tga
[B] gfx/flags/CAL_JAP_3.tga
[B] gfx/flags/CHINA_JAPANESE_PUPPET.tga
[C | 含 Socialist 字样] gfx/flags/CHINA_SOCIALIST_JAPANESE_PUPPET.tga
[B] gfx/flags/CHI_JAP_volkstaat.tga
[B] gfx/flags/CNH_TECHJAP.tga
[B] gfx/flags/FNG_SINO_KOR_FED.tga
[B] gfx/flags/FNG_bandit_jap.tga
[B] gfx/flags/GXC_TAIXUANA.tga
[B] gfx/flags/GXC_TAIXUANA_ASIAOREARTH.tga
[B] gfx/flags/JAP.tga
[B] gfx/flags/JAP_AKAMATSU.tga
[B] gfx/flags/JAP_AKKD.tga
[B] gfx/flags/JAP_ASANUMA.tga
[B] gfx/flags/JAP_Araki.tga
[B] gfx/flags/JAP_BURAKU_LEAGUE.tga
[B] gfx/flags/JAP_COF_puppet.tga
[B] gfx/flags/JAP_FUKUMOTO.tga
[B] gfx/flags/JAP_HASHIMOTO_ASIA.tga
[B] gfx/flags/JAP_HASHIMOTO_WORLD.tga
[B] gfx/flags/JAP_HIRANO.tga
[B] gfx/flags/JAP_HISASHI.tga
[B] gfx/flags/JAP_HISASHI_Reformed.tga
[B] gfx/flags/JAP_Hakko_Ichui.tga
[B] gfx/flags/JAP_IKKI_KITA_WORLD.tga
[B] gfx/flags/JAP_INT_puppet.tga
[B] gfx/flags/JAP_JUDA.tga
[B] gfx/flags/JAP_JUDA_EX.tga
[B] gfx/flags/JAP_KANSON.tga
[B] gfx/flags/JAP_KENJI.tga
[B] gfx/flags/JAP_KENZO.tga
[B] gfx/flags/JAP_KIKUE.tga
[B] gfx/flags/JAP_KINGORO_FX.tga
[B] gfx/flags/JAP_KITA.tga
[B] gfx/flags/JAP_KITA_ASIA.tga
[B] gfx/flags/JAP_KOREA_MONGOLIA_JAPAN.tga
[B] gfx/flags/JAP_KOZABURO.tga
[B] gfx/flags/JAP_KOZABURO_totalist.tga
[B] gfx/flags/JAP_Kingoro.tga
[B] gfx/flags/JAP_Kodoha.tga
[B] gfx/flags/JAP_MANCHURIA_UNION.tga
[B] gfx/flags/JAP_MATSUMOTO.tga
[B] gfx/flags/JAP_MATSUMOTO_FX.tga
[B] gfx/flags/JAP_MONGOL_EMPIRE.tga
[B] gfx/flags/JAP_NAKANO_1984.tga
[B] gfx/flags/JAP_NICHIREN.tga
[B] gfx/flags/JAP_NICHIREN_SHOGUN.tga
[B] gfx/flags/JAP_NICHIREN_SHOGUN_1.tga
[C | 含 Socialist 字样] gfx/flags/JAP_NICHIREN_radical_socialist.tga
[B] gfx/flags/JAP_NICHIREN_social_democrat.tga
[B] gfx/flags/JAP_NICHIREN_totalist.tga
[B] gfx/flags/JAP_NOSAKA.tga
[B] gfx/flags/JAP_NOSAKA_FX.tga
[B] gfx/flags/JAP_PANTHERA_1.tga
[B] gfx/flags/JAP_PANTHERA_2.tga
[C | 含 Socialist 字样] gfx/flags/JAP_RED_radical_socialist.tga
[B] gfx/flags/JAP_RED_syndicalist.tga
[B] gfx/flags/JAP_RED_totalist.tga
[B] gfx/flags/JAP_ROERICH.tga
[B] gfx/flags/JAP_ROERICH_PAN_ASIA.tga
[B] gfx/flags/JAP_ROERICH_WORLD.tga
[B] gfx/flags/JAP_Republican_Fem.tga
[B] gfx/flags/JAP_SANSHIRO.tga
[B] gfx/flags/JAP_SANZO_MONBOL.tga
[B] gfx/flags/JAP_SCHIZO.tga
[B] gfx/flags/JAP_SHUMEI.tga
[B] gfx/flags/JAP_SHUMEI_ASIA.tga
[B] gfx/flags/JAP_SHUMEI_MUSLIM.tga
[B] gfx/flags/JAP_SINO_JAPAN.tga
[B] gfx/flags/JAP_SOKA_GAKKAI_WORLD.tga
[B] gfx/flags/JAP_Shinshu.tga
[B] gfx/flags/JAP_Soka_Gakkai.tga
[B] gfx/flags/JAP_Suiheisha_temp.tga
[B] gfx/flags/JAP_TOHOKAI_TWO.tga
[B] gfx/flags/JAP_TOKOHAI.tga
[B] gfx/flags/JAP_TOKUDA.tga
[B] gfx/flags/JAP_TURANIA.tga
[B] gfx/flags/JAP_TWI.tga
[B] gfx/flags/JAP_Tachi_Asia.tga
[B] gfx/flags/JAP_ULTRA_SCHIZO.tga
[B] gfx/flags/JAP_YAKUZA_national_populist.tga
[B] gfx/flags/JAP_YAKUZA_paternal_autocrat.tga
[B] gfx/flags/JAP_YAMAKAWA.tga
[B] gfx/flags/JAP_YAMANA.tga
[B] gfx/flags/JAP_ZAIBATSU.tga
[B] gfx/flags/JAP_black_dragon.tga
[B] gfx/flags/JAP_diedie.tga
[B] gfx/flags/JAP_iww_asia.tga
[B] gfx/flags/JAP_military.tga
[B] gfx/flags/JAP_national_populist.tga
[B] gfx/flags/JAP_nichiren_redux.tga
[B] gfx/flags/JAP_nouhonsyugi.tga
[B] gfx/flags/JAP_oomoto.tga
[B] gfx/flags/JAP_oomoto_world.tga
[B] gfx/flags/JAP_paternal_autocrat.tga
[C | 含 Socialist 字样] gfx/flags/JAP_radical_socialist.tga
[B] gfx/flags/JAP_red_army.tga
[B] gfx/flags/JAP_red_empire_txt_vanguardist.tga
[B] gfx/flags/JAP_republican.tga
[B] gfx/flags/JAP_rounou.tga
[B] gfx/flags/JAP_ryujinkai.tga
[B] gfx/flags/JAP_shogunate.tga
[B] gfx/flags/JAP_shogunate_authoritarian_democrat.tga
[B] gfx/flags/JAP_shogunate_kuniyuki_paternal_autocrat.tga
[B] gfx/flags/JAP_shogunate_paternal_autocrat.tga
[C | 含 Socialist 字样] gfx/flags/JAP_socialist_league.tga
[B] gfx/flags/JAP_state_totalist.tga
[B] gfx/flags/JAP_syndicalist.tga
[B] gfx/flags/JAP_tohokai.tga
[B] gfx/flags/JAP_totalist.tga
[B] gfx/flags/JAP_valkist.tga
[B] gfx/flags/KOG_POR_formosa.tga
[B] gfx/flags/KOG_POR_korea.tga
[B] gfx/flags/KOR_JAP.tga
[B] gfx/flags/KOR_JUCHEJOE_national_populist.tga
[B] gfx/flags/KOR_JUCHEJOE_totalist.tga
[B] gfx/flags/PHI_jap_puppet.tga
[B] gfx/flags/PHI_jap_puppet_war.tga
[B] gfx/flags/TAI_AGRARIAN.tga
[B] gfx/flags/TAI_AUSTRONESIA.tga
[B] gfx/flags/TAI_CNT.tga
[B] gfx/flags/TAI_CNT_gobal.tga
[B] gfx/flags/TAI_COMMUNIST_syndicalist.tga
[B] gfx/flags/TAI_COMMUNIST_totalist.tga
[B] gfx/flags/TAI_CUONGDE.tga
[B] gfx/flags/TAI_ESPERANTO_WORLD_1.tga
[B] gfx/flags/TAI_ESPERANTO_WORLD_2.tga
[B] gfx/flags/TAI_ESPERANTO_WORLD_3.tga
[B] gfx/flags/TAI_JAPAN_EMPIRE.tga
[B] gfx/flags/TAI_MIN.tga
[B] gfx/flags/TAI_REPUBLIC.tga
[B] gfx/flags/TAI_REPUBLIC_radical_socialist.tga
[B] gfx/flags/TAI_XIONGZHENG.tga
[B] gfx/flags/TAI_communistchi_syndicalist.tga
[B] gfx/flags/TAI_communistchi_totalist.tga
[B] gfx/flags/TAI_hsi_accelerationism.tga
[B] gfx/flags/TAI_tan_accelerationism.tga
[B] gfx/flags/TIA_JAP.tga
[B] gfx/flags/TIB_COM.tga
[B] gfx/flags/TIB_COMMIE_1.tga
[B] gfx/flags/TIB_COMMIE_2.tga
[B] gfx/flags/TIB_JIGME.tga
[B] gfx/flags/TIB_LECREVOLUTION.tga
[B] gfx/flags/TIB_Totalist.tga
[B] gfx/flags/TIB_YUEXE.tga
[B] gfx/flags/TIB_radical_socialist.tga
[B] gfx/flags/TIB_syndicalist.tga
[B] gfx/flags/TWI_FORMOSA.tga
[B] gfx/flags/medium/BRG_ANGLO_JAPAN_JAP_totalist.tga
[B] gfx/flags/medium/BRG_korea.tga
[B] gfx/flags/medium/BRG_korea2.tga
[B] gfx/flags/medium/CAL_JAP.tga
[B] gfx/flags/medium/CAL_jap_1.tga
[B] gfx/flags/medium/CAL_jap_2.tga
[B] gfx/flags/medium/CAL_jap_3.tga
[B] gfx/flags/medium/CHINA_JAPANESE_PUPPET.tga
[C | 含 Socialist 字样] gfx/flags/medium/CHINA_SOCIALIST_JAPANESE_PUPPET.tga
[B] gfx/flags/medium/CHI_JAP_volkstaat.tga
[B] gfx/flags/medium/CNH_TECHJAP.tga
[B] gfx/flags/medium/FNG_SINO_KOR_FED.tga
[B] gfx/flags/medium/FNG_bandit_jap.tga
[B] gfx/flags/medium/GXC_TAIXUANA.tga
[B] gfx/flags/medium/GXC_TAIXUANA_ASIAOREARTH.tga
[B] gfx/flags/medium/JAP.tga
[B] gfx/flags/medium/JAP_AKAMATSU.tga
[B] gfx/flags/medium/JAP_AKKD.tga
[B] gfx/flags/medium/JAP_ASANUMA.tga
[B] gfx/flags/medium/JAP_Araki.tga
[B] gfx/flags/medium/JAP_BLACK_DRAGON.tga
[B] gfx/flags/medium/JAP_BURAKU_LEAGUE.tga
[B] gfx/flags/medium/JAP_COF_puppet.tga
[B] gfx/flags/medium/JAP_FUKUMOTO.tga
[B] gfx/flags/medium/JAP_HASHIMOTO_ASIA.tga
[B] gfx/flags/medium/JAP_HASHIMOTO_WORLD.tga
[B] gfx/flags/medium/JAP_HIRANO.tga
[B] gfx/flags/medium/JAP_HISASHI.tga
[B] gfx/flags/medium/JAP_HISASHI_Reformed.tga
[B] gfx/flags/medium/JAP_Hakko_Ichui.tga
[B] gfx/flags/medium/JAP_IKKI_KITA_WORLD.tga
[B] gfx/flags/medium/JAP_INT_puppet.tga
[B] gfx/flags/medium/JAP_JUDA.tga
[B] gfx/flags/medium/JAP_JUDA_EX.tga
[B] gfx/flags/medium/JAP_KANSON.tga
[B] gfx/flags/medium/JAP_KENJI.tga
[B] gfx/flags/medium/JAP_KENZO.tga
[B] gfx/flags/medium/JAP_KIKUE.tga
[B] gfx/flags/medium/JAP_KINGORO_FX.tga
[B] gfx/flags/medium/JAP_KITA.tga
[B] gfx/flags/medium/JAP_KITA_ASIA.tga
[B] gfx/flags/medium/JAP_KOREA_MONGOLIA_JAPAN.tga
[B] gfx/flags/medium/JAP_KOZABURO.tga
[B] gfx/flags/medium/JAP_KOZABURO_totalist.tga
[B] gfx/flags/medium/JAP_Kingoro.tga
[B] gfx/flags/medium/JAP_Kodoha.tga
[B] gfx/flags/medium/JAP_MANCHURIA_UNION.tga
[B] gfx/flags/medium/JAP_MATSUMOTO.tga
[B] gfx/flags/medium/JAP_MATSUMOTO_FX.tga
[B] gfx/flags/medium/JAP_MONGOL_EMPIRE.tga
[B] gfx/flags/medium/JAP_NAKANO_1984.tga
[B] gfx/flags/medium/JAP_NICHIREN.tga
[B] gfx/flags/medium/JAP_NICHIREN_SHOGUN.tga
[B] gfx/flags/medium/JAP_NICHIREN_SHOGUN_1.tga
[C | 含 Socialist 字样] gfx/flags/medium/JAP_NICHIREN_radical_socialist.tga
[B] gfx/flags/medium/JAP_NICHIREN_social_democrat.tga
[B] gfx/flags/medium/JAP_NICHIREN_totalist.tga
[B] gfx/flags/medium/JAP_NOSAKA.tga
[B] gfx/flags/medium/JAP_NOSAKA_FX.tga
[B] gfx/flags/medium/JAP_OOMOTO.tga
[B] gfx/flags/medium/JAP_OOMOTO_WORLD.tga
[B] gfx/flags/medium/JAP_PANTHERA_1.tga
[B] gfx/flags/medium/JAP_PANTHERA_2.tga
[C | 含 Socialist 字样] gfx/flags/medium/JAP_RED_radical_socialist.tga
[B] gfx/flags/medium/JAP_RED_syndicalist.tga
[B] gfx/flags/medium/JAP_RED_totalist.tga
[B] gfx/flags/medium/JAP_ROERICH.tga
[B] gfx/flags/medium/JAP_ROERICH_PAN_ASIA.tga
[B] gfx/flags/medium/JAP_ROERICH_WORLD.tga
[B] gfx/flags/medium/JAP_Republican_Fem.tga
[B] gfx/flags/medium/JAP_SANSHIRO.tga
[B] gfx/flags/medium/JAP_SANZO_MONBOL.tga
[B] gfx/flags/medium/JAP_SCHIZO.tga
[B] gfx/flags/medium/JAP_SHUMEI.tga
[B] gfx/flags/medium/JAP_SHUMEI_ASIA.tga
[B] gfx/flags/medium/JAP_SHUMEI_MUSLIM.tga
[B] gfx/flags/medium/JAP_SINO_JAPAN.tga
[B] gfx/flags/medium/JAP_SOKA_GAKKAI_WORLD.tga
[B] gfx/flags/medium/JAP_Shinshu.tga
[B] gfx/flags/medium/JAP_Soka_Gakkai.tga
[B] gfx/flags/medium/JAP_Suiheisha_temp.tga
[B] gfx/flags/medium/JAP_TOHOKAI_TWO.tga
[B] gfx/flags/medium/JAP_TOKOHAI.tga
[B] gfx/flags/medium/JAP_TOKUDA.tga
[B] gfx/flags/medium/JAP_TURANIA.tga
[B] gfx/flags/medium/JAP_TWI.tga
[B] gfx/flags/medium/JAP_Tachi_Asia.tga
[B] gfx/flags/medium/JAP_ULTRA_SCHIZO.tga
[B] gfx/flags/medium/JAP_YAKUZA_national_populist.tga
[B] gfx/flags/medium/JAP_YAKUZA_paternal_autocrat.tga
[B] gfx/flags/medium/JAP_YAMAKAWA.tga
[B] gfx/flags/medium/JAP_YAMANA.tga
[B] gfx/flags/medium/JAP_ZAIBATSU.tga
[B] gfx/flags/medium/JAP_diedie.tga
[B] gfx/flags/medium/JAP_iww_asia.tga
[B] gfx/flags/medium/JAP_military.tga
[B] gfx/flags/medium/JAP_national_populist.tga
[B] gfx/flags/medium/JAP_nichiren_redux.tga
[B] gfx/flags/medium/JAP_nouhonsyugi.tga
[B] gfx/flags/medium/JAP_paternal_autocrat.tga
[C | 含 Socialist 字样] gfx/flags/medium/JAP_radical_socialist.tga
[B] gfx/flags/medium/JAP_red_army.tga
[B] gfx/flags/medium/JAP_red_empire_txt_vanguardist.tga
[B] gfx/flags/medium/JAP_republican.tga
[B] gfx/flags/medium/JAP_rounou.tga
[B] gfx/flags/medium/JAP_ryujinkai.tga
[B] gfx/flags/medium/JAP_shogunate.tga
[B] gfx/flags/medium/JAP_shogunate_authoritarian_democrat.tga
[B] gfx/flags/medium/JAP_shogunate_kuniyuki_paternal_autocrat.tga
[B] gfx/flags/medium/JAP_shogunate_paternal_autocrat.tga
[C | 含 Socialist 字样] gfx/flags/medium/JAP_socialist_league.tga
[B] gfx/flags/medium/JAP_state_totalist.tga
[B] gfx/flags/medium/JAP_syndicalist.tga
[B] gfx/flags/medium/JAP_tohokai.tga
[B] gfx/flags/medium/JAP_totalist.tga
[B] gfx/flags/medium/JAP_valkist.tga
[B] gfx/flags/medium/KOG_POR_formosa.tga
[B] gfx/flags/medium/KOG_POR_korea.tga
[B] gfx/flags/medium/KOR_JAP.tga
[B] gfx/flags/medium/KOR_JUCHEJOE_national_populist.tga
[B] gfx/flags/medium/KOR_JUCHEJOE_totalist.tga
[B] gfx/flags/medium/TAI_AGRARIAN.tga
[B] gfx/flags/medium/TAI_AUSTRONESIA.tga
[B] gfx/flags/medium/TAI_CNT.tga
[B] gfx/flags/medium/TAI_CNT_gobal.tga
[B] gfx/flags/medium/TAI_COMMUNIST_syndicalist.tga
[B] gfx/flags/medium/TAI_COMMUNIST_totalist.tga
[B] gfx/flags/medium/TAI_CUONGDE.tga
[B] gfx/flags/medium/TAI_ESPERANTO_WORLD_1.tga
[B] gfx/flags/medium/TAI_ESPERANTO_WORLD_2.tga
[B] gfx/flags/medium/TAI_ESPERANTO_WORLD_3.tga
[B] gfx/flags/medium/TAI_JAPAN_EMPIRE.tga
[B] gfx/flags/medium/TAI_MIN.tga
[B] gfx/flags/medium/TAI_REPUBLIC.tga
[B] gfx/flags/medium/TAI_REPUBLIC_radical_socialist.tga
[B] gfx/flags/medium/TAI_XIONGZHENG.tga
[B] gfx/flags/medium/TAI_communistchi_syndicalist.tga
[B] gfx/flags/medium/TAI_communistchi_totalist.tga
[B] gfx/flags/medium/TAI_hsi_accelerationism.tga
[B] gfx/flags/medium/TAI_tan_accelerationism.tga
[B] gfx/flags/medium/TIA_JAP.tga
[B] gfx/flags/medium/TIB_COM.tga
[B] gfx/flags/medium/TIB_COMMIE_1.tga
[B] gfx/flags/medium/TIB_COMMIE_2.tga
[B] gfx/flags/medium/TIB_JIGME.tga
[B] gfx/flags/medium/TIB_LECREVOLUTION.tga
[B] gfx/flags/medium/TIB_YUEXE.tga
[B] gfx/flags/medium/TIB_radical_socialist.tga
[B] gfx/flags/medium/TIB_syndicalist.tga
[B] gfx/flags/medium/TIB_totalist.tga
[B] gfx/flags/medium/TWI_FORMOSA.tga
[B] gfx/flags/small/BRG_ANGLO_JAPAN_JAP_totalist.tga
[B] gfx/flags/small/BRG_korea.tga
[B] gfx/flags/small/BRG_korea2.tga
[B] gfx/flags/small/CAL_JAP.tga
[B] gfx/flags/small/CAL_jap_1.tga
[B] gfx/flags/small/CAL_jap_2.tga
[B] gfx/flags/small/CAL_jap_3.tga
[B] gfx/flags/small/CHINA_JAPANESE_PUPPET.tga
[C | 含 Socialist 字样] gfx/flags/small/CHINA_SOCIALIST_JAPANESE_PUPPET.tga
[B] gfx/flags/small/CHI_JAP_volkstaat.tga
[B] gfx/flags/small/CNH_TECHJAP.tga
[B] gfx/flags/small/FNG_SINO_KOR_FED.tga
[B] gfx/flags/small/FNG_bandit_jap.tga
[B] gfx/flags/small/GXC_TAIXUANA.tga
[B] gfx/flags/small/GXC_TAIXUANA_ASIAOREARTH.tga
[B] gfx/flags/small/JAP.tga
[B] gfx/flags/small/JAP_AKAMATSU.tga
[B] gfx/flags/small/JAP_AKKD.tga
[B] gfx/flags/small/JAP_ASANUMA.tga
[B] gfx/flags/small/JAP_Araki.tga
[B] gfx/flags/small/JAP_BLACK_DRAGON.tga
[B] gfx/flags/small/JAP_BURAKU_LEAGUE.tga
[B] gfx/flags/small/JAP_COF_puppet.tga
[B] gfx/flags/small/JAP_FUKUMOTO.tga
[B] gfx/flags/small/JAP_HASHIMOTO_ASIA.tga
[B] gfx/flags/small/JAP_HASHIMOTO_WORLD.tga
[B] gfx/flags/small/JAP_HIRANO.tga
[B] gfx/flags/small/JAP_HISASHI.tga
[B] gfx/flags/small/JAP_HISASHI_Reformed.tga
[B] gfx/flags/small/JAP_Hakko_Ichui.tga
[B] gfx/flags/small/JAP_IKKI_KITA_WORLD.tga
[B] gfx/flags/small/JAP_INT_puppet.tga
[B] gfx/flags/small/JAP_JUDA.tga
[B] gfx/flags/small/JAP_JUDA_EX.tga
[B] gfx/flags/small/JAP_KANSON.tga
[B] gfx/flags/small/JAP_KENJI.tga
[B] gfx/flags/small/JAP_KENZO.tga
[B] gfx/flags/small/JAP_KIKUE.tga
[B] gfx/flags/small/JAP_KINGORO_FX.tga
[B] gfx/flags/small/JAP_KITA.tga
[B] gfx/flags/small/JAP_KITA_ASIA.tga
[B] gfx/flags/small/JAP_KOREA_MONGOLIA_JAPAN.tga
[B] gfx/flags/small/JAP_KOZABURO.tga
[B] gfx/flags/small/JAP_KOZABURO_totalist.tga
[B] gfx/flags/small/JAP_Kingoro.tga
[B] gfx/flags/small/JAP_Kodoha.tga
[B] gfx/flags/small/JAP_MANCHURIA_UNION.tga
[B] gfx/flags/small/JAP_MATSUMOTO.tga
[B] gfx/flags/small/JAP_MATSUMOTO_FX.tga
[B] gfx/flags/small/JAP_MONGOL_EMPIRE.tga
[B] gfx/flags/small/JAP_NAKANO_1984.tga
[B] gfx/flags/small/JAP_NICHIREN.tga
[B] gfx/flags/small/JAP_NICHIREN_SHOGUN.tga
[B] gfx/flags/small/JAP_NICHIREN_SHOGUN_1.tga
[C | 含 Socialist 字样] gfx/flags/small/JAP_NICHIREN_radical_socialist.tga
[B] gfx/flags/small/JAP_NICHIREN_social_democrat.tga
[B] gfx/flags/small/JAP_NICHIREN_totalist.tga
[B] gfx/flags/small/JAP_NOSAKA.tga
[B] gfx/flags/small/JAP_NOSAKA_FX.tga
[B] gfx/flags/small/JAP_OOMOTO.tga
[B] gfx/flags/small/JAP_OOMOTO_WORLD.tga
[B] gfx/flags/small/JAP_PANTHERA_1.tga
[B] gfx/flags/small/JAP_PANTHERA_2.tga
[C | 含 Socialist 字样] gfx/flags/small/JAP_RED_radical_socialist.tga
[B] gfx/flags/small/JAP_RED_syndicalist.tga
[B] gfx/flags/small/JAP_RED_totalist.tga
[B] gfx/flags/small/JAP_ROERICH.tga
[B] gfx/flags/small/JAP_ROERICH_PAN_ASIA.tga
[B] gfx/flags/small/JAP_ROERICH_WORLD.tga
[B] gfx/flags/small/JAP_Republican_Fem.tga
[B] gfx/flags/small/JAP_SANSHIRO.tga
[B] gfx/flags/small/JAP_SANZO_MONBOL.tga
[B] gfx/flags/small/JAP_SCHIZO.tga
[B] gfx/flags/small/JAP_SHUMEI.tga
[B] gfx/flags/small/JAP_SHUMEI_ASIA.tga
[B] gfx/flags/small/JAP_SHUMEI_MUSLIM.tga
[B] gfx/flags/small/JAP_SINO_JAPAN.tga
[B] gfx/flags/small/JAP_SOKA_GAKKAI_WORLD.tga
[B] gfx/flags/small/JAP_Shinshu.tga
[B] gfx/flags/small/JAP_Soka_Gakkai.tga
[B] gfx/flags/small/JAP_Suiheisha_temp.tga
[B] gfx/flags/small/JAP_TOHOKAI_TWO.tga
[B] gfx/flags/small/JAP_TOKOHAI.tga
[B] gfx/flags/small/JAP_TOKUDA.tga
[B] gfx/flags/small/JAP_TURANIA.tga
[B] gfx/flags/small/JAP_TWI.tga
[B] gfx/flags/small/JAP_Tachi_Asia.tga
[B] gfx/flags/small/JAP_ULTRA_SCHIZO.tga
[B] gfx/flags/small/JAP_YAKUZA_national_populist.tga
[B] gfx/flags/small/JAP_YAKUZA_paternal_autocrat.tga
[B] gfx/flags/small/JAP_YAMAKAWA.tga
[B] gfx/flags/small/JAP_YAMANA.tga
[B] gfx/flags/small/JAP_ZAIBATSU.tga
[B] gfx/flags/small/JAP_diedie.tga
[B] gfx/flags/small/JAP_iww_asia.tga
[B] gfx/flags/small/JAP_military.tga
[B] gfx/flags/small/JAP_national_populist.tga
[B] gfx/flags/small/JAP_nichiren_redux.tga
[B] gfx/flags/small/JAP_nouhonsyugi.tga
[B] gfx/flags/small/JAP_paternal_autocrat.tga
[C | 含 Socialist 字样] gfx/flags/small/JAP_radical_socialist.tga
[B] gfx/flags/small/JAP_red_army.tga
[B] gfx/flags/small/JAP_red_empire_txt_vanguardist.tga
[B] gfx/flags/small/JAP_republican.tga
[B] gfx/flags/small/JAP_rounou.tga
[B] gfx/flags/small/JAP_ryujinkai.tga
[B] gfx/flags/small/JAP_shogunate.tga
[B] gfx/flags/small/JAP_shogunate_authoritarian_democrat.tga
[B] gfx/flags/small/JAP_shogunate_kuniyuki_paternal_autocrat.tga
[B] gfx/flags/small/JAP_shogunate_paternal_autocrat.tga
[C | 含 Socialist 字样] gfx/flags/small/JAP_socialist_league.tga
[B] gfx/flags/small/JAP_state_totalist.tga
[B] gfx/flags/small/JAP_syndicalist.tga
[B] gfx/flags/small/JAP_tohokai.tga
[B] gfx/flags/small/JAP_totalist.tga
[B] gfx/flags/small/JAP_valkist.tga
[B] gfx/flags/small/KOG_POR_formosa.tga
[B] gfx/flags/small/KOG_POR_korea.tga
[B] gfx/flags/small/KOR_JAP.tga
[B] gfx/flags/small/KOR_JUCHEJOE_national_populist.tga
[B] gfx/flags/small/KOR_JUCHEJOE_totalist.tga
[B] gfx/interface/advisors/CHI/CHI_Quo_Tai_chi.png
[B] gfx/interface/advisors/CHI/CHI_Tai_Chi_tao.png
[B] gfx/interface/decisions/GFX_decision_cat_JAP_Sakurakai_Plot_Picture.dds
[B] gfx/interface/decisions/JAP_Rework/GFX_decision_JAP_congress_icon.png
[B] gfx/interface/decisions/JAP_Rework/bribe_nakaon_icon.png
[B] gfx/interface/decisions/JAP_Rework/no_nakano_icon.png
[B] gfx/interface/decisions/JAP_Rework/no_tokohai_icon.png
[B] gfx/interface/decisions/decision_cat_generic_majapahit_empire.dds
[B] gfx/interface/decisions/decision_cat_jap_attack_china.dds
[B] gfx/interface/decisions/decision_cat_jap_domestic_policy.dds
[B] gfx/interface/decisions/decision_cat_jap_foreign_policy.dds
[B] gfx/interface/decisions/decision_cat_jap_integrate_colonies.dds
[B] gfx/interface/decisions/decision_cat_jap_military_research.dds
[B] gfx/interface/decisions/decision_cat_jap_sadao_coup.dds
[B] gfx/interface/decisions/decision_cat_jap_sasebo_conventions.dds
[B] gfx/interface/decisions/decision_category_jap_intervene_in_china.dds
[B] gfx/interface/decisions/decision_category_jap_pacific_guardian.dds
[B] gfx/interface/decisions/decision_category_jap_southern_expansion.dds
[B] gfx/interface/decisions/decision_jap_conquer_china.dds
[B] gfx/interface/decisions/decision_jap_pacific_guardian.dds
[B] gfx/interface/goals/ARZ_Arizona_and_Japan.png
[B] gfx/interface/goals/BLR/BLR_finland_to_japan.tga
[B] gfx/interface/goals/CAL/CAL_Connect_Jap.png
[B] gfx/interface/goals/CAL/CAL_Follow_pro_Japanese_groups.png
[B] gfx/interface/goals/CAL/CAL_Invite_Japanese_enterprises.png
[B] gfx/interface/goals/CAL/CAL_Japan_is_watching_u.png
[B] gfx/interface/goals/CAL/CAL_another_Tokyo.png
[B] gfx/interface/goals/CAL/CAL_fuck_u_jap.png
[B] gfx/interface/goals/CAL/CAL_shadow_samurai.png
[B] gfx/interface/goals/CAL/destroy_japan.dds
[B] gfx/interface/goals/CHL_JAP.png
[B] gfx/interface/goals/End_to_Japanese_collaborators.png
[B] gfx/interface/goals/GEA_Incite_Japanese_colonies.png
[B] gfx/interface/goals/GFX_AJPSEIYUKAITWO_a_new_era_for_japanese_social_conservatism-248360.dds
[B] gfx/interface/goals/GFX_AJPSEIYUKAITWO_reach_out_to_the_japanese_middle_class-248360.dds
[B] gfx/interface/goals/GFX_CAMJAP_build_up_phnom_penn_university-248360.dds
[B] gfx/interface/goals/GFX_CAMJAP_cambodiasnewfreedom-248360.dds
[B] gfx/interface/goals/GFX_CAMJAP_control_the_assembly-248360.dds
[B] gfx/interface/goals/GFX_CAMJAP_crackdown_on_unionism-248360.dds
[B] gfx/interface/goals/GFX_CAMJAP_economysaved-248360.dds
[B] gfx/interface/goals/GFX_CAMJAP_embrace_the_lunar_calendar-248360.dds
[B] gfx/interface/goals/GFX_CAMJAP_encourage_joint_enterprise-248360.dds
[B] gfx/interface/goals/GFX_CAMJAP_faithful_allies-248360.dds
[B] gfx/interface/goals/GFX_CAMJAP_integratesonsannsliberals-248360.dds
[B] gfx/interface/goals/GFX_CAMJAP_invite_zaibatsu_investment-248360.dds
[B] gfx/interface/goals/GFX_CAMJAP_military_industrialism-248360.dds
[B] gfx/interface/goals/GFX_CAMJAP_pro_japanese_rule-248360.dds
[B] gfx/interface/goals/GFX_CAMJAP_purge_the_country-248360.dds
[B] gfx/interface/goals/GFX_CAMJAP_question_sihanouk-248360.dds
[B] gfx/interface/goals/GFX_CAMJAP_reach_out_to_the_buddhists-248360.dds
[B] gfx/interface/goals/GFX_CAMJAP_stop_the_rural_disruption-248360.dds
[B] gfx/interface/goals/GFX_CAMJAP_undodemocratization-248360.dds
[B] gfx/interface/goals/GFX_CHINA_FOREIGN_POLICY_extending_the_5_tibetan_fingers-248360.dds
[B] gfx/interface/goals/GFX_GXC_break_the_back_of_japan-248360.dds
[B] gfx/interface/goals/GFX_GXC_taixusrevisedmoralism-248360.dds
[B] gfx/interface/goals/GFX_GXC_union_with_japanese_and_korean_anarchists-248360.dds
[B] gfx/interface/goals/GFX_JAPAKAO_a_new_contender_enters_the_ring-248360.dds
[C | 含 Socialist 字样] gfx/interface/goals/GFX_JAPAKAO_akaosutopiansocialiststate-248360.dds
[B] gfx/interface/goals/GFX_JAPAKAO_alliance_with_nakano-248360.dds
[B] gfx/interface/goals/GFX_JAPAKAO_bringing_forth_the_strength_of_the_empire-248360.dds
[B] gfx/interface/goals/GFX_JAPAKAO_bullets_to_the_heads_of_the_reds-248360.dds
[B] gfx/interface/goals/GFX_JAPAKAO_celebrating_the_emperor_jimmu-248360.dds
[B] gfx/interface/goals/GFX_JAPAKAO_creation_of_the_founding_festival-248360.dds
[B] gfx/interface/goals/GFX_JAPAKAO_embracing_socialism-248360.dds
[B] gfx/interface/goals/GFX_JAPAKAO_ending_the_liberal_degeneracy-248360.dds
[B] gfx/interface/goals/GFX_JAPAKAO_forming_the_national_foundation_society-248360.dds
[B] gfx/interface/goals/GFX_JAPAKAO_legacy_of_the_new_village_movement-248360.dds
[B] gfx/interface/goals/GFX_JAPAKAO_nationalsocialism_under_the_japanese_banner-248360.dds
[B] gfx/interface/goals/GFX_JAPAKAO_promotingemperorbasedsocialism-248360.dds
[B] gfx/interface/goals/GFX_JAPAKAO_roots_with_the_yakuza-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_a_liberated_lifestyle-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_a_loyal_figure-248360.dds
[C | 含 Socialist 字样] gfx/interface/goals/GFX_JAPANA_align_with_christian_socialists-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_anarchosyndicalist_programme-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_burnthecrown-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_capitalshallcrumble-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_construct_proletarian_councils-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_court_the_jcp-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_crush_the_foreign_reactionaries-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_dadaism_realized-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_denounce_the_crown_of_evil-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_denounce_the_monks-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_embrace_the_monks-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_expression_through_living-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_form_the_eight_days_committee-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_forming_workers_cooperatives-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_formthetsujijunkoenkai-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_from_our_declaration-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_iamthetengu-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_idolize_the_cooperative_movement-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_in_the_embrace_of_pure_anarchism-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_integrate_the_imperial_unions-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_japanshallbefree-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_legacy_of_imperial_anarchism-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_mutualist_economic_program-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_our_korean_comrades-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_promotingcommunalagrarianism-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_promotingthelocallife-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_purge_the_nobility-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_radicalize_the_art_circles-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_reconciliation_movement-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_reforming_the_zenkoku_jiren-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_removing_the_oppressive_classes-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_renounce_feudalism-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_revolution_against_the_old-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_revolution_for_the_young-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_revolutionary_expansion-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_rule_of_the_council-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_sanshirosanarchismleadsthenation-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_smash_the_zaibatsu-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_syncretic_anarchist_ethos-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_taking_revenge_on_the_yakuza-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_the_anarchist_shogunate-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_the_fight_against_discrimination-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_the_literary_revolution-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_the_old_guard_of_japanese_socialism-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_the_path_of_liberation-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_the_towers_surpass_the_clouds_again-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_true_anarchism_rises-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_understanding_the_peasantry-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_unite_the_zenkoku_and_kyushu_organizations-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_uniting_the_japanese_anarchist_movement-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_upholding_the_showa-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_whatsgoingoninthepsychward-248360.dds
[C | 含 Socialist 字样] gfx/interface/goals/GFX_JAPANA_work_with_the_national_socialists-248360.dds
[B] gfx/interface/goals/GFX_JAPANA_writing_the_true_anarchist_manifesto-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_a_promise_to_the_peasant_soldiers-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_a_revolutionary_shogunate-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_araki_at_the_helm-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_arakissuccess-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_arrest_the_syndicalist_traitors-248360.dds
[C | 含 Socialist 字样] gfx/interface/goals/GFX_JAPARAKI_attack_the_socialist_resistance-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_connectingtheemperorthelandandthepeople-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_continued_the_zaibatsu_nationalisation-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_crush_aristocratic_corruption-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_crush_ugaki_thought-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_declaring_the_3_leaps-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_economic_moblization-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_expand_military_influence-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_extending_the_fist_of_military_might-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_finish_off_the_moderate_factions-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_hashimotosdeclaration-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_isolated_economic_miracle-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_kemalist_leanings-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_kokutai_no_hongi-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_militaristic_social_justice-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_national_mobilization-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_national_spiritual_mobilisation-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_nationalist_propagation-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_on_the_hill_of_hashimoto_thought-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_organize_rural_cooperatives-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_preparing_for_total_war-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_proclaim_a_new_shogunate-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_rally_the_tonarigumi-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_reinforce_security_of_the_state-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_revive_the_kokutai-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_seizing_aristocratic_lands-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_serving_for_the_emperor-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_shinmin_no_michi-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_spiritual_training-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_the_autarky_economic_solution-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_the_bamboo_spear_slay_our_enemies-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_the_cherry_blossoms_bloom-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_the_cherry_blossoms_bring_joy_to_the_empire-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_the_economy_leaps_to_greatness-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_the_military_leap-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_the_nation_awaits_the_era_of_prosperity-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_the_spiritual_leap-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_theemperortheeconomy-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_two_opposing_cross_roads-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_uphold_panasianism-248360.dds
[B] gfx/interface/goals/GFX_JAPARAKI_upholdingkitaspanasianism-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_a_great_naval_power-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_a_magnificent_army-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_abandoning_dissarmament-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_air_land_supremacy-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_army_elitism-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_armynavy_harmony-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_battleship_mega_projects-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_carrier_investment-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_conscript_the_noncitizens-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_conscription_reforms-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_continue_strengthening_military_industry-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_crystallization_of_japanese_technology-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_defence_of_the_home_islands-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_defenders_of_the_sky-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_efficient_munitions_manufacturing-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_elaboration_on_the_army-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_expand_the_kure_naval_arsenal-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_formal_end_to_disarmament-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_from_old_to_new-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_hell_from_above-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_high_performance_firearms-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_hismajestyspower-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_improving_naval_performance-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_increase_the_armynavy_budgets-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_increased_warship_administration_costs-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_increasing_naval_landing_forces-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_increasing_the_worker_numbers-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_increasing_weapons_production-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_jakuniku_kyoshoku-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_kempeitai_training-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_learning_from_the_weltkrieg-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_lessons_from_the_ministry_of_munitions-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_mass_assault_tanks-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_military_education_improvements-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_military_school_expansions-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_military_unity-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_mobilize_the_reserves-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_modernisation_of_the_shipyards-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_new_military_industry-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_new_organization_targets-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_production_rescaling-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_psychological_warfare-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_reform_the_disarmament_policy-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_sailing_across_the_pacific-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_snakes_under_the_waves-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_state_the_mechanization_programme-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_strengthen_the_armyair_corps-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_stronger_and_more_advanced-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_supremacy_of_the_mind-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_supremacy_of_will-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_teishin_shudan-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_the_army_and_the_people-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_the_army_direction-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_the_human_wave-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_the_naval_approach-248360.dds
[B] gfx/interface/goals/GFX_JAPARMY_victorythroughcombinedarms-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_a_general_strike_for_the_proletarian-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_a_japanese_cultural_revolution-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_a_japanese_renaissance-248360.dds
[C | 含 Socialist 字样] gfx/interface/goals/GFX_JAPCOMMUNIST_a_new_form_of_socialist_unity-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_a_revolution_under_party_control-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_a_revolutionary_research_cult-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_a_struggle_against_socialreactionarism-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_a_struggle_against_spies-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_agitative_propaganda-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_akahata_no_uta-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_antiimperialist_rationalization-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_appealing_for_3rd_internationale_support-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_birth_of_the_proletarian_youth_league-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_changingthecourseofjapansproletariat-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_cherry_blossoms_died_red-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_control_the_political_line-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_crush_yamakawa-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_dealing_with_the_emperor-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_defendingthepeoplesinterests-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_denounce_fukumotoism-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_denounce_the_liberal_menace-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_denounce_the_syndicalist_revisionists-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_denounce_the_yamakawaists-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_embracing_smiling_communism-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_emphasis_on_theory-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_enforce_democratic_centralism-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_focus_on_self_reliance-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_foreverapartyforeverarevolution-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_form_the_investigation_committee-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_formation_of_a_grass_roots_faction-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_formthekantowomensleague-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_found_the_national_pioneer_association-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_founding_of_the_industrial_labour_institute-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_glory_under_the_vanguard_party-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_honour_the_martyrs_of_the_revolution-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_increase_the_peasant_livelihood-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_injecting_the_marxist_conscious-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_international_contacts-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_invigorate_the_three_stage_program-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_japanslenin-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_kenzossyndicalistdream-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_legacy_of_japanese_syndicalism-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_legacy_of_the_action_group-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_legacy_of_the_farm_labour_party-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_legacy_of_the_new_men_society-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_longing_for_armed_struggle-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_marching_for_the_true_proletariat-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_militant_syndicalists_take_over_the_party-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_mobilise_the_masses-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_outsidethenationsborders-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_paris_syndicalists_secure_the_party-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_peasant_collaboration-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_proletarian_papers-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_promote_the_student_labour_society-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_promoting_a_true_party_of_the_masses-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_promoting_a_writers_revolution-248360.dds
[C | 含 Socialist 字样] gfx/interface/goals/GFX_JAPCOMMUNIST_promoting_socialist_feminism-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_promoting_the_social_revolution-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_promotion_of_revolutionary_marxism-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_proper_party_reconstruction-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_purge_the_antiproletarian_factions-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_question_of_the_emperor-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_question_of_the_royal_family-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_question_of_the_socialreactionaries-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_reach_out_to_the_masses-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_reach_out_to_the_workers-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_realisation_of_2_staged_revolution-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_red_intellectuals-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_remove_the_stain_of_feudalism-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_representing_all_the_workers_unions-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_revive_akahata-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_revive_the_labourliberty_society-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_revolutionary_bureaucracy-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_revolutionary_intellectualism-248360.dds
[C | 含 Socialist 字样] gfx/interface/goals/GFX_JAPCOMMUNIST_scientific_socialist_outlook-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_securing_the_state-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_socialism_in_one_country-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_strengthen_old_guard_influence-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_strengthening_the_ideological_united_front-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_struggle_of_the_literary_left-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_support_okinawan_independence-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_the_joint_rural_struggle-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_the_red_banner_over_tokyo-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_the_rising_sun_under_the_hammer_and_sickle-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_the_struggle_of_2-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_therevolutionsnewhome-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_true_japanese_communism-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_unification_of_the_trade_unions-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_universal_suffrage-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_upholding_true_leninism-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_victory_of_the_communist_hardliners-248360.dds
[B] gfx/interface/goals/GFX_JAPCOMMUNIST_yamakawasrevolution-248360.dds
[B] gfx/interface/goals/GFX_JAPDOMEITWO_a_call_for_a_national_unity_government-248360.dds
[B] gfx/interface/goals/GFX_JAPDOMEITWO_a_new_round_for_the_kokumin_domei-248360.dds
[B] gfx/interface/goals/GFX_JAPDOMEITWO_advocate_for_mild_authoritarianism-248360.dds
[B] gfx/interface/goals/GFX_JAPDOMEITWO_coalition_with_the_seiyukai-248360.dds
[B] gfx/interface/goals/GFX_JAPDOMEITWO_dissolve_the_diet-248360.dds
[B] gfx/interface/goals/GFX_JAPDOMEITWO_embracingthepartysleftwing-248360.dds
[B] gfx/interface/goals/GFX_JAPDOMEITWO_formation_of_a_new_government-248360.dds
[B] gfx/interface/goals/GFX_JAPDOMEITWO_further_promote_dirigisme_ideas-248360.dds
[B] gfx/interface/goals/GFX_JAPDOMEITWO_kenzo_holding_the_party_helm-248360.dds
[C | 含 Socialist 字样] gfx/interface/goals/GFX_JAPDOMEITWO_promote_national_socialist_theory-248360.dds
[C | 含 Socialist 字样] gfx/interface/goals/GFX_JAPDOMEITWO_socialist_friends-248360.dds
[B] gfx/interface/goals/GFX_JAPDOMEITWO_strengthen_the_peace_preservation_laws-248360.dds
[B] gfx/interface/goals/GFX_JAPDOMEITWO_support_the_trade_unions-248360.dds
[B] gfx/interface/goals/GFX_JAPDOMEITWO_village_relief_petition_movement-248360.dds
[B] gfx/interface/goals/GFX_JAPECON_astarttoforfullrecovery-248360.dds
[B] gfx/interface/goals/GFX_JAPECON_compensate_the_landlords-248360.dds
[B] gfx/interface/goals/GFX_JAPECON_extend_loans_for_the_bank_of_taiwan-248360.dds
[B] gfx/interface/goals/GFX_JAPECON_focus_on_japan-248360.dds
[B] gfx/interface/goals/GFX_JAPECON_further_korean_investments-248360.dds
[B] gfx/interface/goals/GFX_JAPECON_partial_zaibatsu_nationalization-248360.dds
[B] gfx/interface/goals/GFX_JAPECON_propup_further_manchurian_economic_expansion-248360.dds
[B] gfx/interface/goals/GFX_JAPECON_reaffirm_a_focus_on_the_zaibatsu-248360.dds
[B] gfx/interface/goals/GFX_JAPECON_recovering_from_black_monday-248360.dds
[B] gfx/interface/goals/GFX_JAPECON_save_the_colonies-248360.dds
[B] gfx/interface/goals/GFX_JAPECON_statist_recovery-248360.dds
[B] gfx/interface/goals/GFX_JAPECON_subsidise_the_peasants-248360.dds
[B] gfx/interface/goals/GFX_JAPECON_the_3_week_holiday_for_the_bank-248360.dds
[B] gfx/interface/goals/GFX_JAPFOR_australasian_ventures-248360.dds
[B] gfx/interface/goals/GFX_JAPFOR_burn_to_ash-248360.dds
[B] gfx/interface/goals/GFX_JAPFOR_claim_the_german_east-248360.dds
[B] gfx/interface/goals/GFX_JAPFOR_deal_with_transamur-248360.dds
[B] gfx/interface/goals/GFX_JAPFOR_demand_obedience_over_manila-248360.dds
[B] gfx/interface/goals/GFX_JAPFOR_demand_tibetan_submission-248360.dds
[B] gfx/interface/goals/GFX_JAPFOR_destabilize_the_dragon-248360.dds
[B] gfx/interface/goals/GFX_JAPFOR_focus_on_our_allies-248360.dds
[B] gfx/interface/goals/GFX_JAPFOR_fruits_of_loyalty-248360.dds
[B] gfx/interface/goals/GFX_JAPFOR_japansplaceintheworld-248360.dds
[B] gfx/interface/goals/GFX_JAPFOR_loyal_collaborators-248360.dds
[B] gfx/interface/goals/GFX_JAPFOR_mission_to_the_subcontinent-248360.dds
[B] gfx/interface/goals/GFX_JAPFOR_nanshinron-248360.dds
[B] gfx/interface/goals/GFX_JAPFOR_national_mobilization_law-248360.dds
[B] gfx/interface/goals/GFX_JAPFOR_operation_ichiguo-248360.dds
[B] gfx/interface/goals/GFX_JAPFOR_overtures_to_persia_and_the_afghans-248360.dds
[B] gfx/interface/goals/GFX_JAPFOR_planting_sakura_trees-248360.dds
[B] gfx/interface/goals/GFX_JAPFOR_reach_out_to_the_steppe-248360.dds
[B] gfx/interface/goals/GFX_JAPFOR_saving_the_south_from_imperialism-248360.dds
[B] gfx/interface/goals/GFX_JAPFOR_seishinron-248360.dds
[B] gfx/interface/goals/GFX_JAPFOR_support_surkano-248360.dds
[B] gfx/interface/goals/GFX_JAPFOR_the_hawaiian_push-248360.dds
[B] gfx/interface/goals/GFX_JAPFOR_victoryovereuropeanimperialism-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_a_more_hands_off_approach-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_corporatist_economic_hold-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_crackdowns_on_the_army-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_create_the_tokko-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_crush_liberal_remnants-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_cultivate_military_support-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_dealing_with_the_red_menace-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_economic_freedom-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_expand_military_privileges-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_fighting_against_foreign_ideals-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_finish_off_toseiha_elements-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_form_the_national_muslim_association-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_goingoncegoingtwice-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_hand_out_construction_contracts-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_hayashisvictory-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_hiranumasshogunate-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_implement_land_reforms-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_incentivise_new_business-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_investigate_konoe-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_kiichirosvictory-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_kuharasnationaldominance-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_manoeuvre_against_hayashi-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_militarist_victory-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_new_ventures-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_partial_zaibatsu_nationalization-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_preferential_treatment_for_big_businesses-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_privatisation_of_the_public_sector-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_proclaim_toseiha_dominance-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_purge_the_iraa_leftists-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_purging_the_syndicalists-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_quietly_roll_back_labour_regulations-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_realpolitik-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_rightists_dominate_the_conference-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_side_line_the_agitators-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_sneak_in_toseiha_influence-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_stick_with_the_status_quo-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_subsidies_for_small_business-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_the_invisible_hand_of_the_free_market-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_the_japanese_economic_miracle-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_the_market_faction_takes_control-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_the_national_conscription_order-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_tora_tora_tora-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAARIGHTIST_work_against_hashimoto-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAA_closing_of_the_congress-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAA_formation_of_the_imperial_rule_assistance_association-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAA_merging_parties_and_think_tanks-248360.dds
[B] gfx/interface/goals/GFX_JAPIRAA_question_of_the_zaibatsu_industries-248360.dds
[B] gfx/interface/goals/GFX_JAPKOKUMIN_continue_dirigisme_outlook-248360.dds
[B] gfx/interface/goals/GFX_JAPKOKUMIN_control_the_unions-248360.dds
[B] gfx/interface/goals/GFX_JAPKOKUMIN_controlling_the_diet-248360.dds
[C | 含 Socialist 字样] gfx/interface/goals/GFX_JAPKOKUMIN_crush_the_socialist_terrorists-248360.dds
[B] gfx/interface/goals/GFX_JAPKOKUMIN_dealing_with_the_tokohai_split-248360.dds
[B] gfx/interface/goals/GFX_JAPKOKUMIN_denounce_european_imperialism-248360.dds
[B] gfx/interface/goals/GFX_JAPKOKUMIN_distance_ourselves_from_nakano-248360.dds
[B] gfx/interface/goals/GFX_JAPKOKUMIN_japanesemanchurian_union-248360.dds
[B] gfx/interface/goals/GFX_JAPKOKUMIN_kokumin_domei_at_the_helm-248360.dds
[B] gfx/interface/goals/GFX_JAPKOKUMIN_maintaining_the_controlled_economy-248360.dds
[B] gfx/interface/goals/GFX_JAPKOKUMIN_manage_the_foreign_exchange-248360.dds
[B] gfx/interface/goals/GFX_JAPKOKUMIN_promote_panasian_unity-248360.dds
[B] gfx/interface/goals/GFX_JAPKOKUMIN_protection_against_major_monopolies-248360.dds
[B] gfx/interface/goals/GFX_JAPKOKUMIN_reaction_against_the_germanic_centric_peace-248360.dds
[B] gfx/interface/goals/GFX_JAPKOKUMIN_retain_low_interest_rates-248360.dds
[B] gfx/interface/goals/GFX_JAPKOKUMIN_the_cooperative_cabinet_movement-248360.dds
[B] gfx/interface/goals/GFX_JAPKOKUMIN_the_east_asia_monroe_doctrine-248360.dds
[B] gfx/interface/goals/GFX_JAPKOKUMIN_total_kokumin_domei_supremacy-248360.dds
[B] gfx/interface/goals/GFX_JAPKONOE_a_budget_for_war-248360.dds
[B] gfx/interface/goals/GFX_JAPKONOE_a_promise_to_the_rural_soldiers-248360.dds
[B] gfx/interface/goals/GFX_JAPKONOE_absorb_the_trade_unions-248360.dds
[B] gfx/interface/goals/GFX_JAPKONOE_control_the_sanpo-248360.dds
[B] gfx/interface/goals/GFX_JAPKONOE_dontmissthebus-248360.dds
[B] gfx/interface/goals/GFX_JAPKONOE_establish_asianist_organizations-248360.dds
[B] gfx/interface/goals/GFX_JAPKONOE_establish_the_national_railways_service-248360.dds
[B] gfx/interface/goals/GFX_JAPKONOE_expand_the_neighbourhood_associations-248360.dds
[B] gfx/interface/goals/GFX_JAPKONOE_form_the_gjwa-248360.dds
[B] gfx/interface/goals/GFX_JAPKONOE_form_the_greater_japan_religious_information_association-248360.dds
[B] gfx/interface/goals/GFX_JAPKONOE_form_the_national_literature_association-248360.dds
[B] gfx/interface/goals/GFX_JAPKONOE_form_the_national_volunteer_corps-248360.dds
[B] gfx/interface/goals/GFX_JAPKONOE_he_bends_to_the_left-248360.dds
[B] gfx/interface/goals/GFX_JAPKONOE_he_bends_to_the_right-248360.dds
[B] gfx/interface/goals/GFX_JAPKONOE_konoe_controls_the_center-248360.dds
[B] gfx/interface/goals/GFX_JAPKONOE_national_land_reforms-248360.dds
[B] gfx/interface/goals/GFX_JAPKONOE_no_longer_the_weak_premier-248360.dds
[B] gfx/interface/goals/GFX_JAPKONOE_preparing_for_total_war-248360.dds
[B] gfx/interface/goals/GFX_JAPKONOE_promote_nochikaiho-248360.dds
[B] gfx/interface/goals/GFX_JAPKONOE_spiritual_mobilization_plan-248360.dds
[B] gfx/interface/goals/GFX_JAPKONOE_strengthen_the_bia-248360.dds
[B] gfx/interface/goals/GFX_JAPKONOE_strike_against_the_zaibatsu_monsters-248360.dds
[B] gfx/interface/goals/GFX_JAPKONOE_support_the_youth_associations-248360.dds
[B] gfx/interface/goals/GFX_JAPKONOE_the_important_industry_control_act-248360.dds
[B] gfx/interface/goals/GFX_JAPKONOE_total_nationalization-248360.dds
[B] gfx/interface/goals/GFX_JAPKONOE_unify_the_trade_unions-248360.dds
[B] gfx/interface/goals/GFX_JAPKONOE_work_with_the_sanpo-248360.dds
[B] gfx/interface/goals/GFX_JAPKOZA_cleansing_of_national_politics-248360.dds
[B] gfx/interface/goals/GFX_JAPKOZA_ending_the_monsters_of_globalization-248360.dds
[B] gfx/interface/goals/GFX_JAPKOZA_forming_the_imperial_brotherhood-248360.dds
[B] gfx/interface/goals/GFX_JAPKOZA_industrial_transformation-248360.dds
[B] gfx/interface/goals/GFX_JAPKOZA_learning_from_tolstoy-248360.dds
[B] gfx/interface/goals/GFX_JAPKOZA_local_village_reliance-248360.dds
[B] gfx/interface/goals/GFX_JAPKOZA_purge_the_old_order-248360.dds
[B] gfx/interface/goals/GFX_JAPKOZA_radical_land_reforms-248360.dds
[B] gfx/interface/goals/GFX_JAPKOZA_removal_of_the_zaibatsu-248360.dds
[B] gfx/interface/goals/GFX_JAPKOZA_strike_down_capitalism-248360.dds
[B] gfx/interface/goals/GFX_JAPKOZA_tachibanasascension-248360.dds
[B] gfx/interface/goals/GFX_JAPKOZA_tachibanasutopiansociety-248360.dds
[B] gfx/interface/goals/GFX_JAPKOZA_undertheemperorswill-248360.dds
[B] gfx/interface/goals/GFX_JAPKOZA_work_with_bin_akao-248360.dds
[B] gfx/interface/goals/GFX_JAPLEFTIRAA_asanumaspowergrab-248360.dds
[B] gfx/interface/goals/GFX_JAPLEFTIRAA_control_the_trade_unions-248360.dds
[B] gfx/interface/goals/GFX_JAPLEFTIRAA_embracing_totalitarianism-248360.dds
[B] gfx/interface/goals/GFX_JAPLEFTIRAA_embracingkitasstatesocialism-248360.dds
[B] gfx/interface/goals/GFX_JAPLEFTIRAA_hashimoto_victory-248360.dds
[B] gfx/interface/goals/GFX_JAPLEFTIRAA_leftists_dominate-248360.dds
[B] gfx/interface/goals/GFX_JAPLEFTIRAA_purge_adachi_kenzo-248360.dds
[B] gfx/interface/goals/GFX_JAPLEFTIRAA_reach_out_to_kazami-248360.dds
[B] gfx/interface/goals/GFX_JAPLEFTIRAA_reviewing_the_national_syndicalist_system-248360.dds
[B] gfx/interface/goals/GFX_JAPLEFTIRAA_root_out_the_zaibatsu-248360.dds
[B] gfx/interface/goals/GFX_JAPLEFTIRAA_smashtherightistfactions-248360.dds
[B] gfx/interface/goals/GFX_JAPLEFTIRAA_strengthen_the_youth_leagues-248360.dds
[B] gfx/interface/goals/GFX_JAPLEFTIRAA_the_new_shogunate_rises-248360.dds
[B] gfx/interface/goals/GFX_JAPLEFTIRAA_the_red_chrysanthemum_shines_brighter_than_the_rising_sun-248360.dds
[B] gfx/interface/goals/GFX_JAPLEFTIRAA_tokohai_succession-248360.dds
[B] gfx/interface/goals/GFX_JAPLEFTIRAA_work_with_matsumoto-248360.dds
[B] gfx/interface/goals/GFX_JAPLIB_bureaucratic_hold-248360.dds
[B] gfx/interface/goals/GFX_JAPLIB_chip_away_at_military_influence-248360.dds
[B] gfx/interface/goals/GFX_JAPLIB_coalition_with_the_social_democrats-248360.dds
[B] gfx/interface/goals/GFX_JAPLIB_crack_down_on_the_labour_unions-248360.dds
[B] gfx/interface/goals/GFX_JAPLIB_encourage_investment_in_manchuria-248360.dds
[B] gfx/interface/goals/GFX_JAPLIB_ending_interparty_rivals-248360.dds
[B] gfx/interface/goals/GFX_JAPLIB_expanding_free_education-248360.dds
[B] gfx/interface/goals/GFX_JAPLIB_fair_distribution-248360.dds
[B] gfx/interface/goals/GFX_JAPLIB_for_liberty_and_progress-248360.dds
[B] gfx/interface/goals/GFX_JAPLIB_grant_further_support_to_the_zaibatsu-248360.dds
[B] gfx/interface/goals/GFX_JAPLIB_increase_agricultural_policies-248360.dds
[B] gfx/interface/goals/GFX_JAPLIB_increase_japanese_immigration_to_korea-248360.dds
[B] gfx/interface/goals/GFX_JAPLIB_our_universal_goal-248360.dds
[B] gfx/interface/goals/GFX_JAPLIB_panasianist_outlook-248360.dds
[B] gfx/interface/goals/GFX_JAPLIB_parliament_centric_governance-248360.dds
[B] gfx/interface/goals/GFX_JAPLIB_populism_over_factionalism-248360.dds
[B] gfx/interface/goals/GFX_JAPLIB_promote_universal_sufferage-248360.dds
[B] gfx/interface/goals/GFX_JAPLIB_promoting_of_peace-248360.dds
[B] gfx/interface/goals/GFX_JAPLIB_promotion_of_land_reforms-248360.dds
[B] gfx/interface/goals/GFX_JAPLIB_racialequality-248360.dds
[B] gfx/interface/goals/GFX_JAPLIB_support_new_military_powers-248360.dds
[B] gfx/interface/goals/GFX_JAPLIB_tojnha_faction_dominance-248360.dds
[B] gfx/interface/goals/GFX_JAPLIB_victory_of_the_minseito-248360.dds
[B] gfx/interface/goals/GFX_JAPMILICIVIL_an_army_beloved_by_the_people-248360.dds
[B] gfx/interface/goals/GFX_JAPMILICIVIL_favour_the_industrialists-248360.dds
[B] gfx/interface/goals/GFX_JAPMILICIVIL_favour_the_peasant_soldiers-248360.dds
[B] gfx/interface/goals/GFX_JAPMILICIVIL_industrial_war_machine-248360.dds
[B] gfx/interface/goals/GFX_JAPMILICIVIL_loyalty_to_the_kokutai-248360.dds
[B] gfx/interface/goals/GFX_JAPMILICIVIL_secure_international_funding-248360.dds
[B] gfx/interface/goals/GFX_JAPMILICIVIL_uniting_against_the_syndicalist_beast-248360.dds
[B] gfx/interface/goals/GFX_JAPMILICIVIL_we_shall_march_on_for_the_emperor-248360.dds
[B] gfx/interface/goals/GFX_JAPMILICIVIL_welcome_back_the_former_colonial_officers-248360.dds
[B] gfx/interface/goals/GFX_JAPMILICIVIL_yamatogokoro-248360.dds
[B] gfx/interface/goals/GFX_JAPMINSEITOTWO_a_party_of_the_middle_class-248360.dds
[B] gfx/interface/goals/GFX_JAPMINSEITOTWO_a_true_democratic_empire-248360.dds
[B] gfx/interface/goals/GFX_JAPMINSEITOTWO_banning_the_social_masses_party-248360.dds
[B] gfx/interface/goals/GFX_JAPMINSEITOTWO_continue_to_work_with_the_social_masses_party-248360.dds
[B] gfx/interface/goals/GFX_JAPMINSEITOTWO_dismantle_the_unions-248360.dds
[B] gfx/interface/goals/GFX_JAPMINSEITOTWO_displaying_party_centric_politics-248360.dds
[B] gfx/interface/goals/GFX_JAPMINSEITOTWO_espouse_universal_suffrage-248360.dds
[B] gfx/interface/goals/GFX_JAPMINSEITOTWO_further_zaibatsu_reach_out-248360.dds
[B] gfx/interface/goals/GFX_JAPMINSEITOTWO_keeping_party_tradition-248360.dds
[B] gfx/interface/goals/GFX_JAPMINSEITOTWO_promote_new_education_opportunities-248360.dds
[B] gfx/interface/goals/GFX_JAPMINSEITOTWO_realization_of_a_new_democracy-248360.dds
[B] gfx/interface/goals/GFX_JAPMINSEITOTWO_repeal_the_nsa-248360.dds
[B] gfx/interface/goals/GFX_JAPMINSEITOTWO_support_small_business-248360.dds
[B] gfx/interface/goals/GFX_JAPMINSEITOTWO_the_minseito_victory-248360.dds
[B] gfx/interface/goals/GFX_JAPMINSEITOTWO_thriving_on_economic_production-248360.dds
[B] gfx/interface/goals/GFX_JAPNAK_a_plan_for_national_reconstruction-248360.dds
[B] gfx/interface/goals/GFX_JAPNAK_a_strong_armed_government-248360.dds
[B] gfx/interface/goals/GFX_JAPNAK_abolishing_the_cabinet_system-248360.dds
[B] gfx/interface/goals/GFX_JAPNAK_absorb_the_shakai_taishuto-248360.dds
[B] gfx/interface/goals/GFX_JAPNAK_build_up_the_mass_movement-248360.dds
[B] gfx/interface/goals/GFX_JAPNAK_controlling_the_zaibatsu-248360.dds
[B] gfx/interface/goals/GFX_JAPNAK_creation_of_the_board_of_national_affairs-248360.dds
[B] gfx/interface/goals/GFX_JAPNAK_deal_with_the_land_owners-248360.dds
[B] gfx/interface/goals/GFX_JAPNAK_fabian_economic_influences-248360.dds
[B] gfx/interface/goals/GFX_JAPNAK_farming_for_the_nation-248360.dds
[B] gfx/interface/goals/GFX_JAPNAK_formation_of_selfrule_cooperatives-248360.dds
[B] gfx/interface/goals/GFX_JAPNAK_guiding_the_national_economy-248360.dds
[B] gfx/interface/goals/GFX_JAPNAK_increase_peasant_wages-248360.dds
[B] gfx/interface/goals/GFX_JAPNAK_keeping_the_emperor_under_a_close_eye-248360.dds
[B] gfx/interface/goals/GFX_JAPNAK_legacy_of_satsuma-248360.dds
[B] gfx/interface/goals/GFX_JAPNAK_legacy_of_the_visit_to_europe-248360.dds
[B] gfx/interface/goals/GFX_JAPNAK_nakano_above_all-248360.dds
[B] gfx/interface/goals/GFX_JAPNAK_nakano_secures_the_diet-248360.dds
[B] gfx/interface/goals/GFX_JAPNAK_new_trade_policies-248360.dds
[B] gfx/interface/goals/GFX_JAPNAK_proposing_a_greater_asian_economic_bloc-248360.dds
[B] gfx/interface/goals/GFX_JAPNAK_purge_the_liberal_menace-248360.dds
[B] gfx/interface/goals/GFX_JAPNAK_question_of_the_labour_unions-248360.dds
[B] gfx/interface/goals/GFX_JAPNAK_realization_of_a_populist_government-248360.dds
[B] gfx/interface/goals/GFX_JAPNAK_reduce_the_tax_burden_on_farmers-248360.dds
[B] gfx/interface/goals/GFX_JAPNAK_strengthen_the_farmer_unions-248360.dds
[B] gfx/interface/goals/GFX_JAPNAK_support_the_panasianists-248360.dds
[B] gfx/interface/goals/GFX_JAPNAK_the_issue_of_party_factionalism-248360.dds
[B] gfx/interface/goals/GFX_JAPNAK_the_land_question-248360.dds
[B] gfx/interface/goals/GFX_JAPNAK_the_national_agriculture_reserve-248360.dds
[B] gfx/interface/goals/GFX_JAPNAK_the_new_labour_act-248360.dds
[B] gfx/interface/goals/GFX_JAPNAK_under_the_nakano_economic_program-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_birth_of_red_nichirenism-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_blood_shall_reign_for_the_buddha-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_economic_agrarianism-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_encourage_nichiren_shoshu-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_establish_righteous_temples-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_ethnic_harmony-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_expand_military_industry-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_ishiwarasreign-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_jobukkokudo-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_mount_fuji_rumbles-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_pistols_to_the_degenerates-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_promoting_a_panbuddhist_federation-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_reach_out_to_the_buddhist_world-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_rebuild_the_fuji_school-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_redistributethezaibatsuscorps-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_reenvision_the_heian_period-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_relaying_the_gohonzon-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_removethezaibatsumonsters-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_save_the_peasants-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_sekai_sai_shu_senron-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_shinkobukkyo-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_slaughter_the_devils_of_greed-248360.dds
[C | 含 Socialist 字样] gfx/interface/goals/GFX_JAPNICH_stab_the_socialist_snakes-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_syncretic_economics-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_the_crimson_kingdom-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_the_emperor_all_mighty-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_the_eternal_shogun-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_the_hand_of_the_nation_guides_us_forwards-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_the_league_of_blood_incident-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_the_lotus_sutra_shall_blum-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_the_new_shogun-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_toarenmeiundo-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_translate_marx_for_the_masses-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_we_are_called_by_the_sun-248360.dds
[B] gfx/interface/goals/GFX_JAPNICH_zen_imperialism-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_a_battle_between_east_and_west-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_a_front_for_radical_reforms-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_areyouready-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_birth_of_the_east_asia_economic_research_bureau-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_breaking_the_marx_spectre-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_economic_socialism-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_embrace_the_nichirenists-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_found_the_spiritual_research_committee-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_future_of_the_shumei_government-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_havetheinsanetakenpower-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_imperialism_used_for_socialism-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_implement_universal_suffrage-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_initiate_land_reforms-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_internal_democracy-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_merely_an_imperial_organ-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_national_mobilization_law-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_nationalist_alignment-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_nationalsocialism_for_japan-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_our_divine_ruling_in_the_world-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_panasian_economic_affairs-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_panasianist_takeover-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_pronouncing_the_new_kokutairon-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_pure_socialism_has_arrived-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_purge_the_liberals-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_purging_the_nation_of_the_impure-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_question_meiji-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_social_threefolding_policies-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_socialdemocracyrenewedforjapan-248360.dds
[C | 含 Socialist 字样] gfx/interface/goals/GFX_JAPPAN_socialistevolution-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_start_the_panasia_project-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_support_the_red_emperor-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_support_the_student_unions-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_the_drums_of_war_sound-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_the_showa_rises_for_national_salvation-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_the_true_kokutai-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_the_way_of_socialism-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_the_zaibatsu_beast_crashes_to_the_ground-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_totalwarfullspeedahead-248360.dds
[B] gfx/interface/goals/GFX_JAPPAN_whyshouldweextremistsbeenemies-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_a_new_red_fleet-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_a_true_army_of_socialism-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_bicycle_brigades-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_birth_of_the_red_army-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_bring_out_the_armoured_beasts-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_centralize_army_discipline-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_centralized_approach-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_civil_war_recovery_plan-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_collectivisation-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_commissars_of_the_revolution-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_committing_to_the_5_year_plan-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_communalisation-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_communalised_cafeterias-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_cooperative_farming-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_decentralized_economics-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_fixing_the_economy-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_flying_high_above_the_sky-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_form_industrial_cooperatives-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_i_am_a_black_smith-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_keep_the_militias-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_land_lord_trials-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_land_moderation-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_land_to_the_tiller-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_massmobilization_doctrine-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_national_railroad_construction-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_new_radar_links-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_night_raids-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_organizingthepeoplesarmy-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_oursoldiersshallswimfly-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_protecting_the_revolutionary_red_sun-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_radical_redistribution-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_rebuild_the_hiroshima_shipyards-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_rehabilitatingpows-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_son_kosakutai-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_starting_the_land_reformation-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_strengthen_urban_industrial_centres-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_thepeoplesnavy-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_understanding_motorization-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_up_high_in_the_mountains-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_violent_land_revolution-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_working_another_day_for_the_masses_of_the_commune-248360.dds
[B] gfx/interface/goals/GFX_JAPRECOVERY_working_on_the_agrarian_economy-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_a_national_powerhouse-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_a_union_of_the_east-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_appease_the_land_owners-248360.dds
[C | 含 Socialist 字样] gfx/interface/goals/GFX_JAPSEI_crack_down_on_socialists-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_crush_the_unions-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_democratic_imperialism-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_encourage_japanese_integration_to_taiwan_and_chosen-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_end_party_factionalism-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_form_the_dainippon_koadomei-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_form_the_innovation_alliance-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_formal_annexation-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_further_influence_manchuria-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_gain_privy_council_support-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_honour_the_inukai_legacy-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_integration_through_assimilation-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_kuharascabinet-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_maintain_the_democratic_status_quo-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_moderate_land_reforms-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_national_policy_research_institute-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_orthodox_victory-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_promote_zaibatsu_interests-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_purge_the_orthodox_faction-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_question_colonial_rule-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_rentaro_cabinet-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_retain_the_leash-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_seiyukaiforever-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_solve_the_railway_issue-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_support_military_expansion-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_support_small_businesses-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_the_2nd_national_security_debate-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_the_reform_faction_hold-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_uphold_antiminseitoism-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_victory_of_the_seiyukai-248360.dds
[B] gfx/interface/goals/GFX_JAPSEI_zaibatsu_cooperation-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCDEM_a_split_in_the_shakai_taishuto-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCDEM_absorb_the_tokohai-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCDEM_an_empire_of_the_liberation-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCDEM_arrest_the_syndicalists-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCDEM_continue_democratization-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCDEM_crush_military_radicalism-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCDEM_deal_with_the_zaibatsu-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCDEM_denounce_the_syndicalist_folly-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCDEM_japansnewera-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCDEM_kempeitai_reforms-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCDEM_leftwing_victory-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCDEM_maximist_approach-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCDEM_national_equality-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCDEM_nationalize_the_zaibatsu-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCDEM_promote_universal_sufferage-248360.dds
[C | 含 Socialist 字样] gfx/interface/goals/GFX_JAPSOCDEM_promoting_the_national_socialist_image-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCDEM_promotion_of_new_agrarian_reforms-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCDEM_push_for_greater_national_autonomy-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCDEM_retain_the_parliamentary_system-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCDEM_rethinking_japanese_socialism-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCDEM_revoke_the_national_security_act-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCDEM_revoking_liberal_democracy-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCDEM_revolutionary_nationalism-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCDEM_rightist_faction_victory-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCDEM_supportingasanumasnewrevolution-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCDEM_supportingtheholywaragainsteurope-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCDEM_the_child_welfare_act-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCDEM_the_democracy_path-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCDEM_the_path_of_peace-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCDEM_totalitarian_shift-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCDEM_under_the_chrysanthamen-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCIALISM_cooperation_with_the_unions-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCIALISM_letsdoourbest-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCIALISM_liaison_with_shanghai_contacts-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCIALISM_organize_peasant_uprisings-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCIALISM_organize_the_farmers-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCIALISM_seek_internationale_aid-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCIALISM_striking_for_more_than_a_day-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCIALISM_the_revolution_is_calling-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCIALISM_theredflagflieshighovertokyo-248360.dds
[B] gfx/interface/goals/GFX_JAPSOCIALISM_war_socialism-248360.dds
[B] gfx/interface/goals/GFX_JAPTAISHUTOTWO_accept_universal_suffrage-248360.dds
[B] gfx/interface/goals/GFX_JAPTAISHUTOTWO_crumbling_of_the_party-248360.dds
[B] gfx/interface/goals/GFX_JAPTAISHUTOTWO_denounce_the_marxist_faction-248360.dds
[C | 含 Socialist 字样] gfx/interface/goals/GFX_JAPTAISHUTOTWO_proclaim_a_socialist_revolution-248360.dds
[B] gfx/interface/goals/GFX_JAPTAISHUTOTWO_promises_of_peace-248360.dds
[B] gfx/interface/goals/GFX_JAPTAISHUTOTWO_promote_the_holy_war-248360.dds
[B] gfx/interface/goals/GFX_JAPTAISHUTOTWO_promotewomensrights-248360.dds
[C | 含 Socialist 字样] gfx/interface/goals/GFX_JAPTAISHUTOTWO_remove_the_national_socialists-248360.dds
[B] gfx/interface/goals/GFX_JAPTAISHUTOTWO_resolving_the_party_split-248360.dds
[B] gfx/interface/goals/GFX_JAPTAISHUTOTWO_shrivel_up_the_military_industrial_complex-248360.dds
[B] gfx/interface/goals/GFX_JAPTAISHUTOTWO_support_the_diet-248360.dds
[B] gfx/interface/goals/GFX_JAPTAISHUTOTWO_up_hold_a_strong_military_presence-248360.dds
[B] gfx/interface/goals/GFX_JAPTAISHUTOTWO_victory_of_parliamentary_socialism-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_a_military_reign_of_terror-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_a_nation_of_coprosperity-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_a_national_defence_state-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_appease_the_navy-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_build_the_koa_kannon-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_call_for_spiritual_mobilization-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_clean_out_army_corruption-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_controlling_the_army-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_coup_of_the_toseiha-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_crush_the_syndicalist_infiltrators-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_denounce_the_european_devils-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_denounce_the_german_devil-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_eliminate_the_army_factions-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_embrace_japanese_totalitarianism-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_embrace_the_selfstrengthening_movement-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_empower_the_technocrats-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_following_the_emperors_will-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_form_the_asiatic_academic_association-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_form_the_greater_asia_association-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_form_the_national_military_union-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_formtheideologicalnationaldefenceassociation-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_increase_manetsu_investments-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_increase_militaristic_ideals-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_japanspathtoultramilitarism-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_nagataspath-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_national_will_power-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_new_guidelines_on_panasianism-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_oppose_radical_nationalists-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_panturania_calls-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_partner_with_technocrats-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_praise_to_an_old_friend-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_preparation_for_total_mobilization-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_prepare_for_total_war-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_proclaiming_the_new_shogun-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_promote_panasianist_news_papers-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_promotingikedaswritings-248360.dds
[C | 含 Socialist 字样] gfx/interface/goals/GFX_JAPTOSEIHA_purge_the_socialist_degeneration-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_push_forward_modernization-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_rekindling_ideas_of_panasianism-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_retraining_political_opponents-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_securejapansimperiallegacy-248360.dds
[C | 含 Socialist 字样] gfx/interface/goals/GFX_JAPTOSEIHA_socialist_crackdown-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_strengthen_manetsu_influence-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_strengthen_the_kempeitai-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_the_course_shall_shine_for_asia-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_the_tojo_cabinet-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_the_tojo_shogunate-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_turanian_brotherhood-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_turanism_strikes_japan-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_uphold_the_imperial_system-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_wartime_disaster_protection_act-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_weraiseourriflestotheemperor-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_work_with_hungarian_turanists-248360.dds
[B] gfx/interface/goals/GFX_JAPTOSEIHA_zaibatsu_subjegation-248360.dds
[B] gfx/interface/goals/GFX_JAPVINJAP_a_puppet_with_invisible_strings-248360.dds
[B] gfx/interface/goals/GFX_JAPVINJAP_arrest_cuong_de-248360.dds
[B] gfx/interface/goals/GFX_JAPVINJAP_expand_the_38th_army-248360.dds
[B] gfx/interface/goals/GFX_JAPVINJAP_expressing_solidarity_for_panasian_unity-248360.dds
[B] gfx/interface/goals/GFX_JAPVINJAP_extra_kempeitai_presence-248360.dds
[B] gfx/interface/goals/GFX_JAPVINJAP_futureofthecolony-248360.dds
[B] gfx/interface/goals/GFX_JAPVINJAP_hunt_down_independence_activists-248360.dds
[B] gfx/interface/goals/GFX_JAPVINJAP_japanese_volunteers_coup_the_administration-248360.dds
[C | 含 Socialist 字样] gfx/interface/goals/GFX_JAPVINJAP_socialist_witch_hunts-248360.dds
[B] gfx/interface/goals/GFX_JAPVINJAP_southasiastaiwan-248360.dds
[B] gfx/interface/goals/GFX_JAPVINJAP_squeeze_the_papers-248360.dds
[B] gfx/interface/goals/GFX_JAPVINJAP_teaching_dualinguoism-248360.dds
[B] gfx/interface/goals/GFX_JAPVINJAP_the_national_youth_councils-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_a_fight_against_western_colonialism-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_adhering_to_panasianism-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_centralised_under_the_emperor-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_creation_of_the_sacred_showa_society-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_denounce_european_imperialism-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_denouncing_the_liberalist_infiltration-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_esperanto_education-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_federalist_path-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_form_the_japanspiritualist_association-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_further_korean_integration-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_humanitygoodwill-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_japanesekoreanmongolian_federation-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_legacy_of_the_donghak_rebellion-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_legacy_of_the_iljinhoe-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_move_forward_for_humanity-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_new_national_moralism-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_oomoto_faction_victory-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_panasianist_expansion-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_promote_the_panasia_model-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_question_of_korean_guidance-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_reach_the_8_corners_of_the_world-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_reformednationalism-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_revive_the_dainippon_shusaikai-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_secure_pan_asia-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_secure_the_far_east-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_southern_thrust-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_spirit_of_the_satsuma_rebellion-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_strengthen_oomto_ties-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_the_black_dragon_rises-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_the_china_debate-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_the_path_of_peace-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_the_path_of_war-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_the_taisho_restoration-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_touyama_takes_the_reigns-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_uchida_faction-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_unitary_state-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_uphold_article_3-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_urbanization_program-248360.dds
[B] gfx/interface/goals/GFX_JAP_BLACKDRAG_work_with_touyama-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_1936_elections-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_a_nation_of_equals-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_align_with_kita-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_anti_seiyukai_squabbles-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_antieuropean_superiority-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_continue_militarist_expansion-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_denounce_katayama_radicalism-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_denounce_militarist_aggression-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_denounce_the_liberals-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_educate_the_peasants-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_embrace_democratization-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_embrace_dirigism-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_invite_the_social_democracts-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_isoswin-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_kenzosvictory-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_letsdoourbest-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_looking_forward_on_japanese_democracy-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_machidasvictory-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_may_15th_incident-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_procure_statist_economics-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_propose_electoral_reform-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_question_of_the_revolution-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_reach_out_to_the_unions-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_reaffirm_zaibatsu_ties-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_regulate_the_zaibatsu-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_ronoto_victory-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_status_quo-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_strike_for_katayama-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_support_the_military_expansionism-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_support_universal_suffrage-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_the_hand_of_the_tokohai-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_the_sun_rises_for_his_glory-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_the_union_hunt_down-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_tokohai_victory-248360.dds
[B] gfx/interface/goals/GFX_JAP_ELECTION_unite_the_party-248360.dds
[B] gfx/interface/goals/GFX_JAP_SOCFOR_a_revolution_on_the_world_stage-248360.dds
[B] gfx/interface/goals/GFX_JAP_SOCFOR_crush_the_colonialists_of_the_southern_seas-248360.dds
[B] gfx/interface/goals/GFX_JAP_SOCFOR_hunting_the_big_bear-248360.dds
[B] gfx/interface/goals/GFX_JAP_SOCFOR_liberate_the_former_colonies-248360.dds
[B] gfx/interface/goals/GFX_JAP_SOCFOR_our_own_path_of_liberation-248360.dds
[B] gfx/interface/goals/GFX_JAP_SOCFOR_proclaiming_the_red_star_above_india-248360.dds
[B] gfx/interface/goals/GFX_JAP_SOCFOR_proclaiming_the_red_steppe-248360.dds
[B] gfx/interface/goals/GFX_JAP_SOCFOR_promoting_the_global_revolution-248360.dds
[C | 含 Socialist 字样] gfx/interface/goals/GFX_JAP_SOCFOR_reaching_out_to_socialist_allies-248360.dds
[B] gfx/interface/goals/GFX_JAP_SOCFOR_saving_the_far_east-248360.dds
[B] gfx/interface/goals/GFX_JAP_SOCFOR_secure_central_asia-248360.dds
[B] gfx/interface/goals/GFX_JAP_SOCFOR_securing_asia_under_socialism-248360.dds
[B] gfx/interface/goals/GFX_JAP_SOCFOR_the_china_solution-248360.dds
[B] gfx/interface/goals/GFX_JAP_YAKUZA_crush_the_syndicalist_snakes-248360.dds
[B] gfx/interface/goals/GFX_JAP_YAKUZA_dominate_the_other_factions-248360.dds
[B] gfx/interface/goals/GFX_JAP_YAKUZA_embrace_japanese_dominance-248360.dds
[B] gfx/interface/goals/GFX_JAP_YAKUZA_international_smuggling_networks-248360.dds
[B] gfx/interface/goals/GFX_JAP_YAKUZA_japansfixer-248360.dds
[B] gfx/interface/goals/GFX_JAP_YAKUZA_maintaining_tradition-248360.dds
[B] gfx/interface/goals/GFX_JAP_YAKUZA_memories_from_the_rice_riots-248360.dds
[B] gfx/interface/goals/GFX_JAP_YAKUZA_monopolize_on_crime-248360.dds
[B] gfx/interface/goals/GFX_JAP_YAKUZA_no_law_for_our_order-248360.dds
[B] gfx/interface/goals/GFX_JAP_YAKUZA_set_new_inhiations-248360.dds
[B] gfx/interface/goals/GFX_JAP_YAKUZA_strengthen_the_drug_trade-248360.dds
[B] gfx/interface/goals/GFX_JAP_YAKUZA_the_yakuza_in_power-248360.dds
[B] gfx/interface/goals/GFX_JAP_YAKUZA_thejackalstwoheads-248360.dds
[B] gfx/interface/goals/GFX_JAP_YAKUZA_ultranationalist_alliances-248360.dds
[B] gfx/interface/goals/GFX_JAP_YAKUZA_work_with_the_black_dragon-248360.dds
[B] gfx/interface/goals/GFX_JAP_YAKUZA_yoshiospresence-248360.dds
[B] gfx/interface/goals/GFX_JAP_a_totalitarian_state-2708.dds
[B] gfx/interface/goals/GFX_JAP_anticommunism_movement-2684.dds
[B] gfx/interface/goals/GFX_JAP_consolidate_the_minseito-2684.dds
[B] gfx/interface/goals/GFX_JAP_defend_the_country-2684.dds
[B] gfx/interface/goals/GFX_JAP_delete_reaction-2684.dds
[B] gfx/interface/goals/GFX_JAP_expand_the_rights_of_imperial_japanese_army-2684.dds
[B] gfx/interface/goals/GFX_JAP_formalized_with_soical_democrats-2684.dds
[B] gfx/interface/goals/GFX_JAP_instill_loyalty_to_the_military-2684.dds
[B] gfx/interface/goals/GFX_JAP_instill_patriotism-2684.dds
[B] gfx/interface/goals/GFX_JAP_kita_above_all-2684.dds
[B] gfx/interface/goals/GFX_JAP_nakano_above_all-2684.dds
[B] gfx/interface/goals/GFX_JAP_pure_socialism-2684.dds
[B] gfx/interface/goals/GFX_JAP_purge_the_communists-2684.dds
[B] gfx/interface/goals/GFX_JAP_rebuild_with_people-2684.dds
[B] gfx/interface/goals/GFX_JAP_red_sun_rising-2684.dds
[B] gfx/interface/goals/GFX_JAP_reinforce_martial_law_at_night_fixed-2684.dds
[B] gfx/interface/goals/GFX_JAP_review_industrial_plans-2684.dds
[B] gfx/interface/goals/GFX_JAP_rise_labor_wages-2684.dds
[B] gfx/interface/goals/GFX_JAP_start_political_purge-2684.dds
[B] gfx/interface/goals/GFX_JAP_the_emperor_custody-2684.dds
[B] gfx/interface/goals/GFX_JAP_the_first_emperor-2684.dds
[B] gfx/interface/goals/GFX_JAP_whole_nation-2684.dds
[B] gfx/interface/goals/GFX_KORJUCHE_baeuja-248360.dds
[B] gfx/interface/goals/GFX_KORJUCHE_chollimassupremacy-248360.dds
[B] gfx/interface/goals/GFX_KORJUCHE_continuance_of_the_small_internationalism-248360.dds
[B] gfx/interface/goals/GFX_KORJUCHE_embracing_the_korean_identity-248360.dds
[B] gfx/interface/goals/GFX_KORJUCHE_forgoguryeo-248360.dds
[B] gfx/interface/goals/GFX_KORJUCHE_in_memory_of_buyeo-248360.dds
[B] gfx/interface/goals/GFX_KORJUCHE_jaju-248360.dds
[B] gfx/interface/goals/GFX_KORJUCHE_kimsgrandspeech-248360.dds
[B] gfx/interface/goals/GFX_KORJUCHE_koreasgreateridentity-248360.dds
[B] gfx/interface/goals/GFX_KORJUCHE_legacy_of_taejong-248360.dds
[B] gfx/interface/goals/GFX_KORJUCHE_secure_manchuria-248360.dds
[B] gfx/interface/goals/GFX_KORJUCHE_the_perfect_race-248360.dds
[B] gfx/interface/goals/GFX_KORJUCHE_the_ten_principle_mandate-248360.dds
[B] gfx/interface/goals/GFX_RDSOCJAP_asanuma_complete_victory-248360.dds
[C | 含 Socialist 字样] gfx/interface/goals/GFX_RDSOCJAP_national_socialist_continuance-248360.dds
[B] gfx/interface/goals/GFX_RDSOCJAP_the_peasants_advocate-248360.dds
[B] gfx/interface/goals/GFX_RDSOCJAP_the_rightists_triumph-248360.dds
[B] gfx/interface/goals/GFX_SQITWO_anti_japanese_revanchism-248360.dds
[B] gfx/interface/goals/GFX_SQITWO_arrest_japanese_diplomats-248360.dds
[C | 含 Socialist 字样] gfx/interface/goals/GFX_SQITWO_contact_with_japanese_socialists-248360.dds
[B] gfx/interface/goals/GFX_SQITWO_denouncing_the_japanese_menance-248360.dds
[B] gfx/interface/goals/GFX_SQITWO_further_limiting_of_anti_japaneseism-248360.dds
[B] gfx/interface/goals/GFX_SQITWO_humiliate_hirohito-248360.dds
[B] gfx/interface/goals/GFX_SQITWO_support_the_korean_revolution-248360.dds
[B] gfx/interface/goals/GFX_SQITWO_talks_with_korean_exiles-248360.dds
[B] gfx/interface/goals/GFX_SQITWO_thepeoplesantijapaneserevolution-248360.dds
[B] gfx/interface/goals/GFX_SQITWO_uniting_the_left_against_japan-248360.dds
[B] gfx/interface/goals/GFX_TAIECONO_a_national_army-248360.dds
[B] gfx/interface/goals/GFX_TAIECONO_a_new_and_modern_army-248360.dds
[B] gfx/interface/goals/GFX_TAIECONO_a_push_for_a_taiwanese_nation-248360.dds
[B] gfx/interface/goals/GFX_TAIECONO_a_world_of_friends-248360.dds
[B] gfx/interface/goals/GFX_TAIECONO_an_organised_force-248360.dds
[B] gfx/interface/goals/GFX_TAIECONO_beyond_spears_and_bows-248360.dds
[B] gfx/interface/goals/GFX_TAIECONO_beyond_taiwan-248360.dds
[B] gfx/interface/goals/GFX_TAIECONO_claiming_austroneasia-248360.dds
[B] gfx/interface/goals/GFX_TAIECONO_claiming_fujian-248360.dds
[B] gfx/interface/goals/GFX_TAIECONO_flying_boats-248360.dds
[B] gfx/interface/goals/GFX_TAIECONO_for_the_chinese_cause-248360.dds
[B] gfx/interface/goals/GFX_TAIECONO_forming_the_taiwanese_nation-248360.dds
[B] gfx/interface/goals/GFX_TAIECONO_hidden_defence-248360.dds
[B] gfx/interface/goals/GFX_TAIECONO_infiltrating_our_enemies-248360.dds
[B] gfx/interface/goals/GFX_TAIECONO_keep_the_militias-248360.dds
[B] gfx/interface/goals/GFX_TAIECONO_legacy_of_the_austronesian_boats-248360.dds
[B] gfx/interface/goals/GFX_TAIECONO_marine_corps-248360.dds
[B] gfx/interface/goals/GFX_TAIECONO_move_up_the_coast-248360.dds
[B] gfx/interface/goals/GFX_TAIECONO_naval_power_projections-248360.dds
[B] gfx/interface/goals/GFX_TAIECONO_our_own_northern_expedition-248360.dds
[B] gfx/interface/goals/GFX_TAIECONO_ousting_the_foreign_imperialists-248360.dds
[B] gfx/interface/goals/GFX_TAIECONO_sailing_the_asian_seas-248360.dds
[B] gfx/interface/goals/GFX_TAIECONO_securing_southern_china-248360.dds
[B] gfx/interface/goals/GFX_TAIECONO_securing_the_frontier_lands-248360.dds
[B] gfx/interface/goals/GFX_TAIECONO_silent_but_deadly-248360.dds
[B] gfx/interface/goals/GFX_TAIECONO_studying_great_war_tactics-248360.dds
[B] gfx/interface/goals/GFX_TAIECONO_the_conscription_question_answered-248360.dds
[B] gfx/interface/goals/GFX_TAIECONO_the_tanks_role_in-248360.dds
[B] gfx/interface/goals/GFX_TAIECONO_weareasiastruesaviours-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_a_crown_welcomed_back-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_a_new_taiwan-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_a_surprise_guest-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_aligning_the_taiwanese_business_men-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_amnesty_to_japanese_nationals-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_andosregency-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_appointment_of_a_new_governor-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_comfort_under_the_boot-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_construct_taiwanese_banks-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_continue_taiwanese_development-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_continuing_our_integration-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_create_a_tornado_of_unforeseen_power-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_crush_the_syndicalist_traitors-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_declare_the_national_reclamation_war-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_defend_the_opium_trade-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_denounce_the_german_collaborators-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_disband_protaiwanese_groups-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_ending_the_losses_of_black_monday-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_expand_agricultural_development-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_expand_scholarship_funds-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_expand_the_japanese_banking_sector-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_expand_the_opium_trade-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_finish_off_the_last_of_the_traitors-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_help_zaibatsu_corps-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_legacy_of_the_austronesian_boats-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_linsdominanceovertaiwan-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_marching_into_seoul-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_negotiate_with_the_kmt-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_panasian_promotion-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_prepare_for_the_home_coming-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_proclaiming_the_restoration-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_reach_out_to_matsui_iwane-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_reclaiming_the_empire-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_reclaiming_the_old_colonies-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_recovering_from_a_national_loss-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_samurai_spirit-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_secure_hainan-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_secure_ryukyu-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_secure_the_south_china_coast-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_securing_taiwan-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_support_welfare_programs-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_supporting_a_republican_idea-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_supremacy_of_will-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_the_dragon_shall_sail_the_south_seas-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_the_eye_rises_above_all-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_the_loss_of_an_empire-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_the_military_seizes_the_island-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_the_sun_rises_for_a_new_age_of_glory-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_thedivinewind-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_total_war_mobilisation-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_united_under_the_sun-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_uphold_the_hua_nan_bank-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_uphold_the_kodoha-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_we_shall_make_the_enemy_shake_in_fear-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_welcome_the_exiles-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_win_over_the_naval_officers-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_xubingsinfluence-248360.dds
[B] gfx/interface/goals/GFX_TAIMON_yasuhito_regency-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_375_rent_reducation-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_a_liberal_future-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_agricultural_mechanization-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_call_together_the_united_front-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_coming_from_a_harsh_winter_into_a_socialist_spring-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_communist_alliance-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_comrades_in_the_cultural_association-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_develop_the_proletarian_peasant_conscious-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_education_reforms-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_esperantist_education-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_establishment_of_a_proper_workers_party-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_expand_the_taiwan_workers_federation-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_form_peasant_communes-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_form_taiwan_minbao-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_form_tenancy_committees-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_formalize_a_national_army-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_from_the_fires_of_the_2nd_wushe_rebellion-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_improving_taiwanese_culture-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_in_honour_of_dr_sun-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_land_lord_expropriation-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_lessons_from_sun_and_lenin-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_limit_socialist_influence-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_linxiantangsrepublicangamble-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_ourlandrevolution-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_power_to_the_peasant_associations-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_promote_health_care-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_promoting_esperanto-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_promotion_of_taiwanese_cultural_expression-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_revolutionary_enlightenment-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_routeoutthehanjians-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_seize_zaibatsu_holdings-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_social_science_research_associations-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_socialism_with_taiwanese_characteristics-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_starting_national_land_reform-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_supporter_of_the_workers-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_syndicalist_primacy-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_taiwanese_red_culture-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_the_27th_brigade_marches_in-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_the_first_party_congress-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_the_peasants_rise_for_jian_ji-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_the_sun_has_set-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_thepeoplespartybelongstothemasses-248360.dds
[B+C | 含 Socialist 字样] gfx/interface/goals/GFX_TAISOC_ties_with_japanese_socialists-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_unite_the_farmer_associations-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_victoryofthepeoplesparty-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_weishuistaiwan-248360.dds
[B] gfx/interface/goals/GFX_TAISOC_xuehong_stays_the_course-248360.dds
[B] gfx/interface/goals/GFX_TAI_allow_for_integrated_politics-248360.dds
[B] gfx/interface/goals/GFX_TAI_allow_greater_zaibatsu_freedoms-248360.dds
[B] gfx/interface/goals/GFX_TAI_allowing_better_self_governance-248360.dds
[B] gfx/interface/goals/GFX_TAI_astablecolony-248360.dds
[B] gfx/interface/goals/GFX_TAI_brothers_in_arms-248360.dds
[B] gfx/interface/goals/GFX_TAI_colonial_harmony-248360.dds
[B] gfx/interface/goals/GFX_TAI_continuing_the_civilian_period-248360.dds
[B] gfx/interface/goals/GFX_TAI_crush_the_cultural_degeneration-248360.dds
[B] gfx/interface/goals/GFX_TAI_defending_sugar_cane_production-248360.dds
[B] gfx/interface/goals/GFX_TAI_desire_for_great_freedom-248360.dds
[B] gfx/interface/goals/GFX_TAI_determination_for_home_rule-248360.dds
[B] gfx/interface/goals/GFX_TAI_doka-248360.dds
[B] gfx/interface/goals/GFX_TAI_empower_a_provincial_assembly-248360.dds
[B] gfx/interface/goals/GFX_TAI_empower_the_kempeitai-248360.dds
[B] gfx/interface/goals/GFX_TAI_encourage_immigration-248360.dds
[B] gfx/interface/goals/GFX_TAI_expand_the_home_affairs_bureau-248360.dds
[B] gfx/interface/goals/GFX_TAI_expanding_the_ports-248360.dds
[B] gfx/interface/goals/GFX_TAI_favourjapansway-248360.dds
[B] gfx/interface/goals/GFX_TAI_for_imperial_glory-248360.dds
[B] gfx/interface/goals/GFX_TAI_fund_the_assimilation_society-248360.dds
[B] gfx/interface/goals/GFX_TAI_greater_resource_extraction-248360.dds
[B] gfx/interface/goals/GFX_TAI_increasing_in_civilian_modes_of_production-248360.dds
[B] gfx/interface/goals/GFX_TAI_investing_in_sanitation_systems-248360.dds
[B] gfx/interface/goals/GFX_TAI_legacy_of_the_taiwan_exposition-248360.dds
[B] gfx/interface/goals/GFX_TAI_military_victory-248360.dds
[B] gfx/interface/goals/GFX_TAI_minseito_hold-248360.dds
[B] gfx/interface/goals/GFX_TAI_new_industrial_complexes-248360.dds
[B] gfx/interface/goals/GFX_TAI_pushing_forward_zaibatsu_outsourcing-248360.dds
[B] gfx/interface/goals/GFX_TAI_questioning_autonomy-248360.dds
[B] gfx/interface/goals/GFX_TAI_railroad_construction-248360.dds
[B] gfx/interface/goals/GFX_TAI_regulate_zaibatsu_influence-248360.dds
[B] gfx/interface/goals/GFX_TAI_seiyukai_appointed-248360.dds
[B] gfx/interface/goals/GFX_TAI_settling_the_national_question-248360.dds
[B] gfx/interface/goals/GFX_TAI_side_by_side_we_go-248360.dds
[B] gfx/interface/goals/GFX_TAI_sortingouttheautonomyproblem-248360.dds
[B] gfx/interface/goals/GFX_TAI_starting_the_land_reform-248360.dds
[B] gfx/interface/goals/GFX_TAI_the_great_cultural_pavilion-248360.dds
[B] gfx/interface/goals/GFX_TAI_the_new_governor-248360.dds
[B] gfx/interface/goals/GFX_TAI_the_question_of_literary_societies-248360.dds
[B] gfx/interface/goals/GFX_TAI_transition_to_an_independent_parliament-248360.dds
[B] gfx/interface/goals/GFX_TAI_understanding_the_new_literature_movement-248360.dds
[B] gfx/interface/goals/GFX_TAI_win_over_chinese_nationalists-248360.dds
[B] gfx/interface/goals/GFX_TIA_build_up_japanese_hotels-248360.dds
[B] gfx/interface/goals/GFX_TIA_invite_japanese_intellectuals-248360.dds
[B] gfx/interface/goals/GFX_TIA_japanese_occupation-248360.dds
[B] gfx/interface/goals/GFX_TIB_banners_from_the_palace-248360.dds
[B] gfx/interface/goals/GFX_TIB_bazhaheitocomradeyuexi-248360.dds
[B] gfx/interface/goals/GFX_TIB_birth_of_the_revolutionary_committee-248360.dds
[B] gfx/interface/goals/GFX_TIB_burnthemonksaswemust-248360.dds
[B] gfx/interface/goals/GFX_TIB_collectivize_the_lands-248360.dds
[B] gfx/interface/goals/GFX_TIB_communism_over_lhasa-248360.dds
[B] gfx/interface/goals/GFX_TIB_connection_is_vital-248360.dds
[B] gfx/interface/goals/GFX_TIB_continue_a_secular_teaching-248360.dds
[B] gfx/interface/goals/GFX_TIB_crush_the_reactionary_tribes-248360.dds
[B] gfx/interface/goals/GFX_TIB_cultural_revolution_of_the_ages-248360.dds
[B] gfx/interface/goals/GFX_TIB_embrace_the_revolutionary_intellectuals-248360.dds
[B] gfx/interface/goals/GFX_TIB_freeing_the_surfs-248360.dds
[B] gfx/interface/goals/GFX_TIB_guns_of_socialism-248360.dds
[B] gfx/interface/goals/GFX_TIB_junmin_tuanjie_ru_yiren-248360.dds
[B] gfx/interface/goals/GFX_TIB_leaping_to_industrial_success-248360.dds
[B] gfx/interface/goals/GFX_TIB_our_five_fingers_extend_across_the_realm-248360.dds
[B] gfx/interface/goals/GFX_TIB_proclaim_5_year_plans-248360.dds
[B] gfx/interface/goals/GFX_TIB_question_of_the_monasteries-248360.dds
[B] gfx/interface/goals/GFX_TIB_raise_the_militias-248360.dds
[B] gfx/interface/goals/GFX_TIB_readingmaosworks-248360.dds
[B] gfx/interface/goals/GFX_TIB_reforming_the_lands-248360.dds
[B] gfx/interface/goals/GFX_TIB_swear_in_the_red_monastries-248360.dds
[B] gfx/interface/goals/GFX_TIB_takeover_of_the_red_militia-248360.dds
[B] gfx/interface/goals/GFX_TIB_the_red_sun_shines_over_tibet-248360.dds
[B] gfx/interface/goals/GFX_TIB_the_revolution_never_stops-248360.dds
[B] gfx/interface/goals/GFX_TIB_thesunsreachonthehorizon-248360.dds
[B] gfx/interface/goals/GFX_TIB_trains_shall_steam_ahead-248360.dds
[B] gfx/interface/goals/GFX_TRMKOR_bringing_in_revolutionary_korea_culture-248360.dds
[B] gfx/interface/goals/GFX_TRMKOR_koreasmayakovsky-248360.dds
[B] gfx/interface/goals/GFX_TRMKOR_socialist_realism_for_korea-248360.dds
[B] gfx/interface/goals/GFX_TRMKOR_the_korea_nep-248360.dds
[B] gfx/interface/goals/GFX_TRMKOR_the_korean_red_army_gallops_through_the_snow-248360.dds
[B] gfx/interface/goals/GFX_TWI_a_new_sakura_tree-121211.dds
[B] gfx/interface/goals/GFX_TWI_amnesty_to_taiwanese_workers-248360.dds
[B] gfx/interface/goals/GFX_TWI_encourage_reformed_taiwanese_capitalism-248360.dds
[B] gfx/interface/goals/GFX_TWI_enforcing_japanese_culture-121183.dds
[B] gfx/interface/goals/GFX_TWI_enforcing_state_shinto-221.dds
[B] gfx/interface/goals/GFX_TWI_expelling_the_japanese_bandits-248360.dds
[B] gfx/interface/goals/GFX_TWI_expression_of_taiwanese_culture-121203.dds
[B] gfx/interface/goals/GFX_TWI_return_of_the_yamato_dynasty-121103.dds
[B] gfx/interface/goals/GFX_TWI_seize_japanese_land_lord_assets-248360.dds
[B] gfx/interface/goals/GFX_TWI_taiwan_is_free-121206.dds
[B] gfx/interface/goals/GFX_TWI_taiwan_is_reborn-121221.dds
[B] gfx/interface/goals/GFX_TWI_taiwanese_syndicalism-121089.dds
[B] gfx/interface/goals/GFX_TWI_taking_back_choson-121196.dds
[B] gfx/interface/goals/GFX_TWI_the_samurai_sword_falls_from_its_stand-248360.dds
[B] gfx/interface/goals/GFX_TWI_wiping_the_japanese_devils-90818.dds
[B] gfx/interface/goals/GFX_TWI_work_with_the_taiwanese_workers-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_a_centralized_state-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_a_dusty_wind_shall_sweep_the_nation-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_a_new_era_of_greatness-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_a_republic_declared-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_absolute_power_at_the_helm-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_agricultural_modernization-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_aiding_our_farmers-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_allow_foreign_investment-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_amnesty_to_the_former_rebels-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_arewesyndicalists-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_begin_the_land_reform_campaign-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_centralize_the_rural_councils-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_codify_the_imperial_constitution-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_control_the_monopolies-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_crackdown_on_the_buddhists-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_criticise_the_two_systems-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_cuong_de_arises-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_deliberation_on_the_liberation_committee-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_denounce_personalism-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_denounce_the_false_nationalists-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_display_loyalty_to_the_fatherland-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_economic_reconstruction-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_educate_the_nation-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_embrace_corporatocracy-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_embrace_religious_fervour-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_embrace_survival_nationalism-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_enact_labour_laws-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_enact_welfare_reforms-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_encourage_class_collaboration-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_enforce_christian_values-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_establishtherevolutionaryyouth-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_follow_the_kaiser_model-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_for_the_rightful_prince-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_growing_industrialism-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_growing_zaibatsu_influence-248360.dds
[C | 含 Socialist 字样] gfx/interface/goals/GFX_VIETJAP_handling_the_socialists-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_honour_phan_boi_chau-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_honour_the_great_faith-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_honour_the_martyrs-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_imperial_legacy-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_industrial_independence-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_integrate_the_vnqdd-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_laborrevolutionpersonalism-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_national_elections-248360.dds
[C | 含 Socialist 字样] gfx/interface/goals/GFX_VIETJAP_nationalsocialistvictory-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_neoconfucian_constitution-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_ofcoursenot-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_our_own_direction-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_ouremperorsbenevolence-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_panasianist_appeals-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_personalismcommunityspiritualism-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_quadra_lingual_education-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_question_of_our_history-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_question_of_zaibatsu_investment-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_reach_out_to_the_black_dragon-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_rebuild_the_railways-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_reform_the_civil_service-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_remove_army_factionalism-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_removingexploitation-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_revive_mekong_trading-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_rice_export_economy-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_rule_by_decree-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_secure_our_sovereignty-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_social_harmony_under_the_emperor-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_strengthen_the_union_of_catholicism-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_textbook_ethics-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_the_cao_dai_joins_the_government-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_the_caravelle_group_walks_in-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_the_constitutional_monarchy-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_the_dragon_rises-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_the_imperial_restoration-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_the_intellectual_republic-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_the_mandarin_mandate-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_the_question_of_the_japanese_garrison-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_the_rice_bowl_of_asia-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_under_the_divine_eye-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_unite_the_central_highlands-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_vietnamsfirstdemocracy-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_we_push_forward_for_the_fatherland-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_welcome_our_japanese_friends_in_arms-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_wipethemout-248360.dds
[B] gfx/interface/goals/GFX_VIETJAP_xa_hoi_spreads_our_green_revolution-248360.dds
[B] gfx/interface/goals/GFX_VNQ_2_defend_against_japanese_imperialism-248360.dds
[B] gfx/interface/goals/GFX_ZAIJAP_a_miracle_upon_the_nation_of_cherry_blossoms-248360.dds
[B] gfx/interface/goals/GFX_ZAIJAP_a_new_heart_of_commerce-248360.dds
[B] gfx/interface/goals/GFX_ZAIJAP_a_vertically_integrated_nation-248360.dds
[B] gfx/interface/goals/GFX_ZAIJAP_andthegreenoilthatspinsthem-248360.dds
[B] gfx/interface/goals/GFX_ZAIJAP_blessings_of_daikokutent-248360.dds
[B] gfx/interface/goals/GFX_ZAIJAP_bytheinvestorfortheinvestoroftheinvestor-248360.dds
[B] gfx/interface/goals/GFX_ZAIJAP_controlling_the_fruits_of_labour_under_the_showa_authority-248360.dds
[B] gfx/interface/goals/GFX_ZAIJAP_embezzling_in_the_gold_rays_of_asian_prosperity-248360.dds
[B] gfx/interface/goals/GFX_ZAIJAP_emulating_the_idea_of_technocracy-248360.dds
[B] gfx/interface/goals/GFX_ZAIJAP_growth_to_the_sky_and_riding_the_sun-248360.dds
[B] gfx/interface/goals/GFX_ZAIJAP_heavy_industry_investments-248360.dds
[B] gfx/interface/goals/GFX_ZAIJAP_integration_of_second_tier_zaibatsu-248360.dds
[B] gfx/interface/goals/GFX_ZAIJAP_phase1thenewjapan-248360.dds
[B] gfx/interface/goals/GFX_ZAIJAP_phase2thenewasia-248360.dds
[B] gfx/interface/goals/GFX_ZAIJAP_phase3economicdomination-248360.dds
[B] gfx/interface/goals/GFX_ZAIJAP_securing_the_riches_and_prosperity_of_the_conquered_lands-248360.dds
[B] gfx/interface/goals/GFX_ZAIJAP_soldiers_of_fortune-248360.dds
[B] gfx/interface/goals/GFX_ZAIJAP_the_all_japan_industrial_alliance-248360.dds
[B] gfx/interface/goals/GFX_ZAIJAP_the_consolidation_of_japanese_industry-248360.dds
[B] gfx/interface/goals/GFX_ZAIJAP_the_land_disposal_plan-248360.dds
[B] gfx/interface/goals/GFX_ZAIJAP_the_shinkansen_project-248360.dds
[B] gfx/interface/goals/GFX_ZAIJAP_thegoldengearsofindustry-248360.dds
[B] gfx/interface/goals/GFX_ZAIJAP_upholding_and_practising_the_fordist_economic_philosophy-248360.dds
[B] gfx/interface/goals/JAP_Barrel_acros_Middle_East.png
[B] gfx/interface/goals/JAP_DEI_resources.png
[B] gfx/interface/goals/JAP_Riding_the_steppe.png
[B] gfx/interface/goals/JAP_Sword_Prepares_To_Swing.png
[B] gfx/interface/goals/JAP_adventure_bears_nest.png
[B] gfx/interface/goals/JAP_australasia.png
[B] gfx/interface/goals/JAP_barrel_across_pacific.png
[B] gfx/interface/goals/JAP_central_asia_Conquest.png
[B] gfx/interface/goals/JAP_continent_a_blaze.png
[B] gfx/interface/goals/JAP_hideyoshi_vindicated.png
[B] gfx/interface/goals/JAP_himalayan_expansion.png
[B] gfx/interface/goals/JAP_in_eagles_Nest.png
[B] gfx/interface/goals/JAP_overture_subcontinent.png
[B] gfx/interface/goals/JAP_peace_and_reconstruction.png
[B] gfx/interface/goals/JAP_pursuit_of_own_goals.png
[B] gfx/interface/goals/JAP_road_manilla.png
[B] gfx/interface/goals/JAP_sailing_south_seas.png
[B] gfx/interface/goals/JAP_save_china_from_europe.png
[B] gfx/interface/goals/JAP_seisheiron.png
[B] gfx/interface/goals/JAP_south_american_migrants.png
[B] gfx/interface/goals/JAP_squabbles_sea_asia.png
[B] gfx/interface/goals/JAP_subdue_bear.png
[B] gfx/interface/goals/JAP_sword_Swings.png
[B] gfx/interface/goals/JAP_trip_honolulu.png
[B] gfx/interface/goals/JAP_two_dragon_one_master.png
[B] gfx/interface/goals/JAP_vladivstock.png
[B] gfx/interface/goals/JAP_western_frontiers.png
[B] gfx/interface/goals/KMT/KMT_Start_taichi.dds
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_CHI/Exterminate_the_Japanese_Devils.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_COF/FRA_Japanese_socialism.dds
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_COF/FRA_anti_japanese.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/AST_japanese_cooperation.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_IRAA.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_REF.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_Russian_Alliance.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_admiralty_question.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_attack_britain.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_attack_france.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_attack_usa.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_bugyo_guide.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_bureaucrat_reform.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_co_prosperity_sphere.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_combine_bomber_effort.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_combined_government.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_constitution.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_continental_warfare.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_cut_off_british_supplies.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_deconfuciusization.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_electoral_reform.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_expand_army.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_feburary_incident.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_feudal_domain_return.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_feudal_returns.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_fukoku_kyohei.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_government_supervised_complex.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_grand_triumvirate.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_iesato_government.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_imperial_power_q.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_increase_navy_budget.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_increase_navy_size.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_industry.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_kazoku_election.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_kohoda.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_kokutai_minshu.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_kuniyuki_blueprint.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_kyujidai.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_last_answer.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_left_learning_doctrine.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_local_election.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_long_live_shogun.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_maritime_superpower.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_meeting_of_officials.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_megacollab.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_mikawahan.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_mil_parl.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_military_disintegrate.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_municipality_promote_act.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_nagoya_arsenal.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_new_legacy_of_tokugawa.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_oniwahan.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_peoples_power.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_progressive_backsliding.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_prusso_american_abolish.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_public_address.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_regional_imperium.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_reinstall_daimyo.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_report_to_emperor.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_rising_of_sun.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_ritsuryo_code.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_rubberstamp_parl.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_rural_urbanization.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_samurai_law.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_secure_our_place.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_seigaku.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_shinjidai.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_shogunal_democracy.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_shogunate_industry.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_sin_of_lastshogun.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_south_seas_mandate.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_special_tribunal_nagasaki.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_suffrage_chosen_one.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_superior_battlefleet.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_supply_russia.png
[B+C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_taisho_lesson.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_tank.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_the_kingmaker.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_the_manager.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_the_oka.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_the_protector.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_the_two_tokugawas.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_the_yamato.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_to_golden_age.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_tokaido_dev.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_tokugawa_eternal_reign.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_toseiha.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_toza_fudai.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_tripartite_pact.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_ultranat_question.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_ultraroyal_question.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_universal_suffrage.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_unsinkable_carriers.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/JAP_victory_of_alliance.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/Japanese_Glory.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/Japanification_of_Foreign_Subsidification.png
[B] gfx/interface/goals/KXX_FX/Korea_Colony.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/PHI_ally_japan.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/PHI_attack_japan.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/PHI_punish_shogun.png
[B] gfx/interface/goals/KXX_FX/PHI_support_korea.png
[B] gfx/interface/goals/KXX_FX/Taiwan_Colony.png
[B] gfx/interface/goals/KXX_FX/The_korean_problem.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/ZHI_request_japanese_funding.png
[B] gfx/interface/goals/KXX_FX/ZHI_tibet.png
[B] gfx/interface/goals/KXX_FX/generic_attack_tibet.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/generic_focus_japan.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/goal_JAP_yen.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/goal_align_japan.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/goal_flag_japan.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/goal_japan_helmet.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/goal_japanese_imperialism.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/goal_japanese_instructors.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/goal_japanese_investment.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/goal_japanese_navy.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/goal_japanese_officer.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/goal_japanese_tank_import.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/goal_yamato_hotel.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/jap_fuel_anti_british_sentiment.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/jap_imperial_army.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/jap_imperial_navy.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/jap_left.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/jap_right.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/jap_summit_la.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/japanese_corporations_1.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/japanese_economics.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_FX/kmt_contest_the_japanese.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_5_year_production_plan.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_70th_imperial_diet.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_active_service_minister.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_alliance_with_seiyukai.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_appeasement_policy.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_army_navy_budget_coordination.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_birth_of_dai_nippon_political_association.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_china_cooperation_work.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_complete_total_mobilization.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_continued_election_purification.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_create_financial_scandals.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_develop_kinkei_academy.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_eliminate_corruption_in_justice_ministry.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_enforce_national_security_act.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_establish_jurisprudence_research_society.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_establish_kowa_in.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_expand_suzuki_kwantung_army.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_expelling_political_parties.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_force_peace_preservation_law.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_goal_Kill_Tenno.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_hiranuma_cabinet.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_imperial_way_is_jurisprudence.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_increase_execution_preventive_detention.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_industrial_control_expansion.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_inspiration_of_mahatma_gandhi.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_iron_fist_of_thought_prosecutors.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_kempeitai_politics_tokko_state.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_kikkenseishodo.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_kuhara_fusanosuke_leadership.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_liberation_of_asian_race.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_machida_chuji_stability.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_maeda_yonezo_ascent.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_manchurian_network_funding.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_military_zaibatsu_merger.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_mori_kaku_dictatorship.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_nagai_ryutaro_reform.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_national_labor_education.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_national_life_control.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_new_zaibatsu_into_manchuria.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_patriotic_combination.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_privy_council_reform.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_promote_agricultural_association_movement.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_promote_provincial_personnel_reform.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_rebuild_the_moral_nation.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_reject_normalization_of_criminal_police.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_relief_for_colonies.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_resist_military_radicalism.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_return_of_the_new_bureaucrats.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_senior_bureaucrats_protection_act.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_support_imperial_way_diplomacy_renewal.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_suppress_right_wing_agitation.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_suzuki_iron_fist.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_three_year_rearmament.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_total_martial_law.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_unified_organization_of_youth_corps.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_unlimited_military_deficit.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JAP_useful_discretion_of_nationalism.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JSR_coopt_veteran_associations.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JSR_do_our_utmost.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JSR_emperor_and_national_polity.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JSR_enforce_wartime_centralization.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JSR_expropriate_zaibatsu_assets.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JSR_ideology_and_faith_control.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JSR_indiscriminate_revolutionary_terror.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JSR_industrial_and_zaibatsu_liquidation.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JSR_land_and_rural_ownership.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JSR_launch_nichiren_ikki.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JSR_maitreya_socialism.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JSR_make_osugi_sakae_proud.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JSR_military_structure_and_command.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JSR_mobilize_labor_unions.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JSR_one_country_socialism_under_imperial_majesty.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JSR_popular_front_government.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JSR_raise_the_banner_of_joint_struggle.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JSR_rebirth_of_hinomaru.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JSR_reconstruct_the_rising_sun.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JSR_red_flag_over_tokyo.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_JAP/JSR_smuggling_aid_via_yakuza.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_PHI/PHI_anti_ajapan.png
[C | 目录 KXX_/SCB_] gfx/interface/goals/KXX_POL/POL_connect_japan.png
[B] gfx/interface/goals/MNS/GFX_MNS_invite_japanese_scientists-82547.dds
[B] gfx/interface/goals/PB_Goals/CHI_Attack_Tibet.dds
[B] gfx/interface/goals/PB_Goals/CHI_Imperial_Federation_Tibet.dds
[B] gfx/interface/goals/PB_Goals/CHI_Tibet_Campaign.dds
[B] gfx/interface/goals/PB_Goals/Generic_Republican_Japan.dds
[B] gfx/interface/goals/PB_Goals/Generic_Republican_Japanese_Army.dds
[B] gfx/interface/goals/PB_Goals/Generic_Republican_Japanese_Diplomacy.dds
[B] gfx/interface/goals/PB_Goals/Generic_Republican_Japanese_Tanks.dds
[B] gfx/interface/goals/PB_Goals/JAP_Co_Prosperity_Sphere.dds
[B] gfx/interface/goals/PB_Goals/JAP_Exploit_the_Chaos.dds
[B] gfx/interface/goals/PB_Goals/JAP_Fate_of_Hashimoto.dds
[B] gfx/interface/goals/PB_Goals/JAP_Japanese_Glory.dds
[B] gfx/interface/goals/PB_Goals/JAP_Rightful_Rule_Returns.dds
[B] gfx/interface/goals/PB_Goals/PB_ENG_Reconcile_Japan.dds
[B] gfx/interface/goals/PB_Goals/PB_ENG_Taiwan_Issue.dds
[B] gfx/interface/goals/PB_Goals/PB_JAP_And_Dont_Deliver.dds
[B] gfx/interface/goals/PB_Goals/PB_JAP_Contacts_in_Army.dds
[B] gfx/interface/goals/PB_Goals/PB_JAP_Contacts_in_Navy.dds
[B] gfx/interface/goals/PB_Goals/PB_JAP_Debates_on_Military.dds
[B] gfx/interface/goals/PB_Goals/PB_JAP_Debates_on_Militias.dds
[B] gfx/interface/goals/PB_Goals/PB_JAP_Debates_on_Unions.dds
[B] gfx/interface/goals/PB_Goals/PB_JAP_Empower_Red_Guards.dds
[B] gfx/interface/goals/PB_Goals/PB_JAP_Future_of_Republic.dds
[B] gfx/interface/goals/PB_Goals/PB_JAP_Future_of_Republic_Hashimoto.dds
[B] gfx/interface/goals/PB_Goals/PB_JAP_Hashimoto_Breakneck_Industrialization.dds
[B] gfx/interface/goals/PB_Goals/PB_JAP_Hashimoto_Denounce_Democracy.dds
[B] gfx/interface/goals/PB_Goals/PB_JAP_Hashimoto_Embrace_Ishii.dds
[B] gfx/interface/goals/PB_Goals/PB_JAP_Hashimoto_Red_Bushido.dds
[B] gfx/interface/goals/PB_Goals/PB_JAP_Hashimoto_Red_Bushido_New_Tenant.dds
[B] gfx/interface/goals/PB_Goals/PB_JAP_Hashimoto_Womens_Rights_Reform.dds
[B] gfx/interface/goals/PB_Goals/PB_JAP_Intensify_Paranoia.dds
[B] gfx/interface/goals/PB_Goals/PB_JAP_Ishii_Coup.dds
[B] gfx/interface/goals/PB_Goals/PB_JAP_Loyalty_Oaths.dds
[B] gfx/interface/goals/PB_Goals/PB_JAP_Make_Shit_Up.dds
[B] gfx/interface/goals/PB_Goals/PB_JAP_Party_Congress_Conclusion.dds
[B] gfx/interface/goals/PB_Goals/PB_JAP_Promise_Autonomy.dds
[B] gfx/interface/goals/PB_Goals/PB_JAP_Promise_Reforms.dds
[B] gfx/interface/goals/PB_Goals/PB_JAP_Purge_Army.dds
[B] gfx/interface/goals/PB_Goals/PB_JAP_Purge_Bureaucrats.dds
[B] gfx/interface/goals/PB_Goals/PB_JAP_Purge_Navy.dds
[B] gfx/interface/goals/PB_Goals/PB_JAP_Tea_with_Anarchists.dds
[B] gfx/interface/goals/PB_Goals/PB_JAP_Wild_Promises.dds
[B] gfx/interface/goals/ROTG_goals/Japanification_of_Foreign_Subsidification.dds
[B] gfx/interface/goals/ROTG_goals/goal_japanese_instructors.dds
[B] gfx/interface/goals/ROTG_goals/goal_japanese_officer.tga
[B] gfx/interface/goals/ROTG_goals/taiyuan_arsenal.tga
[B] gfx/interface/goals/RUS_dominate_japan.png
[B] gfx/interface/goals/Supporting_Taixu.png
[B] gfx/interface/goals/TAI/2ndsingapore.dds
[B] gfx/interface/goals/TAI/5nationvanguard.dds
[B] gfx/interface/goals/TAI/agriculturalsupport.dds
[B] gfx/interface/goals/TAI/anewmandate.dds
[B] gfx/interface/goals/TAI/beaconofliberty.dds
[B] gfx/interface/goals/TAI/breakingfree.dds
[B] gfx/interface/goals/TAI/chihsingtaiwan.dds
[B] gfx/interface/goals/TAI/chinesefiume.dds
[B] gfx/interface/goals/TAI/chinesesocialism.dds
[B] gfx/interface/goals/TAI/civilliberties.dds
[B] gfx/interface/goals/TAI/corporatestate.dds
[B] gfx/interface/goals/TAI/culturalrevolution.dds
[B] gfx/interface/goals/TAI/curtailcorporate.dds
[B] gfx/interface/goals/TAI/dealwithaustralia.dds
[B] gfx/interface/goals/TAI/dealwiththeanglos.dds
[B] gfx/interface/goals/TAI/dealwiththedutch.dds
[B] gfx/interface/goals/TAI/dealwiththeusa.dds
[B] gfx/interface/goals/TAI/denouncethereactionaries.dds
[B] gfx/interface/goals/TAI/denouncethesocialists.dds
[B] gfx/interface/goals/TAI/economicequality.dds
[B] gfx/interface/goals/TAI/formosapact.dds
[B] gfx/interface/goals/TAI/freeelections.dds
[B] gfx/interface/goals/TAI/frenchconnections.dds
[B] gfx/interface/goals/TAI/friendsinhanoi.dds
[B] gfx/interface/goals/TAI/future.dds
[B] gfx/interface/goals/TAI/huajiachengpo.dds
[B] gfx/interface/goals/TAI/infiltratethecities.dds
[B] gfx/interface/goals/TAI/infiltratethecountryside.dds
[B] gfx/interface/goals/TAI/internationalecontacts.dds
[B] gfx/interface/goals/TAI/jewelofasia.dds
[B] gfx/interface/goals/TAI/jointhecommunes.dds
[B] gfx/interface/goals/TAI/jointhepwl.dds
[B] gfx/interface/goals/TAI/liaosrepublicans.dds
[B] gfx/interface/goals/TAI/linscoalition.dds
[B] gfx/interface/goals/TAI/localchairmen.dds
[B] gfx/interface/goals/TAI/marchnorthoncemore.dds
[B] gfx/interface/goals/TAI/marketeconomy.dds
[B] gfx/interface/goals/TAI/miningcontracts.dds
[B] gfx/interface/goals/TAI/modernchineseideal.dds
[B] gfx/interface/goals/TAI/natureisthesculptorandchinaisthestatue.dds
[B] gfx/interface/goals/TAI/newchinesepopulism.dds
[B] gfx/interface/goals/TAI/newreligiouslaws.dds
[B] gfx/interface/goals/TAI/nodictators.dds
[B] gfx/interface/goals/TAI/noeastorwest.dds
[B] gfx/interface/goals/TAI/nonorthorsouth.dds
[B] gfx/interface/goals/TAI/noracialboundaries.dds
[B] gfx/interface/goals/TAI/occidentalistchina.dds
[B] gfx/interface/goals/TAI/outofonemany.dds
[B] gfx/interface/goals/TAI/pacifictradeorganisation.dds
[B] gfx/interface/goals/TAI/panasianism.dds
[B] gfx/interface/goals/TAI/past.dds
[B] gfx/interface/goals/TAI/pensandpencilstreatise.dds
[B] gfx/interface/goals/TAI/present.dds
[B] gfx/interface/goals/TAI/purgethetechnocrats.dds
[B] gfx/interface/goals/TAI/rallythemoderates.dds
[B] gfx/interface/goals/TAI/serenerepublicofchina.dds
[B] gfx/interface/goals/TAI/shippingcontracts.dds
[B] gfx/interface/goals/TAI/socialistprograms.dds
[B] gfx/interface/goals/TAI/supportshumei.dds
[B] gfx/interface/goals/TAI/surrealarchitecture.dds
[B] gfx/interface/goals/TAI/taiwanesesunyatsen.dds
[B] gfx/interface/goals/TAI/tansclub.dds
[B] gfx/interface/goals/TAI/thechaos.dds
[B] gfx/interface/goals/TAI/thedreamscape.dds
[B] gfx/interface/goals/TAI/thepeoplesparty.dds
[B] gfx/interface/goals/TAI/thetcptakespower.dds
[B] gfx/interface/goals/TAI/theyellowriver.dds
[B] gfx/interface/goals/TAI/urbansupport.dds
[B] gfx/interface/goals/TAI/womensrights.dds
[B] gfx/interface/goals/TAI_DOM_The_Phoenix.png
[B] gfx/interface/goals/The New Order/JAP_Denounce_the_Reformists.dds
[B] gfx/interface/goals/The New Order/JAP_Rebuilding_the_Cities.dds
[B] gfx/interface/goals/The New Order/JAP_Red_Alert.dds
[B] gfx/interface/goals/The New Order/JAP_cabinet_reshuffle.dds
[B] gfx/interface/goals/The New Order/RAJ_India_Diplo_Japan_Border.dds
[B] gfx/interface/goals/The New Order/RAJ_India_Diplo_Japan_Gateway.dds
[B] gfx/interface/goals/The New Order/RAJ_India_Diplo_Japan_Let_it_Go.dds
[B] gfx/interface/goals/The New Order/RAJ_India_Diplo_Japan_Trade.dds
[B] gfx/interface/goals/The New Order/RAJ_India_Diplo_Japan_Without_Us.dds
[B] gfx/interface/goals/The New Order/RAJ_Japanese_Planes.dds
[B] gfx/interface/goals/YTG_contact_comjap.png
[B] gfx/interface/goals/YTG_poisoning_japanese.png
[B] gfx/interface/goals/rework_JAP/KR_ideology_authoritarian_democrat.png
[B] gfx/interface/goals/rework_JAP/KR_ideology_market_liberal.png
[B] gfx/interface/goals/rework_JAP/KR_ideology_national_populist.png
[B] gfx/interface/goals/rework_JAP/KR_ideology_paternal_autocrat.png
[C | 含 Socialist 字样] gfx/interface/goals/rework_JAP/KR_ideology_radical_socialist.png
[B] gfx/interface/goals/rework_JAP/KR_ideology_social_conservative.png
[B] gfx/interface/goals/rework_JAP/KR_ideology_social_democrat.png
[B] gfx/interface/goals/rework_JAP/KR_ideology_social_liberal.png
[B] gfx/interface/goals/rework_JAP/KR_ideology_syndicalist.png
[B] gfx/interface/goals/rework_JAP/KR_ideology_totalist.png
[B] gfx/interface/goals/taiwan/CHI_chicomm.dds
[B] gfx/interface/goals/taiwan/CHI_jap_teachers.dds
[B] gfx/interface/goals/taiwan/GFX_CHI_Evolution_Of_Culture.dds
[B] gfx/interface/goals/taiwan/GFX_TAI_two_occupying.dds
[B] gfx/interface/goals/taiwan/GFX_YUN_What_Did_You_Do_In_The_War.dds
[B] gfx/interface/goals/taiwan/JAP_A_Voice_in_General_Headquarters.dds
[B] gfx/interface/goals/taiwan/JAP_Ministry_of_Pan_Asian_Recovery.dds
[B] gfx/interface/goals/taiwan/JAP_Never_Been_Better.dds
[B] gfx/interface/goals/taiwan/JAP_co_prosperity_sphere.png
[B] gfx/interface/goals/taiwan/JAP_target_philippines.png
[B] gfx/interface/goals/taiwan/Kaohsiung_City.png
[B] gfx/interface/goals/taiwan/MING_rollingchina.png
[B] gfx/interface/goals/taiwan/SeediqBale.png
[B] gfx/interface/goals/taiwan/TAI_Aluminium.png
[B] gfx/interface/goals/taiwan/TAI_Anarchy_gobal.png
[B] gfx/interface/goals/taiwan/TAI_Colorado_Resurgence.png
[B] gfx/interface/goals/taiwan/TAI_Empires_Stockpile.png
[B] gfx/interface/goals/taiwan/TAI_Faster_Industrialization.dds
[B] gfx/interface/goals/taiwan/TAI_FreeSEA.png
[B] gfx/interface/goals/taiwan/TAI_JAP_aircraft_production.png
[B] gfx/interface/goals/taiwan/TAI_Japanesepowerdown.png
[B] gfx/interface/goals/taiwan/TAI_KMTmarco.png
[B] gfx/interface/goals/taiwan/TAI_LeagueofChina.png
[B] gfx/interface/goals/taiwan/TAI_Legacy_of_the_Union.dds
[B] gfx/interface/goals/taiwan/TAI_Mediate_a_Research_Agreement.dds
[B] gfx/interface/goals/taiwan/TAI_Political_Consultative_Conference.png
[B] gfx/interface/goals/taiwan/TAI_ROTflag.png
[B] gfx/interface/goals/taiwan/TAI_SEAflag.png
[B] gfx/interface/goals/taiwan/TAI_Secret_Reforms.dds
[B] gfx/interface/goals/taiwan/TAI_Senkaku.png
[B] gfx/interface/goals/taiwan/TAI_Socialist_primitive_accumulation.png
[B] gfx/interface/goals/taiwan/TAI_beauty_island.png
[B] gfx/interface/goals/taiwan/TAI_checkout_rebels.png
[B] gfx/interface/goals/taiwan/TAI_coal_mining.dds
[B] gfx/interface/goals/taiwan/TAI_flagonmap.png
[B] gfx/interface/goals/taiwan/TAI_focuson_world.png
[B] gfx/interface/goals/taiwan/TAI_gaosha.png
[B] gfx/interface/goals/taiwan/TAI_gov_Burning.png
[B] gfx/interface/goals/taiwan/TAI_help_CHI.png
[B] gfx/interface/goals/taiwan/TAI_help_JAP.png
[B] gfx/interface/goals/taiwan/TAI_jiazhang.png
[B] gfx/interface/goals/taiwan/TAI_keep_neutral.png
[B] gfx/interface/goals/taiwan/TAI_learn_japanese.dds
[B] gfx/interface/goals/taiwan/TAI_marriage.png
[B] gfx/interface/goals/taiwan/TAI_modern_electricity.png
[B] gfx/interface/goals/taiwan/TAI_nantou.png
[B] gfx/interface/goals/taiwan/TAI_national_principle.png
[B] gfx/interface/goals/taiwan/TAI_passport.png
[B] gfx/interface/goals/taiwan/TAI_peace_army.png
[B] gfx/interface/goals/taiwan/TAI_people_livelihood.png
[B] gfx/interface/goals/taiwan/TAI_preview.png
[B] gfx/interface/goals/taiwan/TAI_principles_of_democracy.png
[B] gfx/interface/goals/taiwan/TAI_railway_work.dds
[B] gfx/interface/goals/taiwan/TAI_south_east_asian_offensive.dds
[B] gfx/interface/goals/taiwan/TAI_spiritual_mobilization.dds
[B] gfx/interface/goals/taiwan/TAI_suger_factory.png
[B] gfx/interface/goals/taiwan/TAI_tea_trade.png
[B] gfx/interface/goals/taiwan/TAI_toseiha.png
[B] gfx/interface/goals/taiwan/TAI_underchi.png
[B] gfx/interface/goals/taiwan/TAI_villages.dds
[B] gfx/interface/goals/taiwan/TAI_vsjapan.png
[B] gfx/interface/goals/taiwan/TAI_war_liberation.png
[B] gfx/interface/goals/taiwan/TAI_white_peace_JAP.png
[B] gfx/interface/goals/taiwan/TAI_xiesquestion.png
[B] gfx/interface/goals/taiwan/TWU.png
[B] gfx/interface/goals/taiwan/Taiwan_Colony.png
[B] gfx/interface/goals/taiwan/ba_wan.png
[B] gfx/interface/goals/taiwan/baguashan_buddha.png
[B] gfx/interface/goals/taiwan/bunsaku_arakatsu_research.png
[B] gfx/interface/goals/taiwan/corporate_meeting.dds
[B] gfx/interface/goals/taiwan/focus_attack_japan.dds
[B] gfx/interface/goals/taiwan/jinmen.png
[B] gfx/interface/goals/taiwan/ming.png
[B] gfx/interface/goals/taiwan/ming_nuke.dds
[B] gfx/interface/goals/taiwan/mingkillqing.png
[B] gfx/interface/goals/taiwan/mingreturn.png
[B] gfx/interface/goals/taiwan/minyue.png
[B] gfx/interface/goals/taiwan/radical_socialist_TAI.png
[B] gfx/interface/goals/taiwan/republictai.png
[B] gfx/interface/goals/taiwan/social_democrat_TAI.png
[B] gfx/interface/goals/taiwan/syndicalist_TAI.png
[B] gfx/interface/goals/taiwan/tai_conservative.png
[B] gfx/interface/goals/taiwan/tai_csbc.png
[B] gfx/interface/goals/taiwan/tai_kobelco_factory.dds
[B] gfx/interface/goals/taiwan/tai_social_liberal.png
[B] gfx/interface/goals/taiwan/taiwan1.png
[B] gfx/interface/goals/taiwan/taiwanbigflag1.png
[B] gfx/interface/goals/taiwan/taiwanbigflag2.png
[B] gfx/interface/goals/taiwan/taiwanthreeflags.png
[B] gfx/interface/goals/taiwan/totalist_TAI.png
[B] gfx/interface/goals/taiwan/xiesilltv.dds
[B] gfx/interface/goals/taiwanese_republic.dds
[B] gfx/interface/gui/HOR_Japan_Icon.png
[B] gfx/interface/gui/HOR_Japan_army_Faction_Icon.png
[B] gfx/interface/gui/JAP_zaibatsu_icon.png
[B] gfx/interface/gui/china_map_japan_gui.png
[B] gfx/interface/gui/japan_influence_colonies.png
[B] gfx/interface/ideas/CAL/CAL_Japanese_architectural_style.png
[B] gfx/interface/ideas/CAL/CAL_order_from_jap.png
[B] gfx/interface/ideas/CHL/CHL_JAP.png
[B] gfx/interface/ideas/GFX_idea_JAP_military_divided.png
[B] gfx/interface/ideas/GFX_idea_JAP_naval_army_comp.png
[B] gfx/interface/ideas/Government_Ideas/PB_NI_Japanese_Militarism.dds
[B] gfx/interface/ideas/Government_Ideas/Tech_Teams/Generic/PB_Generic_Tokyo_Arsenal_Contract.dds
[B] gfx/interface/ideas/JAP/1984.png
[B] gfx/interface/ideas/JAP/Idea_JAP_imperial_regency.png
[B] gfx/interface/ideas/JAP/Idea_JAP_imperial_support.png
[B] gfx/interface/ideas/JAP/Idea_JAP_naval_support.png
[B] gfx/interface/ideas/JAP/Idea_JAP_no_emperor.png
[B] gfx/interface/ideas/JAP/Idea_JAP_no_navy.png
[B] gfx/interface/ideas/JAP/Idea_JAP_workers_unite.png
[B] gfx/interface/ideas/JAP/JAP_Kyujidai.png
[B] gfx/interface/ideas/JAP/JAP_Man_of_his_men.png
[B] gfx/interface/ideas/JAP/JAP_Nagasaki_Protocol.png
[B] gfx/interface/ideas/JAP/JAP_Shinjidai.png
[B] gfx/interface/ideas/JAP/JAP_Shitty_Tracks.png
[B] gfx/interface/ideas/JAP/JAP_Tokugawa_full_auth.png
[B] gfx/interface/ideas/JAP/JAP_Tokugawa_restored_auth.png
[B] gfx/interface/ideas/JAP/JAP_Tokugawa_wek_auth.png
[B] gfx/interface/ideas/JAP/JAP_administration_office.png
[B] gfx/interface/ideas/JAP/JAP_bamboo_army.png
[B] gfx/interface/ideas/JAP/JAP_black_monday_dirigisme.png
[B] gfx/interface/ideas/JAP/JAP_bodhisattva_spirit.png
[B] gfx/interface/ideas/JAP/JAP_china_strategy.png
[B] gfx/interface/ideas/JAP/JAP_co_prosper.png
[B] gfx/interface/ideas/JAP/JAP_control_the_unions.png
[B] gfx/interface/ideas/JAP/JAP_controlling_zaibatsu.png
[B] gfx/interface/ideas/JAP/JAP_daikokutent_blessings.png
[B] gfx/interface/ideas/JAP/JAP_democracy.png
[B] gfx/interface/ideas/JAP/JAP_dont_miss_bus.png
[B] gfx/interface/ideas/JAP/JAP_ethnic_unity.png
[B] gfx/interface/ideas/JAP/JAP_faith_inquisition.png
[B] gfx/interface/ideas/JAP/JAP_fallen_zaibatsu.png
[B] gfx/interface/ideas/JAP/JAP_fengtian_exploitation.png
[B] gfx/interface/ideas/JAP/JAP_fixers.png
[B] gfx/interface/ideas/JAP/JAP_golden_age.png
[B] gfx/interface/ideas/JAP/JAP_heinan_revised.png
[B] gfx/interface/ideas/JAP/JAP_hiranumasshogunate.png
[B] gfx/interface/ideas/JAP/JAP_hull_breaking.png
[B] gfx/interface/ideas/JAP/JAP_i_am_tengu.png
[B] gfx/interface/ideas/JAP/JAP_iraa_split.png
[B] gfx/interface/ideas/JAP/JAP_izumo_league.png
[B] gfx/interface/ideas/JAP/JAP_kempeitai_reforms.png
[B] gfx/interface/ideas/JAP/JAP_koa_cannon.png
[B] gfx/interface/ideas/JAP/JAP_kohoda.png
[B] gfx/interface/ideas/JAP/JAP_kuniyuki_regime.png
[B] gfx/interface/ideas/JAP/JAP_lotus_sutra.png
[B] gfx/interface/ideas/JAP/JAP_mantetsu.png
[B] gfx/interface/ideas/JAP/JAP_mantetsu_collapse.png
[B] gfx/interface/ideas/JAP/JAP_maximist_japan.png
[B] gfx/interface/ideas/JAP/JAP_moving_golden_gears.png
[B] gfx/interface/ideas/JAP/JAP_nagata_shogunate.png
[B] gfx/interface/ideas/JAP/JAP_nation_agriculture_reserve.png
[B] gfx/interface/ideas/JAP/JAP_national_unity_government.png
[B] gfx/interface/ideas/JAP/JAP_national_unity_government_kazami.png
[B] gfx/interface/ideas/JAP/JAP_new_age_japanese_socialism.png
[B] gfx/interface/ideas/JAP/JAP_new_army_jsp.png
[B] gfx/interface/ideas/JAP/JAP_new_era_yak.png
[B] gfx/interface/ideas/JAP/JAP_new_esperanto.png
[B] gfx/interface/ideas/JAP/JAP_new_nationalism.png
[B] gfx/interface/ideas/JAP/JAP_no_longer_weak_premier.png
[B] gfx/interface/ideas/JAP/JAP_no_new_army_jsp.png
[B] gfx/interface/ideas/JAP/JAP_nostalgic_period.png
[B] gfx/interface/ideas/JAP/JAP_pan_asian_guidelines_1.png
[B] gfx/interface/ideas/JAP/JAP_party_seiyukai.png
[B] gfx/interface/ideas/JAP/JAP_party_split_jsp.png
[B] gfx/interface/ideas/JAP/JAP_power_secured_yakuza.png
[B] gfx/interface/ideas/JAP/JAP_raise_flag.png
[B] gfx/interface/ideas/JAP/JAP_red_army_resistance_1.png
[B] gfx/interface/ideas/JAP/JAP_repair_economy.dds
[B] gfx/interface/ideas/JAP/JAP_reserve_mobilizers.png
[B] gfx/interface/ideas/JAP/JAP_satsuma_nakano_1.png
[B] gfx/interface/ideas/JAP/JAP_separation_of_command.png
[B] gfx/interface/ideas/JAP/JAP_shogun_loyalty.png
[B] gfx/interface/ideas/JAP/JAP_shuumatsuin.png
[B] gfx/interface/ideas/JAP/JAP_social_folkdings.png
[B] gfx/interface/ideas/JAP/JAP_strengthen_government.png
[B] gfx/interface/ideas/JAP/JAP_stronger_and_more_advanced.png
[B] gfx/interface/ideas/JAP/JAP_student_unions.png
[B] gfx/interface/ideas/JAP/JAP_supremacy_of_will.png
[B] gfx/interface/ideas/JAP/JAP_tanegashima_league.png
[B] gfx/interface/ideas/JAP/JAP_the_army_and_the_people.png
[B] gfx/interface/ideas/JAP/JAP_toseiha.png
[B] gfx/interface/ideas/JAP/JAP_true_faith_ministry.png
[B] gfx/interface/ideas/JAP/JAP_tuned_blessed_sound.png
[B] gfx/interface/ideas/JAP/JAP_ultra_militarism.png
[B] gfx/interface/ideas/JAP/JAP_women.png
[B] gfx/interface/ideas/JAP/JAP_yen.png
[B] gfx/interface/ideas/JAP/JSR_cultural_revolution.png
[B] gfx/interface/ideas/JAP/JSR_dadaism.png
[B] gfx/interface/ideas/JAP/JSR_honour_martyr.png
[B] gfx/interface/ideas/JAP/JSR_party_re_construction.png
[B] gfx/interface/ideas/JAP/JSR_peasant_revolution.png
[B] gfx/interface/ideas/JAP/JSR_red_cherry_blossumss.png
[B] gfx/interface/ideas/JAP/JSR_theory_emphasis.png
[B] gfx/interface/ideas/JAP/JSR_yamakawaist_resistance.png
[B] gfx/interface/ideas/JAP/asian_revolution_jap.png
[B] gfx/interface/ideas/JAP/bop_JAP_hashimoto.png
[B] gfx/interface/ideas/JAP/bop_JAP_hayashi.png
[B] gfx/interface/ideas/JAP/bop_kenzo_no_power.png
[B] gfx/interface/ideas/JAP/bop_kenzo_some_power.png
[B] gfx/interface/ideas/JAP/bop_kenzo_total_power.png
[B] gfx/interface/ideas/JAP/bop_nakano_barely_power.png
[B] gfx/interface/ideas/JAP/bop_nakano_no_power.png
[B] gfx/interface/ideas/JAP/bop_nakano_total_power.png
[B] gfx/interface/ideas/JAP/cherry_trees.png
[B] gfx/interface/ideas/JAP/fukumotonoics.png
[B] gfx/interface/ideas/JAP/generic_agrarian_reform.png
[B] gfx/interface/ideas/JAP/global_revolution_jap.png
[B] gfx/interface/ideas/JAP/idea_JAP_I_blacksmith.png
[B] gfx/interface/ideas/JAP/idea_JAP_mitsubishi_support.png
[B] gfx/interface/ideas/JAP/idea_JAP_pan_asoianism_kita.png
[B] gfx/interface/ideas/JAP/idea_emperor_hirohito.png
[B] gfx/interface/ideas/JAP/idea_emperor_yasuhito.png
[B] gfx/interface/ideas/JAP/ikki_kita_icon.png
[B] gfx/interface/ideas/JAP/inukai_icon.png
[B] gfx/interface/ideas/JAP/jsp_left_dominant_power_icon.png
[B] gfx/interface/ideas/JAP/jsp_left_weak_power_icon.png
[B] gfx/interface/ideas/JAP/jsp_right_dominant_power_icon.png
[B] gfx/interface/ideas/JAP/jsp_right_weak_power_icon.png
[B] gfx/interface/ideas/JAP/nkvd_2.png
[B] gfx/interface/ideas/JAP/peasants_favoured.png
[B] gfx/interface/ideas/JAP/tojo_icon.png
[B] gfx/interface/ideas/JAP/writer_legacy.png
[B] gfx/interface/ideas/JAP/zaibatsu_nationalization.png
[B] gfx/interface/ideas/JSI/GFX_idea_JSI_ijn_defecting.png
[B] gfx/interface/ideas/Japan/idea_JAP_Reactionary_Plot.dds
[B] gfx/interface/ideas/Japan/idea_JAP_Republican_Terror_Legacy.dds
[B] gfx/interface/ideas/Japan/idea_JAP_Sakurakai.dds
[B] gfx/interface/ideas/KOR/KOR_Juche_Idea.png
[B] gfx/interface/ideas/KOR/KOR_Kim.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/FNG/FNG_antijapanese_sentiment.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/FNG/FNG_expel_japanese_bandits.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/FNG/FNG_japan_money.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_Kyujidai.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_Man_of_his_men.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_Nagasaki_Protocol.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_Shinjidai.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_Shitty_Tracks.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_Tokugawa_full_auth.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_Tokugawa_restored_auth.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_Tokugawa_wek_auth.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_administration_office.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_bodhisattva_spirit.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_co_prosper.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_controlling_zaibatsu.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_democracy.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_faith_inquisition.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_fallen_zaibatsu.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_fengtian_exploitation.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_golden_age.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_izumo_league.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_kohoda.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_kuniyuki_regime.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_mantetsu.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_mantetsu_collapse.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_nostalgic_period.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_raise_flag.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_separation_of_command.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_shogun_loyalty.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_shuumatsuin.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_tanegashima_league.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_toseiha.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_true_faith_ministry.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_tuned_blessed_sound.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_women.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/JAP_yen.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/companies/JAP_Ishikawajima_Heavy_Industries.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/companies/JAP_Mitsui_Zaibatsu.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/companies/JAP_Nihon_Musen.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/companies/JAP_Nippon_Electric_Company.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/companies/JAP_Nippon_Oil.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/companies/JAP_aichi.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/companies/JAP_hitachi.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/companies/JAP_isuzu.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/companies/JAP_kawanishi.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/companies/JAP_kawasaki.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/companies/JAP_kokura_arsenal.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/companies/JAP_kure_naval_arsenal.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/companies/JAP_kyushu_hikoki.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/companies/JAP_maizuru_naval_arsenal.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/companies/JAP_mitsubishi.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/companies/JAP_nagoya_arsenal.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/companies/JAP_nakajima.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/companies/JAP_nichitsu.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/companies/JAP_nissan.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/companies/JAP_osaka_army_arsenal.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/companies/JAP_sasebo_naval_arsenal.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/companies/JAP_sumitomo.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/companies/JAP_tachikawa.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/companies/JAP_tokyo_gas.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/companies/JAP_tokyo_shibaura_denki.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/companies/JAP_toyota.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/companies/JAP_yokosuka.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/JAP/companies/JAP_yokosuka_naval_arsenal.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/RUS/RUS_Relations_USA_Japan.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/Vanilla HOI4/idea_jap_duplicate_research.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/Vanilla HOI4/idea_jap_hirohito.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/Vanilla HOI4/idea_jap_ichi_go.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/Vanilla HOI4/idea_jap_interservice_rivalry_army_dominant.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/Vanilla HOI4/idea_jap_interservice_rivalry_army_strengthened.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/Vanilla HOI4/idea_jap_interservice_rivalry_balanced.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/Vanilla HOI4/idea_jap_interservice_rivalry_navy_dominant.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/Vanilla HOI4/idea_jap_interservice_rivalry_navy_strengthened.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/Vanilla HOI4/idea_jap_intervene_in_china.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/Vanilla HOI4/idea_jap_militarism_shogun.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/Vanilla HOI4/idea_jap_militarism_showa.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/Vanilla HOI4/idea_jap_supremacy_of_technology.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/Vanilla HOI4/idea_jap_supremacy_of_will.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/Vanilla HOI4/idea_jap_the_unthinkable_option.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/Vanilla HOI4/idea_jap_zaibatsu.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/Vanilla HOI4/idea_jap_zaibatsu_ally.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/Vanilla HOI4/idea_jap_zaibatsu_control.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/Vanilla HOI4/idea_tokyo_arsenal.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/ZHI/ZHI_fallen_grace_jap.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/ZHI/ZHI_japanese_backing.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/ZHI/ZHI_japanese_corps.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/ideas/idea_japanese_monopolies.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/ideas/jap_gunbatsu.png
[C | 目录 KXX_/SCB_] gfx/interface/ideas/KXX_FX_ideas/ideas/japanese_aid_cut.png
[B] gfx/interface/ideas/Kaiserreich/ANQ_fengtian_cooperationNOJAP.tga
[B] gfx/interface/ideas/Kaiserreich/FNG_expel_japanese_bandits.dds
[B] gfx/interface/ideas/Kaiserreich/FNG_expel_japanese_bandits.tga
[B] gfx/interface/ideas/Kaiserreich/FNG_japan_money.tga
[B] gfx/interface/ideas/Kaiserreich/JAP_Shitty_Tracks.dds
[B] gfx/interface/ideas/Kaiserreich/JAP_Shitty_Tracks.tga
[B] gfx/interface/ideas/Kaiserreich/JAP_co_prosper.dds
[B] gfx/interface/ideas/Kaiserreich/JAP_co_prosper.tga
[B] gfx/interface/ideas/Kaiserreich/JAP_democracy.dds
[B] gfx/interface/ideas/Kaiserreich/JAP_democracy.tga
[B] gfx/interface/ideas/Kaiserreich/JAP_economic_integration.tga
[B] gfx/interface/ideas/Kaiserreich/JAP_fengtian_exploitation.dds
[B] gfx/interface/ideas/Kaiserreich/JAP_kohoda.dds
[B] gfx/interface/ideas/Kaiserreich/JAP_mantetsu_collapse.tga
[B] gfx/interface/ideas/Kaiserreich/JAP_toseiha.dds
[B] gfx/interface/ideas/Kaiserreich/JAP_women.tga
[B] gfx/interface/ideas/Kaiserreich/JAP_yen.dds
[B] gfx/interface/ideas/Kaiserreich/JAP_yen.tga
[B] gfx/interface/ideas/Kaiserreich/idea_japanese_aid_cut.dds
[B] gfx/interface/ideas/Kaiserreich/japanese_aid_cut.tga
[B] gfx/interface/ideas/New Order/AMR_Japanese_Advisors.dds
[B] gfx/interface/ideas/New Order/GFX_idea_japan_korea_tunnel.dds
[B] gfx/interface/ideas/New Order/GFX_idea_nihon_ascendant.dds
[B] gfx/interface/ideas/New Order/PRK_Justice_of_the_Liberated.dds
[B] gfx/interface/ideas/New Order/PRK_Old_Soldiers.dds
[B] gfx/interface/ideas/New Order/PRK_To_the_Death.dds
[B] gfx/interface/ideas/New Order/idea_AST_Looming_Japanese_Empire.dds
[B] gfx/interface/ideas/New Order/idea_CHI_japans_breadbasket.dds
[B] gfx/interface/ideas/New Order/idea_CHI_slave_of_the_samurai_1.dds
[B] gfx/interface/ideas/New Order/idea_CHI_slave_of_the_samurai_2.dds
[B] gfx/interface/ideas/New Order/idea_CHI_slave_of_the_samurai_3.dds
[B] gfx/interface/ideas/New Order/idea_CHI_slave_of_the_samurai_4.dds
[B] gfx/interface/ideas/New Order/idea_CHI_slave_of_the_samurai_5.dds
[B] gfx/interface/ideas/New Order/idea_JAP_Army_Indocrination.dds
[B] gfx/interface/ideas/New Order/idea_JAP_Cult_of_the_Emperor.dds
[B] gfx/interface/ideas/New Order/idea_JAP_Military_Fanatism.dds
[B] gfx/interface/ideas/New Order/idea_japenese_administration.dds
[B] gfx/interface/ideas/PB_SNG_Japanese_Threat.dds
[B] gfx/interface/ideas/SCA/SCA_Tokyo_Steel_Works.dds
[B] gfx/interface/ideas/TAI/MING_coin.png
[B] gfx/interface/ideas/TAI/Native_influence.dds
[B] gfx/interface/ideas/TAI/Native_rebellion.dds
[B] gfx/interface/ideas/TAI/TAI_Military_Police.png
[B] gfx/interface/ideas/TAI/TAI_Morale.png
[B] gfx/interface/ideas/TAI/TAI_peoples_movement.png
[B] gfx/interface/ideas/TAI/Tai_peace.png
[B] gfx/interface/ideas/TAI/Taiwan_dispoint.png
[B] gfx/interface/ideas/TAI/companies/tai_aidc.png
[B] gfx/interface/ideas/TAI/companies/tai_ship.png
[B] gfx/interface/ideas/TAI/free_nation.dds
[B] gfx/interface/ideas/TAI/idea_chi_war_of_resistance3.dds
[B] gfx/interface/ideas/TAI/idea_generic_japanese_conflict.dds
[B] gfx/interface/ideas/TAI/imperial_glory_idea.dds
[B] gfx/interface/ideas/TAI/jewel_of_asia.dds
[B] gfx/interface/ideas/TAI/native_insur.dds
[B] gfx/interface/ideas/TAI/state_shintoism.dds
[B] gfx/interface/ideas/TAI/taiwan_indep.dds
[B] gfx/interface/ideas/TAI/taiwan_soilder.dds
[B] gfx/interface/ideas/TAI/taiwanshelp.dds
[B] gfx/interface/ideas/TAI/warrior_traditions_idea.dds
[B] gfx/interface/ideas/TAI/zhenmingtaiwan.dds
[B] gfx/interface/ideas/TWI/GFX_TWI_idea_jap_lapdongs.png
[B] gfx/interface/ideas/TWI/GFX_idea_TWI_japan_integration.png
[B] gfx/interface/ideas/TWI/TWI_fight_against_taiwanese_nationalism.png
[B] gfx/interface/ideas/ZHR/ZHR_japanese_influence.png
[B] gfx/interface/ideas/gea/GEA_attack_jap.png
[B] gfx/interface/ideas/idea_JAP_generic_land_1.dds
[B] gfx/interface/ideas/idea_JAP_generic_land_2.dds
[B] gfx/interface/ideas/idea_JAP_generic_land_3.dds
[B] gfx/interface/ideas/idea_JAP_generic_land_4.dds
[B] gfx/interface/ideas/idea_JAP_generic_land_5.dds
[B] gfx/interface/ideas/idea_JAP_generic_land_6.dds
[B] gfx/interface/ideas/idea_JAP_generic_land_7.dds
[B] gfx/interface/ideas/idea_JAP_generic_land_8.dds
[B] gfx/interface/ideas/idea_JAP_generic_land_9.dds
[B] gfx/interface/ideas/ideas/FNG_antijapanese_sentiment.png
[B] gfx/interface/ideas/ideas/FNG_expel_japanese_bandits.png
[B] gfx/interface/ideas/ideas/FNG_japan_money.png
[B] gfx/interface/ideas/ideas/JAP_Kyujidai.png
[B] gfx/interface/ideas/ideas/JAP_Man_of_his_men.png
[B] gfx/interface/ideas/ideas/JAP_Nagasaki_Protocol.png
[B] gfx/interface/ideas/ideas/JAP_Shinjidai.png
[B] gfx/interface/ideas/ideas/JAP_Shitty_Tracks.png
[B] gfx/interface/ideas/ideas/JAP_Tokugawa_full_auth.png
[B] gfx/interface/ideas/ideas/JAP_Tokugawa_restored_auth.png
[B] gfx/interface/ideas/ideas/JAP_Tokugawa_wek_auth.png
[B] gfx/interface/ideas/ideas/JAP_administration_office.png
[B] gfx/interface/ideas/ideas/JAP_bodhisattva_spirit.png
[B] gfx/interface/ideas/ideas/JAP_co_prosper.png
[B] gfx/interface/ideas/ideas/JAP_controlling_zaibatsu.png
[B] gfx/interface/ideas/ideas/JAP_democracy.png
[B] gfx/interface/ideas/ideas/JAP_faith_inquisition.png
[B] gfx/interface/ideas/ideas/JAP_fallen_zaibatsu.png
[B] gfx/interface/ideas/ideas/JAP_fengtian_exploitation.png
[B] gfx/interface/ideas/ideas/JAP_golden_age.png
[B] gfx/interface/ideas/ideas/JAP_izumo_league.png
[B] gfx/interface/ideas/ideas/JAP_kohoda.png
[B] gfx/interface/ideas/ideas/JAP_kuniyuki_regime.png
[B] gfx/interface/ideas/ideas/JAP_mantetsu.png
[B] gfx/interface/ideas/ideas/JAP_mantetsu_collapse.png
[B] gfx/interface/ideas/ideas/JAP_nostalgic_period.png
[B] gfx/interface/ideas/ideas/JAP_raise_flag.png
[B] gfx/interface/ideas/ideas/JAP_separation_of_command.png
[B] gfx/interface/ideas/ideas/JAP_shogun_loyalty.png
[B] gfx/interface/ideas/ideas/JAP_shuumatsuin.png
[B] gfx/interface/ideas/ideas/JAP_tanegashima_league.png
[B] gfx/interface/ideas/ideas/JAP_toseiha.png
[B] gfx/interface/ideas/ideas/JAP_true_faith_ministry.png
[B] gfx/interface/ideas/ideas/JAP_tuned_blessed_sound.png
[B] gfx/interface/ideas/ideas/JAP_women.png
[B] gfx/interface/ideas/ideas/JAP_yen.png
[B] gfx/interface/ideas/ideas/RUS_Relations_USA_Japan.png
[B] gfx/interface/ideas/ideas/ZHI_fallen_grace_jap.png
[B] gfx/interface/ideas/ideas/ZHI_japanese_backing.png
[B] gfx/interface/ideas/ideas/ZHI_japanese_corps.png
[B] gfx/interface/ideas/ideas/idea_japanese_aid_cut.png
[B] gfx/interface/ideas/ideas/idea_japanese_monopolies.png
[B] gfx/interface/ideas/ideas/jap_gunbatsu.png
[B] gfx/interface/ideologies/ideology_bars/antijapan.png
[B] gfx/interface/ideologies/ideology_bars/rd/antijapan.png
[B] gfx/interface/ideologies/ideology_bars/rd/japanese_militarism.png
[B] gfx/interface/ideologies/subideologies/anti_japaneseism.png
[B] gfx/interface/ideologies/subideologies/little_japan_group.png
[B] gfx/interface/ideologies/subideologies/natpop_anti_japaneseism.png
[B] gfx/interface/ideologies/subideologies/natpop_nihon_socialism_2.png
[B] gfx/interface/ideologies/subideologies/natpop_shinto_theocracy.png
[B] gfx/interface/ideologies/subideologies/npo_japanese_militarism.png
[B] gfx/interface/ideologies/subideologies/pataut_japanese_militarism.png
[B] gfx/interface/ideologies/subideologies/tot_japanese_militarism.png
[B] gfx/interface/ideologies/subideologies/tot_national_socialism_jap.png
[B] gfx/interface/ideologies/subideologies/tot_nihon_socialism_2.png
[B] gfx/interface/ideologies/subideologies/tot_shinto_theocracy.png
[B] gfx/interface/ministers/CAL/CAL_Hirohito.png
[B] gfx/interface/ministers/GXC/GXC_Taixu_hog_rso.png
[B] gfx/interface/ministers/JAP/GFX_idea_Akria_Kazami.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Aso_Hisashi_hog_tot.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Bin_Akao_eco_npo.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Buraku_Liberation_League_hog_rso.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Chikuhei_Nakajima_hog_sco.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Dai_Oishi_eco_tot.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Eisuke_Yoshiyuki_eco_rso.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Genkuro_Eto_sec_tot.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Giro_Senoo_hog_rso.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Hajime_Kawakami_for_tot.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Hatta_Shuzo_eco_rso.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Hirano_Rikizo_hog_tot.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Hiratsuka_Raicho_for_rso.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Hotsumi_Ozaki_sec_syn.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Imasu_Cho_sec_npo.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Isao_Kawada_eco_pau.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Itsuro_Sakisaka_eco_rso.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Iwane_Matsui_hog_npo.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Jiichiro_Matumoto_hog_rso.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Josei_Toda_hog_sde.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Kametaro_Mitsukawa_for_npo.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Kanichiro_Kamei_for_tot.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Kanji_Ishiwara_hog_npo.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Katsumaro_Akamatsu_hog_tot.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Kawakami_Jotaro_hog_tot.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Kazuo_Fukumoto_hog_tot.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Kazuo_Taoka_for_npo.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Kenji_Miyazawa_eco_rso.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Kingoro_Hashimoto_hog_tot.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Kisaburo_Ando_sec_npo.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Kotaro_Nakamura_sec_pau.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Kozaburo_Tachibana_hog_npo.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Kuniaki_Koiso_for_pau.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Kyuichi_Tokuda_hog_tot.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Manabu_Sano_sec_tot.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Masayoshi_Fukuda_sec_tot.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Minoru_Togo_eco_sco.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Miyamoto_Kenji_hog_rso.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Morihei_Ueshiba_eco_npo.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Nishio_Suehiro_hog_syn.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Nissho_Inoue_hog_npo.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Noboru_Yamaguchi_hog_pau.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Nosaka_Sanzo_hog_syn.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Onisaburo_Deguchi_hog_npo.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Oyama_Ikuo_hog_syn.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Ritsu_Ito_eco_tot.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Ryohei_Uchida_hog_npo.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Ryuichi_Inamura_eco_tot.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Ryutaro_Nagai_hog_sli.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Sanshiro_Ishikawa_hog_rso.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Satomi_Hakamada_eco_tot.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Seishiro_Itagaki_sec_npo.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Shigeru_Honjo_for_npo.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Shigeyoshi_Matsumae_for_tot.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Shiro_Koike_eco_tot.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Soetsu_Yanagi_for_npo.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Sumihisa_Ikeda_hog_tot.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Suzuki_Mosaburo_hog_rso.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Taisaku_Kitahara_sec_rso.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Tanabe_Shichiroku_sec_sco.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Tanaka_Chigaku_eco_npo.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Tatsuo_Tsukui_hog_tot.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Terauchi_Hisaichi_hog_pau.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Teruko_Matsuda_for_syn.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Tomoyoshi_Murayama_for_rso.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Torao_Miura_sec_npo.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Toyama_Mitsuru_hog_npo.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Toyotaro_Yuki_eco_pau.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Tsuji_Jun_hog_rso.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Tsunesaburo_Makiguchi_for_rso.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Vacant_man.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Wada_Hiroo_hog_rso.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Yamakawa_Hitoshi_hog_rso.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Yamakawa_Kikue_for_syn.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Yasaburo_Shimonaka_sec_tot.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Yasuhide_Kurihara_sec_tot.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Yasukuni_Watanabe_for_tot.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Yoshikuru_Yamana_hog_tot.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Yoshio_Kodama_hog_npo.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Yoshio_Shiga_for_tot.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_Yosuke_Matsuoka_for_pau.png
[B] gfx/interface/ministers/JAP/GFX_idea_JAP_tanabe_harumichi_sec_pau.png
[B] gfx/interface/ministers/JAP/JAP_Kametaro_Mitsukawa_hog_tot.png
[B] gfx/interface/ministers/JAP/JAP_Kaya_Okinori.png
[B] gfx/interface/ministers/JAP/JAP_Kido_Koichi.png
[B] gfx/interface/ministers/JAP/JAP_Kita_Ikki_hog_tot.png
[B] gfx/interface/ministers/JAP/JAP_Kiyose_Ichiro.png
[B] gfx/interface/ministers/JAP/JAP_Kono_Mitsu.png
[B] gfx/interface/ministers/JAP/JAP_Miwa_Juso.png
[B] gfx/interface/ministers/JAP/JAP_Muto_Akira.png
[B] gfx/interface/ministers/JAP/JAP_Nakano_Seigo.png
[B] gfx/interface/ministers/JAP/JAP_Nishida_Mitsugi.png
[B] gfx/interface/ministers/JAP/JAP_Otake_Kanichi.png
[B] gfx/interface/ministers/JAP/JAP_Ozaki_Yukio.png
[B] gfx/interface/ministers/JAP/JAP_Seki_Naohiko.png
[B] gfx/interface/ministers/JAP/JAP_Shiina_Etsusaburo.png
[B] gfx/interface/ministers/JAP/JAP_Tanahashi_Kotora.png
[B] gfx/interface/ministers/JAP/JAP_Yoshizawa_Kenkichi.png
[B] gfx/interface/ministers/TAI/TAI_Ando_Rikichi_hog_pau.png
[B] gfx/interface/ministers/TAI/TAI_Bunka_Kyokai - 副本.png
[B] gfx/interface/ministers/TAI/TAI_Bunka_Kyokai.png
[B] gfx/interface/ministers/TAI/TAI_Cai_Peihuo_eco_sde.png
[B] gfx/interface/ministers/TAI/TAI_Chen_Qichuan_eco_ade.png
[B] gfx/interface/ministers/TAI/TAI_Chen_Zhixiong_for_pau.png
[B] gfx/interface/ministers/TAI/TAI_Chiang_Wei_shui.png
[B] gfx/interface/ministers/TAI/TAI_Chiu_Chin_chuen.png
[B] gfx/interface/ministers/TAI/TAI_Cuong_De_hog_npo.png
[B] gfx/interface/ministers/TAI/TAI_Gu_Xianrong_eco_mli.png
[B] gfx/interface/ministers/TAI/TAI_Hong_Huolian_for_sco.png
[B] gfx/interface/ministers/TAI/TAI_Huang_Madian_sec_mli.png
[B] gfx/interface/ministers/TAI/TAI_Jian_Ji_hog_rso.png
[B] gfx/interface/ministers/TAI/TAI_Jiang_Weishui_hog_sde.png
[B] gfx/interface/ministers/TAI/TAI_Jingji.png
[B] gfx/interface/ministers/TAI/TAI_Kiyoshi_Hasegawa_hog_pau.png
[B] gfx/interface/ministers/TAI/TAI_Koo_Chen_fu.png
[B] gfx/interface/ministers/TAI/TAI_Koo_Hsien_jung.png
[B] gfx/interface/ministers/TAI/TAI_Lahu_Ali_for_npo.png
[B] gfx/interface/ministers/TAI/TAI_Lai_He.png
[B] gfx/interface/ministers/TAI/TAI_Lai_He_hog_rso.png
[B] gfx/interface/ministers/TAI/TAI_Lamada_Xianxian_sec_npo.png
[B] gfx/interface/ministers/TAI/TAI_Lan_Gaochuan_eco_sco.png
[B] gfx/interface/ministers/TAI/TAI_Lee_Teng_chin.png
[B] gfx/interface/ministers/TAI/TAI_Lexin_Wattan_eco_sli.png
[B] gfx/interface/ministers/TAI/TAI_Li_Chunqing_for_tot.png
[B] gfx/interface/ministers/TAI/TAI_Lian_Wenqing_hog_syn.png
[B] gfx/interface/ministers/TAI/TAI_Lien_Wenqing.png
[B] gfx/interface/ministers/TAI/TAI_Lin_Chenglu_for_sli.png
[B] gfx/interface/ministers/TAI/TAI_Lin_Dui_eco_tot.png
[B] gfx/interface/ministers/TAI/TAI_Lin_Hsiung_cheng.png
[B] gfx/interface/ministers/TAI/TAI_Lin_Mushun_eco_syn.png
[B] gfx/interface/ministers/TAI/TAI_Lin_Shao_mao.png
[B] gfx/interface/ministers/TAI/TAI_Lin_Xiantang.png
[B] gfx/interface/ministers/TAI/TAI_Lin_Xiantang_hog_sli.png
[B] gfx/interface/ministers/TAI/TAI_Lin_Xiongzheng_hog_ade.png
[B] gfx/interface/ministers/TAI/TAI_Lin_Youbang_eco_rso.png
[B] gfx/interface/ministers/TAI/TAI_Minami_Hiroshi_hog_sco.png
[B] gfx/interface/ministers/TAI/TAI_Mona_Rudao_hog_npo.png
[B] gfx/interface/ministers/TAI/TAI_Nakagawa_Kenzo_hog_mli.png
[B] gfx/interface/ministers/TAI/TAI_Neizhen.png
[B] gfx/interface/ministers/TAI/TAI_Ota_Masahiro_for_ade.png
[B] gfx/interface/ministers/TAI/TAI_Peng_Huaying.png
[B] gfx/interface/ministers/TAI/TAI_Seeqi_Tribal_Council_eco_pau.png
[B] gfx/interface/ministers/TAI/TAI_Seizo_Kobayashi_eco_pau.png
[B] gfx/interface/ministers/TAI/TAI_Sha_Sekko.png
[B] gfx/interface/ministers/TAI/TAI_Shi_Ming_hog_tot.png
[B] gfx/interface/ministers/TAI/TAI_Tong_Li_she.png
[B] gfx/interface/ministers/TAI/TAI_Tsai_Peihuo.png
[B] gfx/interface/ministers/TAI/TAI_Tu_Tsung_min.png
[B] gfx/interface/ministers/TAI/TAI_Waijiao.png
[B] gfx/interface/ministers/TAI/TAI_Wang_Qingshan_for_sli.png
[B] gfx/interface/ministers/TAI/TAI_Wang_Wande_sec_rso.png
[B] gfx/interface/ministers/TAI/TAI_Watanabe_Masanosuke_for_rso.png
[B] gfx/interface/ministers/TAI/TAI_Weng_Zesheng_for_tot.png
[B] gfx/interface/ministers/TAI/TAI_Wuyong_Yadawuyukana_hog_sli.png
[B] gfx/interface/ministers/TAI/TAI_Xie_Chunmu.png
[B] gfx/interface/ministers/TAI/TAI_Xie_Nanguang_sec_sde.png
[B] gfx/interface/ministers/TAI/TAI_Xie_Xuehong.png
[B] gfx/interface/ministers/TAI/TAI_Xie_Xuehong_hog_tot.png
[B] gfx/interface/ministers/TAI/TAI_Xu_Bing_eco_mli.png
[B] gfx/interface/ministers/TAI/TAI_Xu_Jiefu_sec_ade.png
[B] gfx/interface/ministers/TAI/TAI_Yang_Kehuang_sec_tot.png
[B] gfx/interface/ministers/TAI/TAI_Yapasuyong_Yulunana_hog_pau.png
[B] gfx/interface/ministers/TAI/TAI_Yapasuyong_Yulunana_sec_sde.png
[B] gfx/interface/ministers/TAI/TAI_Yasuhito_hog_npo.png
[B] gfx/interface/ministers/TAI/TAI_Zhou_Enlai.png
[B] gfx/interface/operatives/agencies/agency_logo_tai.dds
[B] gfx/leaders/BRG/Portrait_BRG_jap.png
[B] gfx/leaders/BRG/Portrait_Oman_Said_Ibn_Taimur.png
[B] gfx/leaders/CAL/Portrait_CAL_Hirohito.png
[B] gfx/leaders/CHL/Portrait_JAP_Tarou_Yoshihara.png
[B] gfx/leaders/CNH/Portrait_JAP_Yoshio_Nishina.png
[B] gfx/leaders/FRA/Portrait_Pierre_Taittinger.png
[B] gfx/leaders/FRG/Portrait_JAP_Sakai_Eizo.png
[B] gfx/leaders/FRG/Portrait_JAP_Taoka_Kazuo.png
[B] gfx/leaders/GXCA/Portrait_GXC_Taixu.png
[B] gfx/leaders/JAP/Portrait_JAP_Abe_Genki.png
[B] gfx/leaders/JAP/Portrait_JAP_Adachi_Kenzo_KX.png
[B] gfx/leaders/JAP/Portrait_JAP_Aikoku_Kyoto.png
[B] gfx/leaders/JAP/Portrait_JAP_Akihito.png
[B] gfx/leaders/JAP/Portrait_JAP_Akira_Kazami_suit.png
[B] gfx/leaders/JAP/Portrait_JAP_Aso_Hisashi.png
[B] gfx/leaders/JAP/Portrait_JAP_Atsushi_Akaike.png
[B] gfx/leaders/JAP/Portrait_JAP_BLLCC.png
[B] gfx/leaders/JAP/Portrait_JAP_Bin_Akao.png
[B] gfx/leaders/JAP/Portrait_JAP_Bunji_Suzuki.png
[B] gfx/leaders/JAP/Portrait_JAP_Chiba_Saburo.png
[B] gfx/leaders/JAP/Portrait_JAP_Chikuhei_Nakajima.png
[B] gfx/leaders/JAP/Portrait_JAP_Chozaburo_Mizutani.png
[B] gfx/leaders/JAP/Portrait_JAP_Daisaku Kōmoto.png
[B] gfx/leaders/JAP/Portrait_JAP_Egawa_Sakurado.png
[B] gfx/leaders/JAP/Portrait_JAP_Fang_Keguang.png
[B] gfx/leaders/JAP/Portrait_JAP_Gao_Zongwu.png
[B] gfx/leaders/JAP/Portrait_JAP_Gempo_Yamamoto.png
[B] gfx/leaders/JAP/Portrait_JAP_Giro_Senoo_KX.png
[B] gfx/leaders/JAP/Portrait_JAP_Gondou_Seikyou.png
[B] gfx/leaders/JAP/Portrait_JAP_Goto_Fumio.png
[B] gfx/leaders/JAP/Portrait_JAP_Hachiro_Arita.png
[B] gfx/leaders/JAP/Portrait_JAP_Hatoyama_Ichiro.png
[B] gfx/leaders/JAP/Portrait_JAP_Hidetsugu_Yagi.png
[B] gfx/leaders/JAP/Portrait_JAP_Hitoshi_Yamakawa_KX.png
[B] gfx/leaders/JAP/Portrait_JAP_Horikawa_Tatsukichiro.png
[B] gfx/leaders/JAP/Portrait_JAP_Hotsumi_Ozaki.png
[B] gfx/leaders/JAP/Portrait_JAP_Ikeda_Shigeaki.png
[B] gfx/leaders/JAP/Portrait_JAP_Ikuo_Oyama.png
[B] gfx/leaders/JAP/Portrait_JAP_Imao_Hirano.png
[B] gfx/leaders/JAP/Portrait_JAP_Inejiro_Asanuma.png
[B] gfx/leaders/JAP/Portrait_JAP_Inukai_Tsuyoshi.png
[B] gfx/leaders/JAP/Portrait_JAP_Ishiguro_Tadaatsu.png
[B] gfx/leaders/JAP/Portrait_JAP_Ishikawa_Sanshiro.png
[B] gfx/leaders/JAP/Portrait_JAP_Iwasaki_Koyata.png
[B] gfx/leaders/JAP/Portrait_JAP_Izawa_Takio.png
[B] gfx/leaders/JAP/Portrait_JAP_JCP_Central_Committee.png
[B] gfx/leaders/JAP/Portrait_JAP_Jiichiro_Matumoto.png
[B] gfx/leaders/JAP/Portrait_JAP_Joichi_Yamaji.png
[B] gfx/leaders/JAP/Portrait_JAP_Josei_Toda.png
[B] gfx/leaders/JAP/Portrait_JAP_Jotaro_Kawakami.png
[B] gfx/leaders/JAP/Portrait_JAP_Jun_Tsuji.png
[B] gfx/leaders/JAP/Portrait_JAP_Junnosuke_Inoue.png
[B] gfx/leaders/JAP/Portrait_JAP_Kagawa_Toyohiko.png
[B] gfx/leaders/JAP/Portrait_JAP_Kanemitsu_Tsuneo.png
[B] gfx/leaders/JAP/Portrait_JAP_Kani_Yoshio.png
[B] gfx/leaders/JAP/Portrait_JAP_Kantaro_Suzuki.png
[B] gfx/leaders/JAP/Portrait_JAP_Karasawa_Toshiki.png
[B] gfx/leaders/JAP/Portrait_JAP_Katou_Kanji.png
[B] gfx/leaders/JAP/Portrait_JAP_Katsumaro_Akamatsu.png
[B] gfx/leaders/JAP/Portrait_JAP_Kazuo_Fukumoto.png
[B] gfx/leaders/JAP/Portrait_JAP_Kazushige_Ugaki_KX.png
[B] gfx/leaders/JAP/Portrait_JAP_Keisuke_Okada_KX.png
[B] gfx/leaders/JAP/Portrait_JAP_Keisuke_Okada_civilian.png
[B] gfx/leaders/JAP/Portrait_JAP_Kenichiro_Honma.png
[B] gfx/leaders/JAP/Portrait_JAP_Kenji_Miyamoto.png
[B] gfx/leaders/JAP/Portrait_JAP_Kiichiro_Higuchi.png
[B] gfx/leaders/JAP/Portrait_JAP_Kijyuro_Shidehara.png
[B] gfx/leaders/JAP/Portrait_JAP_Kikue_Yamakawa.png
[B] gfx/leaders/JAP/Portrait_JAP_Kingoro_Hashimoto_2.png
[B] gfx/leaders/JAP/Portrait_JAP_Kishida_Masaki.png
[B] gfx/leaders/JAP/Portrait_JAP_Kishio_Satomi.png
[B] gfx/leaders/JAP/Portrait_JAP_Kita_Ikki.png
[B] gfx/leaders/JAP/Portrait_JAP_Kita_Mosley.png
[B] gfx/leaders/JAP/Portrait_JAP_Kiyoteru_Hanada.png
[B] gfx/leaders/JAP/Portrait_JAP_Kiyoteru_Hanada_Nina.png
[B] gfx/leaders/JAP/Portrait_JAP_Kobayashi_Ichizo.png
[B] gfx/leaders/JAP/Portrait_JAP_Kojiro_Fukushi.png
[B] gfx/leaders/JAP/Portrait_JAP_Kokkai.png
[B] gfx/leaders/JAP/Portrait_JAP_Konoe_Fumimaro.png
[B] gfx/leaders/JAP/Portrait_JAP_Kumazawa_Hiromichi.png
[B] gfx/leaders/JAP/Portrait_JAP_Kyuchi_Tokuda_RD_Ver.png
[B] gfx/leaders/JAP/Portrait_JAP_Liang_Hongzhi.png
[B] gfx/leaders/JAP/Portrait_JAP_Luo Junqiang.png
[B] gfx/leaders/JAP/Portrait_JAP_Manabu_Sano.png
[B] gfx/leaders/JAP/Portrait_JAP_Masamichi_Royama.png
[B] gfx/leaders/JAP/Portrait_JAP_Matsutani_Makoto.png
[B] gfx/leaders/JAP/Portrait_JAP_Minami_Jiro.png
[B] gfx/leaders/JAP/Portrait_JAP_Minami_Jiro_civilian.png
[B] gfx/leaders/JAP/Portrait_JAP_Mitsumasa_Yonai.png
[B] gfx/leaders/JAP/Portrait_JAP_Miyamoto_Yuriko.png
[B] gfx/leaders/JAP/Portrait_JAP_Miyazaki_Ryusuke.png
[B] gfx/leaders/JAP/Portrait_JAP_Mori_Tsutomu.png
[B] gfx/leaders/JAP/Portrait_JAP_Morinosuke_Kajima.png
[B] gfx/leaders/JAP/Portrait_JAP_Mosaburo_Suzuki.png
[B] gfx/leaders/JAP/Portrait_JAP_Nakano_Seigo.png
[B] gfx/leaders/JAP/Portrait_JAP_Nakayama_Tadao.png
[B] gfx/leaders/JAP/Portrait_JAP_Naoki_Hoshino.png
[B] gfx/leaders/JAP/Portrait_JAP_Nishida_Mitsugi.png
[B] gfx/leaders/JAP/Portrait_JAP_Nissho_Inoue.png
[B] gfx/leaders/JAP/Portrait_JAP_Noboru_Yamaguchi.png
[B] gfx/leaders/JAP/Portrait_JAP_Nobusuke_Kishi.png
[B] gfx/leaders/JAP/Portrait_JAP_Nobutaka_Shioden.png
[B] gfx/leaders/JAP/Portrait_JAP_Nobuyuki_Abe.png
[B] gfx/leaders/JAP/Portrait_JAP_Norihiro_Yasue.png
[B] gfx/leaders/JAP/Portrait_JAP_Oasa_Tadao.png
[B] gfx/leaders/JAP/Portrait_JAP_Obata_Toshiro.png
[B] gfx/leaders/JAP/Portrait_JAP_Ohara_Naoshi.png
[B] gfx/leaders/JAP/Portrait_JAP_Okawa_Shumei_2.png
[B] gfx/leaders/JAP/Portrait_JAP_Onisburo_Deguchi.png
[B] gfx/leaders/JAP/Portrait_JAP_Rikichi_Okamoto.png
[B] gfx/leaders/JAP/Portrait_JAP_Rikizo_Hirano.png
[B] gfx/leaders/JAP/Portrait_JAP_Roichi_Hayashi.png
[B] gfx/leaders/JAP/Portrait_JAP_Ryohei_Uchida.png
[B] gfx/leaders/JAP/Portrait_JAP_Ryutaro_Nagai.png
[B] gfx/leaders/JAP/Portrait_JAP_Saiko_Mankichi.png
[B] gfx/leaders/JAP/Portrait_JAP_Saito_Takao.png
[B] gfx/leaders/JAP/Portrait_JAP_Saneatsu_Mushanokoji.png
[B] gfx/leaders/JAP/Portrait_JAP_Sanji_Muto.png
[B] gfx/leaders/JAP/Portrait_JAP_Satokata_Takahashi.png
[B] gfx/leaders/JAP/Portrait_JAP_Shigeko_Prince_Fushimi_Hiroyasu.png
[B] gfx/leaders/JAP/Portrait_JAP_Shigemitsu_Mamoru.png
[B] gfx/leaders/JAP/Portrait_JAP_Shimada_Shigetaro.png
[B] gfx/leaders/JAP/Portrait_JAP_Shiratori_Toshio.png
[B] gfx/leaders/JAP/Portrait_JAP_Shiro_Mitamura.png
[B] gfx/leaders/JAP/Portrait_JAP_Shumpachi_Hojo.png
[B] gfx/leaders/JAP/Portrait_JAP_Suehiko_Shiono.png
[B] gfx/leaders/JAP/Portrait_JAP_Suiheisha.png
[B] gfx/leaders/JAP/Portrait_JAP_Sumihisa_Ikeda.png
[B] gfx/leaders/JAP/Portrait_JAP_Suzuki_Kisaburo.png
[B] gfx/leaders/JAP/Portrait_JAP_Tadamasa_Sakai.png
[B] gfx/leaders/JAP/Portrait_JAP_Taisaku_Kitahara.png
[B] gfx/leaders/JAP/Portrait_JAP_Tanzan_Ishibashi.png
[B] gfx/leaders/JAP/Portrait_JAP_Taoka_Kazuo.png
[B] gfx/leaders/JAP/Portrait_JAP_Tatsuo_Tsukui.png
[B] gfx/leaders/JAP/Portrait_JAP_Teiichi_Suzuki.png
[B] gfx/leaders/JAP/Portrait_JAP_Tempu_Nakamura.png
[B] gfx/leaders/JAP/Portrait_JAP_Tokugawa_Iesato_KX.png
[B] gfx/leaders/JAP/Portrait_JAP_Tokugawa_Kuniyuki.png
[B] gfx/leaders/JAP/Portrait_JAP_Tokugawa_Yoshichika.png
[B] gfx/leaders/JAP/Portrait_JAP_Tokutomi_Soho.png
[B] gfx/leaders/JAP/Portrait_JAP_Tomito_Izu.png
[B] gfx/leaders/JAP/Portrait_JAP_Tomozo_Ogawa.png
[B] gfx/leaders/JAP/Portrait_JAP_Tsunesaburo_Makiguchi.png
[B] gfx/leaders/JAP/Portrait_JAP_Tsurumi_Yusuke.png
[B] gfx/leaders/JAP/Portrait_JAP_Yamaguchi_Einosuke.png
[B] gfx/leaders/JAP/Portrait_JAP_Yamamoto_Kenzo.png
[B] gfx/leaders/JAP/Portrait_JAP_Yamamoto_Senji.png
[B] gfx/leaders/JAP/Portrait_JAP_Yamazaki_Tatsunosuke.png
[B] gfx/leaders/JAP/Portrait_JAP_Yasaburo_Shimonaka.png
[B] gfx/leaders/JAP/Portrait_JAP_Yojiro_Matsutani.png
[B] gfx/leaders/JAP/Portrait_JAP_Yoshihito_Kuahara.png
[B] gfx/leaders/JAP/Portrait_JAP_Yoshikuru_Yamana.png
[B] gfx/leaders/JAP/Portrait_JAP_Yoshimichi_Hara.png
[B] gfx/leaders/JAP/Portrait_JAP_Yoshio_Kodama.png
[B] gfx/leaders/JAP/Portrait_JAP_Yoshisuke_Aikawa.png
[B] gfx/leaders/JAP/Portrait_JAP_Yosuke_Matsuoka.png
[B] gfx/leaders/JAP/Portrait_JAP_Yukio_Ozaki.png
[B] gfx/leaders/JAP/Portrait_JAP_Zaibatsu_council.png
[B] gfx/leaders/JAP/Portrait_JAP_kodoha.png
[B] gfx/leaders/JAP/Portrait_Two_Kozaburo_Tachibana.png
[B] gfx/leaders/JAP/Portriat_JAP_Mitsumasa_Yonai.png
[B] gfx/leaders/JAP/Portriat_JAP_Suehiro_Nishio.png
[B] gfx/leaders/JSR/Portrait_JSR_Taisaku_Kitahara.png
[B] gfx/leaders/TUV/Portrait_TIB_Sanggyi_Yuexi.png
[B] gfx/leaders/TUV/Portrait_TIB_Zhang_Baohua.png
[B] gfx/leaders/TUV/Portrait_TIB_ngapoi_ngawang_jigme_2.png
[B] gfx/leaders/TWI/Portrait_JAP_Minami_Hiroshi.png
[B] gfx/leaders/TWI/Portrait_JAP_Nakagawa_Kenzo.png
[B] gfx/leaders/TWI/Portrait_JAP_Rikichi_Ando.png
[B] gfx/leaders/TWI/Portrait_TAI_Jian_Ji.png
[B] gfx/leaders/TWI/Portrait_TAI_Lai_He.png
[B] gfx/leaders/TWI/Portrait_TAI_Lian_Wenqing.png
[B] gfx/leaders/TWI/Portrait_TAI_Shi_ming.png
[B] gfx/leaders/TWI/Portrait_TWI_Taiwan_Sōtoku.png
[B] gfx/leaders/TWI/Portrait_Tai_San_tho.png
[B] gfx/leaders/TWI/TAI_Portrait_liao_wenkui.png
[B] gfx/leaders/TWI/TAI_portrait_jiang_weishui.png
[B] gfx/leaders/TWI/TAI_portrait_lin_xiantang.png
[B] gfx/leaders/TWI/TAI_portrait_lin_xiongzheng.png
[B] gfx/leaders/TWI/TAI_portrait_xie_xuehong.png
[B] gfx/leaders/YUN/Portrait_KOR_Kim_Il_Sung.png
[B] gfx/super_events/GFX_SPEVNT_JAPAN_CW_Commie.png
[B] gfx/super_events/GFX_SPEVNT_JAPAN_CW_army.png
[B] gfx/super_events/GFX_SPEVNT_TAIWAN_COMMIE_UNITE_CHINA.png
[B] gfx/super_events/GFX_SPEVNT_TAIWAN_TPP_UNITE_CHINA.png
[B] gfx/super_events/GFX_SPEVNT_TAIWAN_XIONGZHENG_UNITE_CHINA.png
[B] gfx/super_events/SPEVNT_German_Japanese_War.png
[B] gfx/super_events/SPEVNT_Korean_Revolt (2).png
[B] gfx/super_events/SPEVNT_Korean_Revolt.png
[B] gfx/super_events/SPEVNT_Russo_Japanese_War.png
[B] gfx/super_events/Super_Event_Image_SPEVNT_JAPAN_CW.png
[C | JAP - Japan.txt] history/countries/JAP - Japan.txt
[B] history/countries/JOK - Hokkaido.txt
[B] history/countries/TAI - Taiwan.txt
[B] history/states/524-Taipei.txt
[B] history/units/JAP.txt
[B] history/units/JAP_revolution.txt
[B] history/units/JCW_hokkaido_military.txt
[C | 含 Socialist 字样] history/units/JCW_hokkaido_socialist.txt
[B] history/units/TAI - Colonial Garrison.txt
[B] interface/JAP_parliament_gui.gfx
[B] interface/JAP_parliament_gui.gui
[C | 文件名 KXX_/SCB_ 前缀] interface/KXX_JAP_event_pictures.gfx
[C | 文件名 KXX_/SCB_ 前缀] interface/KXX_JAP_ideas.gfx
[C | 文件名 KXX_/SCB_ 前缀] interface/KXX_JAP_ideologies.gfx
[A+B] interface/RD_Japan_Ministers.gfx
[A+B] interface/RD_Japan_Rework_decisions.gfx
[A+B] interface/RD_Japan_Rework_ideas.gfx
[A+B] interface/RD_Japan_event_pictures.gfx
[A] interface/RD_Lu_xun_ministers.gfx
[A] interface/RD_PHI_ideas.gfx
[A] interface/RD_Philippines_Focus_Icons.gfx
[A] interface/RD_Philippines_ideas.gfx
[A] interface/RD_Shanxi_ministers.gfx
[A] interface/RD_Southern_Warlords_ideas.gfx
[A] interface/RD_TWI_event_pictures.gfx
[A] interface/RD_TWI_ideas.gfx
[A+B] interface/RD_Taiwan_Ministers.gfx
[A+B] interface/RD_Taiwan_ideas.gfx
[A] interface/RD_VNQ_ideas.gfx
[A] interface/RD_decisions.gfx
[A] interface/RD_event_pictures.gfx
[A] interface/RD_game_rules.gfx
[A] interface/RD_game_rules_flags.gfx
[A] interface/RD_ideas.gfx
[A] interface/RD_ideology_picture.gfx
[A] interface/RD_lu_xun_decisions.gfx
[A] interface/RD_lu_xun_ideas.gfx
[A] interface/RD_ministers.gfx
[A] interface/RD_traits.gfx
[B] interface/TAI_goals.gfx
[B] interface/TAI_goals_shine.gfx
[B] interface/TAI_ministers.gfx
[A] interface/focus-AJPSEIYUKAITWO_customicons.gfx
[A] interface/focus-CAMCOMUNIE_customicons.gfx
[A] interface/focus-CAMDEMSOC_customicons.gfx
[A+B] interface/focus-CAMJAP_customicons.gfx
[A] interface/focus-CAMMIL_customicons.gfx
[A] interface/focus-CAMMON_customicons.gfx
[A] interface/focus-CHINA_FOREIGN_POLICY_customicons.gfx
[A] interface/focus-CHI_customicons.gfx
[A] interface/focus-CMC_customicons.gfx
[A] interface/focus-CNHBOL_customicons.gfx
[A] interface/focus-CNH_GUOMON_customicons.gfx
[A] interface/focus-CNH_customicons.gfx
[A] interface/focus-CYU_customicons.gfx
[A] interface/focus-DSY_customicons.gfx
[A] interface/focus-DUX_customicons.gfx
[A] interface/focus-GXCECON_customicons.gfx
[A] interface/focus-GXC_customicons.gfx
[A] interface/focus-HEL_customicons.gfx
[A] interface/focus-HKP_customicons.gfx
[A] interface/focus-ICONONE_customicons.gfx
[A+B] interface/focus-JAPAKAO_customicons.gfx
[A+B] interface/focus-JAPANA_customicons.gfx
[A+B] interface/focus-JAPARAKI_customicons.gfx
[A+B] interface/focus-JAPARMY_customicons.gfx
[A+B] interface/focus-JAPCOMMUNIST_customicons.gfx
[A+B] interface/focus-JAPDOMEITWO_customicons.gfx
[A+B] interface/focus-JAPECON_customicons.gfx
[A+B] interface/focus-JAPFOR_customicons.gfx
[A+B] interface/focus-JAPIRAARIGHTIST_customicons.gfx
[A+B] interface/focus-JAPIRAA_customicons.gfx
[A+B] interface/focus-JAPKOKUMIN_customicons.gfx
[A+B] interface/focus-JAPKONOE_customicons.gfx
[A+B] interface/focus-JAPKOZA_customicons.gfx
[A+B] interface/focus-JAPLEFTIRAA_customicons.gfx
[A+B] interface/focus-JAPLIB_customicons.gfx
[A+B] interface/focus-JAPMILICIVIL_customicons.gfx
[A+B] interface/focus-JAPMINSEITOTWO_customicons.gfx
[A+B] interface/focus-JAPNAK_customicons.gfx
[A+B] interface/focus-JAPNICH_customicons.gfx
[A+B] interface/focus-JAPPAN_customicons.gfx
[A+B] interface/focus-JAPRECOVERY_customicons.gfx
[A+B] interface/focus-JAPSEI_customicons.gfx
[A+B] interface/focus-JAPSOCDEM_customicons.gfx
[A+B] interface/focus-JAPSOCIALISM_customicons.gfx
[A+B] interface/focus-JAPTAISHUTOTWO_customicons.gfx
[A+B] interface/focus-JAPTOSEIHA_customicons.gfx
[A+B] interface/focus-JAPVINJAP_customicons.gfx
[A+B] interface/focus-JAP_BLACKDRAG_customicons.gfx
[A+B] interface/focus-JAP_ELECTION_customicons.gfx
[A+B] interface/focus-JAP_SOCFOR_customicons.gfx
[A+B] interface/focus-JAP_YAKUZA_customicons.gfx
[A+B] interface/focus-JAP_customicons.gfx
[A+B] interface/focus-KORJUCHE_customicons.gfx
[A] interface/focus-LAOCOM_customicons.gfx
[A] interface/focus-LAOREB_customicons.gfx
[A] interface/focus-LECFOR_customicons.gfx
[A] interface/focus-LECQUIBAI_customicons.gfx
[A] interface/focus-LUXUN_customicons.gfx
[A] interface/focus-PHI_customicons.gfx
[A] interface/focus-QIE_customicons.gfx
[A] interface/focus-RDHNNICONTWO_customicons.gfx
[A] interface/focus-RDHNNKMTUNI_customicons.gfx
[A+B] interface/focus-RDSOCJAP_customicons.gfx
[A] interface/focus-SHX_customicons.gfx
[A] interface/focus-SQITWO_customicons.gfx
[A] interface/focus-SQI_customicons.gfx
[A] interface/focus-SZC_customicons.gfx
[A+B] interface/focus-TAIECONO_customicons.gfx
[A+B] interface/focus-TAIMON_customicons.gfx
[A+B] interface/focus-TAISOC_customicons.gfx
[A+B] interface/focus-TAI_customicons.gfx
[A] interface/focus-TECHAUTHCNH_customicons.gfx
[A] interface/focus-TECHNATECHINA_customicons.gfx
[A] interface/focus-TEH_customicons.gfx
[A] interface/focus-TIA_customicons.gfx
[A+B] interface/focus-TIB_customicons.gfx
[A] interface/focus-TRMKOR_customicons.gfx
[A] interface/focus-TWI_customicons.gfx
[A+B] interface/focus-VIETJAP_customicons.gfx
[A] interface/focus-VININC_GIAP_customicons.gfx
[A] interface/focus-VNQ_2_customicons.gfx
[A] interface/focus-VNQ_customicons.gfx
[A] interface/focus-WANGHONGWEN_customicons.gfx
[A] interface/focus-XSM_customicons.gfx
[A] interface/focus-YUNJUCHE_customicons.gfx
[A+B] interface/focus-ZAIJAP_customicons.gfx
[A] interface/focus-ZHA_customicons.gfx
[A] interface/focus-ZHU_customicons.gfx
[B] interface/japan_china_influence_scripted_gui.gui
[B] interface/japan_china_influence_scripted_gui_graphics.gfx
[B] interface/japan_popularity_scripted_gui.gui
[B] interface/japan_popularity_scripted_gui_graphics.gfx
[B] interface/rework_JAP_goal.gfx
[B] interface/rework_JAP_goal_shine.gfx
[B] interface/rework_JAP_ideas.gfx
[B] interface/tai_event.gfx
[B] localisation/FX_Japan_l_simp_chinese.yml
[B] localisation/Japan_diet_gui_l_simp_chinese.yml
[B] localisation/KR_Japan_l_simp_chinese.yml
[C | 文件名 KXX_/SCB_ 前缀] localisation/KXX_JAP_Expand_l_simp_chinese.yml
[C | 文件名 KXX_/SCB_ 前缀] localisation/KXX_JAP_rework_ideas_l_simp_chinese.yml
[B] localisation/Nippon_Taiheiyosenso_l_simp_chinese.yml
[A] localisation/RD_00_Political_l_simp_chinese.yml
[A] localisation/RD_Game_Rules_l_simp_chinese.yml
[A] localisation/RD_Guides_l_simp_chinese.yml
[A+B] localisation/RD_JAP_rework_l_simp_chinese.yml
[A+B] localisation/RD_Japan_Kodoha_l_simp_chinese.yml
[A] localisation/RD_Qiongya_l_simp_chinese.yml
[A] localisation/RD_Shanghai_Commune_l_simp_chinese.yml
[A] localisation/RD_South_Seas_Territory_l_simp_chinese.yml
[A+B] localisation/RD_Taiwan_l_simp_chinese.yml
[B] localisation/RF_Korea_l_simp_chinese.yml
[C | 文件名 KXX_/SCB_ 前缀] localisation/SCB_JAP_Expand_l_simp_chinese.yml
[B] localisation/TAI_l_simp_chinese.yml
[B] localisation/english/replace/KR_Japan_l_english.yml
[B] localisation/english/replace/KR_Taiwan l_english.yml
[B] localisation/focustree_camjap_l_simp_chinese.yml
[B] localisation/focustree_jap-military_l_simp_chinese.yml
[B] localisation/focustree_jap-toseiha_l_simp_chinese.yml
[B] localisation/focustree_japan-anarchist_l_simp_chinese.yml
[B] localisation/focustree_japan-black-dragon-society_l_simp_chinese.yml
[B] localisation/focustree_japan-commmunist_l_simp_chinese.yml
[B] localisation/focustree_japan-economy-recovery_l_simp_chinese.yml
[B] localisation/focustree_japan-election_l_simp_chinese.yml
[B] localisation/focustree_japan-foreign_l_simp_chinese.yml
[B] localisation/focustree_japan-iraa-focus_l_simp_chinese.yml
[B] localisation/focustree_japan-iraa-konoe_l_simp_chinese.yml
[B] localisation/focustree_japan-iraa-rightist_l_simp_chinese.yml
[B] localisation/focustree_japan-left-iraa_l_simp_chinese.yml
[B] localisation/focustree_japan-military-civilwar_l_simp_chinese.yml
[B] localisation/focustree_japan-minseito-two_l_simp_chinese.yml
[B] localisation/focustree_japan-nakano_l_simp_chinese.yml
[B] localisation/focustree_japan-pan-asianist_l_simp_chinese.yml
[B] localisation/focustree_japan-revolution_l_simp_chinese.yml
[B] localisation/focustree_japan-seiyukai-1940_l_simp_chinese.yml
[B] localisation/focustree_japan-seiyukai_l_simp_chinese.yml
[C | 含 Socialist 字样] localisation/focustree_japan-socialist-economy_l_simp_chinese.yml
[C | 含 Socialist 字样] localisation/focustree_japan-socialist-fp-tree_l_simp_chinese.yml
[B] localisation/focustree_korea-juche-expansion_l_simp_chinese.yml
[B] localisation/focustree_minseito-japan_l_simp_chinese.yml
[B] localisation/focustree_nichiren-japan_l_simp_chinese.yml
[B] localisation/focustree_shakai-taishuto-two_l_simp_chinese.yml
[B] localisation/focustree_socdem-japan_l_simp_chinese.yml
[B] localisation/focustree_socialist-tibet_l_simp_chinese.yml
[B] localisation/focustree_taiwan-economic-foreign-tree_l_simp_chinese.yml
[B] localisation/focustree_taiwan-japan-monarchy_l_simp_chinese.yml
[B] localisation/focustree_taiwan-socialist_l_simp_chinese.yml
[B] localisation/focustree_taiwan-tree_l_simp_chinese.yml
[B] localisation/focustree_taiwan-wushe_l_simp_chinese.yml
[B] localisation/focustree_taiwan_l_simp_chinese.yml
[B] localisation/focustree_viet-jap_l_simp_chinese.yml
[B] localisation/focustree_vietjapjap_l_simp_chinese.yml
[B] localisation/focustree_yakuza-japan_l_simp_chinese.yml
[B] localisation/l_simp_chinese/RF_Taiwan_l_simp_chinese.yml
[B] sound/menu/japan_imperial_march.wav
[B] sound/menu/japan_may_day_march.wav
[B] sound/menu/song_of_the_seven_sons_taiwan.wav
```
