import bpy

from bpy.types import Operator


class GBA_OT_Use_Gobo(Operator):
    bl_idname = "object.use_gobo"
    bl_label = "Use Gobo"
    bl_description = "ladkfjdsl"

    @classmethod
    def poll(cls, context):
        obj = context.object

        if obj is not None:
            if obj.mode == "OBJECT" and obj.type == "LIGHT":
                return True
        return False

    def execute(self, context):
        active_obj = context.view_layer.objects.active
        ob = bpy.context.active_object
        gba = ob.gba

        # Set use nodes
        if gba.use_gobo == True:
            active_obj.data.use_nodes = True
        else:
            active_obj.data.use_nodes = False

        print("update use nodes")

        return {"FINISHED"}

