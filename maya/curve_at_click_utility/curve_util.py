import maya.api.OpenMaya as om
import maya.api.OpenMayaUI as omui
import maya.cmds as cmds
import pymel.core as pm

class FollicleBindCurve():
    """create Curve on suface at click points and bind them to Follicles"""
    def __init__(self, cv_count , crv_len, selected, lock_len):
        self.cv_count = cv_count
        self.crv_len = crv_len
        self.selected = selected #cmds.ls(sl=True,long=True) or []
        self.ctx = 'Click2dTo3dCtx'
        self.lock_len = lock_len

        if self.selected:
            self.follicle_grp, self.curve_grp = self.create_group()
        else:
            pass

    def create_group(self):
        f_name = 'follicle_GRP'
        c_name = 'curves_GRP'
        if self.selected and not cmds.objExists(f_name):
            follicle_grp = cmds.group(em=True, name=f_name)
        else:
            follicle_grp = f_name
        if self.selected and not cmds.objExists(c_name):
            curves_grp = cmds.group(em=True, name=c_name)
        else:
            curves_grp = c_name

        return f_name, c_name

    def get_coord_at_click(self, selected, ctx):
        vpX, vpY, _ = cmds.draggerContext(ctx, query=True, anchorPoint=True)
        position = om.MPoint()  # 3D point with double-precision coordinates
        direction = om.MVector()  # 3D vector with double-precision coordinates

        omui.M3dView().active3dView().viewToWorld(
                                                int(vpX),
                                                int(vpY),
                                                position,  # world point
                                                direction)  # world vector

        for mesh in selected:
            selectionList = om.MSelectionList()
            selectionList.add(mesh)
            dagPath = selectionList.getDagPath(0)
            fnMesh = om.MFnMesh(dagPath)

            intersection = fnMesh.closestIntersection(
                                                    om.MFloatPoint(position),  # raySource
                                                    om.MFloatVector(direction),  # rayDirection
                                                    om.MSpace.kWorld,  # space
                                                    99999,  # maxParam
                                                    True)  # testBothDirections

            hitPoint, hitRayParam, hitFace, hitTriangle, \
                hitBary1, hitBary2 = intersection

            x, y, z, _ = hitPoint

        return x, y, z

    def get_coord_on_drag(self, selected, ctx):
        vpX, vpY, _ = cmds.draggerContext(ctx, query=True, dragPoint=True)
        position = om.MPoint()  # 3D point with double-precision coordinates
        direction = om.MVector()  # 3D vector with double-precision coordinates

        omui.M3dView().active3dView().viewToWorld(
                                                int(vpX),
                                                int(vpY),
                                                position,  # world point
                                                direction)  # world vector

        for mesh in selected:
            selectionList = om.MSelectionList()
            selectionList.add(mesh)
            dagPath = selectionList.getDagPath(0)
            fnMesh = om.MFnMesh(dagPath)

            intersection = fnMesh.closestIntersection(
                                                    om.MFloatPoint(position),  # raySource
                                                    om.MFloatVector(direction),  # rayDirection
                                                    om.MSpace.kWorld,  # space
                                                    99999,  # maxParam
                                                    True)  # testBothDirections

            hitPoint, hitRayParam, hitFace, hitTriangle, \
                hitBary1, hitBary2 = intersection

            x, y, z, _ = hitPoint

        return x, y, z

    def get_closest_normal_uv(self, surface, x, y, z):
        node = cmds.createNode('closestPointOnMesh')
        cmds.connectAttr(surface + '.worldMesh ', node + ".inMesh")
        cmds.connectAttr(surface + '.worldMatrix ', node + ".inputMatrix")
        cmds.setAttr( node + ".inPosition", x, y, z, type='double3')
        normal = cmds.getAttr(node + ".normal")
        u = cmds.getAttr(node + '.result.parameterU')
        v = cmds.getAttr(node + '.result.parameterV')

        result_normal = om.MVector(*normal)
        result_normal.normalize()
        uv_coord = (u,v)
        cmds.delete(node)

        return result_normal, uv_coord

    def create_follicle(self, mesh, u, v):
        folicle = cmds.createNode('follicle')
        follicle_trans = cmds.listRelatives(folicle, type='transform', p = True)
        cmds.connectAttr(folicle+'.outRotate', follicle_trans[0]+'.rotate')
        cmds.connectAttr(folicle+'.outTranslate', follicle_trans[0]+'.translate')
        cmds.connectAttr(mesh+'.worldMatrix', folicle+'.inputWorldMatrix')
        cmds.connectAttr(mesh+'.outMesh', folicle+'.inputMesh')
        cmds.setAttr(folicle+'.simulationMethod', 0)
        cmds.setAttr(folicle+'.parameterU', u)
        cmds.setAttr(folicle+'.parameterV', v)

        return follicle_trans[0]

    def create_curve(self, mesh, x,y,z, xn,yn,zn, cv_count, crv_len):
        if (x, y, z) != (0.0, 0.0, 0.0):
            defList = [(x,y,z,1.0)]
            defMirList = [(-x,y,z,1.0)]
            listX = []
            listMirX = []
            t = crv_len/(cv_count-1)
            for _ in range(1,cv_count):
                listX.append(((xn*t)+x, (yn*t)+y, (zn*t)+z, 1.0))
                listMirX.append(((-xn*t)-x, (yn*t)+y, (zn*t)+z, 1.0))
                t+=crv_len/(cv_count-1)

            for i in listX:
                defList.append(i)
            for j in listMirX:
                defMirList.append(j)
            # cv_list = [[0,0,0,1.0], [1,0,0,1.0], [2,0,0,1.0], [3,0,0,1.0], [4,0,0,1.0]]
            # cv_list = [[0, 0, 0, 1.0]]
            # for x in range(1, cv_count):
            #     cv_list.append([x, 0, 0, 1.0])


            crv = cmds.curve(pw=defList)
            cmds.LockCurveLength(crv)
            cmds.setAttr(crv + ".lockLength", self.lock_len)
            # cmds.move(x, y, z, crv)
            # angle_btw = cmds.angleBetween(euler=True, v1=(1.0, 0.0, 0.0), v2=(xn, yn, zn))
            cmds.move(x, y, z, crv+ ".scalePivot", crv+ ".rotatePivot")

            crv_mir = cmds.curve(pw=defMirList)
            cmds.LockCurveLength(crv_mir)
            cmds.setAttr(crv_mir + ".lockLength", self.lock_len)
            # cmds.move(x, y, z, crv)
            # angle_btw = cmds.angleBetween(euler=True, v1=(1.0, 0.0, 0.0), v2=(xn, yn, zn))
            cmds.move(x, y, z, crv_mir+ ".scalePivot", crv_mir+ ".rotatePivot")
            # cmds.rotate(angle_btw[0], angle_btw[1], angle_btw[2], crv)
            # cmds.makeIdentity(apply=True, t=1, r=1, s=1)

        else:
            return None

        return crv



    def create_job(self):
        mesh = self.selected[0]
        x, y, z = self.get_coord_at_click(self.selected, self.ctx)
        xn, yn, zn = self.get_closest_normal_uv(mesh, x,y,z)[0]
        u, v = self.get_closest_normal_uv(mesh, x, y, z)[1]

        if (x, y, z)!=(0.0, 0.0, 0.0):
            follicle_trans = self.create_follicle(mesh, u, v)
            curve = self.create_curve(mesh, x,y,z, xn,yn,zn, self.cv_count, self.crv_len)
            per_curve_grp = cmds.group(em=True, name=curve+'_GRP')
            cmds.parent(curve, per_curve_grp)
            cmds.parentConstraint(follicle_trans, per_curve_grp, mo=True)
            cmds.parent(follicle_trans, self.follicle_grp)
            cmds.parent(per_curve_grp, self.curve_grp)

            self.curve = curve
            self.follicle_trans = follicle_trans


    def move_job(self):
        x, y, z = self.get_coord_at_click(self.selected, self.ctx)
        dxn, dyn, dzn = self.get_closest_normal_uv(self.selected[0], x,y,z)[0]
        if (x,y,z)!=(0.0,0.0,0.0):
            dx, dy, dz = self.get_coord_on_drag(self.selected, self.ctx)
            angle_btw = cmds.angleBetween(euler=True, v1=(1.0, 0.0, 0.0), v2=(dxn, dyn, dzn))
            cmds.move( dx, dy, dz, self.curve, worldSpace=True)
            cmds.rotate(angle_btw[0], angle_btw[1], angle_btw[2], self.curve)
            cmds.move(dx, dy, dz, self.follicle_trans)


    def run(self):
        if self.selected:
            if cmds.draggerContext(self.ctx, exists=True):
                cmds.deleteUI(self.ctx)
            # Create dragger context and set it to the active tool
            # cmds.draggerContext(self.ctx, pressCommand=self.create_job, dragCommand=self.move_job, name=self.ctx, cursor='crossHair', image1='curve_create.png')
            cmds.draggerContext(self.ctx, pressCommand=self.create_job, name=self.ctx, cursor='crossHair', image1='curve_create.png')
            cmds.setToolTo(self.ctx)
        else:
            print("No Mesh Selected!")

    def get_pivot(self):
        pivot = self.get_coord_at_click(self.selected, self.ctx)
        return pivot







# obj = FollicleBindCurve(5, 5.0)
# obj.run()
