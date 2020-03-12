#asigna un nombre al label del joint
#ejemplo hacer un mirror weight con ello

import pymel.core as pm
mySelJnts=pm.ls(sl=1)
for jnt in mySelJnts:
	pm.setAttr((str(jnt) + ".side"), 
		1)
	# center jnts use 0.
	# left jnts use 1.
	# right jnts use 2.
	# currently sets the type to other.
	pm.setAttr((str(jnt) + ".type"), 
		18)
	# strips out the name of the joint so have matching label names
	jntNewName = ""
	jntNewName=jnt.replace("jnt","")
	jntNewName=jntNewName.replace("_lf","")
	pm.setAttr((str(jnt) + ".otherType"), 
		jntNewName, type="string")