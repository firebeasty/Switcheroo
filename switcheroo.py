bl_info = {
    "name": "Switcheroo",
    "category": "Render",
    "version": (1, 1, 0),
    "blender": (2, 79, 0),
    "author": "Keith Morgan",
    "location": "Properties > Render > Dimensions",
    "description": "Swaps the X/Y render dimensions.",
}

import bpy

#Draw Button
def draw_switcheroo(self, context):
    layout = self.layout
    split = layout.split

    row = layout.row()
    row.operator('switcheroo.switch', icon='ARROW_LEFTRIGHT')

#Switcheroo Script
class SWITCHEROO_EXECUTE_BUTTON(bpy.types.Operator):
    bl_idname = "switcheroo.switch"
    bl_label = "Switch X/Y"
    bl_description = "Flip between portrait and landscape camera orientations"

    def execute(self, context):
        bpy.context.scene.render.resolution_x, bpy.context.scene.render.resolution_y = bpy.context.scene.render.resolution_y, bpy.context.scene.render.resolution_x
        return {'FINISHED'}

def register():
    bpy.utils.register_class(SWITCHEROO_EXECUTE_BUTTON)
    bpy.types.RENDER_PT_dimensions.append(draw_switcheroo)

def unregister():
    bpy.utils.unregister_class(SWITCHEROO_EXECUTE_BUTTON)
    bpy.types.RENDER_PT_dimensions.remove(draw_switcheroo)

if __name__ == "__main__":
    register()
