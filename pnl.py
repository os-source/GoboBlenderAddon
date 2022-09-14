import bpy

from bpy.types import Panel, PropertyGroup
from bpy.props import BoolProperty, IntProperty


def useGobo_update(self, context):
    print("update use gobo")
    bpy.ops.object.use_gobo()


def useGoboAnimation_update(self, context):
    print("update use gobo animation")


def goboSpeed_update(self, context):
    print("update gobo speed")


class GBA_settings(PropertyGroup):
    use_gobo: BoolProperty(
        name="Use Gobo",
        description="Enable or disable Gobo",
        default=False,
        update=useGobo_update,
    )

    use_goboAnimation: BoolProperty(
        name="Animation",
        description="Enable or disable Gobo Animation",
        default=False,
        update=useGoboAnimation_update,
    )

    gobo_speed: IntProperty(
        name="Speed",
        description="Change the Speed of the Gobo animation",
        soft_min=1,
        soft_max=100,
        default=10,
        update=goboSpeed_update,
    )

    gobo_distance: IntProperty(
        name="Distance",
        description="Change the Distance of the Gobo",
        soft_min=1,
        soft_max=100,
        default=10,
        # update=goboDistance_update,
    )

    gobo_size: IntProperty(
        name="Size",
        description="Change the Size of the Gobo",
        soft_min=1,
        soft_max=100,
        default=10,
        # update=goboSize_update,
    )

    gobo_opacity: IntProperty(
        name="Opacity",
        description="Change the Opacity of the Gobo",
        soft_min=1,
        soft_max=100,
        default=10,
        # update=goboOpacity_update,
    )


class GBA_PT_GoboPanel(Panel):
    bl_idname = "object.use_gobo"
    bl_label = "Gobo"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "data"

    @classmethod 
    def poll(self, context):
        obj = context.object

        # Check if object is a light
        if obj.type == "LIGHT":
            return True
        else:
            return False

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        obj = context.object
        ob = bpy.context.active_object
        gba = ob.gba

        # Use Gobo button
        layout.prop(gba, "use_gobo", toggle=1)

        # Elements shown when use gobo = true
        if gba.use_gobo == True:
            # Use Gobo Animation
            layout.prop(gba, "use_goboAnimation")

            # Elements shown when use gobo animation = true
            if gba.use_goboAnimation == True:
                # Gobo speed
                layout.prop(gba, "gobo_speed")

            # Gobo Distance
            layout.prop(gba, "gobo_distance")

            # Gobo Size
            layout.prop(gba, "gobo_size")

            # Gobo Opacity
            layout.prop(gba, "gobo_opacity")

            layout.prop(obj, "color")
