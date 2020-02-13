import sys
import os
import maya.cmds as cmds
import maya.OpenMaya as om
path = r'G:\Python\maya\controll_creator'
sys.path.append(path)
os.chdir(path)
t_node = cmds.ls(sl=True,long=False)
# s_node = cmds.listRelatives(t_node[0], shapes=True)

_dict = {}

for i in t_node:
    cvs_list = []
    knot_list = []
    degree_list = []

    s_node = cmds.listRelatives(i, shapes=True)
    for node in s_node:
        # print(s_node)
        cinfo = cmds.createNode('curveInfo')
        cmds.connectAttr(node + '.worldSpace', cinfo + '.inputCurve')
        cvs = cmds.getAttr(cinfo+".cp[*]")
        knots = cmds.getAttr("{0}.knots[*]".format(cinfo))
        degs = cmds.getAttr(node+'.degree')
        cvs_list.append(cvs)
        knot_list.append(knots)
        degree_list.append(degs)

        _dict[i]={'cvs':cvs_list,
                    'knots':knot_list,
                    'degree':degree_list}

        # print('cvs = ',cvs)
        # print('knots = ',knots)
        # print('degree = ',degs)

        cmds.delete(cinfo)
        # c = cmds.curve(p=cvs,k=knots,d=degs)
# make a text file
import json
s = json.dumps(_dict, indent=2, sort_keys=True)
with open('curve_create_data.json', 'w') as f:
    f.write(s)


