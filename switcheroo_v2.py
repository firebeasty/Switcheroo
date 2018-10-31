bl_info = {
    "name": "Switcheroo",
    "category": "Render",
    "author": "Keith Morgan",
    "location": "Properties > Render > Dimensions",
    "description": "Swaps the X/Y render dimensions.",
}

import bpy

def draw_switcheroo(self, context):
    layout = self.layout
    split = layout.split

    #Layout
    row = layout.row()
    row.operator('switcheroo.switch', icon='ARROW_LEFTRIGHT')

class SWITCHEROO_EXECUTE_BUTTON(bpy.types.Operator):
    bl_idname = "switcheroo.switch"
    bl_label = "Switch X/Y"
    bl_description = "Flip between portrait and landscape camera orientations"

    def execute(self, context):
        bpy.context.scene.render.resolution_x, bpy.context.scene.render.resolution_y = bpy.context.scene.render.resolution_y, bpy.context.scene.render.resolution_x
        return {'FINISHED'}


def register():
    bpy.types.RENDER_PT_dimensions.append(draw_switcheroo)
    bpy.utils.register_class(SWITCHEROO_EXECUTE_BUTTON)

def unregister():
    bpy.utils.unregister_class(SWITCHEROO_EXECUTE_BUTTON)
    bpy.types.RENDER_PT_dimensions.remove(draw_switcheroo)

if __name__ == "__main__":
    register()
