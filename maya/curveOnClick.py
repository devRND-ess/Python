import maya.api.OpenMaya as om
import maya.api.OpenMayaUI as omui
import maya.cmds as cmds
import sys
sys.path.append(r'G:\Python\maya\glTools-master')
import glTools.utils.base
import glTools.utils.mesh as mUtil

selected = cmds.ls(sl=True,long=True) or []

def get_closest_normal(surface, x, y , z):
    node = cmds.createNode('closestPointOnMesh')
    cmds.connectAttr(surface + '.worldMesh ', node + ".inMesh")
    cmds.connectAttr(surface + '.worldMatrix ', node + ".inputMatrix")
    cmds.setAttr( node + ".inPosition", x, y, z, type='double3')
    normal = cmds.getAttr(node + ".normal")
    # there's a bug in Maya 2016 where the normal
    # is not properly normalized.  Not sure
    # if it's fixed in other years....  this
    # is the workaround

    result = om.MVector(*normal)
    cmds.delete(node)
    print(result)
    #result.normalize()
    return result


#x = 2.0
#y = 0.0
#z = -1.0
#cmds.curve( pw=[(x, y, z, 1), (x*2, y*2, z*2, 1), (x*3, y*3, z*3, 1), (x*4, y*4, z*4, 1)] )

def onPress():
    if not selected:
        print("No mesh selected!")
        return
    """Take x,y from mouse click, convert into 3d world coordinates"""
    vpX, vpY, _ = cmds.draggerContext(ctx, query=True, anchorPoint=True)
    position = om.MPoint()  # 3D point with double-precision coordinates
    direction = om.MVector()  # 3D vector with double-precision coordinates


    omui.M3dView().active3dView().viewToWorld(
        int(vpX),
        int(vpY),
        position,  # world point
        direction)  # world vector

    for mesh in selected:
        # Create a list which can hold MObjects, MPlugs, MDagPaths
        selectionList = om.MSelectionList()
        selectionList.add(mesh)  # Add mesh to list
        dagPath = selectionList.getDagPath(0)  # Path to a DAG node
        fnMesh = om.MFnMesh(dagPath)  # Function set for operation on meshes


        intersection = fnMesh.closestIntersection(
            om.MFloatPoint(position),  # raySource
            om.MFloatVector(direction),  # rayDirection
            om.MSpace.kWorld,  # space
            99999,  # maxParam
            True)  # testBothDirections

        # Extract the different values from the intersection result
        hitPoint, hitRayParam, hitFace, hitTriangle, \
            hitBary1, hitBary2 = intersection

        # Extract x, y, z world coordinates of the hitPoint result
        ot = 0.5
        x, y, z, _ = hitPoint
        xn, yn, zn = get_closest_normal(mesh, x, y, z)
        if (x, y, z) != (0.0, 0.0, 0.0) and (xn, yn, zn) != (0.0,0.0,0.0):
            # cmds.polySphere(sx=10, sy=15, r=0.05)
            # cmds.move( x, y, z )

            # cmds.polySphere(sx=10, sy=15, r=0.05)
            # cmds.move( (xn*ot)+x, (yn*ot)+y, (zn*ot)+z)
            defList = [(x,y,z,1.0)]
            listX = []
            t = 2.0
            for _ in range(1,5):
                listX.append(((xn*t)+x, (yn*t)+y, (zn*t)+z, 1.0))
                t+=2.0
            # listX = [((xn/t)+x, (yn/t)+y, (zn/t)+z, 1.0) for t in range(1,6) if t>1]
            for i in listX:
                defList.append(i)

            crv = cmds.curve( pw=defList )
            cmds.LockCurveLength(crv)
            cmds.setAttr(crv + ".lockLength", 1)
            cmds.move(x, y, z, crv+ ".scalePivot", crv+ ".rotatePivot", absolute=True)
            #cmds.move( x, y, z )
            # print(x, y, z)  # Print the world coordinates
            # print(xn,yn,zn)
    # cpx, cpy, cpz = cmds.getAttr( crv+'.cv[0]' )
    # cmds.move(cpx, cpy, cpz, crv+ ".scalePivot", crv+ ".rotatePivot", absolute=True)

# Name of dragger context
ctx = 'Click2dTo3dCtx'

if cmds.draggerContext(ctx, exists=True):
    cmds.deleteUI(ctx)
# Create dragger context and set it to the active tool
cmds.draggerContext(ctx, pressCommand=onPress, name=ctx, cursor='crossHair')
cmds.setToolTo(ctx)
