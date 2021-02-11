from assets.dependencies.trigonometry import SideSolver as SS, AngleSolver as AA, PythagoreanSolver as PP

class Solver:
    def TriangleSolver(hyp, leg, base, hyplega, hypbasa):
        
        '''
        Solve any triangle. You only need to pass in 1 side and 1 angle for it to work (or 2 sides no angles).

        

        For example:
        TriangleSolver('x', 10, 'x', 70, 'x') will return the array [29.238044001630865, 10, 27.474774194546217, 70, 20]
        in the order of hypotenuse, leg, base, hypotenuse-leg angle, hypotenuse-base angle

        '''

        if hyplega == 'y' or hyplega == 'x' or hyplega == '' and hypbasa == 'y' or hypbasa == 'x' or hypbasa == '':

            if hyp == 'y' or hyp == 'x' or hyp == '':
                try:
                    hyp = PP.PYTHbl(base, leg)
                except:
                    pass

            elif leg == 'y' or leg == 'x' or leg == '':
                try:
                    leg = PP.PYTHhb(hyp, base)
                except:
                    pass

            elif base == 'y' or base == 'x' or base == '':
                try:
                    base = PP.PYTHhl(hyp, leg)
                except:
                    pass

            timeout = 0
            while hyplega == 'y' or hyplega == 'x' or hyplega == '' or timeout > 5:
                try:
                    hyplega = AA.arcSINhb(base, hyp)
                    break
                except:
                    pass

                try:
                    hyplega = AA.arcCOShl(leg, hyp)
                    break
                except:
                    pass

                try:
                    hyplega = AA.arcTANlb(base, leg)
                    break
                except:
                    pass
                timeout += 1

            timeout = 0
            while hypbasa == 'y' or hypbasa == 'x' or hypbasa == '' or timeout > 5:
                try:
                    hypbasa = AA.arcCOShb(base, hyp)
                    break
                except:
                    pass

                try:
                    hypbasa = AA.arcSINhl(leg, hyp)
                    break
                except:
                    pass

                try:
                    hypbasa = AA.arcTANbl(base, leg)
                    break
                except:
                    pass
                timeout += 1                


        else:
            try:
                hyplega = 90 - hypbasa
            except:
                hypbasa = 90 - hyplega

            timeout = 0
            while hyp == 'y' or hyp == 'x' or hyp == '' or timeout > 5:
                try:
                    hyp = SS.aSINhb(base, hyplega)
                    break
                except:
                    pass
                try:
                    hyp = SS.aCOShl(leg, hyplega)
                    break
                except:
                    pass

                try:
                    hyp = SS.cCOShb(base, hypbasa)
                    break
                except:
                    pass
                try:
                    hyp = SS.cSINhl(leg, hypbasa)
                    break
                except:
                    pass
                timeout += 1

            timeout = 0
            while leg == 'y' or leg == 'x' or leg == '' or timeout > 5:
                try:
                    leg = SS.aCOSlh(hyp, hyplega)
                    break
                except:
                    pass
                try:
                    leg = SS.aTANlb(base, hyplega)
                    break
                except:
                    pass

                try:
                    leg = SS.cSINlh(hyp, hypbasa)
                    break
                except:
                    pass
                try:
                    leg = SS.cTANlb(base, hypbasa)
                    break
                except:
                    pass
                timeout += 1

            timeout = 0
            while base == 'y' or base == 'x' or base == '' or timeout > 5:
                try:
                    base = SS.aTANbl(leg, hyplega)
                    break
                except:
                    pass
                try:
                    base = SS.aSINbh(hyp, hyplega)
                    break
                except:
                    pass

                try:
                    base = SS.cTANbl(leg, hypbasa)
                    break
                except:
                    pass
                try:
                    base = SS.cCOSbh(hyp, hypbasa)
                    break
                except:
                    pass
                timeout += 1

            return [hyp, leg, base, hyplega, hypbasa]
        return [hyp, leg, base, hyplega, hypbasa]

