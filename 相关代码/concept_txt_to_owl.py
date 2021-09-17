import sys
import os


def read_file_to_set(filename):
    temp_set = set()
    with open(filename, "r", encoding="utf-8") as fr:
        for line in fr:
            line = line.strip("\n")
            temp_set.add(line)
    return temp_set


if __name__ == '__main__':
    # 输入文件
    input_file_name = sys.argv[1]
    # 输出文件
    out_file_name = sys.argv[2]
    input_data = read_file_to_set(input_file_name)
    # owl
    owl_head = '<?xml version="1.0"?>\n<rdf:RDF xmlns="http://www.semanticweb.org/administrator/ontologies/2019/4' \
               '/untitled-ontology-25"\n     xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"\n     ' \
               'xmlns:owl="http://www.w3.org/2002/07/owl#"\n     xmlns:xml="http://www.w3.org/XML/1998/namespace"\n   ' \
               '  xmlns:xsd="http://www.w3.org/2001/XMLSchema#"\n     ' \
               'xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#">\n    <owl:Ontology ' \
               'rdf:about="http://www.semanticweb.org/administrator/ontologies/2019/4/untitled-ontology-25"/>\n\n\n '
    owl_end = '\n</rdf:RDF>'

    class_prefix = '<owl:Class rdf:about="http://www.semanticweb.org/administrator/ontologies/2019/4/untitled-ontology-25#'
    class_father_prefix = '<rdfs:subClassOf rdf:resource="http://www.semanticweb.org/administrator/ontologies/2019/4/untitled-ontology-25#'
    entity_prefix = '<owl:NamedIndividual rdf:about="http://www.semanticweb.org/administrator/ontologies/2019/4/untitled-ontology-25#'
    entity_father_prefix = '<rdf:type rdf:resource="http://www.semanticweb.org/administrator/ontologies/2019/4/untitled-ontology-25#'
    comment_prefix = '    \n\n\n    <!-- http://www.semanticweb.org/administrator/ontologies/2019/4/untitled-ontology-25#'

    with open(out_file_name, 'w', encoding='utf8') as f:
        f.writelines(owl_head)
        for line in input_data:
            father_node, current_node, flag = line.split('\t')
            # 当前节点是根节点的情况
            if father_node == 'root':
                f.writelines(comment_prefix + current_node + ' -->\n')
                f.writelines('    ' + class_prefix + current_node + '"/>\n\n\n')
                continue
            # 当前节点属于概念节点的情况
            if flag == 'concept':
                f.writelines(comment_prefix + current_node + ' -->\n')
                f.writelines('    ' + class_prefix + current_node + '">\n')
                f.writelines('        ' + class_father_prefix + father_node + '"/>\n')
                f.writelines('    </owl:Class>\n')
                # 当前节点属于实体节点的情况
            if flag == 'entity':
                f.writelines(comment_prefix + current_node + ' -->\n')
                f.writelines('    ' + entity_prefix + current_node + '">\n')
                f.writelines('        ' + entity_father_prefix + father_node + '"/>\n')
                f.writelines('    </owl:NamedIndividual>\n')
        f.writelines(owl_end)
    f.close()
