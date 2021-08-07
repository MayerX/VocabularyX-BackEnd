# VocabularyX-BackEnd

# Entities

## WordList

```typescript
interface WordList {
    id: string,
    name: string,
    create_time: Date,
    update_time: Date,
    word_count: int
}
```

## Plan

```typescript
interface Plan {
    id: string,
    name: string,
    start_time: Date,
    end_time: Date
    duration: int    
}
```

## Section

```typescript
{
    id: string,
    plan_id: string,
    index: int,
    count: int,
    duration: int
}
```

# API 

## `/w/:id`

### GET 请求

用户查看单个单词的各种解释说明

- 请求参数

| 参数名 | 类型   | 说明   |
| ------ | ------ | ------ |
| id     | string | 单词ID |

- 返回数据

```json
{
    "words": {
        "id": "8eccfbb2c8",
        "spell": "soup",
        "pos": [
            {
                "type": "n",
                "definition": "汤，羹；马力"
            },
            {
                "type": "vt",
                "definition": "加速；增加马力"
            }
        ],
        "cn_etym": null,
        "en_etym": null,
        "sentence": null,
        "phonetic": [
            "suːp",
            "suːp"
        ],
        "word_forms": [
            {
                "name": "复数",
                "value": "soups"
            },
            {
                "name": "过去式",
                "value": "souped"
            },
            {
                "name": "过去分词",
                "value": "souped"
            },
            {
                "name": "现在分词",
                "value": "souping"
            },
            {
                "name": "第三人称单数",
                "value": "soups"
            }
        ],
        "audio_sources": [
            "http://openapi.youdao.com/ttsapi?q=soup&langType=en&sign=45C89EA84E202ECC3BE3D18D80E86E28&salt=1613654689337&voice=6&format=mp3&appKey=2423360539ba5632&ttsVoiceStrict=false",
            "http://openapi.youdao.com/ttsapi?q=soup&langType=en&sign=45C89EA84E202ECC3BE3D18D80E86E28&salt=1613654689337&voice=5&format=mp3&appKey=2423360539ba5632&ttsVoiceStrict=false"
        ],
        "updated": 1,
        "raw": null,
        "parsed": 1
    },
    "msg": "succeed"
}
```

### ~~POST 请求~~ [延后]

添加单词

- 请求参数

| 参数名           | 类型   | 说明 |
| ---------------- | ------ | ---- |
| spell            | string | 单词 |
| 除了ID的所有属性 | …      | …    |

- 返回数据

```json
 {
     "id": string,
     "spell": string,
  ...  // all word properties
 }
```

## `/ws/:id`

### GET请求

用户查看单个单词的各种解释说明

- 请求参数

| 参数名 | 类型   | 说明   |
| ------ | ------ | ------ |
| spell  | string | 单词ID |

- 返回数据

```json
 {
     "id": string,
     "spell": string,
  ...  // all word properties
 }
```

## `/s:id`

### GET 请求

用户搜索单词

- 请求参数

| 参数名   | 类型   | 说明     |
| -------- | ------ | -------- |
| fragment | string | 单词部分 |

- 返回数据

```json
{
  "words": [
        {
            "id": "d4b9775b84",
            "spell": "liken",
            "pos": null,
            "cn_etym": null,
            "en_etym": null,
            "sentence": null,
            "phonetic": null,
            "word_forms": null,
            "audio_sources": null,
            "updated": 1,
            "raw": "{\"exam_type\": [\"IELTS\", \"GRE\"], \"us-phonetic\": \"\ˈla\ɪk\ən\", \"phonetic\": \"\ˈla\ɪk\ən\", \"uk-phonetic\": \"\ˈla\ɪk\ən\", \"wfs\": [{\"wf\": {\"name\": \"\过\去\式\", \"value\": \"likened\"}}, {\"wf\": {\"name\": \"\过\去\分\词\", \"value\": \"likened\"}}, {\"wf\": {\"name\": \"\现\在\分\词\", \"value\": \"likening\"}}, {\"wf\": {\"name\": \"\第\三\人\称\单\数\", \"value\": \"likens\"}}], \"uk-speech\": \"http://openapi.youdao.com/ttsapi?q=liken&langType=en&sign=E0404242794690CB791D7B5C6EA803AC&salt=1613664765117&voice=5&format=mp3&appKey=2423360539ba5632&ttsVoiceStrict=false\", \"explains\": [\"vt. \比\拟\；\把\…\比\作\"], \"us-speech\": \"http://openapi.youdao.com/ttsapi?q=liken&langType=en&sign=E0404242794690CB791D7B5C6EA803AC&salt=1613664765117&voice=6&format=mp3&appKey=2423360539ba5632&ttsVoiceStrict=false\"}",
            "parsed": 0
        },
        {
            "id": "3e4d3f4b85",
            "spell": "likely",
            "pos": null,
            "cn_etym": null,
            "en_etym": null,
            "sentence": null,
            "phonetic": null,
            "word_forms": null,
            "audio_sources": null,
            "updated": 1,
            "raw": "{\"returnPhrase\":[\"likely\"],\"query\":\"likely\",\"errorCode\":\"0\",\"l\":\"en2zh-CHS\",\"tSpeakUrl\":\"http://openapi.youdao.com/ttsapi?q=%E5%8F%AF%E8%83%BD&langType=zh-CHS&sign=46228C72799308E30F3575542138C4A4&salt=1613701588412&voice=4&format=mp3&appKey=0295d75ab7c75b27&ttsVoiceStrict=false\",\"web\":[{\"value\":[\"可能的\",\"很可能的\",\"有希望的\",\"预期的\"],\"key\":\"likely\"},{\"value\":[\"等可能\",\"均相等\",\"等年夜概\"],\"key\":\"Equally likely\"},{\"value\":[\"大概\",\"也许\",\"最可能\",\"很可能\"],\"key\":\"most likely\"}],\"requestId\":\"bddbd066-7867-43fc-a993-f8c78c7a5175\",\"translation\":[\"可能\"],\"dict\":{\"url\":\"yddict://m.youdao.com/dict?le=eng&q=likely\"},\"webdict\":{\"url\":\"http://m.youdao.com/dict?le=eng&q=likely\"},\"basic\":{\"exam_type\":[\"高中\",\"CET4\",\"CET6\",\"考研\",\"商务英语\"],\"us-phonetic\":\"ˈlaɪkli\",\"phonetic\":\"ˈlaɪkli\",\"uk-phonetic\":\"ˈlaɪkli\",\"wfs\":[{\"wf\":{\"name\":\"比较级\",\"value\":\"more likely 或 likelier\"}},{\"wf\":{\"name\":\"最高级\",\"value\":\"most likely 或 likeliest\"}}],\"uk-speech\":\"http://openapi.youdao.com/ttsapi?q=likely&langType=en&sign=ECBAD0D6E4875F93E763E5136C00C4E5&salt=1613701588411&voice=5&format=mp3&appKey=0295d75ab7c75b27&ttsVoiceStrict=false\",\"explains\":[\"adj. 很可能的；合适的；有希望的\",\"adv. 很可能；或许\"],\"us-speech\":\"http://openapi.youdao.com/ttsapi?q=likely&langType=en&sign=FAAEFEA46CCF0FC168BCEA7F998C8F81&salt=1613701588412&voice=6&format=mp3&appKey=0295d75ab7c75b27&ttsVoiceStrict=false\"},\"isWord\":true,\"speakUrl\":\"http://openapi.youdao.com/ttsapi?q=likely&langType=en&sign=FAAEFEA46CCF0FC168BCEA7F998C8F81&salt=1613701588412&voice=4&format=mp3&appKey=0295d75ab7c75b27&ttsVoiceStrict=false\"}",
            "parsed": 0
        }
    ],
    "msg": "succeed"
}
```

## `/wls`

### GET 请求

用户查看所有单词表

- 请求参数

	| 参数名 | 类型 | 说明 |
	| ------ | ---- | ---- |
	| null   | null | null |

- 返回数据

```json
{
  [
    {
      "id": "1e224239c0",
      "name": "test",
      "create_time": "2021-08-07",
      "update_time": "2021-08-07",
      "word_count": 0,
      "word": []
    },
    {
      "id": "a87dcce7ef",
      "name": "test2",
      "create_time": "2021-08-07",
      "update_time": "2021-08-07",
      "word_count": 0,
      "word": []
    }
  ] 
}
```

## `/wl`

### GET 请求

用户查看某个单词表的所有单词

- 请求参数

| 参数名 | 类型   | 说明                            |
| ------ | ------ | ------------------------------- |
| id     | string | 单词表id，`/?id=xxxx`形式传递值 |

- 返回数据

```json
{
		"id": "3a08f06149",
    "name": "new_test",
    "create_time": "2021-08-07",
    "update_time": "2021-08-07",
    "word_count": 0,
    "word": []
}
```

### POST 请求

用户新增单词表

- 请求参数

| 参数名 | 类型   | 说明       |
| ------ | ------ | ---------- |
| name   | string | 单词表名称 |

- 返回数据

```json
{
    "msg": "succeed"
}
```

### PUT 请求

更新某个单词表

- 请求参数

| 参数名 | 类型   | 说明                            |
| ------ | ------ | ------------------------------- |
| id     | string | 单词表id，`/?id=xxxx`形式传递值 |
| name   | string | 单词表名称，表单形式传值        |

- 返回数据

```json
{
    "msg": "succeed"
}
```

### DELETE 请求

删除某个单词表

- 请求参数

| 参数名 | 类型   | 说明                            |
| ------ | ------ | ------------------------------- |
| id     | string | 单词表id，`/?id=xxxx`形式传递值 |

- 返回数据

```json
{
    "msg": "succeed"
}
```

## `/wlc`

### GET 请求

单词表的集合运算

- 请求参数

| 参数名 | 类型   | 说明       |
| ------ | ------ | ---------- |
| exp    | string | 集合表达式 |

- 返回数据

```json
{
    "wl": [word对象{部分属性}]
}
```

## `/wadd`

### GET 请求

某个单词加入到某个单词表

- 请求参数

| 参数名     | 类型   | 说明     |
| ---------- | ------ | -------- |
| wordId     | string | 单词ID   |
| wordListId | string | 单词表ID |

- 返回数据

```json
{
    "wls": [ WordList ]
}
```

## `/wdel`

### GET 请求

在某个单词表删除某个单词

- 请求参数

| 参数名     | 类型   | 说明     |
| ---------- | ------ | -------- |
| wordId     | string | 单词ID   |
| wordListId | string | 单词表ID |

- 返回数据

```json
{
    "wls": [ WordList ]
}
```

## `/plans`

### GET 请求

获取所有时间计划表

- 请求参数

| 参数名 | 类型   | 说明         |
| ------ | ------ | ------------ |
| id     | string | 时间计划表ID |

- 返回数据

```json
{
	时间计划表对象{
		"id": string,
		···时间计划表对象
	}
}
```

## `/plan`

### GET 请求

获取某个时间计划表的所有计划

- 请求参数

| 参数名 | 类型   | 说明         |
| ------ | ------ | ------------ |
| id     | string | 时间计划表ID |

- 返回数据

```json
{
	"id": string,
	···时间计划表的基本属性
	"secs": [
		···section的基本属性
	]
}
```

### POST请求

新增时间计划表

- 请求参数

| 参数名                       | 类型   | 说明         |
| ---------------------------- | ------ | ------------ |
| id                           | string | 时间计划表ID |
| 时间计划表除了id外的其他属性 | ···    | ···          |

- 返回数据

```json
{
	null
}
```

### UPDATE 请求

更新某个时间计划表

- 请求参数

| 参数名                     | 类型   | 说明         |
| -------------------------- | ------ | ------------ |
| planId                     | string | 时间计划表ID |
| 时间计划表除了id外其他属性 | ···    | ···          |

- 返回数据

```json
{
    null
}
```

### DELETE 请求

删除某个时间计划表

- 请求参数

| 参数名 | 类型   | 说明         |
| ------ | ------ | ------------ |
| id     | string | 时间计划表ID |

- 返回数据

```json
{
    null
}
```

## `/sec`

### GET 请求

获取计划

- 获取某个计划中的所有单词

| 参数名 | 类型   | 说明   |
| ------ | ------ | ------ |
| id     | string | 计划ID |

- 返回数据

```json
{
	"id": string,
	···计划的基本属性
	"words": [
		···word的基本属性
	]
}
```

### POST请求

新增计划

- 请求参数

| 参数名                 | 类型   | 说明   |
| ---------------------- | ------ | ------ |
| id                     | string | 计划ID |
| 计划除了id外的其他属性 | ···    | ···    |

- 返回数据

```json
{
	null
}
```

### UPDATE 请求

更新某个计划

- 请求参数

| 参数名               | 类型   | 说明   |
| -------------------- | ------ | ------ |
| id                   | string | 计划ID |
| 计划除了id外其他属性 | ···    | ···    |

- 返回数据

```json
{
    null
}
```

### DELETE 请求

删除某个计划

- 请求参数

| 参数名 | 类型   | 说明   |
| ------ | ------ | ------ |
| id     | string | 计划ID |

- 返回数据

```json
{
    null
}
```

## `/secadd`

### GET 请求

某个单词加入到某个计划

- 请求参数

| 参数名    | 类型   | 说明   |
| --------- | ------ | ------ |
| wordId    | string | 单词ID |
| sectionId | string | 计划ID |

- 返回数据

```json
{
    "wls": [ WordList ]
}
```

## `/secdel`

### GET 请求

在某个计划中删除某个单词

- 请求参数

| 参数名    | 类型   | 说明   |
| --------- | ------ | ------ |
| wordId    | string | 单词ID |
| sectionId | string | 计划ID |

- 返回数据

```json
{
    "wls": [ WordList ]
}
```



