from assets.dependencies.trigonometry import SideSolver as SS, AngleSolver as AA

class Solver:
    def TriangleSolver(hyp, leg, base, hyplega, hypbasa):
        
        #Hold up turns out this is broken?? Well this sounds like a problem for tomorrow
        
        '''
        Solve any triangle. You only need to pass in 1 side and 1 angle for it to work.
        P.S. YOU CAN PASS IN 2 SIDES IN THE FUTURE

        

        For example:
        TriangleSolver('x', 10, 'x', 70, 'x') will return the array [29.238044001630865, 10.0, 3.6397023426620243, 70, 20]
        in the order of hypotenuse, leg, base, hypotenuse-leg angle, hypotenuse-base angle

        '''


        try:
            hyplega = 90 - hypbasa
        except:
            hypbasa = 90 - hyplega

        timeout = 0
        while hyp != 'y' or hyp != 'x' or hyp != '' or timeout > 5:
            try:
                hyp = SS.SINhb(base, hyplega)
                break
            except:
                pass
            try:
                hyp = SS.COShl(leg, hyplega)
                break
            except:
                pass

            try:
                hyp = SS.COShb(base, hypbasa)
                break
            except:
                pass
            try:
                hyp = SS.SINhl(leg, hypbasa)
                break
            except:
                pass
            timeout += 1

        timeout = 0
        while leg != 'y' or leg != 'x' or leg != '' or timeout > 5:
            try:
                leg = SS.COSlh(hyp, hyplega)
                break
            except:
                pass
            try:
                leg = SS.TANlb(base, hyplega)
                break
            except:
                pass

            try:
                leg = SS.SINlh(hyp, hypbasa)
                break
            except:
                pass
            try:
                leg = SS.TANlb(base, hypbasa)
                break
            except:
                pass
            timeout += 1

        timeout = 0
        while base != 'y' or base != 'x' or base != '' or timeout > 5:
            try:
                base = SS.TANbl(leg, hyplega)
                break
            except:
                pass
            try:
                base = SS.SINbh(hyp, hyplega)
                break
            except:
                pass

            try:
                base = SS.TANbl(leg, hypbasa)
                break
            except:
                pass
            try:
                base = SS.COSbh(hyp, hypbasa)
                break
            except:
                pass
            timeout += 1

        return [hyp, leg, base, hyplega, hypbasa]

