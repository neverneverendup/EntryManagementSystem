# category = '''
# {
#  "人物":
#  {
#   "各职业人物":{
#     "人类学家", "哲学家", "地理学家", "思想家", "性学家", "民俗学家", "美学家", "艺术史学家", "语言学家", "宗教人物"，
#     "神学家", "宇航员", "工程师", "建筑师", "机械学家", "水利学家", "发明家", "程序员", "飞行员",
#     "君主", "外交官", "政治人物", "社会运动者", "军事人物", "革命家", "作家", "翻译家", "词人", "诗人", "服装设计师",
#     "模特", "动画师", "漫画家", "游戏设计师", "艺术总监", "陶艺家", "雕刻家", "魔术师", "厨师", "调酒师", "商人", "收藏家",
#     "工业设计师", "书法家", "画家", "雕塑家", "摄影师", "作曲家", "指挥家", "歌手", "音乐制作人", "音乐家", "演员", "舞者",
#     "导演", "音效师", "主持人", "主播", "编辑", "配音员", "历史学家", "图书馆学家", "教育家", "社会学家", "经济学家",
#     "考古学家", "金融家", "农学家", "化学家", "地质学家", "天文学家", "数学家", "物理学家", "生物学家", "计算机科学家",
#     "医学家", "医生", "运动员", "裁判员", "电影人", "律师", "法官"
#      },
#   "特殊人物":{
#     "罪犯", "烈士", "司法人物", "神话人物", "虚构角色"
#     },
#  }
#  "休闲":
#  {
#   "活动":{
#    "旅游", "漫画", "锻练", "烹饪", "收藏", "园艺", "摄影", "宠物", "展览"
#   },
#   "娱乐":{
#    "电影", "电视剧", "综艺节目", "广播"
#   },
#   "制品":{
#    "玩具"
#   },
#  }
#  "历史":
#  {
#   "历史著作":{
#    "历史书籍"
#   },
#   "历史概念":{
#    "历史学", "年代"
#   },
#   "考古学",
#   "世界史",
#   "传说",
#  }
#  "司法":
#  {
#   "法律", "司法制度", "司法组织", "案件"
#  }
#  "哲学":
#  {
#   "逻辑", "伦理学", "哲学问题", "哲学概念"
#  }
#  "地理":
#  {
#   "地理学", "国家", "城市", "地图", "时区", "方位", "地区", "地形", "气候", "土壤", "河流", "山"
#  }
#  "宗教":
#  {
#   "佛教", "基督教", "伊斯兰教", "道教"
#  }
#  "心理学",
#  "文学":
#  {
#   "修辞",
#   "文学体裁":
#   {
#    "小说", "散文", "论文", "文言文", "白话文", "戏剧", "诗歌", "儿童文学", "传记"
#   },
#   "文学奖",
#   "文学组织",
#   "作家协会",
#   "传播类型":
#   {
#    "杂志", "报纸"
#   }
#  }
#  "物质":
#  {
#   "化学元素",
#   "混合物":
#   {
#    "合金", "溶液", "玻璃"
#   },
#   "纯净物":
#   {
#    "酸", "碱", "盐"
#   },
#   "金属",
#   "暗物质",
#   "黑洞"
#  }
#  "社会":
#  {
#   "交通":
#   {
#    "交通工具",
#    "航空":
#    {
#     "航空器", "航天器", "航空公司", "机场"
#    },
#    "公路":
#    {
#     "汽车", "汽车品牌"
#    },
#    "铁路":
#    {
#     "铁路公司", "铁路车站", "铁路线"
#    },
#   },
#   "军事":
#   {
#    "军事组织",
#    "军事装备":
#    {
#     "武器":
#     {
#      "枪械", "导弹", "坦克", "军舰"
#    },
#    "战争"
#   },
#   "教育":
#   {
#    "大学", "考试"
#   },
#   "文化":
#   {
#    "节日", "语言"
#   },
#   "生活":
#   {
#    "服装",
#    "美容"
#   },
#   "经济":{
#    "财政", "贸易", "管理学", "经济学"
#   }
#  },
#  "科学":
#  {
#   "科学组织", "科学竞赛"
#  },
#  "技术"
#  "艺术":
#  {
#   "雕塑作品", "绘画作品", "陶瓷", "舞蹈作品", "书法作品", "乐器", "舞蹈", "歌曲", "音乐奖项"
#  }
#  "自然":
#  {
#   "动物", "植物"
#  }
# }
# '''
# category = category.replace("\n","").replace(" ","").replace("\"\"","\",\"").replace("，",",").replace("}\"","},\"").replace("},}","}}").replace("\",","\":\"\",").replace("\"}","\":\"\"}").replace("\",}","\"}")
# print(category)
a = {
	"人物":{
		"各职业人物":{
			"人类学家":"",
			"哲学家":"",
			"地理学家":"",
			"思想家":"",
			"性学家":"",
			"民俗学家":"",
			"美学家":"",
			"艺术史学家":"",
			"语言学家":"",
			"宗教人物":"",
			"神学家":"",
			"宇航员":"",
			"工程师":"",
			"建筑师":"",
			"机械学家":"",
			"水利学家":"",
			"发明家":"",
			"程序员":"",
			"飞行员":"",
			"君主":"",
			"外交官":"",
			"政治人物":"",
			"社会运动者":"",
			"军事人物":"",
			"革命家":"",
			"作家":"",
			"翻译家":"",
			"词人":"",
			"诗人":"","服装设计师":"",
			"模特":"","动画师":"","漫画家":"",
			"游戏设计师":"","艺术总监":"","陶艺家":"",
			"雕刻家":"","魔术师":"","厨师":"","调酒师":"",
			"商人":"","收藏家":"","工业设计师":"","书法家":"",
			"画家":"","雕塑家":"","摄影师":"","作曲家":"","指挥家":"",
			"歌手":"","音乐制作人":"","音乐家":"","演员":"","舞者":"",
			"导演":"","音效师":"","主持人":"","主播":"","编辑":"",
			"配音员":"","历史学家":"","图书馆学家":"","教育家":"",
			"社会学家":"","经济学家":"","考古学家":"","金融家":"",
			"农学家":"","化学家":"","地质学家":"","天文学家":"",
			"数学家":"","物理学家":"","生物学家":"","计算机科学家":"",
			"医学家":"","医生":"","运动员":"","裁判员":"",
			"电影人":"","律师":"",
			"法官":""
		},
		"特殊人物":{
			"罪犯":"","烈士":"","司法人物":"","神话人物":"","虚构角色":""
		}
	},
	"休闲":{
		"活动":{
			"旅游":"","漫画":"","锻练":"","烹饪":"","收藏":"","园艺":"","摄影":"","宠物":"","展览":""
		},
		"娱乐":{
			"电影":"","电视剧":"","综艺节目":"","广播":""
		},
		"制品":{
			"玩具":""
		}
	},
	"历史":{
		"历史著作":{
			"历史书籍":""
		},
		"历史概念":{
			"历史学":"","年代":""
		},
		"考古学":"",
		"世界史":"",
		"传说":""
	},
	"司法":{
		"法律":"","司法制度":"","司法组织":"","案件":""
	},
	"哲学":{
		"逻辑":"","伦理学":"","哲学问题":"","哲学概念":""
	},
	"地理":{
		"地理学":"","国家":"","城市":"","地图":"","时区":"","方位":"","地区":"","地形":"","气候":"","土壤":"","河流":"","山":""
	},
	"宗教":{
		"佛教":"","基督教":"","伊斯兰教":"","道教":""
	},
	"心理学":"",
	"文学":{
		"修辞":"",
		"文学体裁":{
			"小说":"","散文":"","论文":"","文言文":"","白话文":"","戏剧":"","诗歌":"","儿童文学":"","传记":""
		},
		"文学奖":"",
		"文学组织":"",
		"作家协会":"",
		"传播类型":{
			"杂志":"","报纸":""
		}
	},
	"物质":{
		"化学元素":"",
		"混合物":{
			"合金":"","溶液":"","玻璃":""
		},
		"纯净物":{
			"酸":"","碱":"","盐":""
		},
		"金属":"","暗物质":"","黑洞":""
	},
	"社会":{
		"交通":{
			"交通工具":"",
			"航空":{
				"航空器":"","航天器":"","航空公司":"","机场":""
			},
			"公路":{
				"汽车":"","汽车品牌":""
			},
			"铁路":{
				"铁路公司":"","铁路车站":"","铁路线":""
			}
		},
		"军事":{
			"军事组织":"",
			"军事装备":{
				"武器":{
					"枪械":"","导弹":"","坦克":"","军舰":""
				},
				"战争":""
			},
			"教育":{
				"大学":"","考试":""
			},
			"文化":{
				"节日":"","语言":""
			},
			"生活":{
				"服装":"","美容":""
			},
			"经济":{
				"财政":"","贸易":"","管理学":"","经济学":""
			}
		},
		"科学":{
			"科学组织":"","科学竞赛":""
		},
		"技术":"",
		"艺术":{
			"雕塑作品":"",
			"绘画作品":"",
			"陶瓷":"",
			"舞蹈作品":"","书法作品":"","乐器":"","舞蹈":"","歌曲":"","音乐奖项":""
		},
		"自然":{
			"动物":"","植物":""
		}
	}
}
def handler(d):
	if type(d)==dict:
		k = []
		for key,value in d.items():
			tmp = {}
			tmp["value"] = key
			tmp['label'] = key
			#print(key,value)
			children = handler(value)
			if children:
				tmp["children"] = children
			k.append(tmp)
		return k
	else:
		return []


result = handler(a)
print(result)