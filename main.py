import graph_generate as gg
import matrix_generate as mg
import pagerank as pr

if __name__ == '__main__':
    dg = gg.create_network()
    adj_matrix = mg.create_matrix(dg)
    pr_vec = mg.create_pr_vector(dg)
    pr.pagerank(adj_matrix, pr_vec)
