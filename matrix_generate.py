import numpy as np


def solve_ranking_leaked(adj_matrix):
    """
    解决排名泄露问题
    :param adj_matrix: 邻接矩阵
    """
    col_num = np.size(adj_matrix, 1)  # 获得邻接矩阵列数

    row_num = 0
    for row in adj_matrix:
        # 如果排名泄露，那么这个节点对每个节点都有出链
        if sum(row) == 0:
            for col in range(col_num):
                adj_matrix[row_num][col] = 1
        row_num += 1


def calc_out_degree_ratio(adj_matrix):
    """
    计算每个节点影响力传播的比率，即该节点有多大的概率把影响力传递给下一个节点
    公式：
        out_edge / n
        out_edge: 出边，即这个节点可以把影响力传递给下一个节点
        n: 这个节点共有多少个出度

    :param adj_matrix: 邻接矩阵
    """
    row_num = 0
    for row in adj_matrix:
        n = sum(row)  # 求该节点的所有出度
        col_num = 0
        for col in row:
            adj_matrix[row_num][col_num] = col / n  # out_edge / n
            col_num += 1

        row_num += 1


def create_matrix(dg):
    """
    通过有向图生成邻接矩阵
    :param dg: 有向图
    :return adj_matrix: 邻接矩阵
    """
    node_num = dg.number_of_nodes()

    adj_matrix = np.zeros((node_num, node_num))

    for edge in dg.edges:
        adj_matrix[int(edge[0])][int(edge[1])] = 1

    solve_ranking_leaked(adj_matrix)
    calc_out_degree_ratio(adj_matrix)
    # print(adj_matrix)
    return adj_matrix


def create_pr_vector(dg):
    """
    创建初始PR值的向量

    :param dg: 有向图
    :return pr_vec: 初始PR值向量
    """
    pr_list = []
    nodes = dg.nodes

    # 将初始PR值存入列表
    for node in nodes:
        pr_list.append(nodes[node]['pr'])

    pr_vec = np.array(pr_list)  # 将列表转换为ndarray对象

    return pr_vec
