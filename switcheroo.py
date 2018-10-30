bl_info = {
    "name": "Switcheroo",
    "category": "Render",
    "author": "Keith Morgan"
}

import bpy

class OBJECT_BUTTON(bpy.types.Operator):
    bl_idname = "switcheroo.switch"
    bl_label = "Switch X/Y"

    def execute(self, context):
        bpy.context.scene.render.resolution_x, bpy.context.scene.render.resolution_y = bpy.context.scene.render.resolution_y, bpy.context.scene.render.resolution_x
        return {'FINISHED'}

def draw_switcheroo(self, context):
    layout = self.layout
    split = layout.split

    #Layout
    row = layout.row()
    row.operator('switcheroo.switch', icon='ARROW_LEFTRIGHT')

def register():
    # lets add the menu to the Mesh Display panel via append or prepend
    bpy.utils.register_class(OBJECT_BUTTON)
    bpy.types.RENDER_PT_dimensions.append(draw_switcheroo)

def unregister():
    # remove the menu
    bpy.utils.unregister_class(OBJECT_BUTTON)
    bpy.types.RENDER_PT_dimensions.remove(draw_switcheroo)

if __name__ == "__main__":
    register()
