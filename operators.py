import bpy

class SayHelloOperator(bpy.types.Operator):
    bl_idname = "object.say_hello"
    bl_label = "say hello"

    def execute(self, context):
        return {'FINISHED'}
