bl_info = {
    "name": "Switcheroo",
    "category": "Render",
    "version": (2, 0, 0),
    "blender": (2, 80, 0),
    "author": "Keith Morgan",
    "location": "Properties > Render > Dimensions",
    "description": "Swaps the X/Y render dimensions.",
}

import bpy

#Draw Button
def draw_switcheroo(self, context):
    layout = self.layout
    # split = layout.split

    col = layout.column(align=True)
    col.operator("switcheroo.switch", text="SWITCH XY", icon="ARROW_LEFTRIGHT")

#Switcheroo Script
class SWITCHEROO_EXECUTE_BUTTON(bpy.types.Operator):
    bl_idname = "switcheroo.switch"
    bl_label = "Switch X/Y"
    bl_description = "Flip between portrait and landscape camera orientations"

    def execute(self, context):
        scene = context.scene
        rd = scene.render

        rd.resolution_x, rd.resolution_y = rd.resolution_y, rd.resolution_x
        return {'FINISHED'}

def register():
    bpy.utils.register_class(SWITCHEROO_EXECUTE_BUTTON)
    bpy.types.RENDER_PT_dimensions.prepend(draw_switcheroo)

def unregister():
    bpy.utils.unregister_class(SWITCHEROO_EXECUTE_BUTTON)
    bpy.types.RENDER_PT_dimensions.remove(draw_switcheroo)

if __name__ == "__main__":
    register()
