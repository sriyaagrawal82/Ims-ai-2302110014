
import cadquery as cq

# Brick dimensions in mm
length = 31.2
width = 15.6
height = 9.6

# Stud dimensions
stud_d = 4.8
stud_h = 1.7
spacing = 8.0

# Create the brick body
brick = cq.Workplane("XY").box(length, width, height)

# Calculate positions for 2 x 4 studs
stud_positions = []

for i in range(4):
    for j in range(2):
        x = (i - 1.5) * spacing
        y = (j - 0.5) * spacing
        stud_positions.append((x, y))

# Add eight studs on top
brick = (
    brick.faces(">Z")
    .workplane()
    .pushPoints(stud_positions)
    .circle(stud_d / 2)
    .extrude(stud_h)
)

# Export the 3D model
cq.exporters.export(brick, "brick.step")
cq.exporters.export(brick, "brick.stl")

print("2 x 4 brick created successfully!")
print("Number of studs:", len(stud_positions))
