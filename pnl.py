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


class GBA_PT_Panel(Panel):
    bl_idname = "object.use_gobo"
    bl_label = "Gobo"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "data"
    bl_order = 10

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
            row = layout.row()
            row.prop(gba, "use_goboAnimation")

            # Elements shown when use gobo animation = true
            if gba.use_goboAnimation == True:
                # Gobo speed
                row = layout.row()
                row.prop(gba, "gobo_speed")

