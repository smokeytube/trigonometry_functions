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

'''
Function keys:

Pythagorean functions are in the form of

Pythagorean theorm, side x, side y

For example:
PYTHhb = Pythagorean theorm, hypotenuse value, base value

so the function would look like

PYTHhb(13, 10) will return √69 or 8.3066...

------------------------------

All Side Solver functions are in the form of
MATHFUNCTION, side unknown, sideknown

For example:
SINhb = Sine, unknown hypotenuse, known base

The variable hyplega is shortened for Hypotenuse-leg angle, or angle A on the triangle in my program.
Same with hypbasa. It is shortened for hypotenuse-base angle, or the bottom right C angle.

SINhb(10, 70) where 10 is the base length and 70 is the Hypotenuse-leg angle will return 10.6417...

------------------------------

All Angle Solver functions are in the form of
MATHFUNCTION, side x, side y

For example:
arcSINhb = Sine inverse, side x, side y


arcSINhb(10, 13) where 10 is the base length and 13 is the hypotenuse length will return hyplega 50.2848...

'''

class PythagoreanSolver:

	#---Extemely simple pythagorean functions---#
	def PYTHhb(hyp, base):
		return sqrt(hyp**2 - base**2)

	def PYTHhl(hyp, leg):
		return sqrt(hyp**2 - leg**2)

	def PYTHbl(base, leg):
		return sqrt(base**2 + leg**2)


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
