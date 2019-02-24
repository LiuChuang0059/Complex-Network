---
title:  keras 中模型保存和重新导入
tags:
  - keras
categories:
  - 机器学习
toc: true
mathjax: true
---

![](https://ws1.sinaimg.cn/large/006tKfTcly1g07k1kb1joj31900u0ae7.jpg)

----

### 1. 保存 神经网络模型 到JSON
> JSON 文件能够分层级的描述数据

保存模型 使用 to_json 函数,将模型转换成 json 格式，之后就可以保存模型到文件

```python
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
```

保存 参数

```python
model.save_weights("model.h5")
```


重新创建一个新的模型并导入

```python
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

```


将权重导入到新建的模型里面

```python
loaded_model.load_weights("model.h5")
```

JSON 保存的模型格式

```json

"keras_version":"2.0.2",
   "backend":"theano",
   "config":[
      {
         "config":{
            "dtype":"float32",
            "bias_regularizer":null,
            "activation":"relu",
            "bias_constraint":null,
            "use_bias":true,
            "bias_initializer":{
               "config":{

               },
               "class_name":"Zeros"
            },
            "kernel_regularizer":null,
            "activity_regularizer":null,
            "kernel_constraint":null,
            "trainable":true,
            "name":"dense_1",
            "kernel_initializer":{
               "config":{
                  "maxval":0.05,
                  "minval":-0.05,
                  "seed":null
               },
               "class_name":"RandomUniform"
            },
            "batch_input_shape":[
               null,
               8
            ],
            "units":12
         },
         "class_name":"Dense"
      },
      {
         "config":{
            "kernel_regularizer":null,
            "bias_regularizer":null,
            "activation":"relu",
            "bias_constraint":null,
            "use_bias":true,
            "bias_initializer":{
               "config":{

               },
               "class_name":"Zeros"
            },
            "activity_regularizer":null,
            "kernel_constraint":null,
            "trainable":true,
            "name":"dense_2",
            "kernel_initializer":{
               "config":{
                  "maxval":0.05,
                  "minval":-0.05,
                  "seed":null
               },
               "class_name":"RandomUniform"
            },
            "units":8
         },
         "class_name":"Dense"
      },
      {
         "config":{
            "kernel_regularizer":null,
            "bias_regularizer":null,
            "activation":"sigmoid",
            "bias_constraint":null,
            "use_bias":true,
            "bias_initializer":{
               "config":{

               },
               "class_name":"Zeros"
            },
            "activity_regularizer":null,
            "kernel_constraint":null,
            "trainable":true,
            "name":"dense_3",
            "kernel_initializer":{
               "config":{
                  "maxval":0.05,
                  "minval":-0.05,
                  "seed":null
               },
               "class_name":"RandomUniform"
            },
            "units":1
         },
         "class_name":"Dense"
      }
   ],
   "class_name":"Sequential"
```


---


### 2. 保存模型到 YAML

完全类似于 JSON -- 不详述

----




# 参考

https://machinelearningmastery.com/save-load-keras-deep-learning-models/