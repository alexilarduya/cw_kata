#http://www.codewars.com/kata/52a89c2ea8ddc5547a000863

def loop_size(node):

    nodes = []
    
    while True:
        if nodes.count(id(node)):
            break
        else:
            nodes.append(id(node))
            node = node.next
    
    for idx, node_id in enumerate(nodes):
        if node_id == id(node):
            break
    
    return len(nodes) - idx