
import numpy as np
import pytest

import shakemap.grind.correlation.boore_2003 as b03


def test_boore2003():
    cormod = b03.Boore2003()
    d = np.linspace(0, 10, 101)
    cor = cormod.getSpatialCorrelation(d)
    cor_target = np.array(
      [ 0.        ,  0.21725552,  0.29277765,  0.34574891,  0.38731108,
        0.42173472,  0.45118836,  0.47694783,  0.49983654,  0.52042113,
        0.53911037,  0.55621002,  0.57195551,  0.58653238,  0.60008975,
        0.61274942,  0.62461229,  0.63576299,  0.64627322,  0.65620435,
        0.66560927,  0.67453398,  0.68301871,  0.69109887,  0.69880579,
        0.70616734,  0.71320844,  0.71995142,  0.72641643,  0.73262165,
        0.73858361,  0.74431733,  0.74983652,  0.75515373,  0.76028048,
        0.76522735,  0.77000411,  0.77461978,  0.77908271,  0.78340063,
        0.78758074,  0.79162975,  0.79555388,  0.79935896,  0.80305045,
        0.80663345,  0.81011274,  0.81349282,  0.81677791,  0.81997199,
        0.82307879,  0.82610186,  0.82904453,  0.83190995,  0.83470111,
        0.83742083,  0.84007179,  0.84265654,  0.84517747,  0.8476369 ,
        0.85003699,  0.85237982,  0.85466737,  0.85690152,  0.85908407,
        0.86121673,  0.86330114,  0.86533886,  0.8673314 ,  0.86928018,
        0.87118656,  0.87305188,  0.87487737,  0.87666425,  0.87841367,
        0.88012675,  0.88180455,  0.88344809,  0.88505836,  0.88663631,
        0.88818284,  0.88969883,  0.89118513,  0.89264255,  0.89407187,
        0.89547385,  0.89684921,  0.89819865,  0.89952286,  0.90082249,
        0.90209817,  0.9033505 ,  0.90458009,  0.9057875 ,  0.90697327,
        0.90813795,  0.90928205,  0.91040606,  0.91151048,  0.91259576,
        0.91366237]
                         )
    np.testing.assert_allclose(cor, cor_target)

    with pytest.raises(Exception) as a:
        cormod.getSpatialCorrelation(d, imt = "PGV")
