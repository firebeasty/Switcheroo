bl_info = {
    "name": "Switcheroo",
    "category": "Render",
    "author": "Keith Morgan"
}

import bpy


class Switcheroo(bpy.types.Panel):
    bl_label = "Switcheroo"
    bl_id = "view3D.custom_menu"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "render"


    def draw(self, context):
        layout = self.layout
        split = layout.split

        #Layout
        row = layout.row()
        row.operator('switcheroo.switch', icon='ARROW_LEFTRIGHT')


class OBJECT_BUTTON(bpy.types.Operator):
    bl_idname = "switcheroo.switch"
    bl_label = "Switch X/Y"


    def execute(self, context):
        x = bpy.context.scene.render.resolution_x
        y = bpy.context.scene.render.resolution_y
        bpy.context.scene.render.resolution_x = y
        bpy.context.scene.render.resolution_y = x
        return {'FINISHED'}


def register():
    bpy.utils.register_class(Switcheroo)
    bpy.utils.register_class(OBJECT_BUTTON)

def unregister():
    bpy.utils.unregister_class(Switcheroo)
    bpy.utils.unregister_class(OBJECT_BUTTON)

if __name__ == "__main__":
    register()
