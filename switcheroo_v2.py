bl_info = {
    "name": "Switcheroo",
    "category": "Render",
    "author": "Keith Morgan"
}

import bpy
from bpy.types import Menu, Panel

class RenderButtonsPanel:
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"

    @classmethod
    def poll(cls, context):
        scene = context.scene
        return scene and (scene.render.engine in cls.COMPAT_ENGINES)
#class Switcheroo(bpy.types.Panel):
class RENDER_PT_dimensions(RenderButtonsPanel, Panel):
    bl_label = "Dimensions"
   # bl_label = "Switcheroo"
   # bl_id = "view3D.custom_menu"
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
        bpy.context.scene.render.resolution_x, bpy.context.scene.render.resolution_y = bpy.context.scene.render.resolution_y, bpy.context.scene.render.resolution_x
        return {'FINISHED'}

def menu_func(self, context):
    ui_layout(self.layout, context)

classes = (
    RenderButtonsPanel,
    RENDER_PT_dimensions,
    OBJECT_BUTTON,
)


def register():

   bpy.types.RENDER_PT_performance.append(menu_func)
   # bpy.utils.register_class(RenderButtonsPanel)
   bpy.utils.register_class(OBJECT_BUTTON)

def unregister():
#    bpy.utils.unregister_class(RenderButtonsPanel)
  # bpy.utils.unregister_class(RENDER_PT_dimensions)
   # bpy.utils.unregister_class(RenderButtonsPanel)
   bpy.types.RENDER_PT_performance.remove(menu_func)
   bpy.utils.unregister_class(OBJECT_BUTTON)


if __name__ == "__main__":
   register()

# if __name__ == "__main__":  # only for live edit.
#     from bpy.utils import register_class
#     for cls in classes:
#         register_class(cls)
