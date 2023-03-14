from bigtree import Node, print_tree, list_to_tree
def tree_v1():
    a = Node("Батя", age=90)
    b = Node("Дочь", age=65, parent=a)
    c = Node("Сын", age=60, parent=a)
    d = Node("Внук", age=30, parent=b)

    a.children
    a.depth
    a.max_depth

    print_tree(a, attr_list=["age"])

def tree_v2(corp, dep):
    tree_list = []
    for i in dep:
        sum = corp + '/' + i.depName
        for j in i.posListUser:
            sumj = sum + '/' + j
            for q in i.deptListUser:
                if j == q.workPosition:
                    sumq = sumj + '/' + q.workUserName + ' (' + format(q.workAge) + ' лет)'
                    tree_list.append(sumq)
                else:
                    tree_list.append(sumj)
            if i.deptListUser == [] : tree_list.append(sumj)



    # test_list = [f"{corp}/{b}/d", f"{corp}/{b}/e", f"{corp}/{c}"]
    root = list_to_tree(tree_list)
    print_tree(root)
    # print(sumq)

