import networkx as nx
import matplotlib.pyplot as plt


# 这个方法放在矩阵创建中
# def get_pr(dg):
#     """
#     获得每个节点的PR值
#
#     :param dg: 有向图
#     """
#     nodes_num = dg.number_of_nodes()
#     nodes_out_degree = dg.out_degree
#
#     # 遍历每个节点及其出度
#     for node_out_degree in nodes_out_degree:
#         node = node_out_degree[0]
#         out_degree = node_out_degree[1]
#
#         # 如果一个节点没有出度，那么PR值为1 / N，否则为1 / out_degree
#         if out_degree == 0:
#             pr = 1 / nodes_num
#         else:
#             pr = 1 / out_degree
#
#         dg.add_nodes_from([node], pr=pr)

def get_init_pr(dg):
    """
    获得每个节点的初始PR值

    :param dg: 有向图
    """
    nodes_num = dg.number_of_nodes()
    for node in dg.nodes:
        pr = 1 / nodes_num
        dg.add_nodes_from([node], pr=pr)


def create_network():
    """
    创建有向图

    :return dg: 有向图
    """
    dg = nx.DiGraph()  # 创建有向图
    dg.add_nodes_from(['0', '1', '2', '3', '4'])  # 添加节点
    dg.add_edges_from([('1', '0'), ('2', '1'), ('3', '4'), ('4', '1'), ('3', '1')])  # 添加边

    get_init_pr(dg)

    return dg


def draw_network(dg):
    """
    可视化有向图

    :param dg: 有向图
    """
    fig, ax = plt.subplots()
    nx.draw(dg, ax=ax, with_labels=True)
    plt.show()


# if __name__ == '__main__':
#     dg = create_network()
#     for node in dg.nodes:
#         print(dg.nodes[node])