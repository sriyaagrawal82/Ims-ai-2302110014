
import cadquery as cq
from dataclasses import dataclass

@dataclass
class CellSpec:
    r_cell: float
    h_cell: float

cells = {
    "18650": CellSpec(9.0, 65.0),
    "21700": CellSpec(10.5, 70.0),
    "4680": CellSpec(23.0, 80.0)
}

cell_name = "18650"
spec = cells[cell_name]

clearance = 1.0
wall = 3.0
base = 4.0
n = 3

pitch = 2 * (spec.r_cell + clearance) + wall

length = (n - 1) * pitch + 2 * (spec.r_cell + clearance) + 2 * wall
width = 2 * (spec.r_cell + clearance) + 2 * wall
height = spec.h_cell * 0.25 + base

holder = cq.Workplane("XY").box(length, width, height)

for i in range(n):
    x = (i - (n - 1) / 2) * pitch

    pocket = (
        cq.Workplane("XY")
        .workplane(offset=base)
        .center(x, 0)
        .circle(spec.r_cell + clearance)
        .extrude(height)
    )

    holder = holder.cut(pocket)

cq.exporters.export(holder, "battery_holder.step")
cq.exporters.export(holder, "battery_holder.stl")

print("Battery holder created successfully!")
