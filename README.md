# VocabularyX-BackEnd

# Entities

## WordList

```typescript
interface WordList {
    id: string,
    name: string,
    create_time: Date,
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
    "id": string,
    "spell": string,
 ...  // all word properties
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

## `/s`

### GET 请求

用户搜索单词

- 请求参数

| 参数名   | 类型   | 说明     |
| -------- | ------ | -------- |
| fragment | string | 部分单词 |

- 返回数据

```json
{
    "words": [
     Word对象{word所有属性}
    ]
}
```

## `/wls`

### GET 请求

用户查看所有单词表

- 请求参数

| 参数名 | 类型   | 说明     |
| ------ | ------ | -------- |
| id     | string | 单词表ID |

- 返回数据

```json
{
    单词表对象:{
		"id": string,
	    ···单词表基本属性
	}
}
```

## `/wl`

### GET 请求

用户查看某个单词表的所有单词

- 请求参数

| 参数名 | 类型   | 说明     |
| ------ | ------ | -------- |
| id     | string | 单词表ID |

- 返回数据

```json
{
    "id": string,
    ···单词表基本属性
    "wl": [word对象{部分属性}]
}
```

### POST 请求

用户新增单词表

- 请求参数

| 参数名                 | 类型   | 说明     |
| ---------------------- | ------ | -------- |
| id                     | string | 单词表ID |
| 单词表除了id外其他属性 | ···    | ···      |

- 返回数据

```json
{
    null
}
```

### UPDATE 请求

更新某个单词表

- 请求参数

| 参数名                 | 类型   | 说明     |
| ---------------------- | ------ | -------- |
| id                     | string | 单词表ID |
| 单词表除了id外其他属性 | ···    | ···      |

- 返回数据

```json
{
    null
}
```

### DELETE 请求

删除某个单词表

- 请求参数

| 参数名 | 类型   | 说明     |
| ------ | ------ | -------- |
| id     | string | 单词表ID |

- 返回数据

```json
{
    null
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

