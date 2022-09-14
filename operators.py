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
        light = context.view_layer.objects.active
        ob = bpy.context.active_object
        gba = ob.gba

        # Set use nodes
        if gba.use_gobo == True:
            # === Cycles ===
            light.data.use_nodes = True

            # === Eevee ===
            cursor = bpy.context.scene.cursor

            # save location, rotation
            SAVED_CURSOR_LOCATION = cursor.location[:]
            SAVED_LIGHT_LOCATION = light.location[:]
            SAVED_LIGHT_ROTATION = light.rotation_euler[:]

            cursor.location = (0, 0, 0)

            light.location = cursor.location
            light.rotation_euler = (0, 0, 0)

            # Add plane/gobo
            bpy.ops.mesh.primitive_plane_add(
                size=1,
                enter_editmode=False,
                align="WORLD",
                location=cursor.location,
                scale=(1, 1, 1),
            )
            bpy.context.active_object.name = light.name + "_eeveeGobo"
            bpy.context.active_object.location[2] = -1
            bpy.ops.object.origin_set(type="ORIGIN_CURSOR")

            # add contraints
            constraint_copyLocation = bpy.context.active_object.constraints.new(
                type="COPY_LOCATION"
            )
            constraint_copyRotation = bpy.context.active_object.constraints.new(
                type="COPY_ROTATION"
            )

            constraint_copyLocation.target = light
            constraint_copyRotation.target = light

            # reset location, rotation
            cursor.location = SAVED_CURSOR_LOCATION

            light.location = SAVED_LIGHT_LOCATION
            light.rotation_euler = SAVED_LIGHT_ROTATION

        else:
            light.data.use_nodes = False

        print("update use nodes")

        return {"FINISHED"}
