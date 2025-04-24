# 用于将文本转化为embedding
# embedding 结果存在 embedding.json 文件中
# 用于将 embedding 进行相似度计算
# 相似度计算结果存在 similarity_matrix_list.json 文件中
# 用于将相似度矩阵进行归一化
# 归一化结果存在 normalization_matrix.json 文件中
# ---------------------------------------------------------

# 存在若干文本，t1，t2，t3....
# 每一个文本都由多行字符串组成，每行之间用换行符\n分隔

# For 循环读取目录下所有文本，每一个循环处理一个文本
# 1. 读取当前要处理的文本内容
# 2. 对文本内容根据换行符\n进行分割，得到每一行的字符串，存到列表中
import os
import numpy as np
import Tools.main as tools
import json
import math

def list_to_embedding(text_list_temp):
    # 如果没有embedding.json文件，就新建一个
    if not os.path.exists("embedding.json"):
        with open("embedding.json", "w") as file:
            json.dump([], file, indent=4)
    with open("embedding.json", "r") as file:
        data = json.load(file)

    start = len(data)
    flag = 0
    now = 0

    embedding_list_temp1 = []
    # 循环遍历二维列表， 对每一个文本进行embedding
    for text in text_list_temp:
        now += 1
        # 跳过已经处理过的文本
        # start 为已经处理过的文本数量
        if flag < start:
            print("跳过第" + str(now) + "个文本")
            flag += 1
            continue

        print("处理第" + str(now) + "个文本")
        embedding_list_temp2 = []
        for line in text:
            if line == "":
                continue
            print(line)
            embedding = tools.get_embedding(line)
            embedding_list_temp2.append(embedding)
        embedding_list_temp1.append(embedding_list_temp2)
        # 立即更新 data 到 json 文件的末尾新增
        output_file2 = "embedding.json"
        with open(output_file2, "r") as file:
            data_list = json.load(file)
            data_list.append(embedding_list_temp2)

        with open(output_file2, "w") as file:
            json.dump(data_list, file, indent=4)

    return embedding_list_temp1

def eucliDist(A, B):
    if A is None:
        A = [0] * 1536
    if B is None:
        B = [0] * 1536
    return math.sqrt(sum([(a - b) ** 2 for (a, b) in zip(A, B)]))

def normalize_min_max(matrix):
    min_val = np.min(matrix)
    max_val = np.max(matrix)
    if max_val == min_val:  # 避免除以零
        return np.zeros_like(matrix)
    return (matrix - min_val) / (max_val - min_val)

if __name__ == "__main__":
    # 读取要 embedding 的文本描述 json 文件，自行修改名字
    json_name = "2000_train_set.json"

    with open( json_name , "r", encoding="utf-8") as f:
        data = json.load(f)

    # 切片
    text_list = []
    for text in data:
        text_lines = text["description"][:-1].split("\n")
        text_list.append(text_lines)
        if len(text_lines) != 14:
            print(text["image_name"])

    # 生成 Embedding 分为两步  使用布尔变量 flag 控制
    # flag 设置为 0 第一步先调用 list_to_embedding 函数得到 embedding.json 转化得到全部的 Embedding
    # flag 设置为 1 第二步使用 embedding.json 进行相似度计算以及后续的归一化等操作
    flag = 0

    if flag == 0:
        # 调用 list_to_embedding 函数在当前目录下生成 embedding.json
        list_to_embedding(text_list)

    if flag == 1:
        # flag == 0 跑完了以后使用 embedding.json 进行接下来的处理
        with open("embedding.json", "r") as file:
            embedding_list = json.load(file)

        text_number = 14   # 有 14 个特征
        dimension = 1000   # 有多少条数据，根据条数进行修改

        # 一份输出的文本由24次 prompt chaining 生成，所以需要得到24个相似矩阵
        # 24句话，24个特征，24个相似矩阵，每一个相似矩阵都是一个二维列表
        # 二维列表中的每一个元素都是一个浮点数，代表两个embedding的相似度，通过计算欧氏距离
        similarity_matrix_list = np.zeros((text_number, dimension, dimension))
        for i in range(text_number - 1):
            # 计算欧氏距离 dimension*(dimension-1)/2 次
            print("计算第" + str(i + 1) + "个相似矩阵")
            for j in range(dimension):
                similarity_matrix_list[i][j][j] = 0.00000000
                for k in range(j + 1, dimension):
                    similarity_matrix_list[i][j][k] = eucliDist(
                        embedding_list[j][i], embedding_list[k][i]
                    )
                    similarity_matrix_list[i][k][j] = similarity_matrix_list[i][j][k]
            print(similarity_matrix_list[i])
            print("-----------------------")

        # 保存 similarity_matrix_list 到 similarity_matrix_list.json
        output_file = "similarity_matrix_list.json"
        with open(output_file, "w") as file:
            json.dump([], file, indent=4)
            json.dump(similarity_matrix_list.tolist(), file, indent=4)

        # 归一化
        w_list = [1] * text_number

        w_matrix = np.zeros((dimension, dimension))
        for i in range(text_number):
            normalized_matrix = normalize_min_max(similarity_matrix_list[i])
            w_matrix += w_list[i] * normalized_matrix

        print(w_matrix)
        print("-----------------------")

        # 保存 w_matrix 到 normalization_matrix_1.txt
        # normalization_matrix_1.json 的是保存权重为 1 的归一化矩阵，与其他权重生成的归一化矩阵相分开
        output_file = "normalization_matrix_1.json"
        with open(output_file, "w") as file:
            json.dump(w_matrix.tolist(), file, indent=4)

        # tsne降维  看本地能不能跑，可能会爆内存，需要放到 a6000
        # from sklearn.manifold import TSNE
        #
        # perplexity = min(dimension - 1, 30)
        #
        # # 嵌入空间的维度为2，即将数据降维成2维
        # ts = TSNE(n_components=2, perplexity=perplexity)
        # # 训练模型
        # ts.fit_transform(w_matrix)
        # # 打印结果
        # print(ts.embedding_)
