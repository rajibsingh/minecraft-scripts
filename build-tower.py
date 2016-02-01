
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z


for i in range(1,5):
    for j in range(1,5):
        mc.setBlock(x+i, y+j+i, z+j, 98)
