bl_info = {
    "name": "Switcheroo",
    "category": "Render",
    "author": "Keith Morgan"
}

import bpy
import mathutils



# Class
class Switcheroo(bpy.types.Panel):
    bl_label = "Switcheroo"
    bl_id = "view3D.custom_menu"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "render"


    def draw(self, context):
        layout = self.layout
        split = layout.split()

        # Layout for addon
        row = layout.row()
        row.label("Swap Portrait and Landscape")
        row = layout.row()
        row.operator("switcheroo.switch")


class OBJECT_OT_BUTTON(bpy.types.Operator):
    bl_idname = "switcheroo.switch"
    bl_label = "Switcheroo!"
    #bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # x = render.resolution_x
        # y = render.resolution_y
        storage
        switcher
        # render.resolution_x = y
        # render.rsolution_y = x
        return{storage}


def storage():
    m = render.resolution_x
    n = render.resolution_y


def switcher():
    x = n
    y = m


def register():
    bpy.utils.register_class(Switcheroo)


def unregister():
    bpy.utils.unregister_class(Switcheroo)


if __name__ == "__main__":
    register()
