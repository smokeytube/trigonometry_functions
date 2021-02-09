# package

import math
import time

#---Computing Functions---#

def sin_deg(deg):
    return (math.sin(math.radians(deg)))

def cos_deg(deg):
    return (math.cos(math.radians(deg)))

def tan_deg(deg):
    return (math.tan(math.radians(deg)))


def inv_sin_deg(deg):
    return math.degrees((math.asin(deg)))

def inv_cos_deg(deg):
    return math.degrees((math.acos(deg)))

def inv_tan_deg(deg):
    return math.degrees((math.atan(deg)))


def sqrt(x):
	return math.sqrt(x)

#---Trig Class---#

class SideSolver:

	#---Hypotenuse Leg Angle---#
	def SINhb(base, hyplega):
		return (base/(sin_deg(hyplega)))

	def COShl(leg, hyplega):
		return (leg/(cos_deg(hyplega)))

	def TANbl(leg, hyplega):
		return (leg*(tan_deg(hyplega)))

	def SINbh(hyp, hyplega):
		return (hyp*(sin_deg(hyplega)))

	def COSlh(hyp, hyplega):
		return (hyp*(cos_deg(hyplega)))

	def TANlb(base, hyplega):
		return (base/(tan_deg(hyplega)))



	#---Hypotenuse Base Angle---#
	def COShb(base, hypbasa):
		return (base/(cos_deg(hypbasa)))

	def SINhl(leg, hypbasa):
		return (leg/(sin_deg(hypbasa)))

	def TANbl(leg, hypbasa):
		return (leg/(tan_deg(hypbasa)))

	def COSbh(hyp, hypbasa):
		return (hyp*(cos_deg(hypbasa)))

	def SINlh(hyp, hypbasa):
		return (hyp*(sin_deg(hypbasa)))

	def TANlb(base, hypbasa):
		return (base*(tan_deg(hypbasa)))


class AngleSolver:

	#---Hypotenuse Leg Angle---#
	def arcSINhb(base, hyp):
		return (inv_sin_deg(base/hyp))

	def arcCOShl(leg, hyp):
		return (inv_cos_deg(leg/hyp))

	def arcTANlb(base, leg):
		return (inv_tan_deg(base/leg))


	#---Hypotenuse Base Angle---#
	def arcCOShb(base, hyp):
		return (inv_cos_deg(base/hyp))

	def arcSINhl(leg, hyp):
		return (inv_sin_deg(leg/hyp))

	def arcTANbl(leg, base):
		return (inv_tan_deg(leg/base))






class TriangleSolver:
	pass

