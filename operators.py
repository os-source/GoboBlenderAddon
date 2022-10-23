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

        if gba.use_gobo == True:
            # === Cycles ===
            # Set use nodes
            light.data.use_nodes = True

            # === Eevee ===
            createGoboEevee(light, ob, gba)

        else:
            light.data.use_nodes = False

        print("update use nodes")

        return {"FINISHED"}

    

def createGoboEevee(light, ob, gba): 
    cursor = bpy.context.scene.cursor

    # save location, rotation
    SAVED_CURSOR_LOCATION = cursor.location[:]
    SAVED_LIGHT_LOCATION = light.location[:]
    SAVED_LIGHT_ROTATION = light.rotation_euler[:]

    cursor.location = (0, 0, 0)

    light.location = cursor.location
    light.rotation_euler = (0, 0, 0)
    

    # Create new Collection for Gobos if it doesnt exist
    goboCollection = bpy.data.collections.get("EeveeGobos")

    if not goboCollection:
        goboCollection = bpy.data.collections.new("EeveeGobos")
        bpy.context.scene.collection.children.link(goboCollection)


    # Create Gobo plane
    goboPlane = bpy.ops.mesh.primitive_plane_add(
        size=1,
        enter_editmode=False,
        align="WORLD",
        location=cursor.location,
        scale=(1, 1, 1)
    )

    bpy.context.active_object.name = light.name + "_eeveeGobo"
    bpy.context.active_object.location[2] = -1
    bpy.ops.object.origin_set(type="ORIGIN_CURSOR")

    # Turn off visibility
    bpy.context.active_object.hide_viewport = True


    # add constraints
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


    # add gobo plane to gobo collection
    obj = bpy.context.active_object
    bpy.ops.collection.objects_remove_all()
    bpy.data.collections['EeveeGobos'].objects.link(obj)
